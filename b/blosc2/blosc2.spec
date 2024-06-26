%ifnarch armh
%def_with check
%else
%def_without check
%endif

Name:    blosc2
Version: 2.15.0
Release: alt1

Summary: A fast, compressed, persistent binary data store library for C
License: BSD-3-Clause
Group:   System/Libraries
Url:     https://www.blosc.org/
VCS:     https://github.com/Blosc/c-blosc2

Source:  %name-%version.tar
Patch1:  0001-init_shuffle_implementation-use-a-proper-synchroniza.patch

BuildRequires(pre): cmake gcc-c++
BuildRequires: zlib-devel liblz4-devel libzstd-devel ctest

%description
C-Blosc2 is the new major version of C-Blosc, and tries hard to be backward
compatible with both the C-Blosc1 API and its in-memory format. However,
the reverse thing is generally not true for the format; buffers generated
with C-Blosc2 are not format-compatible with C-Blosc1 (i.e. forward
compatibility is not supported). In case you want to ensure full API
compatibility with C-Blosc1 API, define the BLOSC1_COMPAT symbol.

%package -n lib%name
Summary: %summary
Group: System/Libraries

%description -n lib%name
C-Blosc2 is the new major version of C-Blosc, and tries hard to be backward
compatible with both the C-Blosc1 API and its in-memory format. However,
the reverse thing is generally not true for the format; buffers generated
with C-Blosc2 are not format-compatible with C-Blosc1 (i.e. forward
compatibility is not supported). In case you want to ensure full API
compatibility with C-Blosc1 API, define the BLOSC1_COMPAT symbol.

%package -n lib%name-devel
Summary: Development files of Blosc2 library
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
C-Blosc2 is the new major version of C-Blosc, and tries hard to be backward
compatible with both the C-Blosc1 API and its in-memory format. However,
the reverse thing is generally not true for the format; buffers generated
with C-Blosc2 are not format-compatible with C-Blosc1 (i.e. forward
compatibility is not supported). In case you want to ensure full API
compatibility with C-Blosc1 API, define the BLOSC1_COMPAT symbol.

This package contains development files of Blosc2 library.

%prep
%setup
%patch1 -p1
%ifarch %e2k
# why is libdl used but not linked?
sed -i '1i set(LIBS ${LIBS} "dl")' blosc/CMakeLists.txt
%endif

# remove bundled libraries
rm -rf internal-complibs

%build
%cmake \
        -DBUILD_STATIC=OFF \
        -DBUILD_EXAMPLES=OFF \
        -DBUILD_FUZZERS=OFF \
        -DBUILD_BENCHMARKS=OFF \
        -DPREFER_EXTERNAL_ZLIB=ON \
        -DPREFER_EXTERNAL_LZ4=ON \
        -DPREFER_EXTERNAL_ZSTD=ON
%cmake_build

%install
%cmakeinstall_std

%check
%cmake_build --target test

%files -n lib%name
%doc README.rst LICENSE.txt RELEASE_NOTES.md
%_libdir/libblosc2.so.*

%files -n lib%name-devel
%_libdir/libblosc2.so
%dir %_includedir/blosc2
%_includedir/blosc2.h
%_includedir/b2nd.h
%_includedir/blosc2
%_pkgconfigdir/blosc2.pc
%dir %_libdir/cmake
%_libdir/cmake/Blosc2

%changelog
* Tue Jun 25 2024 Anton Vyatkin <toni@altlinux.org> 2.15.0-alt1
- New version 2.15.0.

* Sat Apr 13 2024 Anton Vyatkin <toni@altlinux.org> 2.14.4-alt1
- New version 2.14.4.

* Mon Mar 04 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.13.2-alt2
- NMU: added a proper synchronization to `init_shuffle_implementation`.
  Now tests pass properly on LoongArch (and possibly other weakly ordered
  CPUs).

* Mon Feb 12 2024 Anton Vyatkin <toni@altlinux.org> 2.13.2-alt1
- New version 2.13.2.

* Fri Jan 26 2024 Anton Vyatkin <toni@altlinux.org> 2.13.1-alt1
- New version 2.13.1.

* Fri Jan 19 2024 Anton Vyatkin <toni@altlinux.org> 2.12.0-alt1
- New version 2.12.0.

* Mon Dec 04 2023 Anton Vyatkin <toni@altlinux.org> 2.11.3-alt1
- New version 2.11.3.

* Fri Nov 24 2023 Anton Vyatkin <toni@altlinux.org> 2.11.2-alt1
- New version 2.11.2.

* Mon Oct 09 2023 Anton Vyatkin <toni@altlinux.org> 2.10.5-alt1
- New version 2.10.5.

* Fri Sep 29 2023 Anton Vyatkin <toni@altlinux.org> 2.10.4-alt1
- New version 2.10.4.

* Mon Sep 18 2023 Anton Vyatkin <toni@altlinux.org> 2.10.3-alt1
- New version 2.10.3.

* Mon Aug 21 2023 Anton Vyatkin <toni@altlinux.org> 2.10.2-alt1
- New version 2.10.2.

* Fri May 26 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.9.2-alt1.1
- Fixed build for Elbrus.

* Sun May 21 2023 Anton Vyatkin <toni@altlinux.org> 2.9.2-alt1
- New version 2.9.2.

* Fri May 12 2023 Anton Vyatkin <toni@altlinux.org> 2.9.1-alt1
- New version 2.9.1.

* Sun Mar 26 2023 Anton Vyatkin <toni@altlinux.org> 2.8.0-alt1
- New version 2.8.0.

* Tue Mar 21 2023 Anton Vyatkin <toni@altlinux.org> 2.7.1-alt1
- New version 2.7.1.

* Mon Jan 16 2023 Anton Vyatkin <toni@altlinux.org> 2.6.1-alt1
- Initial build for Sisyphus
