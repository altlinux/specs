%set_verify_elf_method textrel=relaxed
Name: ocaml-charInfo_width
Version: 1.1.0
Release: alt1
Summary: Determine column width for a character

Group: Development/ML
License: MIT
Url: https://bitbucket.org/zandoye/charinfo_width/
Source: %name-%version.tar

BuildRequires: dune ocaml-camomile ocaml-result
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
%dir %_libdir/ocaml/charInfo_width
%_libdir/ocaml/charInfo_width*/META
%_libdir/ocaml/charInfo_width*/*.cma
%_libdir/ocaml/charInfo_width*/*.cmi
%_libdir/ocaml/charInfo_width*/*.cmxs

%files devel
%_libdir/ocaml/charInfo_width*/dune-package
%_libdir/ocaml/charInfo_width*/opam
%_libdir/ocaml/charInfo_width*/*.a
%_libdir/ocaml/charInfo_width*/*.cmt*
%_libdir/ocaml/charInfo_width*/*.cmxa
%_libdir/ocaml/charInfo_width*/*.cmx
%_libdir/ocaml/charInfo_width*/*.mli
%_libdir/ocaml/charInfo_width*/*.ml

%changelog
* Sun Jun 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
