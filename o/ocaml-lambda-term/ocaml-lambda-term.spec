%set_verify_elf_method textrel=relaxed
Name: ocaml-lambda-term
Version: 3.1.0
Release: alt1
Summary: Terminal manipulation library for OCaml

Group: Development/ML
License: MIT
Url: https://github.com/ocaml-community/lambda-term
Source: %name-%version.tar

BuildRequires: dune ocaml-cppo ocaml-mew-devel ocaml-mew_vi-devel
BuildRequires: ocaml-lwt_log-devel ocaml-zed-devel ocaml-result-devel
BuildRequires: ocaml-trie-devel ocaml-lwt-devel ocaml-charInfo_width-devel
BuildRequires: ocaml-camomile-devel
BuildRequires: libev-devel
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
Lambda-Term is a cross-platform library for manipulating the terminal. It
provides an abstraction for keys, mouse events, colors, as well as a set of
widgets to write curses-like applications.

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
%doc %_datadir/lambda-term-inputrc
%doc %_datadir/lambda-termrc
%_man1dir/lambda-term-actions.1.*
%_man5dir/lambda-term-inputrc.5.*
%_bindir/lambda-term-actions
%dir %_libdir/ocaml/lambda-term
%_libdir/ocaml/lambda-term*/META
%_libdir/ocaml/lambda-term*/*.cma
%_libdir/ocaml/lambda-term*/*.cmi
%_libdir/ocaml/lambda-term*/*.cmxs
%_libdir/ocaml/stublibs/*.so

%files devel
%_libdir/ocaml/lambda-term*/dune-package
%_libdir/ocaml/lambda-term*/opam
%_libdir/ocaml/lambda-term*/*.a
%_libdir/ocaml/lambda-term*/*.cmt*
%_libdir/ocaml/lambda-term*/*.cmxa
%_libdir/ocaml/lambda-term*/*.cmx
%_libdir/ocaml/lambda-term*/*.mli
%_libdir/ocaml/lambda-term*/*.ml

%changelog
* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus
