%set_verify_elf_method textrel=relaxed
Name: ocaml-xmlm
%global libname %(sed -e 's/^ocaml-//' <<< %name)
Group: Development/ML
Version: 1.3.0
Release: alt1%ubt
Summary: A streaming XML codec
License: BSD
Url: http://erratique.ch/software/xmlm
# https://github.com/dbuenzli/xmlm
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.06
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-topkg
BuildRequires: opam
BuildRequires(pre):rpm-build-ubt

%description
Xmlm is an OCaml streaming codec to decode and encode the XML data
format. It can process XML documents without a complete in-memory
representation of the data.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
ocaml ./pkg/pkg.ml build

%install
mkdir -p %buildroot%_libdir/ocaml
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc README.md LICENSE.md
%_bindir/xmltrip
%_libdir/ocaml/xmlm/
%exclude %_libdir/ocaml/*/*.a
%exclude %_libdir/ocaml/*/*.cmxa
%exclude %_libdir/ocaml/*/*.cmxs
%exclude %_libdir/ocaml/*/*.cmx
%exclude %_libdir/ocaml/*/*.mli

%files devel
%doc CHANGES.md _build/test/examples.ml _build/test/xhtml.ml doc
%_libdir/ocaml/*/*.a
%_libdir/ocaml/*/*.cmxa
%_libdir/ocaml/*/*.cmxs
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.mli

%changelog
* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1%ubt
- 1.3.0

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt3%ubt
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt2%ubt
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1%ubt
- first build for ALT, based on RH spec
