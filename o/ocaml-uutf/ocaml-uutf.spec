%set_verify_elf_method textrel=relaxed
Name: ocaml-uutf
Version: 1.0.1
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
BuildRequires: ocaml-topkg opam
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
ocaml pkg/pkg.ml build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml 

%files
%doc README.md CHANGES.md
%dir %_libdir/ocaml/uutf
%_libdir/ocaml/uutf/META
%_libdir/ocaml/uutf/*.cma
%_libdir/ocaml/uutf/*.cmi
%_libdir/ocaml/uutf/*.cmti
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
* Mon May 21 2018 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1%ubt
- 1.0.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 0.9.4-alt1%ubt
- first build for ALT, based on specfile from Mageia

