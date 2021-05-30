# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: dwgrep
Version: 0.4
Release: alt2.1
Summary: A tool for querying Dwarf (debuginfo) graphs
License: GPLv3+ and (GPLv2+ or LGPLv3+)
Group: Development/Debuggers
Url: http://pmachata.github.io/dwgrep/index.html
Vcs: https://github.com/pmachata/dwgrep.git
Provides: libzwerg-devel

Source: %name-%version.tar
BuildRequires(pre): cmake
BuildRequires: ctest
BuildRequires: elfutils-devel
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: libgtest-devel
BuildRequires: python3-module-sphinx

%description
Dwgrep is a tool, an associated language (called Zwerg) and a library
(libzwerg) for querying Dwarf (debuginfo) graphs.

You can think of dwgrep expressions as instructions describing a path
through a graph, with assertions about the type of nodes along the way:
that a node is of given type, that it has a given attribute, etc. There
are also means of expressing sub-conditions, i.e. assertions that a given
node is acceptable if a separate expression matches (or does not match)
a different path through the graph.

%prep
%setup

%build
%cmake -DSPHINX_EXECUTABLE=/usr/bin/sphinx-build-3
%cmake_build
%cmake_build --target doc

%install
%cmake_install

rm -rf %buildroot%_includedir/libzwerg
rm -rf %buildroot%_libdir/libzwerg.so

%check
# %%cmake_buidl cannot be used due to newline prefix.
LD_LIBRARY_PATH=%buildroot%_libdir \
	ctest --output-on-failure

%files
%doc AUTHORS COPYING COPYING-LGPLV3 NEWS README
%_bindir/dwgrep
%_libdir/libzwerg.so.*
%_man1dir/dwgrep.1.xz

%changelog
* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.4-alt2.1
- NMU: spec: adapted to new cmake macros.

* Sat Dec 05 2020 Vitaly Chikunov <vt@altlinux.org> 0.4-alt2
- Do not package libzwerg development files.

* Thu Dec 03 2020 Vitaly Chikunov <vt@altlinux.org> 0.4-alt1
- First import of 0.4-13-g24b93c3 (2020-11-20).
