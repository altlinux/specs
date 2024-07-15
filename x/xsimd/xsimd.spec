Name: xsimd
Version: 13.0.0
Release: alt1
Summary: C++ wrappers for SIMD intrinsics
Group: Development/C++
License: BSD
Url: https://xsimd.readthedocs.io/
VCS: https://github.com/xtensor-stack/xsimd
Source0: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgtest-devel
BuildRequires: doctest-devel

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
%ifarch %e2k
sed -i '/#elif defined(__x86_64__)/i #elif defined(__e2k__)\nsse2=sse3=ssse3=sse4_1=1;best=sse4_1::version();' \
	include/xsimd/config/xsimd_cpuid.hpp
sed -i -E 's/#ifdef __(SSE4_2|AVX|AVX2|FMA|FMA4)__/#if 0/' include/xsimd/config/xsimd_config.hpp
# EDG bug workaround
sed -i -E 's/\((typename .*)\)(G::get\(Is, sizeof\.\.\.\(Is\)\))/static_cast<\1>(\2)/' \
	include/xsimd/types/xsimd_batch_constant.hpp
# remove extra annoying warnings
sed -i 's/-Wextra/& -Wno-type-limits -Wno-overflow -Wno-reduced-alignment/' test/CMakeLists.txt
sed -i 's/<T, A>::batch.*(register_type reg/& __attribute__((unused))/' \
	include/xsimd/types/xsimd_batch.hpp
%endif

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
* Mon Jul 15 2024 Anton Farygin <rider@altlinux.ru> 13.0.0-alt1
- 11.1.0 -> 13.0.0

* Thu Nov 02 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 11.1.0-alt1.1
- fixed build for Elbrus

* Thu Jul 06 2023 Anton Farygin <rider@altlinux.ru> 11.1.0-alt1
- 10.0.0 -> 11.1.0

* Sat Feb 04 2023 Anton Farygin <rider@altlinux.ru> 10.0.0-alt1
- 9.0.1 -> 10.0.0

* Sat Dec 03 2022 Anton Farygin <rider@altlinux.ru> 9.0.1-alt1
- first build for ALT, based on specfile from Fedora
