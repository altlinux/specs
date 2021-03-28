Name: utop
Version: 2.7.0
Release: alt1
Summary: Universal toplevel for OCaml

Group: Development/ML
License: MIT
Url: https://github.com/ocaml-community/utop
Source: %name-%version.tar

BuildRequires: dune ocaml-cppo ocaml-lambda-term ocaml-findlib
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
utop is an improved toplevel (i.e., Read-Eval-Print Loop) for OCaml.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
sed -i 's/%%%%VERSION%%%%/%version/' src/lib/uTop.ml

%build
%dune_build -p %name

%install
%dune_install %name

%check
%dune_check

%files
%doc CHANGES.md README.md
%doc %_datadir/utop
%_man1dir/utop*
%_man5dir/utop*
%_bindir/utop
%_bindir/utop-full
%_emacslispdir/utop.el
%dir %_libdir/ocaml/utop
%_libdir/ocaml/utop*/META
%_libdir/ocaml/utop*/*.cma
%_libdir/ocaml/utop*/*.cmi

%files devel
%_libdir/ocaml/utop*/dune-package
%_libdir/ocaml/utop*/opam
%_libdir/ocaml/utop*/*.cmt*
%_libdir/ocaml/utop*/*.mli
%_libdir/ocaml/utop*/*.ml

%changelog
* Sun Mar 28 2021 Mikhail Gordeev <obirvalger@altlinux.org> 2.7.0-alt1
- new version 2.7.0

* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus
