%define _unpackaged_files_terminate_build 1

Name: pax-utils
Version: 1.3.7
Release: alt1

Summary: ELF utils that can check files for security relevant properties
License: GPL-2.0
Group: Development/Tools
Url: https://wiki.gentoo.org/wiki/Hardened/PaX_Utilities
VCS: https://anongit.gentoo.org/git/proj/pax-utils.git

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-elftools

BuildRequires: meson
BuildRequires: xmlto
BuildRequires: libcap-devel

%description
pax-utils is a small set of utilities for performing Q/A (mostly security)
checks on systems (most notably, scanelf). It is focused on the ELF format, but
does include a Mach-O helper too for OS X systems.

While heavily integrated into Gentoo's build system, it can be used on any
distro as it is a generic toolset.

Originally focused only on PaX, it has been expanded to be generally security
focused. It still has a good number of PaX helpers for people interested in
that.

%prep
%setup
%patch0 -p1

sed -i -e 's|/usr/bin/env python|/usr/bin/python3|' lddtree.py

%build
%meson \
    -Dlddtree_implementation=python \
    -Duse_libcap=enabled \
    -Duse_seccomp=true \
    -Dbuild_manpages=enabled \
    -Dtests=true \
    -Duse_fuzzing=false

%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md COPYING
%_bindir/*
%_man1dir/*

%changelog
* Mon Jun 05 2023 Egor Ignatov <egori@altlinux.org> 1.3.7-alt1
- First build for ALT
