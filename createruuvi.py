import uos
from requests import *

def create_www():
    uos.mkdir('www')

def fill_www():
    d = uos.listdir()

    #Create index.html
    if 'index.html' not in d:
        with open("/www/index.html", "w") as f:
            f.write(head1 + home_selected + head2 + home_content + end)

    #Create about.html
    if 'about.html' not in d:
        with open("/www/about.html", "w") as f:
            f.write(head1 + about_selected + head2 + about_content + end)

    #Create reset.html
    if 'reset.html' not in d:
        with open("/www/reset.html", "w") as f:
            f.write(head1 + reset_selected + head2 + reset_content + end)

    #Create status.pyhtml
    if 'status.pyhtml' not in d:
        with open("/www/status.pyhtml", "w") as f:
            f.write(head1 + status_selected + head2 + status_content + end)

    #Create Ruuvi Eye SVG
    if 're.svg' not in d:
        with open("/www/re.svg", "w") as f:
            f.write("""\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 999.97 1000"><defs><style>.a{fill:#fff;}.b{fill:#160d0d;}</style></defs><title>web-ruuvi-eye</title><path class="a" d="M952.87,497.93c0,246.23-203.82,445.84-455.2,445.84S42.44,744.16,42.44,497.93,246.26,52.1,497.67,52.1,952.87,251.71,952.87,497.93Z" transform="translate(0.29 -0.1)"/><path class="b" d="M499.69,94.36A405.73,405.73,0,1,1,94,500.08,405,405,0,0,1,499.69,94.36Zm0-94.26c-275.58,0-500,224.4-500,500s224.41,500,500,500,500-224.44,500-500S775.27.1,499.69.1Z" transform="translate(0.29 -0.1)"/><path class="b" d="M603.54,762.73c81.07-7.7,153.35-52.23,197.23-121.59,11.14-17.58,23.29-44.56,29.16-64.74C844,528,843.45,472.59,828.37,424.85S781.88,331,743.45,300.25A261.72,261.72,0,0,0,517.34,250c-6.55,1.6-12.26,3-12.67,3.15s.8,3.52,2.73,7.54a174.32,174.32,0,0,1,14.5,47.86c1.67,10.87,1.7,36.69,0,48.18-8.6,59.7-49.37,111.58-105,133.71-26.46,10.52-60.66,14.63-86.39,10.4-4.91-.8-9.56-1.48-10.33-1.48-1.16,0-1.28,2.44-.8,14.69a260.41,260.41,0,0,0,124.6,211.54c34.39,21.07,71.19,33.07,114.63,37.44,8,.8,35,.57,44.95-.35Z" transform="translate(0.29 -0.1)"/></svg>""")

    #Create Ruuvi Eye Neg SVG
    if 'ren.svg' not in d:
        with open("/www/ren.svg", "w") as f:
            f.write("""\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 999.56 1000"><defs><style>.a{fill:#fff;}</style></defs><title>web-ruuvi-eye-nega</title><path class="a" d="M499.59,2C223.56,2-.22,225.81-.25,501.95S223.46,1002,499.48,1002,999.23,778.26,999.32,502.16C999.78,226.42,776.72,2.51,501.1,2.05h-1.51M603,829.42c-174.61,0-316.64-140.69-318.36-315.37a216.85,216.85,0,0,0,70.71,11.63c121.74,0,220.43-98.72,220.44-220.51A220.6,220.6,0,0,0,547.46,197,328.75,328.75,0,0,1,603,191.8c175.87,0,318.44,142.63,318.44,318.58S778.86,829,603,829" transform="translate(0.25 -2)"/></svg>""")

    #Create Ruuvi Logo Neg SVG
    if 'rln.svg' not in d:
        with open("/www/rln.svg", "w") as f:
            f.write("""\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1928.63 388.38"><defs><style>.a{fill:#fff;}</style></defs><title>web-ruuvi-logo-nega</title><path class="a" d="M1717.63,347C1610.7,347,1524,433.7,1524,540.67s86.66,193.7,193.59,193.71,193.6-86.67,193.63-193.63S1825,347.2,1718.22,347h-.59m40.06,320.51a123.36,123.36,0,0,1-123.33-122.17,84,84,0,0,0,27.39,4.51,85.43,85.43,0,0,0,74.42-127.32,127.35,127.35,0,0,1,21.51-2,123.41,123.41,0,0,1,0,246.83" transform="translate(17.41 -346.01)"/><path class="a" d="M1375.08,733.14c-10.88-1.07-22.46-6.66-28.68-13.65a40.93,40.93,0,0,1-9-18.36c-1.52-6.74-1.15-9.88-1.15-83.56,0-88.33,0-80.32,4.76-93.11a43.68,43.68,0,0,1,17-17.37,55.7,55.7,0,0,1,32.63-5.14c24.27,2.79,35.55,14.39,37.69,38.87.43,5,.61,33.45.53,81.41-.28,73.23-.28,69.79-1.7,78.7-3.67,13-10.8,22-22.12,27.66-7.37,3.68-19.44,5.47-29.84,4.49Zm-614.62,0c-43.61-2-81.38-19.76-110.33-51.38A152.59,152.59,0,0,1,611,602c-2.61-15.29-2.88-26.44-2.61-123.4.26-104-1-92.58,5.29-106.59a42.09,42.09,0,0,1,27.51-21.74,68.45,68.45,0,0,1,27.43.43,43.72,43.72,0,0,1,31.21,32c1,3.77,1.17,12.84,1.44,102.53l.43,98.4c1.09,20.43,13.59,37.54,27.79,46.42,22,15.65,54,14.92,77,1.17,19.16-12.86,30.38-31.85,32.73-52.19.43-3.77.71-40.74.71-99,0-103.17-.28-97.67,4.33-107.12A44,44,0,0,1,873,349.66a75.71,75.71,0,0,1,27,0,44.49,44.49,0,0,1,19.44,10.61c8,7.55,12.07,16.56,12.68,23.22v102c0,114.61.28,108.68-5,129.15A157.08,157.08,0,0,1,875.94,696C844.6,723,806.22,735.22,760.46,733.14Zm-738.82,0C10.68,732.08-1,726.48-7,719.49a53.12,53.12,0,0,1-9.07-18.36c-1.64-7.47-1.26-10.89-1.26-105,0-78.62.18-101.92.89-107.4C-12,452.87,2,422.91,26.14,397.86c30.2-31.48,67-47.86,111.38-49.56,12.15-.55,18,.16,25.08,2.79a45.1,45.1,0,0,1,24.91,24.46,55.35,55.35,0,0,1,3.24,22c-1.26,19.76-9.88,32.37-26.51,38.69a85.51,85.51,0,0,1-21.13,4.58c-14,1.7-21,3.68-31,8.81a68.16,68.16,0,0,0-30.22,29.5A91.51,91.51,0,0,0,76.67,494c-1.44,8.36-.89,26.79-1.26,102.36.55,88.7.81,95.52-1.8,104.61-3.67,13.12-10.71,21.85-22.12,27.66C44.14,732.33,32.15,734.13,21.64,733.14Zm1071.84-27.66c-3.16-6.38-117.72-297.09-119.24-302.76a37,37,0,0,1,0-22.59c4.68-15.29,18.88-28,35.24-31.75,10.88-2.33,24.65-.81,33.44,3.77a46.09,46.09,0,0,1,15.47,15.37c3,5,2.63,4.05,44.7,111.11,16.37,41.5,29.92,75.09,30.1,74.93s16.37-41,35.89-90.6c25-63.51,36.42-91.75,38.57-95.36a40.37,40.37,0,0,1,26-19.33,62.66,62.66,0,0,1,27.24,1.34A47.4,47.4,0,0,1,1281,362.49a36.56,36.56,0,0,1,10.88,18.26,36,36,0,0,1,0,21.22c-1.26,5.3-115,294.42-119.32,303.3-17.24,40.39-65.26,32.74-79.1.28Z" transform="translate(17.41 -346.01)"/><path class="a" d="M390.81,733.89c-43.59-2-81.28-19.62-110.33-51.38a153.7,153.7,0,0,1-39.11-79.69c-2.61-15.29-2.78-26.52-2.61-123.4.28-104-1-92.58,5.39-106.7a41.86,41.86,0,0,1,27.55-21.64,66.67,66.67,0,0,1,27.32.34,43.94,43.94,0,0,1,31.21,31.93c1.07,3.77,1.15,13,1.52,102.53l.38,98.5a60.21,60.21,0,0,0,27.79,46.4c22.12,15.57,53.92,14.94,77,1.17a67.17,67.17,0,0,0,25.89-28.41,68.83,68.83,0,0,0,6.93-23.85c.38-3.68.61-40.65.61-98.92,0-103.09-.26-97.71,4.33-107.14a43.85,43.85,0,0,1,28.68-23.22c6-1.7,21.13-1.7,27.06,0a45,45,0,0,1,19.34,10.71c7.9,7.49,12,16.56,12.66,23.22v101.9c0,114.61.28,108.68-4.92,129.15a157.36,157.36,0,0,1-51.16,81.49C475.09,723.7,436.69,736,390.81,733.89Z" transform="translate(17.41 -346.01)"/><path class="a" d="M1439.64,404.2a58.16,58.16,0,1,1,0-.06Z" transform="translate(17.41 -346.01)"/></svg>""")

    if 'prue-min.css' not in d:
        with open("/www/pure-min.css", "w") as f:
            f.write("""\
/*!
Pure v1.0.1
Copyright 2013 Yahoo!
Licensed under the BSD License.
https://github.com/pure-css/pure/blob/master/LICENSE.md
*/
/*!
normalize.css v^3.0 | MIT License | git.io/normalize
Copyright (c) Nicolas Gallagher and Jonathan Neal
*/
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background-color:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:1px dotted}b,strong{font-weight:700}dfn{font-style:italic}h1{font-size:2em;margin:.67em 0}mark{background:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-.5em}sub{bottom:-.25em}img{border:0}svg:not(:root){overflow:hidden}figure{margin:1em 40px}hr{-webkit-box-sizing:content-box;box-sizing:content-box;height:0}pre{overflow:auto}code,kbd,pre,samp{font-family:monospace,monospace;font-size:1em}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type=button],input[type=reset],input[type=submit]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type=checkbox],input[type=radio]{-webkit-box-sizing:border-box;box-sizing:border-box;padding:0}input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{height:auto}input[type=search]{-webkit-appearance:textfield;-webkit-box-sizing:content-box;box-sizing:content-box}input[type=search]::-webkit-search-cancel-button,input[type=search]::-webkit-search-decoration{-webkit-appearance:none}fieldset{border:1px solid silver;margin:0 2px;padding:.35em .625em .75em}legend{border:0;padding:0}textarea{overflow:auto}optgroup{font-weight:700}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}.hidden,[hidden]{display:none!important}.pure-img{max-width:100%;height:auto;display:block}.pure-g{letter-spacing:-.31em;text-rendering:optimizespeed;font-family:FreeSans,Arimo,"Droid Sans",Helvetica,Arial,sans-serif;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-flow:row wrap;-ms-flex-flow:row wrap;flex-flow:row wrap;-webkit-align-content:flex-start;-ms-flex-line-pack:start;align-content:flex-start}@media all and (-ms-high-contrast:none),(-ms-high-contrast:active){table .pure-g{display:block}}.opera-only :-o-prefocus,.pure-g{word-spacing:-.43em}.pure-u{display:inline-block;zoom:1;letter-spacing:normal;word-spacing:normal;vertical-align:top;text-rendering:auto}.pure-g [class*=pure-u]{font-family:sans-serif}.pure-u-1,.pure-u-1-1,.pure-u-1-12,.pure-u-1-2,.pure-u-1-24,.pure-u-1-3,.pure-u-1-4,.pure-u-1-5,.pure-u-1-6,.pure-u-1-8,.pure-u-10-24,.pure-u-11-12,.pure-u-11-24,.pure-u-12-24,.pure-u-13-24,.pure-u-14-24,.pure-u-15-24,.pure-u-16-24,.pure-u-17-24,.pure-u-18-24,.pure-u-19-24,.pure-u-2-24,.pure-u-2-3,.pure-u-2-5,.pure-u-20-24,.pure-u-21-24,.pure-u-22-24,.pure-u-23-24,.pure-u-24-24,.pure-u-3-24,.pure-u-3-4,.pure-u-3-5,.pure-u-3-8,.pure-u-4-24,.pure-u-4-5,.pure-u-5-12,.pure-u-5-24,.pure-u-5-5,.pure-u-5-6,.pure-u-5-8,.pure-u-6-24,.pure-u-7-12,.pure-u-7-24,.pure-u-7-8,.pure-u-8-24,.pure-u-9-24{display:inline-block;zoom:1;letter-spacing:normal;word-spacing:normal;vertical-align:top;text-rendering:auto}.pure-u-1-24{width:4.1667%}.pure-u-1-12,.pure-u-2-24{width:8.3333%}.pure-u-1-8,.pure-u-3-24{width:12.5%}.pure-u-1-6,.pure-u-4-24{width:16.6667%}.pure-u-1-5{width:20%}.pure-u-5-24{width:20.8333%}.pure-u-1-4,.pure-u-6-24{width:25%}.pure-u-7-24{width:29.1667%}.pure-u-1-3,.pure-u-8-24{width:33.3333%}.pure-u-3-8,.pure-u-9-24{width:37.5%}.pure-u-2-5{width:40%}.pure-u-10-24,.pure-u-5-12{width:41.6667%}.pure-u-11-24{width:45.8333%}.pure-u-1-2,.pure-u-12-24{width:50%}.pure-u-13-24{width:54.1667%}.pure-u-14-24,.pure-u-7-12{width:58.3333%}.pure-u-3-5{width:60%}.pure-u-15-24,.pure-u-5-8{width:62.5%}.pure-u-16-24,.pure-u-2-3{width:66.6667%}.pure-u-17-24{width:70.8333%}.pure-u-18-24,.pure-u-3-4{width:75%}.pure-u-19-24{width:79.1667%}.pure-u-4-5{width:80%}.pure-u-20-24,.pure-u-5-6{width:83.3333%}.pure-u-21-24,.pure-u-7-8{width:87.5%}.pure-u-11-12,.pure-u-22-24{width:91.6667%}.pure-u-23-24{width:95.8333%}.pure-u-1,.pure-u-1-1,.pure-u-24-24,.pure-u-5-5{width:100%}.pure-button{display:inline-block;zoom:1;line-height:normal;white-space:nowrap;vertical-align:middle;text-align:center;cursor:pointer;-webkit-user-drag:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-box-sizing:border-box;box-sizing:border-box}.pure-button::-moz-focus-inner{padding:0;border:0}.pure-button-group{letter-spacing:-.31em;text-rendering:optimizespeed}.opera-only :-o-prefocus,.pure-button-group{word-spacing:-.43em}.pure-button-group .pure-button{letter-spacing:normal;word-spacing:normal;vertical-align:top;text-rendering:auto}.pure-button{font-family:inherit;font-size:100%;padding:.5em 1em;color:#444;color:rgba(0,0,0,.8);border:1px solid #999;border:none transparent;background-color:#e6e6e6;text-decoration:none;border-radius:2px}.pure-button-hover,.pure-button:focus,.pure-button:hover{background-image:-webkit-gradient(linear,left top,left bottom,from(transparent),color-stop(40%,rgba(0,0,0,.05)),to(rgba(0,0,0,.1)));background-image:-webkit-linear-gradient(transparent,rgba(0,0,0,.05) 40%,rgba(0,0,0,.1));background-image:linear-gradient(transparent,rgba(0,0,0,.05) 40%,rgba(0,0,0,.1))}.pure-button:focus{outline:0}.pure-button-active,.pure-button:active{-webkit-box-shadow:0 0 0 1px rgba(0,0,0,.15) inset,0 0 6px rgba(0,0,0,.2) inset;box-shadow:0 0 0 1px rgba(0,0,0,.15) inset,0 0 6px rgba(0,0,0,.2) inset;border-color:#000}.pure-button-disabled,.pure-button-disabled:active,.pure-button-disabled:focus,.pure-button-disabled:hover,.pure-button[disabled]{border:none;background-image:none;opacity:.4;cursor:not-allowed;-webkit-box-shadow:none;box-shadow:none;pointer-events:none}.pure-button-hidden{display:none}.pure-button-primary,.pure-button-selected,a.pure-button-primary,a.pure-button-selected{background-color:#0078e7;color:#fff}.pure-button-group .pure-button{margin:0;border-radius:0;border-right:1px solid #111;border-right:1px solid rgba(0,0,0,.2)}.pure-button-group .pure-button:first-child{border-top-left-radius:2px;border-bottom-left-radius:2px}.pure-button-group .pure-button:last-child{border-top-right-radius:2px;border-bottom-right-radius:2px;border-right:none}.pure-form input[type=color],.pure-form input[type=date],.pure-form input[type=datetime-local],.pure-form input[type=datetime],.pure-form input[type=email],.pure-form input[type=month],.pure-form input[type=number],.pure-form input[type=password],.pure-form input[type=search],.pure-form input[type=tel],.pure-form input[type=text],.pure-form input[type=time],.pure-form input[type=url],.pure-form input[type=week],.pure-form select,.pure-form textarea{padding:.5em .6em;display:inline-block;border:1px solid #ccc;-webkit-box-shadow:inset 0 1px 3px #ddd;box-shadow:inset 0 1px 3px #ddd;border-radius:4px;vertical-align:middle;-webkit-box-sizing:border-box;box-sizing:border-box}.pure-form input:not([type]){padding:.5em .6em;display:inline-block;border:1px solid #ccc;-webkit-box-shadow:inset 0 1px 3px #ddd;box-shadow:inset 0 1px 3px #ddd;border-radius:4px;-webkit-box-sizing:border-box;box-sizing:border-box}.pure-form input[type=color]{padding:.2em .5em}.pure-form input[type=color]:focus,.pure-form input[type=date]:focus,.pure-form input[type=datetime-local]:focus,.pure-form input[type=datetime]:focus,.pure-form input[type=email]:focus,.pure-form input[type=month]:focus,.pure-form input[type=number]:focus,.pure-form input[type=password]:focus,.pure-form input[type=search]:focus,.pure-form input[type=tel]:focus,.pure-form input[type=text]:focus,.pure-form input[type=time]:focus,.pure-form input[type=url]:focus,.pure-form input[type=week]:focus,.pure-form select:focus,.pure-form textarea:focus{outline:0;border-color:#129fea}.pure-form input:not([type]):focus{outline:0;border-color:#129fea}.pure-form input[type=checkbox]:focus,.pure-form input[type=file]:focus,.pure-form input[type=radio]:focus{outline:thin solid #129fea;outline:1px auto #129fea}.pure-form .pure-checkbox,.pure-form .pure-radio{margin:.5em 0;display:block}.pure-form input[type=color][disabled],.pure-form input[type=date][disabled],.pure-form input[type=datetime-local][disabled],.pure-form input[type=datetime][disabled],.pure-form input[type=email][disabled],.pure-form input[type=month][disabled],.pure-form input[type=number][disabled],.pure-form input[type=password][disabled],.pure-form input[type=search][disabled],.pure-form input[type=tel][disabled],.pure-form input[type=text][disabled],.pure-form input[type=time][disabled],.pure-form input[type=url][disabled],.pure-form input[type=week][disabled],.pure-form select[disabled],.pure-form textarea[disabled]{cursor:not-allowed;background-color:#eaeded;color:#cad2d3}.pure-form input:not([type])[disabled]{cursor:not-allowed;background-color:#eaeded;color:#cad2d3}.pure-form input[readonly],.pure-form select[readonly],.pure-form textarea[readonly]{background-color:#eee;color:#777;border-color:#ccc}.pure-form input:focus:invalid,.pure-form select:focus:invalid,.pure-form textarea:focus:invalid{color:#b94a48;border-color:#e9322d}.pure-form input[type=checkbox]:focus:invalid:focus,.pure-form input[type=file]:focus:invalid:focus,.pure-form input[type=radio]:focus:invalid:focus{outline-color:#e9322d}.pure-form select{height:2.25em;border:1px solid #ccc;background-color:#fff}.pure-form select[multiple]{height:auto}.pure-form label{margin:.5em 0 .2em}.pure-form fieldset{margin:0;padding:.35em 0 .75em;border:0}.pure-form legend{display:block;width:100%;padding:.3em 0;margin-bottom:.3em;color:#333;border-bottom:1px solid #e5e5e5}.pure-form-stacked input[type=color],.pure-form-stacked input[type=date],.pure-form-stacked input[type=datetime-local],.pure-form-stacked input[type=datetime],.pure-form-stacked input[type=email],.pure-form-stacked input[type=file],.pure-form-stacked input[type=month],.pure-form-stacked input[type=number],.pure-form-stacked input[type=password],.pure-form-stacked input[type=search],.pure-form-stacked input[type=tel],.pure-form-stacked input[type=text],.pure-form-stacked input[type=time],.pure-form-stacked input[type=url],.pure-form-stacked input[type=week],.pure-form-stacked label,.pure-form-stacked select,.pure-form-stacked textarea{display:block;margin:.25em 0}.pure-form-stacked input:not([type]){display:block;margin:.25em 0}.pure-form-aligned .pure-help-inline,.pure-form-aligned input,.pure-form-aligned select,.pure-form-aligned textarea,.pure-form-message-inline{display:inline-block;vertical-align:middle}.pure-form-aligned textarea{vertical-align:top}.pure-form-aligned .pure-control-group{margin-bottom:.5em}.pure-form-aligned .pure-control-group label{text-align:right;display:inline-block;vertical-align:middle;width:10em;margin:0 1em 0 0}.pure-form-aligned .pure-controls{margin:1.5em 0 0 11em}.pure-form .pure-input-rounded,.pure-form input.pure-input-rounded{border-radius:2em;padding:.5em 1em}.pure-form .pure-group fieldset{margin-bottom:10px}.pure-form .pure-group input,.pure-form .pure-group textarea{display:block;padding:10px;margin:0 0 -1px;border-radius:0;position:relative;top:-1px}.pure-form .pure-group input:focus,.pure-form .pure-group textarea:focus{z-index:3}.pure-form .pure-group input:first-child,.pure-form .pure-group textarea:first-child{top:1px;border-radius:4px 4px 0 0;margin:0}.pure-form .pure-group input:first-child:last-child,.pure-form .pure-group textarea:first-child:last-child{top:1px;border-radius:4px;margin:0}.pure-form .pure-group input:last-child,.pure-form .pure-group textarea:last-child{top:-2px;border-radius:0 0 4px 4px;margin:0}.pure-form .pure-group button{margin:.35em 0}.pure-form .pure-input-1{width:100%}.pure-form .pure-input-3-4{width:75%}.pure-form .pure-input-2-3{width:66%}.pure-form .pure-input-1-2{width:50%}.pure-form .pure-input-1-3{width:33%}.pure-form .pure-input-1-4{width:25%}.pure-form .pure-help-inline,.pure-form-message-inline{display:inline-block;padding-left:.3em;color:#666;vertical-align:middle;font-size:.875em}.pure-form-message{display:block;color:#666;font-size:.875em}@media only screen and (max-width :480px){.pure-form button[type=submit]{margin:.7em 0 0}.pure-form input:not([type]),.pure-form input[type=color],.pure-form input[type=date],.pure-form input[type=datetime-local],.pure-form input[type=datetime],.pure-form input[type=email],.pure-form input[type=month],.pure-form input[type=number],.pure-form input[type=password],.pure-form input[type=search],.pure-form input[type=tel],.pure-form input[type=text],.pure-form input[type=time],.pure-form input[type=url],.pure-form input[type=week],.pure-form label{margin-bottom:.3em;display:block}.pure-group input:not([type]),.pure-group input[type=color],.pure-group input[type=date],.pure-group input[type=datetime-local],.pure-group input[type=datetime],.pure-group input[type=email],.pure-group input[type=month],.pure-group input[type=number],.pure-group input[type=password],.pure-group input[type=search],.pure-group input[type=tel],.pure-group input[type=text],.pure-group input[type=time],.pure-group input[type=url],.pure-group input[type=week]{margin-bottom:0}.pure-form-aligned .pure-control-group label{margin-bottom:.3em;text-align:left;display:block;width:100%}.pure-form-aligned .pure-controls{margin:1.5em 0 0 0}.pure-form .pure-help-inline,.pure-form-message,.pure-form-message-inline{display:block;font-size:.75em;padding:.2em 0 .8em}}.pure-menu{-webkit-box-sizing:border-box;box-sizing:border-box}.pure-menu-fixed{position:fixed;left:0;top:0;z-index:3}.pure-menu-item,.pure-menu-list{position:relative}.pure-menu-list{list-style:none;margin:0;padding:0}.pure-menu-item{padding:0;margin:0;height:100%}.pure-menu-heading,.pure-menu-link{display:block;text-decoration:none;white-space:nowrap}.pure-menu-horizontal{width:100%;white-space:nowrap}.pure-menu-horizontal .pure-menu-list{display:inline-block}.pure-menu-horizontal .pure-menu-heading,.pure-menu-horizontal .pure-menu-item,.pure-menu-horizontal .pure-menu-separator{display:inline-block;zoom:1;vertical-align:middle}.pure-menu-item .pure-menu-item{display:block}.pure-menu-children{display:none;position:absolute;left:100%;top:0;margin:0;padding:0;z-index:3}.pure-menu-horizontal .pure-menu-children{left:0;top:auto;width:inherit}.pure-menu-active>.pure-menu-children,.pure-menu-allow-hover:hover>.pure-menu-children{display:block;position:absolute}.pure-menu-has-children>.pure-menu-link:after{padding-left:.5em;content:"\25B8";font-size:small}.pure-menu-horizontal .pure-menu-has-children>.pure-menu-link:after{content:"\25BE"}.pure-menu-scrollable{overflow-y:scroll;overflow-x:hidden}.pure-menu-scrollable .pure-menu-list{display:block}.pure-menu-horizontal.pure-menu-scrollable .pure-menu-list{display:inline-block}.pure-menu-horizontal.pure-menu-scrollable{white-space:nowrap;overflow-y:hidden;overflow-x:auto;-webkit-overflow-scrolling:touch;padding:.5em 0}.pure-menu-horizontal .pure-menu-children .pure-menu-separator,.pure-menu-separator{background-color:#ccc;height:1px;margin:.3em 0}.pure-menu-horizontal .pure-menu-separator{width:1px;height:1.3em;margin:0 .3em}.pure-menu-horizontal .pure-menu-children .pure-menu-separator{display:block;width:auto}.pure-menu-heading{text-transform:uppercase;color:#565d64}.pure-menu-link{color:#777}.pure-menu-children{background-color:#fff}.pure-menu-disabled,.pure-menu-heading,.pure-menu-link{padding:.5em 1em}.pure-menu-disabled{opacity:.5}.pure-menu-disabled .pure-menu-link:hover{background-color:transparent}.pure-menu-active>.pure-menu-link,.pure-menu-link:focus,.pure-menu-link:hover{background-color:#eee}.pure-menu-selected>.pure-menu-link,.pure-menu-selected>.pure-menu-link:visited{color:#000}.pure-table{border-collapse:collapse;border-spacing:0;empty-cells:show;border:1px solid #cbcbcb}.pure-table caption{color:#000;font:italic 85%/1 arial,sans-serif;padding:1em 0;text-align:center}.pure-table td,.pure-table th{border-left:1px solid #cbcbcb;border-width:0 0 0 1px;font-size:inherit;margin:0;overflow:visible;padding:.5em 1em}.pure-table thead{background-color:#e0e0e0;color:#000;text-align:left;vertical-align:bottom}.pure-table td{background-color:transparent}.pure-table-odd td{background-color:#f2f2f2}.pure-table-striped tr:nth-child(2n-1) td{background-color:#f2f2f2}.pure-table-bordered td{border-bottom:1px solid #cbcbcb}.pure-table-bordered tbody>tr:last-child>td{border-bottom-width:0}.pure-table-horizontal td,.pure-table-horizontal th{border-width:0 0 1px 0;border-bottom:1px solid #cbcbcb}.pure-table-horizontal tbody>tr:last-child>td{border-bottom-width:0}""")

    if 'side-menu.css' not in d:
        with open("/www/side-menu.css", "w") as f:
            f.write("""\
body {
    color: #777;
}

.pure-img-responsive {
    max-width: 100%;
    height: auto;
}

.pure-img-responsive-padding {
    max-width: 85%;
    height: auto;
    padding: 5px 5px 0px 5px;
}

.ruuvi-eye {
    position:fixed;
    bottom:10px;
    right:10px;
    max-height: 10%;
    max-width: 10%;
    float: right;
    padding:15px 15px 15px 15px;
    transform: rotate(-360deg);
    transition: all 1s ease-in-out 0s;
}

.ruuvi-eye:hover {
    transform: rotate(360deg);
    transition: all 1s ease-in-out 0s;
}

/*
Add transition to containers so they can push in and out.
*/
#layout,
#menu,
.menu-link {
    -webkit-transition: all 0.2s ease-out;
    -moz-transition: all 0.2s ease-out;
    -ms-transition: all 0.2s ease-out;
    -o-transition: all 0.2s ease-out;
    transition: all 0.2s ease-out;
}

/*
This is the parent `<div>` that contains the menu and the content area.
*/
#layout {
    position: relative;
    left: 0;
    padding-left: 0;
}
    #layout.active #menu {
        left: 150px;
        width: 150px;
    }

    #layout.active .menu-link {
        left: 150px;
    }
/*
The content `<div>` is where all your content goes.
*/
.content {
    margin: 0 auto;
    padding: 0 2em;
    max-width: 800px;
    margin-bottom: 50px;
    line-height: 1.6em;
}

.header {
     margin: 0;
     color: #333;
     text-align: center;
     padding: 2.5em 2em 0;
     border-bottom: 1px solid #eee;
 }
    .header h1 {
        margin: 0.2em 0;
        font-size: 3em;
        font-weight: 300;
    }
     .header h2 {
        font-weight: 300;
        color: #ccc;
        padding: 0;
        margin-top: 0;
    }

.content-subhead {
    margin: 50px 0 20px 0;
    font-weight: 300;
    color: #888;
}



/*
The `#menu` `<div>` is the parent `<div>` that contains the `.pure-menu` that
appears on the left side of the page.
*/

#menu {
    margin-left: -150px; /* "#menu" width */
    width: 150px;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    z-index: 1000; /* so the menu or its navicon stays above all content */
    background: #191818;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
}
    /*
    All anchors inside the menu should be styled like this.
    */
    #menu a {
        color: #999;
        border: none;
        padding: 0.6em 0 0.6em 0.6em;
    }

    /*
    Remove all background/borders, since we are applying them to #menu.
    */
     #menu .pure-menu,
     #menu .pure-menu ul {
        border: none;
        background: transparent;
    }

    /*
    Add that light border to separate items into groups.
    */
    #menu .pure-menu ul,
    #menu .pure-menu .menu-item-divided {
        border-top: 1px solid #333;
    }
        /*
        Change color of the anchor links on hover/focus.
        */
        #menu .pure-menu li a:hover,
        #menu .pure-menu li a:focus {
            background: #333;
        }

    /*
    This styles the selected menu item `<li>`.
    */
    #menu .pure-menu-selected,
    #menu .pure-menu-heading {
        background: #1f8dd6;
    }
        /*
        This styles a link within a selected menu item `<li>`.
        */
        #menu .pure-menu-selected a {
            color: #fff;
        }

    /*
    This styles the menu heading.
    */
    #menu .pure-menu-heading {
        font-size: 110%;
        color: #fff;
        margin: 0;
    }

/* -- Dynamic Button For Responsive Menu -------------------------------------*/

/*
The button to open/close the Menu is custom-made and not part of Pure. Here's
how it works:
*/

/*
`.menu-link` represents the responsive menu toggle that shows/hides on
small screens.
*/
.menu-link {
    position: fixed;
    display: block; /* show this only on small screens */
    top: 0;
    left: 0; /* "#menu width" */
    background: #000;
    background: rgba(0,0,0,0.7);
    font-size: 10px; /* change this value to increase/decrease button size */
    z-index: 10;
    width: 2em;
    height: auto;
    padding: 2.1em 1.6em;
}

    .menu-link:hover,
    .menu-link:focus {
        background: #000;
    }

    .menu-link span {
        position: relative;
        display: block;
    }

    .menu-link span,
    .menu-link span:before,
    .menu-link span:after {
        background-color: #fff;
        width: 100%;
        height: 0.2em;
    }

        .menu-link span:before,
        .menu-link span:after {
            position: absolute;
            margin-top: -0.6em;
            content: " ";
        }

        .menu-link span:after {
            margin-top: 0.6em;
        }


/* -- Responsive Styles (Media Queries) ------------------------------------- */

/*
Hides the menu at `48em`, but modify this based on your app's needs.
*/
@media (min-width: 48em) {

    .header,
    .content {
        padding-left: 2em;
        padding-right: 2em;
    }

    #layout {
        padding-left: 150px; /* left col width "#menu" */
        left: 0;
    }
    #menu {
        left: 150px;
    }

    .menu-link {
        position: fixed;
        left: 150px;
        display: none;
    }

    #layout.active .menu-link {
        left: 150px;
    }
}

@media (max-width: 48em) {
    /* Only apply this when the window is small. Otherwise, the following
    case results in extra padding on the left:
        * Make the window small.
        * Tap the menu to trigger the active state.
        * Make the window large again.
    */
    #layout.active {
        position: relative;
        left: 150px;
    }
}
""")

    if '/ui.js' not in d:
        with open("/www/ui.js", "w") as f:
            f.write("""\
(function (window, document) {

    var layout   = document.getElementById('layout'),
        menu     = document.getElementById('menu'),
        menuLink = document.getElementById('menuLink'),
        content  = document.getElementById('main');

    function toggleClass(element, className) {
        var classes = element.className.split(/\s+/),
            length = classes.length,
            i = 0;

        for(; i < length; i++) {
          if (classes[i] === className) {
            classes.splice(i, 1);
            break;
          }
        }
        // The className is not found
        if (length === classes.length) {
            classes.push(className);
        }

        element.className = classes.join(' ');
    }

    function toggleAll(e) {
        var active = 'active';

        e.preventDefault();
        toggleClass(layout, active);
        toggleClass(menu, active);
        toggleClass(menuLink, active);
    }

    menuLink.onclick = function (e) {
        toggleAll(e);
    };

    content.onclick = function(e) {
        if (menu.className.indexOf('active') !== -1) {
            toggleAll(e);
        }
    };

}(this, this.document));""")

def create():
    d = uos.listdir()
    if 'www' not in d:
        create_www()
        fill_www()
    else:
        fill_www()
