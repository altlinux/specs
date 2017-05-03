%set_verify_elf_method textrel=relaxed
%define module sqlite3
Name: ocaml-%module
Version: 4.1.2
Release: alt3%ubt

Summary: OCaml library for accessing SQLite3 databases
License: GPL
Group: Development/ML
Url: http://www.ocaml.info/home/ocaml_sources.html
Source: http://www.ocaml.info/ocaml_sources/%name-%version.tar

BuildRequires: ocaml-findlib libsqlite3-devel ocaml-ocamldoc ocaml-ocamlbuild
Provides:	ocaml4-%module
Obsoletes:	ocaml4-%module


BuildPreReq: rpm-build-ocaml >= 1.1.1-alt2
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
* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 4.1.2-alt3%ubt
- rebuild with ocaml 4.04.1

* Wed Mar 29 2017 Anton Farygin <rider@altlinux.ru> 4.1.2-alt2%ubt
- updated to new version

* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Sep 17 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.2.0-alt1
- updated to new version

* Thu Mar 06 2008 Veaceslav Grecea <slavutich@altlinux.org> 0.23.0-alt1
- Adapted for ALTLinux

* Fri Feb 29 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-2
- Added BR ocaml-camlp4-devel.

* Sun Feb 24 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-1
- Initial RPM release.
