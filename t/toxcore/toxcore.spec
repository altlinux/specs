#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: toxcore
Summary: All-in-one secure communication platform
Version: 0.0.1
Release: alt2.20160725
License: ISC license
Group: System/Libraries
BuildRequires: libopus-devel libsodium-devel libvpx-devel libcheck-devel
BuildPreReq: libconfig-devel >= 1.4
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Url: https://github.com/irungentoo/toxcore/

%package -n libtoxav0
Summary: %summary
Group: System/Libraries

%description -n libtoxav0
%summary

%package -n libtoxcore0
Summary: %summary
Group: System/Libraries

%description -n libtoxcore0
%summary

%package -n libtoxdns0
Summary: %summary
Group: System/Libraries

%description -n libtoxdns0
%summary

%package -n libtoxencryptsave0
Summary: %summary
Group: System/Libraries

%description -n libtoxencryptsave0
%summary

%package bootstrapd
Summary: %summary
Group: System/Libraries

%description bootstrapd
%summary

%package devel
Summary: %summary
Group: System/Libraries

%description devel
%summary

%package devel-static
Summary: %summary
Group: System/Libraries
Requires: toxcore-devel

%description devel-static
%summary

%description
With the rise of governmental monitoring programs,
Tox, a FOSS initiative, aims to be an easy to use,
all-in-one communication platform that ensures
their users full privacy and secure message delivery.


%prep
%setup
%patch -p1

%build
%autoreconf
%configure --enable-daemon
%make_build

%install
%makeinstall
rm -f %buildroot%_bindir/DHT_bootstrap
install -d -m700 %buildroot/var/lib/tox-bootstrapd/
install -D -m644 other/bootstrap_daemon/tox-bootstrapd.conf %buildroot/etc/tox-bootstrapd.conf
install -D -m644 other/bootstrap_daemon/tox-bootstrapd.service %buildroot%_unitdir/tox-bootstrapd.service
%__subst "s|/usr/local/bin|%_bindir|g" %buildroot%_unitdir/tox-bootstrapd.service

%pre bootstrapd
/usr/sbin/groupadd -r -f tox-bootstrapd
/usr/sbin/useradd -r -d /var/lib/tox-bootstrapd -s /dev/null -c 'TOX DHT bootstrap daemon' -g tox-bootstrapd tox-bootstrapd >/dev/null 2>&1 ||:

%files -n libtoxav0
%_libdir/libtoxav.so.0
%_libdir/libtoxav.so.0.0.0

%files -n libtoxcore0
%_libdir/libtoxcore.so.0
%_libdir/libtoxcore.so.0.0.0

%files -n libtoxdns0
%_libdir/libtoxdns.so.0
%_libdir/libtoxdns.so.0.0.0

%files -n libtoxencryptsave0
%_libdir/libtoxencryptsave.so.0
%_libdir/libtoxencryptsave.so.0.0.0

%files bootstrapd
%doc other/bootstrap_daemon/README.md
%_bindir/tox-bootstrapd
%dir %attr(700,tox-bootstrapd,tox-bootstrapd) /var/lib/tox-bootstrapd
%_sysconfdir/tox-bootstrapd.conf
%_unitdir/tox-bootstrapd.service

%files devel
%_includedir/tox
%_libdir/libtoxav.so
%_libdir/libtoxcore.so
%_libdir/libtoxdns.so
%_libdir/libtoxencryptsave.so
%_pkgconfigdir/libtoxav.pc
%_pkgconfigdir/libtoxcore.pc

%files devel-static
%_libdir/libtoxav.a
%_libdir/libtoxcore.a
%_libdir/libtoxdns.a
%_libdir/libtoxencryptsave.a

%changelog
* Mon Jul 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt2.20160725
- build tox-bootstrapd subpackage

* Mon Jul 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1.20160725
- update from upstream git (ALT #32105)

* Tue Jun 16 2015 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20150616
- update from upstream git (ALT #31056)

* Tue Dec 16 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20141216
- update from upstream git

* Tue Nov 04 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20141104
- update from upstream git

* Wed Oct 22 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20141022
- update from upstream git

* Tue Oct 14 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20141014
- update from upstream git (ALT #30394)

* Mon Aug 25 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140717.1
- rebuild with new libsodium

* Thu Jul 17 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140717
- update from upstream git

* Thu Jul 17 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140628.1
- package tox/tox.h (ALT #30195)

* Sat Jun 28 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140628
- update from upstream git

* Thu Jun 26 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140626
- update from upstream git

* Thu Jun 26 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus

