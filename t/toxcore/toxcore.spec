#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: toxcore
Summary: %name
Version: 0.0.1
Release: alt1.20140626
License: ISC license
Group: System/Libraries
BuildRequires: libopus-devel libsodium-devel libvpx-devel
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
%name


%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files -n libtoxav0
%_libdir/libtoxav.so.0
%_libdir/libtoxav.so.0.0.0

%files -n libtoxcore0
%_libdir/libtoxcore.so.0
%_libdir/libtoxcore.so.0.0.0

%files -n libtoxdns0
%_libdir/libtoxdns.so.0
%_libdir/libtoxdns.so.0.0.0

%files devel
%_includedir/tox/tox.h
%_includedir/tox/toxav.h
%_includedir/tox/toxdns.h
%_libdir/libtoxav.so
%_libdir/libtoxcore.so
%_libdir/libtoxdns.so
%_pkgconfigdir/libtoxav.pc
%_pkgconfigdir/libtoxcore.pc

%files devel-static
%_libdir/libtoxav.a
%_libdir/libtoxcore.a
%_libdir/libtoxdns.a

%changelog
* Thu Jun 26 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140626
- update from upstream git

* Thu Jun 26 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus

