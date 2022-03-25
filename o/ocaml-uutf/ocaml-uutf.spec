%set_verify_elf_method textrel=relaxed
Name: ocaml-uutf
Version: 1.0.3
Release: alt1
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
%_libdir/ocaml/uutf/opam
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
* Thu Mar 24 2022 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Tue Mar 30 2021 Anton Farygin <rider@altlinux.org> 1.0.2-alt2
- removed uutf dependency

* Fri Jan 31 2020 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 1.0.1-alt4
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.1-alt3
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.0.1-alt2
- rebuilt with ocaml-4.07

* Mon May 21 2018 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 0.9.4-alt1
- first build for ALT, based on specfile from Mageia

