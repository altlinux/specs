%define npmver 0.9.5-a

Name: meshcommander
Version: 0.9.5a
Release: alt1

Summary: Web based Intel AMT remote management console

License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/Ylianst/MeshCommander

# Source-url: https://registry.npmjs.org/meshcommander/-/meshcommander-%npmver.tgz
Source: %name-%version.tar
Source1: %name-production-%version.tar

BuildArch: noarch

AutoReq: yes,nonodejs,nonodejs_native,nolua,nomono,nopython,noshebang
AutoProv: no

BuildRequires: node

Requires: /usr/bin/node

%description
MeshCommander is an Intel Active Management Technology (Intel AMT)
remote management tool. It includes a built-in remote desktop viewer
for Hardware-KVM, a Serial-over-LAN terminal, IDE-Redirection support
and much more.

This package provides the MeshCommander web server: run meshcommander
and open http://127.0.0.1:3000 in a web browser.
Options: --port N to change the port, --any to listen on all interfaces.

%prep
%setup -a1

%install
mkdir -p %buildroot%_datadir/%name
# bin/ contains only an npm launcher and a prebuilt Windows DLL, not installed
cp -a *.js package.json public node_modules %buildroot%_datadir/%name/
# drop Windows/macOS file manager caches
rm -v %buildroot%_datadir/%name/public/images-commander/Thumbs.db
rm -v %buildroot%_datadir/%name/node_modules/ws/lib/.DS_Store

mkdir -p %buildroot%_bindir
cat >%buildroot%_bindir/%name <<'EOF'
#!/bin/sh
exec /usr/bin/node %_datadir/%name/meshcommander.js "$@"
EOF
chmod 0755 %buildroot%_bindir/%name

%check
grep -q "MeshCommander" public/default.htm
node -e 'require("./node_modules/express"); require("./node_modules/express-ws"); require("./node_modules/minimist")'

%files
%doc LICENSE readme.txt
%_bindir/%name
%_datadir/%name/

%changelog
* Tue Oct 13 2026 Vitaly Lipatov <lav@altlinux.ru> 0.9.5a-alt1
- initial build for Sisyphus
