Name: kvmd-oled
Version: 0.19
Release: alt1

Summary: PiKVM - A small OLED daemon
License: GPLv3
Group: System/Servers
Url: https://pikvm.org/

Requires: python3(luma.oled)
Requires: fonts-ttf-grimmer-proggy-tinysz

Source: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-python3

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%_unitdir %buildroot%_datadir/kvmd-oled
install -pm0755 -D kvmd-oled.py %buildroot%_bindir/kvmd-oled
install -pm0644 *.service %buildroot%_unitdir/
install -pm0644 *.ppm %buildroot%_datadir/kvmd-oled/

%files
%_unitdir/*.service
%_bindir/kvmd-oled
%_datadir/kvmd-oled

%changelog
* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19-alt1
- 0.19 released
