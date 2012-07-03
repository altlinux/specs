
Name: eigen
Version: 1.0.5
Release: alt1

Group: Development/C++
Summary: Lightweight C++ template library for vector and matrix math, a.k.a. linear algebra
License: LGPL
Url: http://eigen.tuxfamily.org/

Provides: %name-devel = %version-%release

Source: eigen-%version.tar.gz

BuildRequires: cmake >= 2.4.6 gcc-c++

%description
Eigen is a lightweight C++ template library for vector and matrix math, a.k.a.
linear algebra.

%prep
%setup -q -n %name

%build
%define _optlevel s
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

%install
%make -C %_target_platform DESTDIR=%buildroot install

%files
%_includedir/eigen/

%changelog
* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.5-alt1
- initial specfile
