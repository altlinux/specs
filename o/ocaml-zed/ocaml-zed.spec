%set_verify_elf_method textrel=relaxed
Name: ocaml-zed
Version: 3.1.0
Release: alt1
Summary: Abstract engine for text edition in OCaml

Group: Development/ML
License: BSD-3-Clause
Url: https://github.com/ocaml-community/zed
Source: %name-%version.tar

BuildRequires: dune ocaml-charInfo_width ocaml-camomile ocaml-result ocaml-react
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
%summary.

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
%doc CHANGES.md README.md
%dir %_libdir/ocaml/zed
%_libdir/ocaml/zed*/META
%_libdir/ocaml/zed*/*.cma
%_libdir/ocaml/zed*/*.cmi
%_libdir/ocaml/zed*/*.cmxs

%files devel
%_libdir/ocaml/zed*/dune-package
%_libdir/ocaml/zed*/opam
%_libdir/ocaml/zed*/*.a
%_libdir/ocaml/zed*/*.cmt*
%_libdir/ocaml/zed*/*.cmxa
%_libdir/ocaml/zed*/*.cmx
%_libdir/ocaml/zed*/*.mli
%_libdir/ocaml/zed*/*.ml

%changelog
* Sun Jun 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus
