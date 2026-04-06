%define soname 8

Name: primecount
Version: 8.4
Release: alt1

Summary: Count the number of primes

License: BSD-2-Clause
Group: Sciences/Mathematics
Url: https://github.com/kimwalisch/primecount
VCS: https://github.com/kimwalisch/primecount

# Source-url: https://github.com/kimwalisch/primecount/archive/v%version.tar.gz#/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-ninja ctest
BuildRequires: gcc-c++ libgomp-devel cmake asciidoc-a2x libprimesieve-devel

%description
primecount is a command-line program that counts the primes below an
integer x less than or equal to 10^31 using highly optimized implementations of the
combinatorial prime counting algorithms.

%package -n lib%name%soname
Summary: C/C++ library for counting prime numbers
Group: System/Libraries

%description -n lib%name%soname
This package contains the shared runtime library for primecount.

%package -n lib%name-devel
Summary: Development files for the primecount library
Group: Development/Other

%description -n lib%name-devel
This package contains the C/C++ header files and the configuration
files for developing applications that use the primecount library.

%prep
%setup
%patch -p1

%build
%cmake \
    -GNinja \
    -DPRIMECOUNT_VERSION=%version \
%ifarch %e2k
    -DCMAKE_SHARED_LINKER_FLAGS="-fopenmp" \
    -DCMAKE_EXE_LINKER_FLAGS="-fopenmp" \
%endif
    -DBUILD_LIBPRIMESIEVE=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_STATIC_LIBS=OFF \
    -DSTATICALLY_LINK_LIBPRIMECOUNT=OFF \
    -DBUILD_MANPAGE=ON \
%ifnarch i586
    -DBUILD_TESTS=ON \
%endif
    -DCMAKE_SKIP_RPATH:BOOL=OFF
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%ifnarch i586
%check
cd %_cmake__builddir
ctest
%endif

%files
%doc README.md ChangeLog COPYING
%_bindir/primecount
%_man1dir/primecount.1*

%files -n lib%name%soname
%_libdir/libprimecount.so.%soname
%_libdir/libprimecount.so.%version

%files -n lib%name-devel
%doc doc/libprimecount.md
%_libdir/libprimecount.so
%_includedir/primecount.h
%_includedir/primecount.hpp
%_pkgconfigdir/primecount.pc
%_libdir/cmake/primecount/

%changelog
* Mon Apr 06 2026 Leontiy Volodin <lvol@altlinux.org> 8.4-alt1
- New version 8.4.

* Wed Mar 18 2026 Leontiy Volodin <lvol@altlinux.org> 8.3-alt1
- New version 8.3.

* Mon Feb 09 2026 Leontiy Volodin <lvol@altlinux.org> 8.2-alt1
- New version 8.2.

* Tue Jan 27 2026 Leontiy Volodin <lvol@altlinux.org> 8.1-alt1
- New version 8.1.

* Thu Dec 18 2025 Leontiy Volodin <lvol@altlinux.org> 8.0-alt1
- New version 8.0.

* Thu Nov 06 2025 Leontiy Volodin <lvol@altlinux.org> 7.20-alt1
- New version 7.20.

* Thu Jun 05 2025 Leontiy Volodin <lvol@altlinux.org> 7.19-alt1
- New version 7.19.

* Mon May 26 2025 Leontiy Volodin <lvol@altlinux.org> 7.18-alt1
- New version 7.18.

* Mon May 05 2025 Leontiy Volodin <lvol@altlinux.org> 7.17-alt1
- New version 7.17.

* Thu Apr 03 2025 Leontiy Volodin <lvol@altlinux.org> 7.16-alt1
- New version 7.16.

* Tue Mar 04 2025 Leontiy Volodin <lvol@altlinux.org> 7.15-alt1
- New version 7.15.
- Added vcs tag.

* Tue Aug 06 2024 Leontiy Volodin <lvol@altlinux.org> 7.14-alt1
- New version 7.14.

* Fri Apr 19 2024 Leontiy Volodin <lvol@altlinux.org> 7.13-alt1
- New version 7.13.

* Thu Apr 04 2024 Leontiy Volodin <lvol@altlinux.org> 7.12-alt1
- New version 7.12.

* Fri Mar 15 2024 Leontiy Volodin <lvol@altlinux.org> 7.11-alt1
- New version 7.11.
- Disabled tests on i586.

* Thu Jan 11 2024 Leontiy Volodin <lvol@altlinux.org> 7.10-alt1
- New version 7.10.

* Tue Jul 04 2023 Leontiy Volodin <lvol@altlinux.org> 7.9-alt1
- New version 7.9.

* Wed Jun 07 2023 Leontiy Volodin <lvol@altlinux.org> 7.8-alt1
- New version 7.8.

* Tue Dec 13 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 7.6-alt1.1
- Fixed build for Elbrus.

* Fri Dec 09 2022 Leontiy Volodin <lvol@altlinux.org> 7.6-alt1
- New version (7.6).

* Mon Jul 11 2022 Leontiy Volodin <lvol@altlinux.org> 7.4-alt1
- New version (7.4).

* Wed May 04 2022 Leontiy Volodin <lvol@altlinux.org> 7.3-alt1
- New version (7.3).

* Wed Dec 08 2021 Leontiy Volodin <lvol@altlinux.org> 7.2-alt1
- New version (7.2).

* Fri Nov 26 2021 Leontiy Volodin <lvol@altlinux.org> 7.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
