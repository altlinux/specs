# vim: set ft=spec: -*- rpm-spec -*-

Name: wmwifi
Version: 0.6
Release: alt1

Summary: A wireless network signal stength monitor for Window Maker
Group: Graphical desktop/Window Maker
License: GPL
Url: http://wmwifi.digitalssg.net/

Packager: Sir Raorn <raorn@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Thu Feb 22 2007
BuildRequires: libICE-devel libXext-devel libXpm-devel

%description
wmwifi is a wireless network interface monitor dockapp for the
Window Maker desktop. It is designed to fit well with dockapps like
wmcpuload and wmnetload.  wmwifi relys on the Wireless Exntension
being enabled in the kernel.

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
%__install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc AUTHORS README ChangeLog
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Thu Feb 22 2007 Sir Raorn <raorn@altlinux.ru> 0.6-alt1
- Built for Sisyphus

