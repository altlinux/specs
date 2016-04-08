Name:		libsidplayfp
Version:	1.0.3
Release:	alt1.qa1
Summary:	SID chip music module playing library
Group:		System/Libraries
License:	GPLv2+
Url:		http://sourceforge.net/projects/sidplay-residfp/
Source0:	http://downloads.sourceforge.net/sidplay-residfp/%name-%version.tar.gz

# Automatically added by buildreq on Sun Apr 28 2013 (-bi)
# optimized out: elfutils libstdc++-devel pkg-config
BuildRequires: doxygen gcc-c++ glibc-devel-static

%description
This library provides support for playing SID music modules originally
created on Commodore 64 and compatibles. It contains a processing engine
for MOS 6510 machine code and MOS 6581 Sound Interface Device (SID)
chip output. It is used by music player programs like SIDPLAY and
several plug-ins for versatile audio players.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
These are the files needed for compiling programs that use %name.

%package devel-static
Summary: Development static libraries for the %name
Group: Development/C++
Requires: %name-devel = %version-%release

%description devel-static
Development static libraries for the %name.

%package devel-doc
Summary: API documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
This package contains API documentation for %name.

%prep
%setup

%build
%configure
%make_build all doc

%install
make DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING NEWS README TODO
%_libdir/libsidplayfp.so.3*
%_libdir/libstilview.so.0*

%files devel
%_libdir/libsidplayfp.so
%_libdir/libstilview.so
%_includedir/sidplayfp/
%_includedir/stilview/
%_libdir/pkgconfig/*.pc

%files devel-static
%_libdir/*.a

%files devel-doc
%doc docs/html

%changelog
* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.0.3-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon Jul 15 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Wed May 01 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.2-alt2
- fix missing constructor (Ilya Kotov aka trialuser)

* Sun Apr 28 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux from FC package
