Name: m-ping
Version: 0.4
Release: alt2

Summary: Visual graphical ping, traceroute and whois tool
License: GPLv2
Group: Monitoring

Url: http://m-ping.sourceforge.net/
Packager: Alexandr Boltris <alex@altlinux.org>

Source: %name-%version.tar.gz
Source1: %name.desktop

# Automatically added by buildreq on Wed Dec 15 2010
BuildRequires: gcc-c++ libqt4-devel

%description
M-Ping application provides three types of operations:
- Ping
- Traceroute
- Whois
All of these operations can be executed at the same time and in multiple
instances. The results are visualized either using graphical methods or
with text output (or both) inside an MDI window. The processing itself
is based on standard external tools (e.g. for ping and traceroute)
or on internal implementation inside the application.

%prep
%setup

%build
export PATH=%_qt4dir/bin/:$PATH
%configure
%make_build all

%install
install -pD -m755 bin/m-ping %buildroot/%_bindir/%name
install -pD -m644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop
install -pD -m644 res/%name.png %buildroot/%_liconsdir/%name.png

%files
%_bindir/*
%_desktopdir/*
%_liconsdir/*
%doc README

%changelog
* Wed Dec 22 2010 Alexandr Boltris <alex@altlinux.org> 0.4-alt2
- added menu entry

* Wed Dec 15 2010 Alexandr Boltris <alex@altlinux.org> 0.4-alt1
- initial build for ALT Linux Sisyphus

