Name: yosyshq-abc
Version: 0.67
Release: alt1
Summary: Sequential logic synthesis and formal verification
# The ABC code itself is MIT-Modern-Variant.
# The bundled CUDD code is BSD-3-Clause.
# The bundled glucose code is MIT.
# The bundled minisat code is MIT.
# The bundled satoko code is BSD-2-Clause
License: MIT-Modern-Variant AND MIT AND BSD-2-Clause AND BSD-3-Clause
Group: Engineering
URL: https://github.com/YosysHQ/abc
VCS: https://github.com/YosysHQ/abc
Source: %name-%version.tar
Source1: abc.1
Patch: %name-%version-%release.patch
Patch1: 0001-fedora-do-not-use-bundled-libraries.patch
Patch2: 0002-fedora-build-shared-instead-of-static-library.patch
Patch3: 0003-fedora-fix-minor-header-issue.patch
Patch4: 0004-fedora-set-soname-on-the-library.patch
Patch5: 0005-fedora-fix-sprintf-calls-that-may-overflow-their-buf.patch
Patch6: 0006-fedora-fix-out-of-bounds-array-access-in-gia-code-be.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(zlib)

Requires: %name-libs = %EVR

Obsoletes: alanmi-abc =< 20221019.0.70cb339f-alt1

# upstream abc commit 0ff43a1 (Command "aigsim".) added breaking change
ExcludeArch: %ix86

%description
ABC is a growing software system for synthesis and verification of
binary sequential logic circuits appearing in synchronous hardware
designs.  ABC combines scalable logic optimization based on And-Inverter
Graphs (AIGs), optimal-delay DAG-based technology mapping for look-up
tables and standard cells, and innovative algorithms for sequential
synthesis and verification.

ABC provides an experimental implementation of these algorithms and a
programming environment for building similar applications.  Future
development will focus on improving the algorithms and making most of
the packages stand-alone.  This will allow the user to customize ABC for
their needs as if it were a toolbox rather than a complete tool.

%package libs
Summary: Library for sequential synthesis and verification
Group: System/Libraries

%description libs
This package contains the core functionality of ABC as a shared library.

%package devel
Summary: Headers and libraries for developing with ABC
Group: Development/Other	
Requires: %name-libs = %EVR

%description devel
Headers and libraries for developing applications that use ABC.

%prep
%setup
%autopatch -p1

# Do not use the bundled bzip2 or zlib libraries
rm -r lib src/misc/{bzlib,zlib}

# Do not override ALT Linux optimization flags
sed -i 's/ -O//' Makefile

%build
export CFLAGS='%optflags -DNDEBUG'
export CXXFLAGS='%optflags -DNDEBUG'
export ABC_MAKE_VERBOSE=1
export ABC_USE_STDINT_H=1
export ABC_USE_PIC=1
%cmake  -DCMAKE_SKIP_RPATH:BOOL=YES \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
	-DABC_SKIP_TESTS:BOOL=YES \
	-DBUILD_SHARED_LIBS:BOOL=ON

%cmake_build

%install
# %%cmake_install does not install anything.  Install by hand.

# Install the binary
cd %_cmake__builddir
install -Dpm 0755 abc %buildroot%_bindir/abc

# Install the library
mkdir -p %buildroot%_libdir
cp -pd libabc.so* %buildroot%_libdir
cd -

# Install the header files
cd src
mkdir -p %buildroot%_includedir/abc
tar -cf - $(find -O3 . -name \*.h) | \
  (cd %buildroot%_includedir/abc; tar -xf -)
cd -

# Install the man page
install -pD -m 0644 %SOURCE1 %buildroot%_man1dir/abc.1

%files
%doc README.md readmeaig
%_bindir/abc
%_man1dir/abc.1.*

%files libs
%doc copyright.txt
%_libdir/libabc.so.0*

%files devel
%_includedir/abc/
%_libdir/libabc.so

%changelog
* Sun Jul 19 2026 Anton Midyukov <antohami@altlinux.org> 0.67-alt1
- Initial build.
