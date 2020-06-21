%set_verify_elf_method textrel=relaxed
Name: ocaml-trie
Version: 1.0.0
Release: alt1
Summary: Strict impure trie tree

Group: Development/ML
License: MIT
Url: https://github.com/kandu/trie
Source: %name-%version.tar

BuildRequires: dune ocaml-cppo
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
%dir %_libdir/ocaml/trie
%_libdir/ocaml/trie*/META
%_libdir/ocaml/trie*/*.cma
%_libdir/ocaml/trie*/*.cmi
%_libdir/ocaml/trie*/*.cmxs

%files devel
%_libdir/ocaml/trie*/dune-package
%_libdir/ocaml/trie*/opam
%_libdir/ocaml/trie*/*.a
%_libdir/ocaml/trie*/*.cmt*
%_libdir/ocaml/trie*/*.cmxa
%_libdir/ocaml/trie*/*.cmx
%_libdir/ocaml/trie*/*.mli
%_libdir/ocaml/trie*/*.ml

%changelog
* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
