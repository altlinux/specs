%define optflags_lto %nil
%define _cmake__builddir BUILD
%define sover 0
%define libname libfreecell-solver%sover
%add_findreq_skiplist %_datadir/freecell-solver/presets/*.sh

Name: freecell-solver
Version: 6.8.0
Release: alt1

Group: Games/Cards
Summary: Library and application for solving Freecell card games
License: MIT
Url: http://fc-solve.shlomifish.org/

Requires: %name-common

Source: %name-%version.tar

# Automatically added by buildreq on Fri Jan 20 2023 (-bi)
# optimized out: bash4 bashrc cmake-modules debugedit elfutils glibc-kernheaders-generic libctf-nobfd0 libgpg-error libsasl2-3 libstdc++-devel perl perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Sub-Quote perl-Tie-RefHash perl-parent perl-podlators pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste python3-module-six rpm-build-file rpm-build-gir rpm-build-python3 rpm-macros-python3 sh4 tzdata xz
#BuildRequires: cmake gcc-c++ glibc-devel-static gperf libssl-devel perl-Moo perl-Path-Tiny perl-Pod-Usage perl-Template perl-autodie python-modules-encodings python3-module-mpl_toolkits python3-module-pysol-cards python3-module-random2 python3-module-setuptools python3-module-zope rinutils
BuildRequires: cmake gcc-c++ libgmp-devel
BuildRequires: rinutils gperf
BuildRequires: /usr/bin/pod2man
BuildRequires: perl(Moo.pm) perl(Template.pm) perl(autodie.pm) perl(Path/Tiny.pm)
BuildRequires: rpm-build-python3 python3(pysol_cards) python3(random2) python3(six)
#BuildRequires: perl-Moo perl-Path-Tiny perl-Pod-Usage perl-Template perl-autodie
#BuildRequires: python-modules-encodings python3-module-mpl_toolkits python3-module-pysol-cards python3-module-random2 python3-module-setuptools python3-module-zope

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

%build
%cmake \
    -DDISABLE_APPLYING_RPATH=TRUE \
    -DFCS_WITH_TEST_SUITE=OFF \
    -DBUILD_STATIC_LIBRARY=OFF \
    -DLIB_INSTALL_DIR=%{_libdir} \
    -DLOCALE_INSTALL_DIR=%_datadir/locale \
    -DMAX_NUM_FREECELLS=8 \
    -DMAX_NUM_STACKS=20 \
    -DMAX_NUM_INITIAL_CARDS_IN_A_STACK=60 \
    #
%cmake_build

%install
%makeinstall_std -C BUILD

%files common
%_datadir/freecell-solver/

%files -n %libname
%_libdir/libfreecell-solver.so.*
%_libdir/libfreecell-solver.so.%sover

%files
%_bindir/dbm-fc-solver
%_bindir/depth-dbm-fc-solver
%_bindir/fc-solve
%_bindir/freecell-solver-fc-pro-range-solve
%_bindir/freecell-solver-multi-thread-solve
%_bindir/freecell-solver-range-parallel-solve
%_bindir/make_pysol_freecell_board.py
%_bindir/fc_solve_find_index_s2ints.py
%_bindir/find-freecell-deal-index.py
%_bindir/gen-multiple-pysol-layouts
%_bindir/transpose-freecell-board.py
%_bindir/pi-make-microsoft-freecell-board
%_man6dir/*.6.*
#_docdir/*

%files devel
%_includedir/freecell-solver/
%_libdir/pkgconfig/*.pc
%_libdir/lib*.so

%changelog
* Fri Jan 20 2023 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- initial build
