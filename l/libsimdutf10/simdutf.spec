%global optflags_lto %optflags_lto -ffat-lto-objects

%def_with check

Name:      libsimdutf10
Version:   5.5.0
Release:   alt1

Summary:   Unicode validation and transcoding at billions of characters per second
License:   MIT or Apache-2.0
Group:     Development/C++
URL:       https://simdutf.github.io/simdutf
VCS:       https://github.com/simdutf/simdutf

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
%if_with check
BuildRequires: ctest
%endif

ExcludeArch: s390 s390x

%description
Unicode routines (UTF8, UTF16, UTF32) and Base64: billions of characters
per second using SSE2, AVX2, NEON, AVX-512, RISC-V Vector Extension.
Part of Node.js, WebKit/Safari and Bun.

%package devel
Summary:  Unicode validation and transcoding at billions of characters per second
Group:    Development/C++

%description devel
Unicode routines (UTF8, UTF16, UTF32) and Base64: billions of characters
per second using SSE2, AVX2, NEON, AVX-512, RISC-V Vector Extension.
Part of Node.js, WebKit/Safari and Bun.

%prep
%setup

%build
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DSIMDUTF_BENCHMARKS=OFF \
	-DSIMDUTF_TOOLS=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc *.md LICENSE-MIT LICENSE-APACHE AUTHORS CONTRIBUTORS
%_libdir/libsimdutf.so.*

%files devel
%_includedir/simdutf.h
%_includedir/simdutf
%_libdir/cmake/simdutf
%_libdir/pkgconfig/simdutf.pc
%_libdir/libsimdutf.so

%changelog
* Fri Oct 04 2024 Ilya Sorochan <k0tran@altlinux.org> 5.5.0-alt1
- Initial build.
