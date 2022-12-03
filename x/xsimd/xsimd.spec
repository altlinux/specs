Name: xsimd
Version: 9.0.1
Release: alt1
Summary: C++ wrappers for SIMD intrinsics
Group: Development/C++
License: BSD
Url: https://xsimd.readthedocs.io/
VCS: https://github.com/xtensor-stack/xsimd
Source0: %name-%version.tar
Patch1: %name-%version-%release.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgtest-devel

%ifarch %arm
# Only used for testing, as it's a header-only package.
%global optflags %(echo %optflags -mfpu=neon)
%endif

%global _description \
SIMD (Single Instruction, Multiple Data) is a feature of microprocessors that \
has been available for many years. SIMD instructions perform a single operation \
on a batch of values at once, and thus provide a way to significantly \
accelerate code execution. However, these instructions differ between \
microprocessor vendors and compilers. \
 \
xsimd provides a unified means for using these features for library authors. \
Namely, it enables manipulation of batches of numbers with the same arithmetic \
operators as for single values. It also provides accelerated implementation \
of common mathematical functions operating on batches. \

%description %_description
%package devel
Group: Development/C++
Summary: %summary
Provides: %name = %version-%release
Provides: %name-static = %version-%release
%description devel %_description

%prep
%setup
%patch1 -p1

%build
%cmake -DBUILD_TESTS=ON
%ifnarch ppc64le
%cmake_build
%endif

%install
%cmake_install

%check
%ifnarch ppc64le
%cmake_build -- xtest
%endif

%files devel
%doc README.md LICENSE
%_includedir/%name/
%_libdir/cmake/%name/
%_libdir/pkgconfig/%name.pc

%changelog
* Sat Dec 03 2022 Anton Farygin <rider@altlinux.ru> 9.0.1-alt1
- first build for ALT, based on specfile from Fedora
