%def_with mdns
%def_with python
%def_with mono

%ifndef _qt3dir
%define _qt3dir %_libdir/qt3
%endif

%define avahi_user _avahi
%define autoipd_user _autoipd
%define avahi_group_priv netadmin
%define systemdsystemunitdir /lib/systemd/system

Name: avahi
Version: 0.6.31
Release: alt3

Summary: Local network service discovery
License: LGPL
Group: System/Servers
Url: http://www.avahi.org/

Source: %name-%version-%release.tar

Requires: %name-autoipd = %version-%release
Requires: %name-daemon = %version-%release
Requires: %name-dnsconfd = %version-%release

%if_with mdns
Obsoletes: mdnsresponder
%endif

BuildPreReq: /proc
BuildRequires: doxygen gcc-c++ glib2-devel graphviz intltool libcap-devel libdaemon-devel >= 0.13-alt2
BuildRequires: libdbus-devel libexpat-devel libgdbm-devel libgtk+2-devel
BuildRequires: libgtk+3-devel libqt3-devel libtqt-devel libqt4-devel xmltoman
%{?_with_python:BuildRequires: python-devel python-module-pygtk python-module-dbus}
%{?_with_mono:BuildRequires: libgtk-sharp2-devel mono-devel mono-mcs monodoc-devel rpm-build-mono >= 1.3.2-alt2}
BuildRequires: desktop-file-utils

%description
Avahi is a system which facilitates service discovery on
a local network -- this means that you can plug your laptop or
computer into a network and instantly be able to view other people
who you can chat with, find printers to print to or find files being
shared. This kind of technology is already found in MacOS X
(branded 'Rendezvous', 'Bonjour' and sometimes 'ZeroConf')
and is very convenient.

%package autoipd
Summary: Assigning link-local IP addresses service
Group: System/Servers
Requires(pre): shadow-utils
Conflicts: lib%name > %version-%release
Conflicts: lib%name < %version-%release

%package daemon
Summary: Local network service discovery
Group: System/Servers
Requires(pre): shadow-utils
Requires: chrooted-resolv dbus lib%name = %version-%release
Requires(post): %post_service dbus-tools
Requires(preun): %preun_service

%package dnsconfd
Summary: DNS configuration aquiring service
Group: System/Servers
Requires: lib%name = %version-%release %name-daemon = %version-%release

%package -n lib%name
Summary: Libraries for avahi
Group: System/Libraries

%if_with mdns
Obsoletes: libmdnsresponder
Provides: libmdnsresponder
%endif

%package -n lib%name-devel
Summary: Libraries and header files for avahi development
Group: Development/C
Requires: lib%name = %version-%release

%if_with mdns
Obsoletes: libmdnsresponder-devel
%endif

%package -n lib%name-glib
Summary: Glib libraries for avahi
Group: System/Libraries
Requires: lib%name = %version-%release

%package -n lib%name-glib-devel
Summary: Libraries and header files for avahi glib development
Group: Development/C
Requires: lib%name-devel = %version-%release
Requires: lib%name-glib = %version-%release
Requires: glib2-devel

%package -n lib%name-gobject
Summary: GObject'ified version of avahi API
Group: System/Libraries
Requires: lib%name = %version-%release
Requires: lib%name-glib = %version-%release

%package -n lib%name-gobject-devel
Summary: Libraries and header files for avahi gobject development
Group: Development/C
Requires: lib%name-devel = %version-%release
Requires: lib%name-glib-devel = %version-%release
Requires: lib%name-gobject = %version-%release

%package -n lib%name-qt3
Summary: Qt3 libraries for avahi
Group: System/Libraries
Requires: lib%name = %version-%release

%package -n lib%name-qt3-devel
Summary: Libraries and header files for avahi Qt3 development
Group: Development/KDE and QT
Requires: lib%name-devel = %version-%release
Requires: lib%name-qt3 = %version
Requires: libqt3-devel

%package -n lib%name-tqt
Summary: Trinity Qt wrapper libraries for avahi
Group: System/Libraries
Requires: lib%name = %version-%release

%package -n lib%name-tqt-devel
Summary: Libraries and header files for avahi Trinity Qt development
Group: Development/KDE and QT
Requires: lib%name-devel = %version-%release
Requires: lib%name-tqt = %version
Requires: libtqt-devel

%package -n lib%name-qt4
Summary: Qt4 libraries for avahi
Group: System/Libraries
Requires: lib%name = %version-%release

%package -n lib%name-qt4-devel
Summary: Libraries and header files for avahi Qt4 development
Group: Development/KDE and QT
Requires: lib%name-devel = %version-%release
Requires: lib%name-qt4 = %version
Requires: libqt4-devel

%package -n lib%name-ui
Summary: UI libraries for avahi
Group: System/Libraries
Requires: lib%name = %version-%release
Requires: lib%name-glib = %version-%release

%package -n lib%name-ui-common-devel
Summary: Common header files for avahi UI development
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release
Requires: lib%name-glib-devel = %version-%release

%package -n lib%name-ui-devel
Summary: Libraries for avahi UI development
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release
Requires: lib%name-ui-common-devel = %version-%release
Requires: lib%name-glib-devel = %version-%release
Requires: lib%name-ui = %version-%release

%package -n lib%name-ui-gtk3
Summary: GTK3 UI libraries for avahi
Group: System/Libraries
Requires: lib%name = %version-%release
Requires: lib%name-glib = %version-%release

%package -n lib%name-ui-gtk3-devel
Summary: Libraries for avahi GTK3 UI development
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release
Requires: lib%name-glib-devel = %version-%release
Requires: lib%name-ui-gtk3 = %version-%release
Requires: lib%name-ui-common-devel = %version-%release

%package -n lib%name-sharp
Summary: Mono bindings for avahi
Group: Development/Other
Requires: lib%name = %version-%release

%package -n lib%name-sharp-doc
Summary: Mono bindings for avahi -- monodoc
Group: Development/Other
Requires: lib%name-sharp = %version-%release
BuildArch: noarch

%package -n lib%name-ui-sharp
Summary: GTK/Sharp bindings for avahi
Group: Development/Other
Requires: lib%name-ui = %version-%release

%package -n lib%name-ui-sharp-doc
Summary: GTK/Sharp bindings for avahi -- monodoc
Group: Development/Other
Requires: lib%name-ui-sharp = %version-%release
BuildArch: noarch

%package -n lib%name-sharp-devel
Summary: Mono bindings for avahi
Group: Development/Other
Requires: lib%name-sharp = %version-%release
Requires: lib%name-ui-sharp = %version-%release

%package -n python-module-%name
Summary: Python bindings for Avahi
Group: Development/Python

%package bookmarks
Summary: Web service showing mDNS/DNS-SD announced HTTP services using the Avahi
Group: Networking/WWW
# still needed. that sucks
%py_requires avahi gobject dbus twisted twisted.internet
# p-m-t-w doesn't provide twisted.web. that sucks too
Requires: python-module-twisted-web
BuildArch: noarch

%package tools
Summary: Tools for mDNS browsing and publishing
Group: System/Base
Requires: lib%name = %version-%release

%package ui
Summary: UI tools for mDNS discovery
Group: Graphical desktop/Other
Requires: %name-daemon = %version-%release
%py_requires avahi gtk gobject dbus

# {{{ descriptions

%description autoipd
avahi-autoipd is an implementation of IPv4LL as defined in RFC3927,
a technology for assigning link-local IP addresses without DHCP server.
The same functionality has been available on Windows under the name APIPA.
While it is not the first implemenatation of this technology
for Free operating systems it is clearly the most powerful and hopefully
even the most secure. (Because it chroot()s and drops priviliges and suchlike)

%description daemon
Avahi is a system which facilitates service discovery on
a local network -- this means that you can plug your laptop or
computer into a network and instantly be able to view other people
who you can chat with, find printers to print to or find files being
shared. This kind of technology is already found in MacOS X
(branded 'Rendezvous', 'Bonjour' and sometimes 'ZeroConf')
and is very convenient.

This package provides avahi daemon.

%description dnsconfd
Avahi is a system which facilitates service discovery on
a local network -- this means that you can plug your laptop or
computer into a network and instantly be able to view other people
who you can chat with, find printers to print to or find files being
shared. This kind of technology is already found in MacOS X
(branded 'Rendezvous', 'Bonjour' and sometimes 'ZeroConf')
and is very convenient.

This package provides complementary DNS tracking service.

%description -n lib%name
Libraries for use of avahi.

%description -n lib%name-devel
Header files and libraries necessary for developing
programs using avahi.

%description -n lib%name-glib
Libraries for easy use of avahi from glib applications.

%description -n lib%name-glib-devel
Header files and libraries necessary for developing
programs using avahi with glib.

%description -n lib%name-gobject
GObject'ified version of avahi API

%description -n lib%name-gobject-devel
Header files and libraries necessary for developing
programs using avahi with GObject/glib.

%description -n lib%name-qt3
Libraries for easy use of avahi from Qt3 applications.

%description -n lib%name-qt3-devel
Header files and libraries necessary for developing
programs using avahi with Qt3.

%description -n lib%name-tqt
Libraries for easy use of avahi from Trinity Qt applications.

%description -n lib%name-tqt-devel
Header files and libraries necessary for developing
programs using avahi with Trinity Qt3.

%description -n lib%name-qt4
Libraries for easy use of avahi from Qt4 applications.

%description -n lib%name-qt4-devel
Header files and libraries necessary for developing
programs using avahi with Qt4.

%description -n lib%name-ui
Libraries for easy use of avahi from UI applications.

%description -n lib%name-ui-common-devel
Common header files necessary for developing programs using avahi with
GTK+2 or GTK+3 UI.

%description -n lib%name-ui-devel
Header files and libraries necessary for developing
programs using avahi with UI.

%description -n lib%name-ui-gtk3
Libraries for easy use of avahi from UI applications.

%description -n lib%name-ui-gtk3-devel
Header files and libraries necessary for developing
programs using avahi with UI.

%description bookmarks
A web service for listing HTTP services that are announced via mDNS/DNS-SD
using the Avahi daemon. %name opens a TCP socket on port 8080 and waits for
incoming HTTP connections returning a dynamic web site containing links
to all services of type _http._tcp on the LAN.
Point your browser to http://localhost:8080/ to make use of avahi-bookmarks.

%description tools
command-line utilitiesthat use avahi to browse and publish mDNS services and hosts.

%description ui
Various UI tools that use avahi to discover and use mDNS services and hosts.

%description -n lib%name-sharp
Mono bindings for Avahi.

%description -n lib%name-sharp-doc
Mono bindings for Avahi -- monodoc

%description -n lib%name-ui-sharp
GTK/Sharp bindings for Avahi.

%description -n lib%name-ui-sharp-doc
GTK/Sharp bindings for Avahi -- monodoc

%description -n lib%name-sharp-devel
Mono bindings for Avahi.

%description -n python-module-%name
Python bindings for Avahi.

# }}}

%prep
%setup
touch config.rpath

%build
%autoreconf
%configure \
    --localstatedir=%_var \
    --with-distro=altlinux \
    --enable-core-docs \
%if_with mono
    --enable-mono \
    --enable-monodoc \
%else
    --disable-mono \
    --disable-monodoc \
%endif
    --disable-compat-howl \
    --disable-static \
%if_with python
    --enable-python \
    --enable-pygtk \
    --enable-python-dbus \
%else
    --disable-python \
    --disable-pygtk \
    --disable-python-dbus \
%endif
%if_with mdns
    --enable-compat-libdns_sd \
%endif
    --with-systemdsystemunitdir=%systemdsystemunitdir \
    --with-avahi-user=%avahi_user \
    --with-avahi-group=%avahi_user \
    --with-avahi-priv-access-group=%avahi_group_priv \
    --with-autoipd-user=%autoipd_user \
    --with-autoipd-group=%autoipd_user

%make_build

%install
%make_install DESTDIR=%buildroot \
    pythondir=%python_sitelibdir \
    pyexecdir=%python_sitelibdir \
    install

mkdir -p %buildroot%_var/resolv/var/avahi \
    %buildroot%_var/run/avahi-daemon \
    %buildroot%_localstatedir/autoipd \
    %buildroot%_var/run/autoipd

ln -s resolv/var/avahi %buildroot%_var/avahi

mkdir -p %buildroot%_sysconfdir/hooks/resolv.conf.d
cat <<EOF > %buildroot%_sysconfdir/hooks/resolv.conf.d/reload_avahi-daemon
#!/bin/sh

service messagebus status >/dev/null 2>&1 && service avahi-daemon condreload >/dev/null 2>&1 ||:
EOF

find %buildroot%_libdir -name '*.la' -delete
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=RemoteAccess \
	%buildroot%_desktopdir/avahi-discover.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=RemoteAccess \
	%buildroot%_desktopdir/bvnc.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=RemoteAccess \
	%buildroot%_desktopdir/bssh.desktop

%pre autoipd
/usr/sbin/groupadd -r -f %autoipd_user &>/dev/null ||:
/usr/sbin/useradd -r -g %autoipd_user -d %_localstatedir/autoipd -s /dev/null \
    -c "Avahi autoipd service" -M -n %autoipd_user &>/dev/null ||:

%pre daemon
/usr/sbin/groupadd -r -f %avahi_user &>/dev/null ||:
/usr/sbin/useradd -r -g %avahi_user -d %_var/run/avahi-daemon -s /dev/null \
    -c "Avahi service" -M -n %avahi_user &>/dev/null ||:

%post daemon
%post_service avahi-daemon
/sbin/service avahi-dnsconfd condrestart 2>/dev/null ||:
if /sbin/service messagebus status &>/dev/null; then
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig &>/dev/null ||:
else
echo "Avahi requires running messagebus service." >&2
fi

%preun daemon
%preun_service avahi-daemon

%files

%files daemon
%doc docs/* specs

%_initdir/avahi-daemon

%systemdsystemunitdir/avahi-daemon.service
%systemdsystemunitdir/avahi-daemon.socket

%dir %_sysconfdir/avahi

%config %_sysconfdir/avahi/hosts

%config(noreplace) %_sysconfdir/avahi/avahi-daemon.conf

%dir %_sysconfdir/avahi/services
%config %_sysconfdir/avahi/services/ssh.service
%exclude %_sysconfdir/avahi/services/sftp-ssh.service

%config %_sysconfdir/dbus-1/system.d/avahi-dbus.conf

%attr(755, root, root) %_sysconfdir/hooks/resolv.conf.d/reload_avahi-daemon

%_sbindir/avahi-daemon

%_datadir/dbus-1/system-services/org.freedesktop.Avahi.service

%_datadir/avahi/*
%exclude %_datadir/avahi/interfaces

%_man5dir/*
%_man8dir/avahi-daemon.*

%_var/avahi
%attr(0771, root, _avahi) %dir /var/resolv/var/avahi
%attr(0770, root, _avahi) %dir %_var/run/avahi-daemon

%files autoipd
%dir %_sysconfdir/avahi
%config(noreplace) %_sysconfdir/avahi/avahi-autoipd.action
%_sbindir/avahi-autoipd
%_man8dir/avahi-autoipd.*
%attr(0770, root, %autoipd_user) %dir %_localstatedir/autoipd
%attr(0770, root, %autoipd_user) %dir %_var/run/autoipd

%files dnsconfd
%_initdir/avahi-dnsconfd
%systemdsystemunitdir/avahi-dnsconfd.service
%config(noreplace) %_sysconfdir/avahi/avahi-dnsconfd.action
%_sbindir/avahi-dnsconfd
%_man8dir/avahi-dnsconfd.*

%files -n lib%name -f %name.lang
%_libdir/libavahi-common.so.*
%_libdir/libavahi-core.so.*
%_libdir/libavahi-client.so.*

%if_with mdns
%_libdir/libdns_sd.so.*
%endif

%dir %_datadir/avahi
%dir %_datadir/avahi/interfaces

%dir %_libdir/avahi
%_libdir/avahi/service-types.db

%if_with python
%files bookmarks
%_bindir/avahi-bookmarks
%_man1dir/avahi-bookmarks.*
%endif # python

%files tools
%_bindir/avahi-browse*
%_bindir/avahi-publish*
%_bindir/avahi-resolve*
%_bindir/avahi-set-host-name

%_man1dir/avahi-browse*
%_man1dir/avahi-publish*
%_man1dir/avahi-resolve*
%_man1dir/avahi-set-host-name.*

%if_with python
%files ui
%_bindir/bshell
%_bindir/bssh
%_bindir/bvnc
%_bindir/avahi-discover
%_bindir/avahi-discover-standalone

%_datadir/avahi/interfaces/avahi-discover.ui

%_desktopdir/avahi-discover.desktop
%_desktopdir/bssh.desktop
%_desktopdir/bvnc.desktop

%python_sitelibdir/avahi_discover

%_man1dir/bssh.*
%_man1dir/bvnc.*
%_man1dir/avahi-discover.*
%endif #python

%files -n lib%name-devel
%_libdir/libavahi-common.so
%_libdir/libavahi-core.so
%_libdir/libavahi-client.so

%if_with mdns
%_libdir/libdns_sd.so
%endif

%_includedir/avahi-client
%_includedir/avahi-common
%_includedir/avahi-core

%_datadir/dbus-1/interfaces/*

%if_with mdns
%_includedir/avahi-compat-libdns_sd
%endif

%_pkgconfigdir/avahi-core.pc
%_pkgconfigdir/avahi-client.pc

%if_with mdns
%_pkgconfigdir/avahi-compat-libdns_sd.pc
%endif

%files -n lib%name-glib
%_libdir/libavahi-glib.so.*

%files -n lib%name-glib-devel
%_libdir/libavahi-glib.so
%_includedir/avahi-glib
%_pkgconfigdir/avahi-glib.pc

%files -n lib%name-gobject
%_libdir/libavahi-gobject.so.*

%files -n lib%name-gobject-devel
%_libdir/libavahi-gobject.so
%_includedir/avahi-gobject
%_pkgconfigdir/avahi-gobject.pc

%files -n lib%name-qt3
%_libdir/libavahi-qt3.so.*

%files -n lib%name-qt3-devel
%_libdir/libavahi-qt3.so
%_pkgconfigdir/avahi-qt3.pc
%_includedir/avahi-qt3

%files -n lib%name-tqt
%_libdir/libavahi-tqt.so.*

%files -n lib%name-tqt-devel
%_libdir/libavahi-tqt.so
%_pkgconfigdir/avahi-tqt.pc
%_includedir/avahi-tqt

%files -n lib%name-qt4
%_libdir/libavahi-qt4.so.*

%files -n lib%name-qt4-devel
%_libdir/libavahi-qt4.so
%_pkgconfigdir/avahi-qt4.pc
%_includedir/avahi-qt4

%files -n lib%name-ui
%_libdir/libavahi-ui.so.*

%files -n lib%name-ui-common-devel
%_includedir/avahi-ui

%files -n lib%name-ui-devel
%_libdir/libavahi-ui.so
%_pkgconfigdir/avahi-ui.pc

%files -n lib%name-ui-gtk3
%_libdir/libavahi-ui-gtk3.so.*

%files -n lib%name-ui-gtk3-devel
%_libdir/libavahi-ui-gtk3.so
%_pkgconfigdir/avahi-ui-gtk3.pc

%if_with mono
%files -n lib%name-sharp
%_monodir/avahi-sharp/avahi-sharp.dll
%_monogacdir/avahi-sharp

%files -n lib%name-sharp-doc
%_monodocdir/avahi-sharp-docs.*

%files -n lib%name-ui-sharp
%_monodir/avahi-ui-sharp/avahi-ui-sharp.dll
%_monogacdir/avahi-ui-sharp

%files -n lib%name-ui-sharp-doc
%_monodocdir/avahi-ui-sharp-docs.*

%files -n lib%name-sharp-devel
%_pkgconfigdir/avahi-sharp.pc
%_pkgconfigdir/avahi-ui-sharp.pc
%endif # mono

%if_with python
%files -n python-module-%name
%python_sitelibdir/%name
%endif		    

%changelog
* Mon May 21 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.31-alt3
- Avoid avahi reloading if messagebus is not running.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.6.31-alt2
- Binding to Trinity TQT interface is added.

* Thu Feb 16 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.31-alt1
- 0.6.31 released

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.30-alt1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.30-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for avahi-ui

* Sun May 08 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.30-alt1
- 0.6.30

* Tue Feb 22 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.28-alt6
- rebuilt due to gtk+3 soname change

* Mon Feb 21 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.28-alt5
- systemd stuff packaged

* Wed Feb 09 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.28-alt4
- split ui-devel subpackage (aris@)

* Thu Jan 06 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.28-alt3
- fix avahi-discover breakage (#24548)

* Sun Oct 17 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.28-alt2
- made some subpackages noarch

* Fri Oct 15 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.28-alt1
- 0.6.28 released

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.25-alt4.1
- Rebuilt with python 2.6

* Tue Nov 17 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.25-alt4
- initscript fixed (#19929)
- openresolv hook added (raorn@)

* Thu Jul  9 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.25-alt3
- introduced libavahi-sharp-devel subpackage, by mono team request

* Mon Jul  6 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.25-alt2
- fixed build with mono, again

* Fri May 29 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.25-alt1
- 0.6.25 released

* Tue Feb 24 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.24-alt3
- fixed build with mono >= 2.2

* Wed Dec 24 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.24-alt2
- rebuilt with versioned libdaemon (#18319)

* Sun Dec 14 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.24-alt1
- 0.6.24 released

* Mon Dec  1 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.23-alt2
- ui subpackage requires avahi-daemon (#17747)
- obsolete by filetriggers macros removed
- fixed build with recent rpm-build-mono

* Fri Aug 29 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.23-alt1
- 0.6.23 released

* Sat Feb 16 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.22-alt6
- fixed interpackage deps: qt[34] vs qt[34]-devel

* Wed Feb 13 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.22-alt5
- rebuilt against python 2.5

* Thu Jan  3 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.22-alt4
- made mono pkgconfig files compliant with alt's mono policy (#13862)

* Wed Dec 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.22-alt3
- build with automake >= 1.10 fixed

* Tue Dec 18 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.22-alt2
- build on x86_64 fixed

* Mon Dec 17 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.22-alt1
- 0.6.22
- mono bindings enabled by default

* Thu Sep  6 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.21-alt3
- do not announce sftp by default

* Fri Aug 31 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.21-alt2
- add default route on device after address selection by autoipd
- package missed avahi-daemon runtime dir

* Tue Aug 21 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.21-alt1
- 0.6.21 released

* Fri Jun 29 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.20-alt2
- reload dbus config instead of restart

* Tue Jun 26 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.20-alt1
- new version

* Tue May 22 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.19-alt1
- new version

* Tue Apr 24 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.18-alt2
- fix requires

* Fri Apr 20 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.18-alt1
- new version

* Tue Jan 09 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.16-alt1
- new version

* Tue Dec 26 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.15-alt4
- rebuilt with new dbus
- move %%_datadir/avahi ownership to libavahi

* Tue Dec 05 2006 Igor Zubkov <icesik@altlinux.org> 0.6.15-alt3
- NMU
- add patch from upstream for dbus 1.0

* Mon Nov 27 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.15-alt2
- add BuildRequires to libc-linux-headers
- built with python; thanks avm@alt

* Mon Nov 13 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.15-alt1
- new version

* Fri Oct 13 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.14-alt2
- remove requires to libc-linux-headers

* Mon Oct 02 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.14-alt1
- restart messagebus only on first install
- add group %avahi_group_priv
- built with Qt4

* Tue Aug 29 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.13-alt1
- new version

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.11-alt1
- new version

* Mon May 15 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.9-alt2
- rebuilt with new gcc

* Fri Mar 03 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.9-alt1
- new version
- fix username in initscript

* Mon Feb 27 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.8-alt1
- new version
- rename avahi user to _avahi
- fix runtime directory path

* Tue Jan 10 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt3
- fix requires

* Fri Dec 16 2005 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt2
- generate config at first start

* Wed Dec 14 2005 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt1
- built for ALT
- built without howl by default

* Mon Nov 21 2005 Jason Vas Dias<jvdias@redhat.com> - 0.6-1
- Upgrade to upstream version 0.6 - now provides 'avahi-howl-compat'
  libraries / includes.

* Mon Nov 14 2005 Jason Vas Dias<jvdias@redhat.com> - 0.5.2-7
- fix bug 172034: fix ownership of /var/run/avahi-daemon/
- fix bug 172772: .spec file improvements from matthias@rpmforge.net

* Mon Oct 31 2005 Jason Vas Dias<jvdias@redhat.com> - 0.5.2-6
- put back avahi-devel Obsoletes: howl-devel

* Mon Oct 31 2005 Alexander Larsson <alexl@redhat.com> - 0.5.2-5
- Obsoletes howl, howl-libs, as we want to get rid of them on updates
- No provides yet, as the howl compat library is in Avahi 0.6.0.

* Sun Oct 30 2005 Florian La Roche <laroche@redhat.com>
- disable the Obsoletes: howl until the transition is complete

* Fri Oct 28 2005 Jason Vas Dias<jvdias@redhat.com> - 0.5.2-3
- change initscript to start avahi-daemon AFTER messagebus

* Wed Oct 26 2005 Karsten Hopp <karsten@redhat.de> 0.5.2-2
- add buildrequires dbus-python

* Fri Oct 21 2005 Alexander Larsson <alexl@redhat.com> - 0.5.2-1
- Initial package
