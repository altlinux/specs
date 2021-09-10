# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:		sparse
Version:	0.6.4
Release:	alt1
Summary: 	A semantic parser for C
License:	MIT
Group:		Development/C
Vcs:		https://git.kernel.org/pub/scm/devel/sparse/sparse.git
Url:		http://sparse.wiki.kernel.org/

Source:		%name-%version.tar
BuildRequires:	libxml2-devel
# for test-inspect:
BuildRequires:	libgtk+3-devel
# for semind (ex sindex)
BuildRequires:	libsqlite3-devel
# for docs
BuildRequires:	python3-module-recommonmark
BuildRequires:	python3-module-sphinx
BuildRequires:	python3-module-sphinx_rtd_theme
BuildRequires:	sphinx

%description
Sparse, the semantic parser, provides a compiler frontend capable of parsing
most of ANSI C as well as many GCC extensions, and a collection of sample
compiler backends, including a static analyzer also called "sparse". Sparse
provides a set of annotations designed to convey semantic information about
types, such as what address space pointers point to, or what locks a function
acquires or releases.

Sparse is primarily used in the development and debugging of the Linux kernel.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%make_build CFLAGS="%optflags" V=1
%make_build -C Documentation SPHINXBUILD=sphinx-build-3 html

%install
%makeinstall_std PREFIX=%_prefix

%check
%make_build check

%files
%doc LICENSE README FAQ Documentation/build/html
%_bindir/c2xml
%_bindir/cgcc
%_bindir/semind
%_bindir/sparse
%_bindir/test-inspect
%_man1dir/*.1*

%changelog
* Fri Sep 10 2021 Vitaly Chikunov <vt@altlinux.org> 0.6.4-alt1
- Update to v0.6.4 (2021-09-06).

* Fri Oct 23 2020 Vitaly Chikunov <vt@altlinux.org> 0.6.3-alt1
- Update to v0.6.3 (2020-10-17).
- spec: Build html documentation.

* Wed Jul 01 2020 Vitaly Chikunov <vt@altlinux.org> 0.6.2-alt1
- Update to v0.6.2 (2020-06-16).
- Build cindex.

* Sat Mar 14 2020 Vitaly Chikunov <vt@altlinux.org> 0.6.1-alt2
- Update to v0.6.1 release.

* Wed Mar 13 2019 Vitaly Chikunov <vt@altlinux.org> 0.6.1-alt1_rc1
- First import of v0.6.1-rc1-2-g7fd3778.
- Newer version than in autoimports (0.6.0) and uses gtk3.
