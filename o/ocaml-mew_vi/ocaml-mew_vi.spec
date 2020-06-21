%set_verify_elf_method textrel=relaxed
Name: ocaml-mew_vi
Version: 0.5.0
Release: alt1
Summary: Modal editing witch, VI interpreter

Group: Development/ML
License: MIT
Url: https://github.com/kandu/mew_vi
Source: %name-%version.tar

BuildRequires: dune ocaml-cppo ocaml-react ocaml-mew
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
This is a vi-like modal editing engine generator.

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
%dir %_libdir/ocaml/mew_vi
%_libdir/ocaml/mew_vi*/META
%_libdir/ocaml/mew_vi*/*.cma
%_libdir/ocaml/mew_vi*/*.cmi
%_libdir/ocaml/mew_vi*/*.cmxs

%files devel
%_libdir/ocaml/mew_vi*/dune-package
%_libdir/ocaml/mew_vi*/opam
%_libdir/ocaml/mew_vi*/*.a
%_libdir/ocaml/mew_vi*/*.cmt*
%_libdir/ocaml/mew_vi*/*.cmxa
%_libdir/ocaml/mew_vi*/*.cmx
%_libdir/ocaml/mew_vi*/*.ml

%changelog
* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
