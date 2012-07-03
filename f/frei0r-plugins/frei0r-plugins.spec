%define bname frei0r
%define major_ver 1
%define minor_ver 3

Name: %bname-plugins
Version: %major_ver.%minor_ver
Release: alt2
Summary: Frei0r - a minimalistic plugin API for video effects
License: %lgpl2plus
Group: Video
URL: http://www.piksel.org/frei0r
Source: http://propirate.net/frei0r/%name-%version.tar
Patch: %name-%version-%release.patch
Packager: Alexey Shabalin <shaba@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++
BuildRequires: libgavl-devel >= 0.2.3
BuildRequires: libopencv-devel
BuildRequires: doxygen fonts-ttf-dejavu graphviz

%description
It is a minimalistic plugin API for video sources and filters. The behaviour of
the effects can be controlled from the host by simple parameters. The intent is
to solve the recurring reimplementation or adaptation issue of standard effect

%package -n frei0r-devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description -n frei0r-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n frei0r-devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description -n frei0r-devel-doc
This package contains development documentation for %name

%package facedetect
Summary: Face detect plugin for %name
Group: Video
Requires: %name = %version-%release
Requires: libopencv-utils

%description facedetect
Face detect plugin for %name

%prep
%setup
%patch -p1

%build
%__aclocal
%__autoheader
%__libtoolize --automake -c
%__automake --add-missing -c
%__autoconf
%configure --disable-static

# workaround cvconfig.h
/bin/ln -s -- config.h include/cvconfig.h

%make_build

%install
%make DESTDIR=%buildroot install

%files
%dir %_libdir/%bname-%major_ver
%_libdir/%bname-%major_ver/*.so
%exclude %_libdir/%bname-%major_ver/facebl0r.so

%files -n frei0r-devel
%_includedir/frei0r.h
%_pkgconfigdir/*.pc

%files -n frei0r-devel-doc
%_defaultdocdir/%name/*

%files facedetect
%_libdir/%bname-%major_ver/facebl0r.so

%changelog
* Mon Dec 19 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3-alt2
- rebuild with new libopencv

* Mon Apr 04 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3-alt1
- 1.3
- rebuild with new libopencv

* Thu Nov 25 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- 1.2.1
- build with libopencv2 (tnx to real@)

* Wed Sep 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2-alt1
- 1.2

* Fri Dec 04 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.22-alt2.git7a5488
- split facedetect package

* Mon Nov 30 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.22-alt1.git7a5488
- 1.1.22 + git 2009-11-09
- update Summary, URL, description
- change Packager
- add frei0r-devel package
- add frei0r-devel-doc package
- update buildreq

* Mon Nov 10 2008 Led <led@altlinux.ru> 1.1.19-alt3
- fixed build with g++ 4.3

* Sat Mar 15 2008 Led <led@altlinux.ru> 1.1.19-alt2
- moved to %_libexecdir/%bname-%major_ver/
- fixed License

* Wed May 30 2007 Led <led@altlinux.ru> 1.1.19-alt1
- initial build
