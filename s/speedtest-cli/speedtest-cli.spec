%define name speedtest-cli
%define version 0.3.4
%define release alt2

%setup_python_module %name

Summary: Network bandwidth testing tool
Name: %name
Version: %version
Release: %release
Source: %name-%version.tar
Patch: %name-%version-%release.patch
License: Apache2
Group: System/Configuration/Networking
Url: https://github.com/sivel/speedtest-cli

Packager: L.A. Kostis <lakostis@altlinux.org>

BuildArch: noarch

%description
Command line interface for testing internet bandwidth using
speedtest.net

%prep
%setup -q
%patch -p1

%build
%install
mkdir -p %buildroot%_bindir
install speedtest_cli.py %buildroot%_bindir/%name

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=speedtest-cli
Comment=CLI for speedtest.net
Icon=%name
Exec=%name
Terminal=true
Categories=Settings;HardwareSettings;
EOF


%files
%_bindir/*
%doc README.rst CONTRIBUTING.md
%_desktopdir/%name.desktop

%changelog
* Sun Oct 30 2016 L.A. Kostis <lakostis@altlinux.ru> 0.3.4-alt2
- Use correct naming during install.

* Wed Oct 19 2016 L.A. Kostis <lakostis@altlinux.ru> 0.3.4-alt1
- 0.3.4.

* Mon Sep 14 2015 L.A. Kostis <lakostis@altlinux.ru> 0.3.2-alt1
- initial build for ALTLinux.
