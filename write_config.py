# python 3.x
from configparser import ConfigParser

config = ConfigParser()

config.add_section('main')
config.set('main', 'CLIENT_ID', 'FAKE_CLIENT_ID')
config.set('main', 'REDIRECT_URI', 'FAKE_REDIRECT_URL')
config.set('main', 'JSON_PATH', 'FAKE_PATH')
config.set('main', 'ACCOUNT_NUMBER', 'FAKE_ACCT')

with open(file='config/config.ini', mode='w') as f:
    config.write(f)
    
    .highlight table td { padding: 5px; }
.highlight table pre { margin: 0; }
.highlight {
  color: #FFFFFF;
  background-color: #231529;
}
.highlight .c, .highlight .cd, .highlight .cm, .highlight .c1, .highlight .cs {
  color: #6D6E70;
  font-style: italic;
}
.highlight .cp {
  color: #41ff5b;
  font-weight: bold;
  font-style: italic;
}
.highlight .err {
  color: #FFFFFF;
  background-color: #CC0000;
}
.highlight .gr {
  color: #FFFFFF;
  background-color: #CC0000;
}
.highlight .k, .highlight .kd, .highlight .kv {
  color: #FFF02A;
  font-weight: bold;
}
.highlight .o, .highlight .ow {
  color: #41ff5b;
}
.highlight .p, .highlight .pi {
  color: #41ff5b;
}
.highlight .gd {
  color: #CC0000;
}
.highlight .gi {
  color: #3FB34F;
}
.highlight .ge {
  font-style: italic;
}
.highlight .gs {
  font-weight: bold;
}
.highlight .gt {
  color: #FFFFFF;
  background-color: #766DAF;
}
.highlight .gl {
  color: #FFFFFF;
  background-color: #766DAF;
}
.highlight .kc {
  color: #9f93e6;
  font-weight: bold;
}
.highlight .kn {
  color: #FFFFFF;
  font-weight: bold;
}
.highlight .kp {
  color: #FFFFFF;
  font-weight: bold;
}
.highlight .kr {
  color: #FFFFFF;
  font-weight: bold;
}
.highlight .gh {
  color: #FFFFFF;
  font-weight: bold;
}
.highlight .gu {
  color: #FFFFFF;
  font-weight: bold;
}
.highlight .kt {
  color: #FAAF4C;
  font-weight: bold;
}
.highlight .no {
  color: #FAAF4C;
  font-weight: bold;
}
.highlight .nc {
  color: #FAAF4C;
  font-weight: bold;
}
.highlight .nd {
  color: #FAAF4C;
  font-weight: bold;
}
.highlight .nn {
  color: #FAAF4C;
  font-weight: bold;
}
.highlight .bp {
  color: #FAAF4C;
  font-weight: bold;
}
.highlight .ne {
  color: #FAAF4C;
  font-weight: bold;
}
.highlight .nl {
  color: #9f93e6;
  font-weight: bold;
}
.highlight .nt {
  color: #9f93e6;
  font-weight: bold;
}
.highlight .m, .highlight .mf, .highlight .mh, .highlight .mi, .highlight .il, .highlight .mo, .highlight .mb, .highlight .mx {
  color: #9f93e6;
  font-weight: bold;
}
.highlight .ld {
  color: #9f93e6;
  font-weight: bold;
}
.highlight .ss {
  color: #9f93e6;
  font-weight: bold;
}
.highlight .s, .highlight .sb, .highlight .sd, .highlight .s2, .highlight .sh, .highlight .sx, .highlight .sr, .highlight .s1 {
  color: #fff0a6;
  font-weight: bold;
}
.highlight .se {
  color: #FAAF4C;
  font-weight: bold;
}
.highlight .sc {
  color: #FAAF4C;
  font-weight: bold;
}
.highlight .si {
  color: #FAAF4C;
  font-weight: bold;
}
.highlight .nb {
  font-weight: bold;
}
.highlight .ni {
  color: #999999;
  font-weight: bold;
}
.highlight .w {
  color: #BBBBBB;
}
.highlight .nf {
  color: #41ff5b;
}
.highlight .py {
  color: #41ff5b;
}
.highlight .na {
  color: #41ff5b;
}
.highlight .nv, .highlight .vc, .highlight .vg, .highlight .vi {
  color: #41ff5b;
  font-weight: bold;
}
