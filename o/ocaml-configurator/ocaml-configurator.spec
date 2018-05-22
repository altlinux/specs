%set_verify_elf_method textrel=relaxed
%define oname configurator
Name: ocaml-%oname
Version: 0.11.0
Release: alt1%ubt
Summary: Helper library for gathering system configuration
Group: Development/ML
License: ASL 2.0
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: jbuilder
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: opam
BuildRequires: ocaml-base >= 0.11
BuildRequires: ocaml-stdio >= 0.11
BuildRequires(pre): rpm-build-ubt

%description
Helper library for gathering system configuration

Configurator is a small library that helps writing OCaml scripts that
test features available on the system, in order to generate config.h
files for instance.

Configurator allows one to:
- test if a C program compiles
- query pkg-config
- import #define from OCaml header files
- generate config.h file

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
jbuilder build --verbose -p %oname %_smp_mflags

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %oname.install
rm -rf %buildroot/usr/doc

%check
jbuilder runtest

%files
%doc LICENSE.txt
%doc README.org
%dir %_libdir/ocaml/%oname
%_libdir/ocaml/%oname/META
%_libdir/ocaml/%oname/*.cmi
%_libdir/ocaml/%oname/*.cma
%_libdir/ocaml/%oname/*.a
%_libdir/ocaml/%oname/*.cmxa
%_libdir/ocaml/%oname/*.cmxs

%files devel
%_libdir/ocaml/%oname/opam
%_libdir/ocaml/%oname/*.cmt
%_libdir/ocaml/%oname/*.cmti
%_libdir/ocaml/%oname/*.cmx
%_libdir/ocaml/%oname/*.ml*

%changelog
* Thu May 17 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1%ubt
- first build for ALT, based on Mageia spec

