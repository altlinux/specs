%define soname 11

Name: primesieve
Version: 11.0
Release: alt1
Summary: A prime number generator
License: BSD-2-Clause
Group: Sciences/Mathematics
Url: https://github.com/kimwalisch/primesieve

Source: https://github.com/kimwalisch/primesieve/archive/v%version.tar.gz#/%name-%version.tar.gz

BuildPreReq: rpm-build-ninja ctest
BuildRequires: gcc-c++ cmake >= 3.7 doxygen texlive asciidoc-a2x graphviz

%description
primesieve is a command-line program that generates primes using the
sieve of Eratosthenes algorithm. It can generate primes and prime
k-tuplets (twin primes, prime triplets, ...) up to 2^64 and find the
nth prime.

%package -n lib%name%soname
Summary: C/C++ library for generating prime numbers
Group: System/Libraries

%description -n lib%name%soname
This package contains the shared runtime library for primesieve.

%package -n lib%name-devel
Summary: Development files for the primesieve library
Group: Development/Other

%description -n lib%name-devel
This package contains the C/C++ header files and the configuration
files for developing applications that use the primesieve library.
It also contains the API documentation of the library.

%prep
%setup

%build
%cmake \
    -GNinja \
    -DBUILD_STATIC_LIBS=OFF \
    -DBUILD_DOC=ON \
    -DBUILD_MANPAGE=ON \
    -DBUILD_TESTS=ON \
    -DCMAKE_SKIP_RPATH:BOOL=OFF
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%check
cd %_cmake__builddir
ctest

%files
%doc README.md ChangeLog
%_bindir/primesieve
%_man1dir/primesieve.1*

%files -n lib%name%soname
%doc COPYING
%_libdir/libprimesieve.so.%{soname}*

%files -n lib%name-devel
%doc examples
%_libdir/libprimesieve.so
%_includedir/primesieve.h
%_includedir/primesieve.hpp
%dir %_includedir/primesieve
%_includedir/primesieve/StorePrimes.hpp
%_includedir/primesieve/iterator.h
%_includedir/primesieve/iterator.hpp
%_includedir/primesieve/primesieve_error.hpp
%dir %_libdir/cmake/primesieve
%_libdir/cmake/primesieve/*.cmake
%_pkgconfigdir/primesieve.pc

%changelog
* Fri Dec 09 2022 Leontiy Volodin <lvol@altlinux.org> 11.0-alt1
- New version (11.0).

* Mon Jul 11 2022 Leontiy Volodin <lvol@altlinux.org> 8.0-alt1
- New version (8.0).

* Wed May 04 2022 Leontiy Volodin <lvol@altlinux.org> 7.9-alt1
- New version (7.9).

* Thu Mar 10 2022 Leontiy Volodin <lvol@altlinux.org> 7.8-alt1
- New version (7.8).

* Wed Dec 08 2021 Leontiy Volodin <lvol@altlinux.org> 7.7-alt1
- New version (7.7).

* Fri Nov 26 2021 Leontiy Volodin <lvol@altlinux.org> 7.6-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
