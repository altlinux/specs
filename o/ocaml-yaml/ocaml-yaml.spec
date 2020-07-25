%set_verify_elf_method textrel=relaxed
Name: ocaml-yaml
Version: 2.1.0
Release: alt1
Summary: Parse and generate YAML 1.1 files

Group: Development/ML
License: ISC
Url: https://github.com/avsm/ocaml-yaml
Source: %name-%version.tar

BuildRequires: dune ocaml-bos-devel ocaml-ctypes-devel
BuildRequires: ocaml-ppx_sexp_conv-devel ocaml-sexplib-devel ocaml-result-devel
BuildRequires: ocaml-integers-devel ocaml-compiler-libs-devel
BuildRequires: ocaml-migrate-parsetree-devel ocaml-ppxlib-devel
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
This is an OCaml library to parse and generate the YAML file format. It is
intended to interoperable with the Ezjsonm JSON handling library, if the simple
common subset of Yaml is used. Anchors and other advanced Yaml features are not
implemented in the JSON compatibility layer.

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
dune build

%install
dune install --destdir=%buildroot

%files
%doc README.md
%dir %_libdir/ocaml/yaml
%_libdir/ocaml/yaml*/META
%_libdir/ocaml/yaml*/*.cma
%_libdir/ocaml/yaml*/*.cmi
%_libdir/ocaml/yaml*/*.cmxs
%_libdir/ocaml/stublibs/*.so
%dir %_libdir/ocaml/yaml/unix
%_libdir/ocaml/yaml/unix/*.cma
%_libdir/ocaml/yaml/unix/*.cmi
%_libdir/ocaml/yaml/unix/*.cmxs
%dir %_libdir/ocaml/yaml/types
%_libdir/ocaml/yaml/types/*.cma
%_libdir/ocaml/yaml/types/*.cmi
%_libdir/ocaml/yaml/types/*.cmxs
%dir %_libdir/ocaml/yaml/ffi
%_libdir/ocaml/yaml/ffi/*.cma
%_libdir/ocaml/yaml/ffi/*.cmi
%_libdir/ocaml/yaml/ffi/*.cmxs
%dir %_libdir/ocaml/yaml/c
%_libdir/ocaml/yaml/c/*.cma
%_libdir/ocaml/yaml/c/*.cmi
%_libdir/ocaml/yaml/c/*.cmxs
%dir %_libdir/ocaml/yaml/bindings
%_libdir/ocaml/yaml/bindings/*.cma
%_libdir/ocaml/yaml/bindings/*.cmi
%_libdir/ocaml/yaml/bindings/*.cmxs
%dir %_libdir/ocaml/yaml/bindings/types
%_libdir/ocaml/yaml/bindings/types/*.cma
%_libdir/ocaml/yaml/bindings/types/*.cmi
%_libdir/ocaml/yaml/bindings/types/*.cmxs

%files devel
%_libdir/ocaml/yaml*/dune-package
%_libdir/ocaml/yaml*/opam
%_libdir/ocaml/yaml*/*.a
%_libdir/ocaml/yaml*/*.cmt*
%_libdir/ocaml/yaml*/*.cmxa
%_libdir/ocaml/yaml*/*.cmx
%_libdir/ocaml/yaml*/*.ml
%_libdir/ocaml/yaml*/*.mli
%_libdir/ocaml/yaml/c/*.a
%_libdir/ocaml/yaml/c/*.cmt*
%_libdir/ocaml/yaml/c/*.cmxa
%_libdir/ocaml/yaml/c/*.cmx
%_libdir/ocaml/yaml/c/*.ml
%_libdir/ocaml/yaml/ffi/*.a
%_libdir/ocaml/yaml/ffi/*.cmt*
%_libdir/ocaml/yaml/ffi/*.cmxa
%_libdir/ocaml/yaml/ffi/*.cmx
%_libdir/ocaml/yaml/ffi/*.ml
%_libdir/ocaml/yaml/unix/*.a
%_libdir/ocaml/yaml/unix/*.cmt*
%_libdir/ocaml/yaml/unix/*.cmxa
%_libdir/ocaml/yaml/unix/*.cmx
%_libdir/ocaml/yaml/unix/*.ml
%_libdir/ocaml/yaml/unix/*.mli
%_libdir/ocaml/yaml/types/*.a
%_libdir/ocaml/yaml/types/*.cmt*
%_libdir/ocaml/yaml/types/*.cmxa
%_libdir/ocaml/yaml/types/*.cmx
%_libdir/ocaml/yaml/types/*.ml
%_libdir/ocaml/yaml/bindings/*.a
%_libdir/ocaml/yaml/bindings/*.cmt*
%_libdir/ocaml/yaml/bindings/*.cmxa
%_libdir/ocaml/yaml/bindings/*.cmx
%_libdir/ocaml/yaml/bindings/*.ml
%_libdir/ocaml/yaml/bindings/types/*.a
%_libdir/ocaml/yaml/bindings/types/*.cmt*
%_libdir/ocaml/yaml/bindings/types/*.cmxa
%_libdir/ocaml/yaml/bindings/types/*.cmx
%_libdir/ocaml/yaml/bindings/types/*.ml
%_libdir/ocaml/yaml/bindings/types/*.mli

%changelog
* Wed Jul 08 2020 Mikhail Gordeev <obirvalger@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
