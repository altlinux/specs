%set_verify_elf_method textrel=relaxed
%add_ocaml_req_skip Ppx_sigs_reflected
%define libname tyxml
Name:           ocaml-%libname
Version:        4.2.0
Release:        alt1
Summary:        TyXML is a library for building statically correct HTML5 and SVG documents
License:        LGPL with exeptions
Group:          Development/ML
Url:            https://ocsigen.org/tyxml/
# https://github.com/ocsigen/tyxml
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml >= 4.07.1 opam
BuildRequires: ocaml-ocamldoc ocaml-re ocaml-ppx_tools_versioned ocaml-uutf-devel ocaml-markup-devel
BuildRequires: ocaml-re-devel ocaml-result-devel
BuildRequires(pre):rpm-build-ocaml

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %version-%release

%description
TyXML allows you to build HTML5 and SVG trees whose validity is ensured by the typechecker.
It provides a printer for said XML trees, along with a ppx syntax extension. Finally 
it also provides a functorial interface to choose your XML datastructure. 
It's part of the ocsigen project and is used in js_of_ocaml and eliom.

%description devel
This package includes development files necessary for developing 
programs which use %name

%prep
%setup
%patch0 -p1

%build
./configure --prefix=%_prefix --destdir=%buildroot
%make

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc LICENSE CHANGES README.md COPYING Contributing.md
%_libdir/ocaml/%libname
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.mli

%files devel
%_bindir/ppx_tyxml_standalone
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.mli

%changelog
* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 4.2.0-alt1
- first build for ALT

