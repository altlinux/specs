%define optflags_lto %nil
%define _cmake__builddir BUILD
%define sover 1
%define libname libblack_hole_solver%sover

Name: black-hole-solver
Version: 1.12.0
Release: alt1

Group: Games/Cards
Summary: The Black Hole Solitaire Solver Executable
URL: https://www.shlomifish.org/open-source/projects/black-hole-solitaire-solver/
License: MIT

Requires: %name-common

Source: %name-%version.tar
# SuSE
Patch1: fix-pkgconfig-libdir.patch

# Automatically added by buildreq on Mon Jan 23 2023 (-bi)
# optimized out: cmake-modules debugedit elfutils glibc-kernheaders-generic libctf-nobfd0 libgpg-error libsasl2-3 libstdc++-devel perl perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Tie-RefHash perl-parent perl-podlators pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste rpm-build-file rpm-build-python3 sh4 tzdata xz
#BuildRequires: cmake gcc-c++ libssl-devel libxxhash-devel perl-Path-Tiny perl-Pod-Usage perl-autodie python-modules-encodings python3-module-mpl_toolkits python3-module-setuptools python3-module-zope rinutils
BuildRequires: cmake gcc-c++
BuildRequires: libxxhash-devel
BuildRequires: perl-Path-Tiny perl-Pod-Usage perl-autodie
BuildRequires: python-modules-encodings python3-module-mpl_toolkits python3-module-setuptools python3-module-zope
BuildRequires: rinutils

%description
The Freecell Solver package contains the fc-solve executable which is
a command-line program that can be used to solve games of Freecell and
similar card solitaire variants.

This package also contains command line executables to generate the initial
boards of several popular Freecell implementations.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package

%package -n %libname
Group: System/Libraries
Summary: The Freecell Solver dynamic libraries for solving Freecell games
Requires: %name-common
%description -n %libname
Contains the Freecell Solver libraries that are used by some programs to solve
games of Freecell and similar variants of card solitaire.

%package devel
Group: Development/Other
Summary: The Freecell Solver development tools for solving Freecell games
Requires: %name-common
%description devel
You should install it if you are a game developer who would like to use
Freecell Solver from within your programs.


%prep
%setup
%patch1 -p1

%build
%cmake \
    -DLIB_INSTALL_DIR=%{_libdir} \
    -DLOCALE_INSTALL_DIR=%_datadir/locale \
    -DBUILD_STATIC_LIBRARY=OFF \
    -DDISABLE_APPLYING_RPATH=TRUE \
    -DFCS_WITH_TEST_SUITE=OFF \
    -DFCS_AVOID_TCMALLOC=ON \
    -DUSE_SYSTEM_XXHASH=ON \
    -DENABLE_DISPLAYING_MAX_NUM_PLAYED_CARDS=ON \
    #
%cmake_build

%install
%makeinstall_std -C BUILD

%files common
%doc COPYING
#%_datadir/black-hole-solver/

%files -n %libname
%_libdir/libblack_hole_solver.so.*
%_libdir/libblack_hole_solver.so.%sover

%files
%_bindir/black-hole-solve
%_man6dir/*.6.*

%files devel
%_includedir/black-hole-solver/
%_libdir/pkgconfig/*.pc
%_libdir/lib*.so

%changelog
* Mon Jan 23 2023 Sergey V Turchin <zerg@altlinux.org> 1.12.0-alt1
- initial build
