%def_disable static

Name: zrtpcpp
Version: 2.3.4
Release: alt2.1
%define sover 2
%define libzrtpcpp libzrtpcpp%sover

Summary: ZRTP support for GNU RTP/RTCP stack

License: GPL
Group: System/Libraries
Url: http://www.gnu.org/software/ccrtp/

Source: %name-%version.tar

# Automatically added by buildreq on Wed Sep 24 2014 (-bi)
# optimized out: cmake-modules elfutils libcloog-isl4 libgpg-error libssl-devel libstdc++-devel pkg-config python-base ruby ruby-stdlibs ucommon-devel
#BuildRequires: ccrtp-devel cmake gcc-c++ libgcrypt-devel rpm-build-ruby
BuildRequires: ccrtp-devel cmake gcc-c++ libgcrypt-devel

%description
This package provides a library that adds support to the GNU RTP stack 
for the zrtp protocol specification developed by Phil Zimmermen for 
zphone.  Using this package, together with GNU ccrtp (1.5.0 or later) 
provides a zrtp implimentation that can be directly embedded into client
and server applications, rather than the overhead penalty of using an 
external proxy such as zphone.  The first application to demonstrate 
this capability is the 0.8.2 release of the Twinkle softphone client.

%package devel
Summary: Header files for zrtpcpp library
Group: Development/Other
Requires: ccrtp-devel
Conflicts: libzrtpcpp-devel
%description devel
Header files for zrtpcpp library.

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release
%description devel-static
Common C++ devel static files

%package -n %libzrtpcpp
Summary: %name library
Group: System/Libraries
%description -n %libzrtpcpp
%name library


%prep
%setup

%build
%cmake
%cmake_build

%install
#cmake_install DESTDIR=%buildroot
%make install -C BUILD DESTDIR=%buildroot

%files -n %libzrtpcpp
%doc AUTHORS README.md
%_libdir/lib*.so.%sover
%_libdir/lib*.so.%sover.*

%files devel
%_libdir/lib*.so
%_includedir/lib%name
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libddir/*.a
%endif

%changelog
* Sun Mar 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt2.1
- NMU: autorebuild with ucommon-7.0.0

* Mon Jun 15 2015 Sergey V Turchin <zerg@altlinux.org> 2.3.4-alt2
- rebuild with new ccrtp

* Sun Jun 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.3.4-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Oct 23 2014 Sergey V Turchin <zerg@altlinux.org> 2.3.4-alt0.M70P.1
- built for M70P

* Wed Sep 24 2014 Sergey V Turchin <zerg@altlinux.org> 2.3.4-alt1
- initial build
