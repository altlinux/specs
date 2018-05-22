%set_verify_elf_method textrel=relaxed
Name: ocaml-jsonm
Version: 1.0.1
Release: alt1%ubt
Summary: Non-blocking streaming codec to decode and encode JSON
License: BSD3
Group: Development/ML
Url: http://erratique.ch/software/jsonm
Source0: %name-%version.tar
BuildRequires: ocaml-findlib
BuildRequires: ocaml-uutf-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-ocamlbuild opam ocaml-topkg
BuildRequires: ocaml-uutf 
Requires: ocaml-uutf
BuildRequires(pre):rpm-build-ubt

%description
Jsonm is a non-blocking streaming codec to decode and encode the JSON data
format. It can process JSON text without blocking on IO and without a
complete in-memory representation of the data.

The uncut codec also processes whitespace and (non-standard) JSON with
JavaScript comments.

Jsonm is made of a single module and depends on Uutf.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: ocaml-uutf-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
ocaml pkg/pkg.ml build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc README.md CHANGES.md
%dir %_libdir/ocaml/jsonm
%_libdir/ocaml/jsonm/META
%_libdir/ocaml/jsonm/*.cma
%_libdir/ocaml/jsonm/*.cmi
%_libdir/ocaml/jsonm/*.cmti
%_libdir/ocaml/jsonm/*.cmxs
%_bindir/jsontrip

%files devel
%doc doc/
%_libdir/ocaml/jsonm/*.a
%_libdir/ocaml/jsonm/*.cmxa
%_libdir/ocaml/jsonm/*.cmx
%_libdir/ocaml/jsonm/*.mli

%changelog
* Mon May 21 2018 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1%ubt
- 1.0.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1%ubt
- first build for ALT, based on Mageia spec

