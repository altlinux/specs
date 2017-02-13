%set_verify_elf_method textrel=relaxed
%define module sqlite3
Name: ocaml4-%module
Version: 4.1.2
Release: alt1%ubt

Summary: OCaml library for accessing SQLite3 databases
License: GPL
Group: Development/ML
Url: http://www.ocaml.info/home/ocaml_sources.html
Source: http://www.ocaml.info/ocaml_sources/%name-%version.tar

BuildRequires: ocaml4-findlib libsqlite3-devel ocaml4-ocamldoc ocaml4-ocamlbuild
Conflicts: ocaml-%module
Provides:	ocaml-%module
Obsoletes:	ocaml-%module


BuildPreReq: rpm-build-ocaml4 >= 1.1
BuildRequires(pre): rpm-build-ubt
%description
SQLite 3 database library wrapper for OCaml.

%package runtime
Summary: OCaml library for accessing SQLite3 databases
Group: Development/ML

%description runtime
Runtime part of OCaml library for accessing SQLite3 databases

%prep
%setup -q 
%define docdir %_docdir/%name-%version
./configure --mandir=%_mandir --docdir=%buildroot%docdir --destdir=%buildroot

%build
make all

%install
%define ocamlsitelib %_libdir/ocaml/site-lib
%define ocamlstublib %_libdir/ocaml/stublibs/
export OCAMLFIND_LDCONF=ignore
export OCAMLFIND_DESTDIR=%buildroot%ocamlsitelib/
export DESTDIR=%buildroot
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs

%makeinstall

rm -f %buildroot%ocamlsitelib/%module/*.annot
rm -f %buildroot%ocamlsitelib/%module/*.cmx
rm -f %buildroot%ocamlsitelib/%module/*.cmt
rm -f %buildroot%ocamlsitelib/%module/*.cmti
rm -f %buildroot%ocamlsitelib/%module/*.ml
rm -f %buildroot%ocamlsitelib/%module/*.mli

mkdir -p %buildroot%ocamlstublib/
mv $OCAMLFIND_DESTDIR/stublibs/* %buildroot%ocamlstublib/

%files
%doc COPYING.txt CHANGES.txt README.md TODO.md
%ocamlsitelib/%module

%files runtime
%ocamlstublib/*.so
%ocamlstublib/*.so.owner

%changelog
* Mon Feb 13 2017 Anton Farygin <rider@altlinux.ru> 4.1.2-alt1%ubt
- build for ocaml4
