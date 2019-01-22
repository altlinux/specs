%set_verify_elf_method textrel=relaxed
Name: ocaml-odoc
Version: 1.3.0
Release: alt2.git05241eb
Summary: Documentation compiler for OCaml and Reason
Group: Development/ML
License: ISC
Url: https://github.com/ocaml/odoc
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml >= 4.07.1
BuildRequires: ocaml-findlib-devel
BuildRequires: opam dune
BuildRequires: ocaml-cmdliner-devel ocaml-bos-devel
BuildRequires: ocaml-cppo
BuildRequires: ocaml-fmt-devel
BuildRequires: ocaml-tyxml-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-rresult-devel
BuildRequires: ocaml-astring-devel
BuildRequires: ocaml-fpath-devel
BuildRequires: ocaml-bisect_ppx-devel
BuildRequires: ocaml-migrate-parsetree-devel

%description
odoc is a documentation generator for OCaml. It reads doc comments ,
delimited with (** ... *), and outputs HTML.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml --mandir=%buildroot/%_mandir --docdir=%buildroot/%_docdir
mv %buildroot/%_docdir/odoc %buildroot/%_docdir/%name-%version

%files
%_docdir/*
%_bindir/odoc
%_datadir/odoc
%_libdir/ocaml/odoc

%changelog
* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 1.3.0-alt2.git05241eb
- updated to upstream unstable git 05241eb with fixes for ocaml-tyxml-4.3.0

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- first build for ALT

