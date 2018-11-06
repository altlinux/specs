%set_verify_elf_method textrel=relaxed
%define libname syndic
Name: ocaml-%libname
Version: 1.5.3
Release: alt1
Summary: RSS1, RSS2, Atom and OPML1 parsing for OCaml
Group: Development/ML
License: MIT
Url: https://github.com/Cumulus/Syndic
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-oasis
BuildRequires: ocaml-ocamlbuild
BuildRequires: opam
BuildRequires: ocaml-xmlm-devel
BuildRequires: ocaml-uri-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-ptime-devel

%description
Pure OCaml Library for parsing and writing various types of feeds and subscriber
lists.

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
oasis setup
ocaml setup.ml -configure --prefix %buildroot%prefix
ocaml setup.ml -build


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%ocamldir
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install

%files
%doc README.md LICENSE
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.annot

%files devel
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs
%_libdir/ocaml/%libname/*.cmt
%_libdir/ocaml/%libname/*.cmti
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.ml*

%changelog
* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 1.5.3-alt1
- first build for ALT

