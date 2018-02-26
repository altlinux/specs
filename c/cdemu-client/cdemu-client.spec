Name: cdemu-client
Version: 1.5.0
Release: alt1

Summary: A simple command-line client to control CDEmu daemon
License: GPLv2+
Group: File tools

URL: http://cdemu.sourceforge.net
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

Source0: %name-%version.tar.bz2
Source1: %name.conf

BuildRequires: intltool python-module-distribute rpm-build-gir

Requires: cdemu-daemon >= 1.5.0

%description
This is cdemu-client, a simple command-line client for controlling CDEmu daemon.
It is part of the userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator 
for linux.

It provides a way to perform the key tasks related to controlling the CDEmu
daemon, such as loading and unloading devices, displaying devices' status and
retrieving/setting devices' debug masks.

%prep
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install
install -Dp -m0644 %SOURCE1 %buildroot%_sysconfdir/%name.conf
%find_lang %name

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/cdemu
%_desktopdir/%name.desktop
%_mandir/man1/*
%_sysconfdir/%name.conf
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/cdemu-bashcomp

%changelog
* Wed Jan 25 2012 Nazarov Denis <nenderus@altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt1.1
- Rebuild with Python-2.7

* Tue Sep 20 2011 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Jan 25 2011 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt3
- Add lang files after install 

* Tue Nov 23 2010 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt2
- Fix build architecture

* Fri Nov 19 2010 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.1
- Rebuilt with python 2.6

* Fri Nov 14 2008 Nick S. Grechukh <gns@altlinux.org> 1.1.0-alt1
- first build for ALT Linux

* Sat Jun 28 2008 Rok Mandeljc <rok.mandeljc@email.si> - 1.1.0-1
- Updated to 1.1.0

* Thu Dec 20 2007 Rok Mandeljc <rok.mandeljc@email.si> - 1.0.0-1
- Initial RPM release.
