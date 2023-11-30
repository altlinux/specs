%define libname omd
Name: ocaml-%libname
Version: 1.3.2
Release: alt1
Summary: OMD: extensible Markdown library and tool in OCaml
Group: Development/ML
License: ISC
Url: https://github.com/ocaml/omd
Source0: %name-%version.tar
BuildRequires: ocaml dune
BuildRequires: rpm-build-ocaml > 1.4

%description
This Markdown library is implemented using only pure OCaml (including
I/O operations provided by the standard OCaml compiler distribution).
OMD is meant to be as faithful as possible to the original Markdown.
Additionally, OMD implements a few Github markdown features, an extension
mechanism, and some other features. Note that the opam package installs both the
OMD library and the command line tool omd

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md ABOUT.md
%_bindir/omd

%files devel -f ocaml-files.devel

%changelog
* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Wed Sep 16 2020 Anton Farygin <rider@altlinux.ru> 1.3.1-alt3
- adaptation for rpm-build-ocaml-1.4
- devel parts moved to devel package

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 1.3.1-alt2
- rebuilt with ocaml-4.08

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- first build for ALT

