%define _libexecdir %_prefix/libexec

%def_disable server

Name: obexd
Version: 0.41
Release: alt1
Summary: D-Bus service for Obex Client access
Group: System/Servers
License: GPLv2+
Url: http://www.bluez.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

%if_enabled server
Provides: obex-data-server
%endif

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: glib2-devel libbluez-devel libdbus-devel libical-devel libopenobex-devel

%description
obexd contains obex-client, a D-Bus service to allow sending files
using the Obex Push protocol, common on mobile phones and other
Bluetooth-equipped devices

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--libexecdir=%_libexecdir \
	%{subst_enable server}

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README ChangeLog AUTHORS doc/*.txt
%_libexecdir/obex*
%_datadir/dbus-1/services/obex*.service

%changelog
* Mon Jun 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.41-alt1
- 0.41

* Sat Jan 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.40-alt1
- 0.40

* Sun Jan 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.39-alt1
- 0.39

* Tue Dec 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.38-alt1
- 0.38

* Mon Nov 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.37-alt1
- 0.37

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.36-alt1
- 0.36

* Fri Oct 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.35-alt1
- 0.35

* Wed Oct 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.34-alt1
- 0.34

* Thu Sep 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.33-alt1
- 0.33

* Thu Aug 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.32-alt1
- 0.32

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.31-alt1
- 0.31

* Sun Jul 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.29-alt1
- 0.29

* Tue Jun 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.28-alt1
- 0.28

* Mon Jun 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.27-alt1
- 0.27

* Thu May 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.26-alt1
- 0.26

* Mon May 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.25-alt1
- 0.25

* Sat May 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.24-alt1
- 0.24

* Sat Apr 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.23-alt1
- 0.23

* Mon Mar 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.22-alt1
- 0.22

* Tue Dec 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.21-alt1
- 0.21

* Sat Dec 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.20-alt1
- 0.20

* Thu Nov 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.19-alt1
- 0.19

* Sat Sep 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.18-alt1
- 0.18

* Mon Aug 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.17-alt1
- 0.17

* Mon Aug 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt1
- 0.16

* Thu Jul 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.15-alt1
- 0.15

* Sat Jul 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.14-alt1
- 0.14

* Thu Jun 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13-alt1
- initial release
