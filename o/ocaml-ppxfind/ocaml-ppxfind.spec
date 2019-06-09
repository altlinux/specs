%set_verify_elf_method textrel=relaxed
%define oname ppxfind
Name: ocaml-%oname
Version: 1.3
Release: alt1
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
make all

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %oname.install

%files
%doc README.md
%_bindir/ppxfind

%changelog
* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- first build for ALT

