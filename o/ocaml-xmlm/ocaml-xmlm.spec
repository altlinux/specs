%set_verify_elf_method textrel=relaxed
Name: ocaml-xmlm
%global libname %(sed -e 's/^ocaml-//' <<< %name)
Group: Development/ML
Version: 1.2.0
Release: alt3%ubt
Summary: A streaming XML codec
License: BSD
Url: http://erratique.ch/software/xmlm
# https://github.com/dbuenzli/xmlm
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild
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
#patch0 -p1 -b .debug

%build
./pkg/build true

%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p %buildroot%_bindir
mkdir -p $OCAMLFIND_DESTDIR/%libname

install -m 755 -p _build/test/xmltrip.native %buildroot%_bindir/xmltrip
install -m 644 -p _build/src/xmlm.{a,cmxa} $OCAMLFIND_DESTDIR/%libname/
install -m 755 -p _build/src/xmlm.cmxs $OCAMLFIND_DESTDIR/%libname/
install -m 644 -p _build/pkg/META _build/src/xmlm.{cm?,mli} $OCAMLFIND_DESTDIR/%libname/

%files
%doc README.md
%_bindir/xmltrip
%_libdir/ocaml/xmlm/
%exclude %_libdir/ocaml/*/*.a
%exclude %_libdir/ocaml/*/*.cmxa
%exclude %_libdir/ocaml/*/*.cmxs
%exclude %_libdir/ocaml/*/*.cmx
%exclude %_libdir/ocaml/*/*.mli

%files devel
# LICENSE not bundled
%doc CHANGES.md _build/test/examples.ml _build/test/xhtml.ml doc
%_libdir/ocaml/*/*.a
%_libdir/ocaml/*/*.cmxa
%_libdir/ocaml/*/*.cmxs
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.mli

%changelog
* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt3%ubt
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt2%ubt
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1%ubt
- first build for ALT, based on RH spec
