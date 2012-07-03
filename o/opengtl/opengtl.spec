%define sover 0.7
%define libver 0.9.15
%define libname libopengtl%sover
%define develname libopengtl-devel
%define llvm_req_str llvm >= 2.7 llvm <= 2.9

Name: opengtl
Version: 0.9.15.2
Release: alt2

Group: System/Libraries
Summary: Open Graphics Transformation Languages
Url: http://www.opengtl.org/
License: LGPLv2+

Requires: %llvm_req_str
Provides: OpenGTL = %version-%release

Source: http://www.opengtl.org/download/OpenGTL-%version.tar.bz2
Patch1: opengtl-0.9.10-alt-find-llvm.patch
Patch2: opengtl-0.9.10-alt-extensions-dir.patch
Patch3: opengtl-0.9.15-alt-fix-linking.patch

# Automatically added by buildreq on Thu Jan 20 2011 (-bb)
#BuildRequires: ImageMagick-tools cmake gcc-c++ ghostscript-utils latex2html libpng-devel llvm-devel rpm-build-ruby tetex-latex-listings zlib-devel-static
BuildRequires: tetex-core tetex-latex tetex-latex-listings tetex-dvips
BuildRequires: ImageMagick-tools cmake gcc-c++ ghostscript-utils latex2html libpng-devel llvm-devel zlib-devel

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
#%patch1 -p1
#%patch2 -p1
%patch3 -p1


%build
%cmake
pushd BUILD
%make VERBOSE=1
popd


%install
pushd BUILD
%make install DESTDIR=%buildroot
popd


%files
%_bindir/*

%files -n %libname
%_libdir/GTLImageIO
%_libdir/lib*.so.%sover
%_libdir/lib*.so.%libver
%_datadir/OpenGTL

%files -n %develname
%doc BUILD/OpenShiva/doc/reference/ShivaRef.pdf
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/*.pc

%changelog
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

