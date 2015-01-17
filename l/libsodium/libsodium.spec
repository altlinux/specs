#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: libsodium
Summary: %name
Version: 1.0.2
Release: alt1
License: ISC license
Group: System/Libraries
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Source100: %name.watch
Url: https://download.libsodium.org/libsodium/releases/

%package devel
Summary: %summary
Group: System/Libraries

%description devel
%summary

%package devel-static
Summary: %summary
Group: System/Libraries
Requires: %name-devel

%description devel-static
%summary

%package -n libsodium13
Summary: %summary
Group: System/Libraries

%description -n libsodium13
%summary

%description
%name


%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files devel
%_libdir/libsodium.so
%_libdir/pkgconfig/%name.pc
%_includedir/sodium.h
%_includedir/sodium

%files devel-static
%_libdir/libsodium.a

%files -n libsodium13
%_libdir/libsodium.so.13*

%changelog
* Sat Jan 17 2015 Denis Smirnov <mithraen@altlinux.ru> 1.0.2-alt1
- new version 1.0.2

* Tue Nov 25 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt1
- new version 1.0.1

* Fri Sep 26 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0.0-alt1
- new version 1.0.0

* Mon Sep 22 2014 Denis Smirnov <mithraen@altlinux.ru> 0.7.1-alt1
- new version 0.7.1

* Mon Aug 25 2014 Denis Smirnov <mithraen@altlinux.ru> 0.7.0-alt1
- new version 0.7.0

* Sat Jul 26 2014 Denis Smirnov <mithraen@altlinux.ru> 0.6.1-alt1
- new version 0.6.1

* Fri Jul 04 2014 Denis Smirnov <mithraen@altlinux.ru> 0.6.0-alt1
- new version 0.6.0

* Wed Jun 25 2014 Denis Smirnov <mithraen@altlinux.ru> 0.5.0-alt1
- first build for Sisyphus

