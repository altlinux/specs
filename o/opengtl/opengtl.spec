%define sover 0.8
%define libver 0.9.18
%define libname libopengtl%sover
%define develname libopengtl-devel
%define llvm_bin_req_str llvm >= 3.0 llvm <= 3.2
%define llvm_dev_req_str llvm-devel >= 3.0 llvm-devel <= 3.3

Name: opengtl
Version: 0.9.18
Release: alt2

Group: System/Libraries
Summary: Open Graphics Transformation Languages
Url: http://www.opengtl.org/
License: LGPLv2+

#Requires: %llvm_bin_req_str
Provides: OpenGTL = %version-%release

Source: http://www.opengtl.org/download/OpenGTL-%version.tar.bz2
Patch2: opengtl-0.9.10-alt-extensions-dir.patch
Patch3: opengtl-0.9.15-alt-fix-linking.patch
Patch4: opengtl-0.9.18-alt-pkgconfig.patch
Patch5: opengtl-0.9.18-alt-llvm-3.3.patch

# Automatically added by buildreq on Thu Jan 20 2011 (-bb)
#BuildRequires: ImageMagick-tools cmake gcc-c++ ghostscript-utils latex2html libpng-devel llvm-devel rpm-build-ruby tetex-latex-listings zlib-devel-static
BuildRequires: tetex-core tetex-latex tetex-latex-listings tetex-dvips
BuildRequires: ImageMagick-tools cmake gcc-c++ ghostscript-utils latex2html libpng-devel llvm-devel zlib-devel
BuildRequires: %llvm_dev_req_str
BuildRequires: kde-common-devel

%description
Graphics Transformation Languages is a set of library for using and
integrating transformation algorithms (such as filter or color conversion)
in graphics applications

%package -n %libname
Summary: OpenGTL library
Group: System/Libraries
%description -n %libname
OpenGTL library.

%package -n %{develname}
Summary: OpenGTL development files
Group: Development/C++
Requires: %libname = %version-%release
Provides: OpenGTL-devel = %version-%release
Provides: OpenCTL-devel = %version-%release
Provides: OpenShiva-devel = %version-%release
%description -n %{develname}
This package contains header files needed if you wish to build applications
based on OpenGTL.


%prep
%setup -q -n OpenGTL-%version
#%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2


%build
%Kcmake
%Kmake


%install
%Kinstall


%files
%_bindir/*

%files -n %libname
%_libdir/GTLImageIO
%_libdir/lib*.so.%sover
%_libdir/lib*.so.%libver
%_datadir/OpenGTL

%files -n %develname
%doc BUILD-*/OpenShiva/doc/reference/ShivaRef.pdf
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/*.pc

%changelog
* Wed Aug 28 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.18-alt2
- fixed build with llvm 3.3
- drop old llvm patch

* Tue Feb 26 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.18-alt1
- new version

* Tue Nov 06 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.15.2-alt3
- rebuild with new libpng

* Mon May 21 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.15.2-alt2
- rebuild with new llvm

* Mon Apr 23 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.15.2-alt0.M60P.1
- build for M60P

* Mon Apr 23 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.15.2-alt1
- new version

* Wed Apr 27 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.15.1-alt1
- new version

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.15-alt1
- built for ALT

