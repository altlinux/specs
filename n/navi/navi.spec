Name: navi
Version: 0.18.3
Release: alt1

Summary: An interactive cheatsheet tool for the command-line

License: Apache 2.0
Group: Other
Url: https://github.com/denisidoro/navi

# Source-url: https://github.com/denisidoro/navi/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%description
An interactive cheatsheet tool for the command-line
so that you won't say the following anymore:

- How to run that command again?
- Oh, it's not in my shell history
- Geez, it's almost what I wanted but I need to change some args

%prep
%setup

%build
# Nothing to do

%install
mkdir -p %buildroot%_bindir
cat <<EOF >%buildroot%_bindir/%name
#!/usr/bin/env bash
%_datadir/%name/navi "\$@"
EOF
chmod 0755 %buildroot%_bindir/%name

#scripts/install %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name/
cp -a cheats src navi navi.plugin*  %buildroot%_datadir/%name/

%files
%doc README.md
%_bindir/%name
%_datadir/%name

%changelog
* Sun Feb 16 2020 Vitaly Lipatov <lav@altlinux.ru> 0.18.3-alt1
- initial build for ALT Sisyphus
