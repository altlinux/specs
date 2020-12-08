%set_verify_elf_method textrel=relaxed
%define oname ppxfind
Name: ocaml-%oname
Version: 1.4
Release: alt2
Summary: Ocamlfind ppx tool
License: MIT
Group: Development/ML
Url: https://github.com/alainfrisch/ppx_tools
Source0: %name-%version.tar
BuildRequires: ocaml-findlib dune ocaml-migrate-parsetree-devel opam
Provides: ppxfind

%description
Ppxfind is a small command line tool that allow to apply ppx rewriters
installed on the system on a file. It supports both new style ppx
rewriters (driverised) and old styles ones.

At the moment new styles ppx rewriters are executed in byte-code mode
as Ppxfind relies on dynamic loading and the packaging of a lot of ppx
rewriters is incomplete, i.e. the cmxs files are missing


%prep
%setup

%build
%dune_build -p %oname

%install
%dune_install

%files
%doc README.md
%_bindir/ppxfind

%changelog
* Sat Dec 12 2020 Anton Farygin <rider@altlinux.ru> 1.4-alt2
- used macros from rpm-build-ocaml 1.4

* Sat Apr 25 2020 Anton Farygin <rider@altlinux.ru> 1.4-alt1
- 1.4

* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 1.3-alt2
- fix for build by dune-2.x

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- first build for ALT

