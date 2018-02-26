
Name: eigen2
Version: 2.0.17
Release: alt1

Group: Development/C++
Summary: Lightweight C++ template library for vector and matrix math, a.k.a. linear algebra
License: LGPL
Url: http://eigen.tuxfamily.org/
BuildArch: noarch

Provides: %name-devel = %version-%release

Source: eigen-%version.tar

# Automatically added by buildreq on Tue Feb 17 2009 (-bi)
#BuildRequires: cmake doxygen gcc-c++ subversion tetex-dvips tetex-latex
BuildRequires: cmake >= 2.4.6 doxygen gcc-c++ subversion tetex-dvips tetex-latex

%description
Eigen is a lightweight C++ template library for vector and matrix math, a.k.a.
linear algebra.

%prep
%setup -q -n eigen-%version

%build
%add_optflags -DNDEBUG
%define lib_suffix %nil
%ifarch x86_64 ppc64
%define lib_suffix 64
%endif
mkdir -p %_target_platform
pushd %_target_platform
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DCMAKE_C_FLAGS_RELEASE:STRING='%optflags' \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING='%optflags' \
    -DLIB_DESTINATION=%_lib \
    -DLIB_SUFFIX=%lib_suffix
popd
%make_build -C %_target_platform VERBOSE=1
%make_build -C %_target_platform/doc VERBOSE=1

%install
%make -C %_target_platform DESTDIR=%buildroot install

%files
%doc %_target_platform/doc/html
%_includedir/eigen2/
%_datadir/pkgconfig/%name.pc

%changelog
* Fri Mar 30 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.17-alt1
- new version

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.15-alt1
- new version

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.12-alt1
- new version

* Thu Oct 08 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.6-alt1
- new version

* Thu Jun 25 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt1
- new version

* Thu Apr 09 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt3
- release 2.0.0

* Tue Feb 17 2009 Sergey V Turchin <zerg at altlinux dot org> 2.0-alt2
- package html docs

* Wed Nov 19 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0-alt1
- initial specfile
