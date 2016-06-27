Name: ocaml4-menhir
Version: 20160518
Release: alt1
Summary: LR(1) parser generator for the OCaml programming language.

Group: Development/ML
License: QPL
Url: http://gallium.inria.fr/~fpottier/menhir/
Packager: %packager

Source: menhir-%version.tar.gz

BuildRequires(pre): ocaml4

# Automatically added by buildreq on Mon Jun 27 2016
# optimized out: ocaml4 ocaml4-runtime python-base python-modules python3
BuildRequires: ocaml4-camlp4 ocaml4-findlib ocaml4-ocamlbuild python-module-google python3-base

%description
Menhir is a LR(1) parser generator for the OCaml programming language.
That is, Menhir compiles LR(1) grammar specifications down to OCaml
code. Menhir is 90 percent compatible with ocamlyacc. Legacy ocamlyacc
grammar specifications are accepted and compiled by Menhir. The
resulting parsers run and produce correct parse trees. However, parsers
that explicitly invoke functions in module Parsing behave slightly
incorrectly. For instance, the functions that provide access
to positions return a dummy position when invoked by a Menhir parser.
Porting a grammar specification from ocamlyacc to Menhir requires
replacing all calls to module Parsing with new Menhir-specific keywords.

%prep
%setup -q -n menhir-%version

%build
make PREFIX=%buildroot/usr all

%install
%define ocamlsitelib %_libdir/ocaml/site-lib
mkdir -p %buildroot%ocamlsitelib/menhirLib
make OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml PREFIX=%buildroot/usr install

mv %buildroot%_libdir/ocaml/menhirLib/META %buildroot%ocamlsitelib/menhirLib
mkdir -p %buildroot%_datadir/doc/%name-%version
mv %buildroot%_datadir/doc/menhir/* %buildroot%_datadir/doc/%name-%version/
rm -rf %buildroot%_datadir/doc/menhir
rm -rf %buildroot%_datadir/doc/%name-%version/src/

bzip2 -z9 %buildroot%_man1dir/menhir.1

%files
%_bindir/*
%_man1dir/*
%dir %_datadir/menhir
%_datadir/menhir/*

%doc AUTHORS
%doc CHANGES
%doc demos
%doc INSTALLATION
%doc LICENSE
%doc Makefile
%doc manual.pdf

%dir %ocamlsitelib/menhirLib
%ocamlsitelib/menhirLib/META
%dir %_libdir/ocaml/menhirLib
%_libdir/ocaml/menhirLib/*

%changelog
* Mon Jun 27 2016 Andrey Bergman <vkni@altlinux.org> 20160518-alt1
- Initial release for Sisyphus.

