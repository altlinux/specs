%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
# For historical reasons, these have been out of step with the ABI
# versioning used by the base source.  The soversion reflects the stable
# "base" functionality, while the rest is considered unstable upstream.
%global somajor 1
%global sominor 10
%define fortran %nil
%define git f60be0f1c
%global optflags_lto %nil
# Avoid FTBFS with gcc 15 https://github.com/libxsmm/libxsmm/issues/933
%add_optflags -std=gnu17
# FIXME: we don't need fortran now
%def_without fortran
%if_without fortran
%define fortran FORTRAN=0
%endif
# AVX=0 no AVX/fallback to SSE
# AVX=1 is AVX
# AVX=2 is FMA
# AVX=3/MIC=1 is AXV512
%global makeflags STATIC=0 SYM=1 AVX=1 BLAS=1 %fortran PYTHON=%__python3 PREFIX=%_prefix POUTDIR=%_lib PPKGDIR=%_lib/pkgconfig VERSION_API=%somajor OMPLIB=-lgomp

Name: libxsmm
Version: 1.17
Release: alt1.g%{git}
Summary: Library for specialized dense and sparse matrix operations, and deep learning primitives
Group: System/Libraries
License: BSD-3-Clause
Url: https://libxsmm.readthedocs.io
Vcs: https://github.com/libxsmm/libxsmm.git
Source: %name-%version.tar
Patch: %name-rpath.patch

BuildRequires(pre): /proc rpm-build-python3
BuildRequires: gcc-c++ gcc-fortran libgomp-devel libgfortran-devel libopenblas-devel
%if_with fortran
BuildRequires: gcc-fortran libgfortran-devel
%endif

# https://github.com/libxsmm/libxsmm/issues/103#issuecomment-256887962
# the library does not support IA-32 in general!
ExclusiveArch: x86_64 aarch64

%description
Library for specialized dense and sparse matrix operations, and deep learning
primitives.

%package -n %name%somajor
Summary: Library for specialized dense and sparse matrix operations, and deep learning primitives
Group: System/Libraries
Provides: %name = %EVR

%description -n %name%somajor
Library for specialized dense and sparse matrix operations, and deep learning
primitives.

%package devel
Group: Development/C++
Summary: Headers and libraries for %name devel
Requires: %name = %EVR

%description devel
%summary.

%package doc
Group: Development/Documentation
Summary: Documentation for %name
BuildArch: noarch

%description doc
Documentation for %name

%prep
%setup
%autopatch -p1

# MS-Windows stuff that rpmlint would complain about
find samples -name \*.vcxproj | xargs rm
# README would clobber the main one, and the others would be dangling links
rm documentation/{README,LICENSE,CONTRIBUTING}.md
 
%build
%make_build V=1 %makeflags

%install
%if_with fortran
# f is fortran library and should be excluded
%add_verify_elf_skiplist %_libdir/%{name}f.so*
%endif

# Supply STATIC etc. since this actually builds stuff (a bug?),
# and otherwise we end up with bits built wrongly.
%make_install install %makeflags DESTDIR=%buildroot
mkdir -p %buildroot%_pkgconfigdir
[ -d %buildroot%_datadir/libxsmm ] && rm -r %buildroot%_datadir/libxsmm
# Build artifacts
cp Makefile.inc samples		# included by the sub-directories
echo "These are set up to be built in the original source tree.
You will have to adjust the make files to use an installed version." >samples/README
 
%check
LD_LIBRARY_PATH=%buildroot%_libdir make test-cp2k %makeflags
rm -rf samples/cp2k/obj
rm -r samples/cp2k/{.make,.state,cp2k-dbcsr,cp2k-collocate,cp2k-test.txt}

%files -n %name%somajor
%doc LICENSE.md
%_libdir/%{name}*.so.%{somajor}*

%files devel
%doc README.md
%_libdir/%{name}*.so
%_includedir/*
%_bindir/*
%_pkgconfigdir/*.pc

%files doc
%doc README.md documentation/*.md documentation/*.pdf samples CONTRIBUTING.md

%changelog
* Mon May 26 2025 L.A. Kostis <lakostis@altlinux.ru> 1.17-alt1.gf60be0f1c
- GIT f60be0f1c.
- Built without fortran (not needed for now).
- Initial build for ALTLinux based on some ideas from rawhide package with the
  same name.

