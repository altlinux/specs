%set_verify_elf_method textrel=relaxed
Name: ocaml-mew
Version: 0.1.0
Release: alt1
Summary: Modal Editing Witch

Group: Development/ML
License: MIT
Url: https://github.com/kandu/mew
Source: %name-%version.tar

BuildRequires: dune ocaml-cppo ocaml-trie
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
This is the core module of mew, a general modal editing engine generator.

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
%dir %_libdir/ocaml/mew
%_libdir/ocaml/mew*/META
%_libdir/ocaml/mew*/*.cma
%_libdir/ocaml/mew*/*.cmi
%_libdir/ocaml/mew*/*.cmxs

%files devel
%_libdir/ocaml/mew*/dune-package
%_libdir/ocaml/mew*/opam
%_libdir/ocaml/mew*/*.a
%_libdir/ocaml/mew*/*.cmt*
%_libdir/ocaml/mew*/*.cmxa
%_libdir/ocaml/mew*/*.cmx
%_libdir/ocaml/mew*/*.ml

%changelog
* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
