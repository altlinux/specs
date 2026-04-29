Name: simdutf
Version: 9.0.0
Release: alt1

Summary: SIMD assisted Unicode validation and transcoding
License: MIT or Apache-2.0
Group: Development/C++
URL: https://simdutf.github.io/simdutf
VCS: https://github.com/simdutf/simdutf

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: ctest

%package -n libsimdutf34
Summary: SIMD assisted Unicode validation and transcoding
Group: Development/C++

%package -n libsimdutf-devel
Summary: SIMD assisted Unicode validation and transcoding
Group: Development/C++

%define desc\
Unicode routines (UTF8, UTF16, UTF32) and Base64: billions of characters\
per second using SSE2, AVX2, NEON, AVX-512, RISC-V Vector Extension.\
Part of Node.js, WebKit/Safari and Bun.

%description %desc

%description -n libsimdutf34 %desc
This package provides simdutf shared library.

%description -n libsimdutf-devel %desc
This package contains simdutf development part.

%prep
%setup

%build
%cmake	-DBUILD_SHARED_LIBS=ON \
	-DSIMDUTF_BENCHMARKS=OFF \
	-DSIMDUTF_TOOLS=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n libsimdutf34
%doc AUTHORS CONTRIBUTORS LICENSE*
%_libdir/libsimdutf.so.*

%files -n libsimdutf-devel
%doc AUTHORS CONTRIBUTORS LICENSE* *.md
%_includedir/simdutf.h
%_includedir/simdutf_c.h
%_includedir/simdutf
%_libdir/cmake/simdutf
%_libdir/pkgconfig/simdutf.pc
%_libdir/libsimdutf.so

%changelog
* Wed Apr 29 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 9.0.0-alt1
- 9.0.0 released

* Wed Feb 18 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 8.0.0-alt1
- 8.0.0 released

* Wed Nov 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 7.6.0-alt1
- 7.6.0 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 7.5.0-alt1
- 7.5.0 released

* Tue Sep 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 7.4.0-alt1
- 7.4.0 released

* Mon Jun 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 7.3.0-alt1
- 7.3.0 released

* Wed May 28 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 7.0.0-alt1
- 7.0.0 released

* Wed Apr 30 2025 Ilya Sorochan <k0tran@altlinux.org> 6.5.0-alt1
- 5.5.0 -> 6.5.0 (libsimdutf10 -> libsimdutf20)

* Fri Oct 04 2024 Ilya Sorochan <k0tran@altlinux.org> 5.5.0-alt1
- Initial build.
