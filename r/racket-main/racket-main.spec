%define _unpackaged_files_terminate_build 1

%add_debuginfo_skiplist %_bindir/*

%define _racket       %_bindir/racket
%define _raco	      %_racket -l raco/main.rkt
%define _raco_install %_raco pkg install --copy -i -t dir

%define fakechroot_dir %_builddir/fakechroot
%define fakechroot_default_pkgset bash coreutils racket-core

%define fakechroot_rpmi %_builddir/fakechroot-rpm-i %fakechroot_dir
%define fakechroot_rpme %_builddir/fakechroot-rpm-e %fakechroot_dir

%define fakechroot_init   %fakechroot_rpmi %fakechroot_default_pkgset
%define fakechroot_deinit %fakechroot_rpme %fakechroot_default_pkgset

%define fakechroot_bash_execute fakechroot chroot %fakechroot_dir /bin/bash -c
%define fakechroot_raco_install() %fakechroot_bash_execute '%_raco_install %*'

Name: racket-main
Version: 8.6
Release: alt3

Summary: Racket, the programming language (main-distribution packages)
License: GPL-3.0 or LGPL-3.0 or Apache-2.0 or MIT
Group: Development/Scheme
Url: https://racket-lang.org
Vcs: https://github.com/racket/racket

# racket: https://download.racket-lang.org/racket-8-6-src-tgz.html

Source0: %name-%version.tar
Source1: fakechroot-rpm-e
Source2: fakechroot-rpm-i

BuildRequires(pre): /proc
BuildRequires(pre): rpm-macros-racket
BuildRequires: racket-core

BuildRequires: fakechroot

BuildRequires: libcairo
BuildRequires: libpango
BuildRequires: libjpeg
BuildRequires: libsqlite3
BuildRequires: fontconfig
BuildRequires: fonts-ttf-liberation

%add_findreq_skiplist %racket_pkgsdir/*/*
%add_findreq_skiplist %racket_pkgsdir/*/*/*
%add_findreq_skiplist %racket_pkgsdir/*/*/*/*

%add_findprov_skiplist %racket_pkgsdir/*/*
%add_findprov_skiplist %racket_pkgsdir/*/*/*
%add_findprov_skiplist %racket_pkgsdir/*/*/*/*

Provides:  plt = %EVR
Obsoletes: plt < %EVR

Provides:  racket = %EVR
Obsoletes: racket < %EVR

Requires: racket-core
# some games from `plt-games' requires libGLU
Requires: libGLU

# The arches where cpu time limit is not exceeded...
ExclusiveArch: x86_64 aarch64

%description
%summary.

This package contains main-distribution packages (and DrRacket).

%prep
%setup
cp %SOURCE1 %_builddir
cp %SOURCE2 %_builddir

# prepare fakechroot packages
%fakechroot_init
%fakechroot_rpmi fontconfig
%fakechroot_rpmi fonts-ttf-liberation

# copy racket packages to fakechroot
cp -rT share/pkgs %fakechroot_dir%racket_pkgsdir

# remove pkgs.rktd to use raco with '-t dir *' option
rm %fakechroot_dir%racket_pkgsdir/pkgs.rktd

%build
# build packages in fakechroot
%fakechroot_raco_install %racket_pkgsdir/*

# remove fakechroot packages
%fakechroot_rpme fonts-ttf-liberation
%fakechroot_rpme fontconfig
%fakechroot_deinit

# remove cache and garbage
rm -rfv %fakechroot_dir%_datadir/fonts
rm -rfv %fakechroot_dir%_cachedir/fontconfig

%install
# racket(1) is provided by racket-base
rm %fakechroot_dir%_man1dir/racket.1

# follow .d rule for launchers and mans inside %%libdir
mkdir -p %fakechroot_dir%racket_libdir/launchers.d
mkdir -p %fakechroot_dir%racket_libdir/mans.d

mv %fakechroot_dir%racket_libdir/launchers.{rktd,d/%name.rktd}
mv %fakechroot_dir%racket_libdir/mans.{rktd,d/%name.rktd}

# fix sources paths for packages in generated pkgs.rktd
sed -i 's|"/usr/lib/racket/pkgs/[^"[:space:]]*"|"ALT"|g' \
       %fakechroot_dir%racket_pkgsdir/pkgs.rktd

mv %fakechroot_dir %buildroot

%files
%_man1dir/*
%_bindir/*
%_desktopdir/*
%racket_sharedir/
%racket_docdir/
%racket_pkgsdir/
%racket_libdir/*.d/

%changelog
* Sun Feb 12 2023 Anton Zhukharev <ancieg@altlinux.org> 8.6-alt3
- fix removing fonts from fakechroot (force it)

* Mon Jan 09 2023 Anton Zhukharev <ancieg@altlinux.org> 8.6-alt2
- set dependency on racket-core package

* Sun Jan 08 2023 Anton Zhukharev <ancieg@altlinux.org> 8.6-alt1
- main distribution packages for Racket

