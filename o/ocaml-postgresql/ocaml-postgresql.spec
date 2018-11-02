%set_verify_elf_method textrel=relaxed
%define libname postgresql
Name: ocaml-%libname
Version: 4.4.1
Release: alt1
Summary: PostgreSQL Bindings for OCaml
Group: Development/ML
License: LGPLv3 with exceptions
Url: https://github.com/mmottl/postgresql-ocaml
Source0: %name-%version.tar
BuildRequires: dune
BuildRequires: ocaml
BuildRequires: ocaml-base-devel
BuildRequires: ocaml-stdio-devel
BuildRequires: opam
BuildRequires: postgresql-devel
BuildRequires: chrpath

%description
OCAML Postgresql offers library functions for accessing PostgreSQL databases.

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
dune build -p %libname 

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %libname.install
rm -rf %buildroot/usr/doc
chrpath -d %buildroot%_libdir/ocaml/stublibs/dllpostgresql_stubs.so


%check
dune runtest

%files
%doc README.md LICENSE.md CHANGES.md
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.dune
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/stublibs/dllpostgresql_stubs.so

%files devel
%_libdir/ocaml/%libname/opam
%_libdir/ocaml/%libname/*.cmt
%_libdir/ocaml/%libname/*.cmti
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs
%_libdir/ocaml/%libname/*.ml*

%changelog
* Fri Nov 02 2018 Anton Farygin <rider@altlinux.ru> 4.4.1-alt1
- first build for ALT
