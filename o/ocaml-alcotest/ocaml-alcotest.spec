%set_verify_elf_method textrel=relaxed
%define libname alcotest
Name: ocaml-%libname
Version: 1.0.0
Release: alt1
Summary: Alcotest is a lightweight and colourful test framework.
Group: Development/ML
License: ISC
Url: https://github.com/mirage/alcotest
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune >= 1.8
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: opam
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-lwt-devel
BuildRequires: ocaml-logs-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-astring-devel
BuildRequires: ocaml-uuidm-devel
BuildRequires: ocaml-fmt-devel

%description
Alcotest exposes simple interface to perform unit tests. It exposes a simple
TESTABLE module type, a check function to assert test predicates and a run
function to perform a list of unit -> unit test callbacks.

Alcotest provides a quiet and colorful output where only faulty runs are fully
displayed at the end of the run (with the full logs ready to inspect), with a
simple (yet expressive) query language to select the tests to run.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
dune build -p %libname

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %libname.install
rm -rf %buildroot/usr/doc

# Makes *.cmxs executable such that they will be stripped.
find %buildroot -name '*.cmxs' -exec chmod 0755 {} \;

%check
dune runtest

%files
%doc README.md
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a

%files devel
%_libdir/ocaml/%libname/opam
%_libdir/ocaml/%libname/dune-package
%_libdir/ocaml/%libname/*.cmt
%_libdir/ocaml/%libname/*.cmti
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.ml*
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs

%changelog
* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.8.5-alt3
- rebuilt with ocaml-4.08

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.8.5-alt2
- rebuilt with dune-1.8

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.8.4-alt1
- first build for ALT

