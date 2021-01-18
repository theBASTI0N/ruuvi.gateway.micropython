try:
    import uasyncio as asyncio
except:
    import asyncio

app = "REQUESTS_AS"
version = "0.1.0"

class Response:

    def __init__(self, f, r):
        self.raw = f
        self.writerraw = r
        self.encoding = "utf-8"
        self._cached = None

    async def close(self):
        if self.writerraw:
            self.writerraw.close()
            await self.writerraw.wait_closed()
            self.raw = None
            self.writerraw = None
        self._cached = None

    @property
    async def content(self):
        if self._cached is None:
            try:
                self._cached = await self.raw.read()
            finally:
                self.writerraw.close()
                await self.writerraw.wait_closed()
                self.raw = None
                self.writerraw = None
        return self._cached

    @property
    async def text(self):
        return str(await self.content, self.encoding)

    def json(self):
        try:
            import ujson
        except:
            import json as ujson
        return ujson.loads(self.content)


async def request(method, url, data=None, json=None, headers={}, stream=None):
    try:
        proto, dummy, host, path = url.split("/", 3)
    except ValueError:
        proto, dummy, host = url.split("/", 2)
        path = ""
    if proto == "http:":
        port = 80
        # Uncomment when supported by uasyncio
    #elif proto == "https:":
        #port = 443
        #ssl = True
    else:
        raise ValueError("Unsupported protocol: " + proto)

    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)
    
    try:
        # Pass SSL when supported
        reader, writer = await asyncio.open_connection(str(host), int(port))
        writer.write(str.encode("%s /%s HTTP/1.0\r\n" % (method, path),"utf-8") )
        await writer.drain()
        if not "Host" in headers:
            writer.write(str.encode("Host: %s\r\n" % host,"utf-8"))
            await writer.drain()
        # Iterate over keys to avoid tuple alloc
        for k in headers:
            writer.write(k)
            await writer.drain()
            writer.write(str.encode(": ", "utf-8"))
            await writer.drain()
            writer.write(str.encode(headers[k], "utf-8"))
            await writer.drain()
            writer.write(str.encode("\r\n", "utf-8"))
            await writer.drain()
        if json is not None:
            assert data is None
            try:
                import ujson
            except:
                import json as ujson
            data = ujson.dumps(json)
            writer.write(str.encode("Content-Type: application/json\r\n", "utf-8"))
            await writer.drain()
        if data:
            writer.write(str.encode("Content-Length: %d\r\n" % len(data), "utf-8"))
            await writer.drain()
        writer.write(str.encode("\r\n", "utf-8"))
        await writer.drain()
        if data:
            writer.write(str.encode(data, "utf-8"))
            await writer.drain()

        l = await reader.readline()
        #print(l)
        l = l.split(None, 2)
        status = int(l[1])
        reason = ""
        if len(l) > 2:
            reason = l[2].rstrip()
        while True:
            l = await reader.readline()
            if not l or l == b"\r\n":
                break
            #print(l)
            if l.startswith(b"Transfer-Encoding:"):
                if b"chunked" in l:
                    raise ValueError("Unsupported " + str(l, "utf-8"))
            if l.startswith(b"Location:") and not 200 <= status <= 299:
                raise NotImplementedError("Redirects not yet supported")
    except OSError:
        writer.close()
        await writer.wait_closed()
        raise

    resp = Response(reader, writer)
    resp.status_code = status
    resp.reason = reason
    return resp

async def head(url, **kw):
    return await request("HEAD", url, **kw)

async def get(url, **kw):
    return await request("GET", url, **kw)

async def post(url, **kw):
    return await request("POST", url, **kw)

async def put(url, **kw):
    return await request("PUT", url, **kw)

async def patch(url, **kw):
    return await request("PATCH", url, **kw)

async def delete(url, **kw):
    return await request("DELETE", url, **kw)
