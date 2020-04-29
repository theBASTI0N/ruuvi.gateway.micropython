from binascii import hexlify
import machine

MAC = str.upper(hexlify(machine.unique_id(),).decode())
id = "RuuviGW_" + MAC[-3:]
head_small="""
    <!doctype html>
        <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">

                <title>Ruuvi Gateway Configuration</title>
                <link rel="icon" type="image/svg+xml" href="re.svg">
                <link rel="stylesheet" href="pure-min.css">
                <link rel="stylesheet" href="side-menu.css">
            </head>
        <div id="main">
            <div class="header">
"""

head1="""
    <!doctype html>
        <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">

                <title>Ruuvi Gateway Configuration</title>
                <link rel="icon" type="image/svg+xml" href="re.svg">
                <link rel="stylesheet" href="pure-min.css">
                <link rel="stylesheet" href="side-menu.css">
            </head>
            <body>
                <div id="layout">
                    <!-- Menu toggle -->
                    <a href="#menu" id="menuLink" class="menu-link">
                        <!-- Hamburger icon -->
                        <span></span>
                    </a>
                    <div id="menu">
                        <div class="pure-menu">
                            <a href="https://ruuvi.com">
                            <img class="pure-img-responsive-padding" src="rln.svg" >
                            </a>
                            <ul class="pure-menu-heading pure-menu-heading-right" href="index.html">Gateway</ul>
                            <ul class="pure-menu-list">
                        """

none_selected="""\
                <li class="pure-menu-item"><a href="index.html" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="about.html" class="pure-menu-link">About</a></li>
                <li class="pure-menu-item"><a href="status.pyhtml" class="pure-menu-link">Status</a></li>
                <li class="pure-menu-item"><a href="wifi" class="pure-menu-link">WiFi</a></li>
                <li class="pure-menu-item"><a href="cloud" class="pure-menu-link">Cloud</a></li>
                <li class="pure-menu-item"><a href="syslog" class="pure-menu-link">Syslog</a></li>
                <li class="pure-menu-item"><a href="reset.html" class="pure-menu-link">Reset</a></li>
                <li class="pure-menu-item"><a href="restart" class="pure-menu-link">Restart</a></li>
                </ul>
"""

wifi_selected="""\
                <li class="pure-menu-item"><a href="index.html" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="about.html" class="pure-menu-link">About</a></li>
                <li class="pure-menu-item"><a href="status.pyhtml" class="pure-menu-link">Status</a></li>
                <li class="pure-menu-item pure-menu-selected"><a href="wifi" class="pure-menu-link">WiFi</a></li>
                <li class="pure-menu-item"><a href="cloud" class="pure-menu-link">Cloud</a></li>
                <li class="pure-menu-item"><a href="syslog" class="pure-menu-link">Syslog</a></li>
                <li class="pure-menu-item"><a href="reset.html" class="pure-menu-link">Reset</a></li>
                <li class="pure-menu-item"><a href="restart" class="pure-menu-link">Restart</a></li>
                </ul>
"""

cloud_selected="""\
                <li class="pure-menu-item"><a href="index.html" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="about.html" class="pure-menu-link">About</a></li>
                <li class="pure-menu-item"><a href="status.pyhtml" class="pure-menu-link">Status</a></li>
                <li class="pure-menu-item"><a href="wifi" class="pure-menu-link">WiFi</a></li>
                <li class="pure-menu-item pure-menu-selected"><a href="cloud" class="pure-menu-link">Cloud</a></li>
                <li class="pure-menu-item"><a href="syslog" class="pure-menu-link">Syslog</a></li>
                <li class="pure-menu-item"><a href="reset.html" class="pure-menu-link">Reset</a></li>
                <li class="pure-menu-item"><a href="restart" class="pure-menu-link">Restart</a></li>
                </ul>
"""

home_selected="""\
                <li class="pure-menu-item pure-menu-selected"><a href="index.html" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="about.html" class="pure-menu-link">About</a></li>
                <li class="pure-menu-item"><a href="status.pyhtml" class="pure-menu-link">Status</a></li>
                <li class="pure-menu-item"><a href="wifi" class="pure-menu-link">WiFi</a></li>
                <li class="pure-menu-item"><a href="cloud" class="pure-menu-link">Cloud</a></li>
                <li class="pure-menu-item"><a href="syslog" class="pure-menu-link">Syslog</a></li>
                <li class="pure-menu-item"><a href="reset.html" class="pure-menu-link">Reset</a></li>
                <li class="pure-menu-item"><a href="restart" class="pure-menu-link">Restart</a></li>
                </ul>
"""

about_selected="""\
                <li class="pure-menu-item"><a href="index.html" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item pure-menu-selected"><a href="about.html" class="pure-menu-link">About</a></li>
                <li class="pure-menu-item"><a href="status.pyhtml" class="pure-menu-link">Status</a></li>
                <li class="pure-menu-item"><a href="wifi" class="pure-menu-link">WiFi</a></li>
                <li class="pure-menu-item"><a href="cloud" class="pure-menu-link">Cloud</a></li>
                <li class="pure-menu-item"><a href="syslog" class="pure-menu-link">Syslog</a></li>
                <li class="pure-menu-item"><a href="reset.html" class="pure-menu-link">Reset</a></li>
                <li class="pure-menu-item"><a href="restart" class="pure-menu-link">Restart</a></li>
                </ul>
"""

status_selected="""\
                <li class="pure-menu-item"><a href="index.html" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="about.html" class="pure-menu-link">About</a></li>
                <li class="pure-menu-item pure-menu-selected"><a href="status.pyhtml" class="pure-menu-link">Status</a></li>
                <li class="pure-menu-item"><a href="wifi" class="pure-menu-link">WiFi</a></li>
                <li class="pure-menu-item"><a href="cloud" class="pure-menu-link">Cloud</a></li>
                <li class="pure-menu-item"><a href="syslog" class="pure-menu-link">Syslog</a></li>
                <li class="pure-menu-item"><a href="reset.html" class="pure-menu-link">Reset</a></li>
                <li class="pure-menu-item"><a href="restart" class="pure-menu-link">Restart</a></li>
                </ul>
"""

reset_selected="""\
                <li class="pure-menu-item"><a href="index.html" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="about.html" class="pure-menu-link">About</a></li>
                <li class="pure-menu-item"><a href="status.pyhtml" class="pure-menu-link">Status</a></li>
                <li class="pure-menu-item"><a href="wifi" class="pure-menu-link">WiFi</a></li>
                <li class="pure-menu-item"><a href="cloud" class="pure-menu-link">Cloud</a></li>
                <li class="pure-menu-item"><a href="syslog" class="pure-menu-link">Syslog</a></li>
                <li class="pure-menu-item pure-menu-selected"><a href="reset.html" class="pure-menu-link">Reset</a></li>
                <li class="pure-menu-item"><a href="restart" class="pure-menu-link">Restart</a></li>
                </ul>
"""

restart_selected="""\
                <li class="pure-menu-item"><a href="index.html" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="about.html" class="pure-menu-link">About</a></li>
                <li class="pure-menu-item"><a href="status.pyhtml" class="pure-menu-link">Status</a></li>
                <li class="pure-menu-item"><a href="wifi" class="pure-menu-link">WiFi</a></li>
                <li class="pure-menu-item"><a href="cloud" class="pure-menu-link">Cloud</a></li>
                <li class="pure-menu-item"><a href="syslog" class="pure-menu-link">Syslog</a></li>
                <li class="pure-menu-item pure-menu-selected"><a href="reset.html" class="pure-menu-link">Reset</a></li>
                <li class="pure-menu-item"><a href="restart" class="pure-menu-link">Restart</a></li>
                </ul>
"""

sys_selected="""\
                <li class="pure-menu-item"><a href="index.html" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="about.html" class="pure-menu-link">About</a></li>
                <li class="pure-menu-item"><a href="status.pyhtml" class="pure-menu-link">Status</a></li>
                <li class="pure-menu-item"><a href="wifi" class="pure-menu-link">WiFi</a></li>
                <li class="pure-menu-item"><a href="cloud" class="pure-menu-link">Cloud</a></li>
                <li class="pure-menu-item pure-menu-selected"><a href="syslog" class="pure-menu-link">Syslog</a></li>
                <li class="pure-menu-item"><a href="reset.html" class="pure-menu-link">Reset</a></li>
                <li class="pure-menu-item"><a href="restart" class="pure-menu-link">Restart</a></li>
                </ul>
"""

head2="""\
            </div>
        </div>
        <div id="main">
            <div class="header">
"""

home_content="""
                <h1>Ruuvi Gateway</h1>
                <h2>Welcome to your ruuvi GW</h2>
            </div>
            <div class="content">
                <h2 class="content-subhead">Overview</h2>
                <p>
                    This firmware is built on top of micropython and is designed to be a drop in replacement
                    to the original firmware.
                </p>
                <p>
                    <br />
                    It supports MQTT and HTTP messages and the ability to decode the messages before sending.
                    MQTT with support for TLS is comming.
                </p>
            </div>
"""

about_content="""
                <h1>Ruuvi Gateway</h1>
            </div>
            <div class="content">
                <h2 class="content-subhead">Reason For Development</h2>
                <p>
                    The reason I developed this firmware was to create and easy to add on solution for users
                    that are not familiar or comforatable with programming in C.
                </p>
                <p>
                    <br />
                    This project is completely open source and can be found at: <a href="https://github.com/theBASTI0N/ruuvi.gateway.micropython" alt="theBASTI0N">theBASTI0N/ruuvi.gateway.micropython</a>
                </p>
            </div>
"""

reset_content="""
            <h1>Reset Ruuvi Gateway</h1>
            <h2>Proceed with caution</h2>
            </div>
            <div class="content">
            <h2 class="content-subhead">Reset Function</h2>
            <form class="pure-form pure-form-aligned" action="/reset-gw" method="post">
                <label for="resetM" class="pure-radio"> <input type="radio" name="resetM" value="0">WiFi Reset </label>
                <label for="resetM" class="pure-radio"> <input type="radio" name="resetM" value="1">WiFi Rescan </label>
                <label for="resetM" class="pure-radio"> <input type="radio" name="resetM" value="2">Cloud Connection </label>
                <label for="resetM" class="pure-radio"> <input type="radio" name="resetM" value="3">Syslog Server </label>
                <label for="resetM" class="pure-radio"> <input type="radio" name="resetM" value="4">Factory Reset </label>
                <button type="submit" value="ok" class="pure-button pure-button-primary">Submit</button>
            </form>
            </div>
            """

restart_content="""
            <h1>Reset Ruuvi Gateway</h1>
            <h2>Proceed with caution</h2>
            </div>
            <div class="content">
            <h2 class="content-subhead">Reset Function</h2>
            <form class="pure-form pure-form-aligned" action="/restart-post" method="post">
                <label for="restart" class="pure-radio"> <input type="radio" name="restart" value="0">Cancel </label>
                <label for="restart" class="pure-radio"> <input type="radio" name="restart" value="1">Restart </label>
                <button type="submit" value="ok" class="pure-button pure-button-primary">Submit</button>
            </form>
            </div>
            """

status_content="""
                <h1>Ruuvi Gateway</h1>
                <h2>Status</h2>
                </div>
                <div class="content">
                <br />
                <br />
                <table class="pure-table pure-table-horizontal" align="center">
                <thead>
                <tr>
                <th>Mode</th>
                <th>Active</th>
                <th>Messages Sent</th>
                <th>Heart Beats</th>
                <th>Uptime (s)</th>
                <th>Memory Free (bytes)</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                {{ if GwMode == 1 }}
                <td>MQTT</td>
                {{ py }}
                   from gwmqtt import mqtt_update
                   data = mqtt_update()
                {{ end }}
                {{ elif GwMode == 0 }}
                <td>HTTP</td>
                {{ py }}
                   from gwhttp import http_update
                   data = http_update()
                   data['heartMessages'] = NA
                {{ end }}
                {{ else }}
                <td>Not Configured</td>
                {{ end }}

                {{ if data['active'] == 1 }}
                <td>Yes</td>
                {{ elif data['active'] == 0 }}
                <td>No</td>
                {{ else }}
                <td>Unknown</td>
                {{ end }}
                <td>{{ data['Messages'] }}</td>
                <td>{{ data['heartMessages'] }}</td>
                <td>{{ data['uptime'] }}</td>
                <td>{{ data['memFree'] }}</td>
                </tr>
                </tbody>
                </table>
                </div>
"""

wifi1= """
                        <h1> WiFi Configuration</h1>
                        <h2> Select Network </h2>
                    </div>
                        <div class="content">
                            <form class="pure-form pure-form-aligned" action="/wifi-post" method="post">
                        """

wifi2= """
            <div class="pure-control-group">
                                            <label for="password">Password</label>
                                            <input name="password" type="password" placeholder="Password">
                                        </div>
                                        <button type="submit" value="ok" class="pure-button pure-button-primary">Submit</button>
                                    </form>
                                </div>
            </div>"""

sys_mode= """
                        <h1> Syslog Configuration</h1>
                    </div>
                        <div class="content">
                            </br>
                            <form class="pure-form pure-form-aligned" action="/syslog-post" method="post">
                            <fieldset>
                            <div class="pure-control-group">
                            <label for="host">Syslog Server</label>
                            <input id="host" name="host" type="text" placeholder="server">
                            </div>
                            <div class="pure-control-group">
                            <label for="port">Port</label>
                            <input id="port" name="port" type="number" value="514" placeholder="514">
                            </div>
                            <div class="pure-control-group">
                            <label for="TZ">Time Zone</label>
                            <input id="TZ" name="TZ" type="number" min="-12" max="12" value="0" placeholder="0">
                            </div>
                            <div class="pure-control-group">
                            <label for="tcp" class="pure-radio">
                                <input id="tcp" type="radio" name="tcp" value="1">
                                TCP
                            </label>
                            </div>
                            <div class="pure-control-group">
                            <label for="tcp" class="pure-radio">
                                <input id="tcp" type="radio" name="tcp" value="0" checked>
                                UDP
                            </label>
                            </div>
                            <button type="submit" value="ok" class="pure-button pure-button-primary">Submit</button>
                            </fieldset>
                            </form>
                        </div>
            </div>"""

cloud_mode= """
                         <h1> Cloud Configuration</h1>
                            <h2> Choose Mode</h2>
                    </div>
                        <div class="content">
                            <form class="pure-form pure-form-aligned" action="/cloud-post" method="post">
                            <label for="mode" class="pure-radio"> <input type="radio" name="mode" value="0">HTTP </label>
                            <label for="mode" class="pure-radio"> <input type="radio" name="mode" value="1">MQTT </label>
                            <button type="submit" value="ok" class="pure-button pure-button-primary">Submit</button>
                            </form>
                        </div>
            </div>"""

cloud_http= """
                        <h1> Cloud Configuration</h1>
                            <h2> HTTP Configuration</h2>
                    </div>
                        <div class="content">
                            </br>
                            <form class="pure-form pure-form-aligned" action="/cloud-posthttp" method="post">
                            <fieldset>
                            <div class="pure-control-group">
                            <label for="host">HTTP URL</label>
                            <input id="host" name="host" type="text" placeholder="https://url.com">
                            </div>
                            <div class="pure-control-group">
                            <label for="epoch" class="pure-radio">
                                <input id="epoch" type="radio" name="epoch" value="1">
                                Unix Timestamps: 1585735460
                            </label>
                            </div>
                            <div class="pure-control-group">
                            <label for="epoch" class="pure-radio">
                                <input id="epoch" type="radio" name="epoch" value="0" checked>
                                Human Readable Timestamps: 2020-04-01T11:05:00Z
                            </label>
                            </div>
                             <div class="pure-control-group">
                            <label for="dble" class="pure-radio">
                                <input id="dble" type="radio" name="dble" value="1" checked>
                                BLE data will be decoded
                            </label>
                            </div>
                            <div class="pure-control-group">
                            <label for="dble" class="pure-radio">
                                <input id="dble" type="radio" name="dble" value="0">
                                Only raw data is sent
                            </label>
                            </div>
                            <button type="submit" value="ok" class="pure-button pure-button-primary">Submit</button>
                            </fieldset>
                            </form>
                        </div>
            </div>
                        """

cloud_mqtt= """
                        <h1> Cloud Configuration</h1>
                            <h2> MQTT Config<uration/h2>
                    </div>
                        <div class="content">
                            </br>
                            <form class="pure-form pure-form-aligned" action="/cloud-postmqtt" method="post">
                            <fieldset>
                            <div class="pure-control-group">
                            <label for="host">MQTT Server</label>
                            <input id="host" name="host" type="text" placeholder="server">
                            </div>
                            <div class="pure-control-group">
                            <label for="port">MQTT Port</label>
                            <input id="port" name="port" type="number" value="1883" placeholder="1883">
                            </div>
                            <div class="pure-control-group">
                            <label for="username">MQTT Username</label>
                            <input id="username" name="username" type="text" value="" placeholder="user1">
                            </div>
                            <div class="pure-control-group">
                            <label for="password">MQTT Password</label>
                            <input id="password" name="password" type="password" value="" placeholder="password">
                            </div>
                            <div class="pure-control-group">
                            <label for="topic1">Topic 1</label>
                            <input id="topic1" name="topic1" type="text" value="ruuvigw">
                            </div>
                            <div class="pure-control-group">
                            <label for="topic2">Topic 2</label>
                            <input id="topic2" name="topic2" type="text" value="room1">
                            </div>
                            <div class="pure-control-group">
                            <label for="epoch" class="pure-radio">
                                <input id="epoch" type="radio" name="epoch" value="1">
                                Unix Timestamps: 1585735460
                            </label>
                            </div>
                            <div class="pure-control-group">
                            <label for="epoch" class="pure-radio">
                                <input id="epoch" type="radio" name="epoch" value="0" checked>
                                Human Readable Timestamps: 2020-04-01T11:05:00Z
                            </label>
                            </div>
                            <div class="pure-control-group">
                            <label for="dble" class="pure-radio">
                                <input id="dble" type="radio" name="dble" value="1" checked>
                                BLE data will be decoded
                            </label>
                            </div>
                            <div class="pure-control-group">
                            <label for="dble" class="pure-radio">
                                <input id="dble" type="radio" name="dble" value="0">
                                Only raw data is sent
                            </label>
                            </div>
                            <button type="submit" value="ok" class="pure-button pure-button-primary">Submit</button>
                            </fieldset>
                            </form>
                        </div>
            </div>"""

end= """               </div>
                </div>
                <script src="ui.js"></script>
                <a href="https://ruuvi.com">
                <img class="ruuvi-eye" src="re.svg" >
                </a>
                </body>
                </html>"""
