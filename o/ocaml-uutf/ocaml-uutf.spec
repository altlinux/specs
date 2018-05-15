%set_verify_elf_method textrel=relaxed
Name: ocaml-uutf
Version: 0.9.4
Release: alt1%ubt
Summary: Non-blocking streaming codec for UTF-8, UTF-16, UTF-16LE and UTF-16BE
License: BSD3
Group: Development/ML
Url: http://erratique.ch/software/uutf
Source0: %name-%version.tar
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-result-devel
BuildRequires(pre): rpm-build-ubt

%description
Uutf is an non-blocking streaming Unicode codec for OCaml to decode and
encode the UTF-8, UTF-16, UTF-16LE and UTF-16BE encoding schemes. It can
efficiently work character by character without blocking on IO. Decoders
perform character position tracking and support newline normalization.

Functions are also provided to fold over the characters of UTF encoded OCaml
string values and to directly encode characters in OCaml Buffer.t values.

Uutf is made of a single, independent, module.

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
ocaml pkg/git.ml
ocaml pkg/build.ml native=true native-dynlink=true cmdliner=true

ocamlfind ocamlc -c -bin-annot -package cmdliner -I test -I _build/src -o test/utftrip.cmo test/utftrip.ml
ocamlfind ocamlopt -c -bin-annot -package cmdliner -I test -I _build/src -o test/utftrip.cmx test/utftrip.ml

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot/%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR/uutf
pushd _build/src/
 ocamlfind install uutf ../pkg/META *.a *.cm[iax] *.cmx[as] *.mli
popd

install -d %buildroot%_bindir/
install -m 0755 _build/test/utftrip.native %buildroot%_bindir/utftrip

%files
%doc README.md CHANGES.md
%dir %_libdir/ocaml/uutf
%_libdir/ocaml/uutf/META
%_libdir/ocaml/uutf/*.cma
%_libdir/ocaml/uutf/*.cmi
%_libdir/ocaml/uutf/*.cmxs
%_bindir/utftrip

%files devel
%doc doc/
%doc test/
%_libdir/ocaml/uutf/*.a
%_libdir/ocaml/uutf/*.cmxa
%_libdir/ocaml/uutf/*.cmx
%_libdir/ocaml/uutf/*.mli

%changelog
* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 0.9.4-alt1%ubt
- first build for ALT, based on specfile from Mageia

