Name: ocaml-menhir
Version: 20180530
Release: alt1%ubt
Summary: LR(1) parser generator for the OCaml programming language.

Group: Development/ML
License: QPL
Url: http://gallium.inria.fr/~fpottier/menhir/
Source: menhir-%version.tar

BuildRequires(pre): ocaml rpm-build-ubt
Provides: ocaml4-menhir
Obsoletes: ocaml4-menhir

# Automatically added by buildreq on Mon Jun 27 2016
# optimized out: ocaml4 ocaml4-runtime python-base python-modules python3
BuildRequires: ocaml-camlp4 ocaml-findlib ocaml-ocamlbuild python-module-google python3-base

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
make PREFIX=/usr all

%install
#mkdir -p %buildroot%ocamlsitelib/menhirLib
#mkdir -p %buildroot%ocamlsitelib/menhirSdk
mkdir -p %buildroot%_libdir/ocaml
make OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml PREFIX=%buildroot/usr install

mkdir -p %buildroot%_datadir/doc/%name-%version
mv %buildroot%_datadir/doc/menhir/* %buildroot%_datadir/doc/%name-%version/
rm -rf %buildroot%_datadir/doc/menhir
rm -rf %buildroot%_datadir/doc/%name-%version/src/

bzip2 -z9 %buildroot%_man1dir/menhir.1

%files
%doc CHANGES.md
%doc demos
%doc INSTALLATION.md
%doc README.md
%doc LICENSE
%doc Makefile
%doc manual.pdf
%_bindir/*
%_man1dir/*
%dir %_datadir/menhir
%_datadir/menhir/*
%dir %_libdir/ocaml/menhirLib
%dir %_libdir/ocaml/menhirSdk
%_libdir/ocaml/menhirLib/*
%_libdir/ocaml/menhirSdk/*

%changelog
* Thu May 31 2018 Anton Farygin <rider@altlinux.ru> 20180530-alt1%ubt
- 20180530 (closes: #34902)

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 20171222-alt1%ubt
- 20171222

* Tue Dec 19 2017 Anton Farygin <rider@altlinux.ru> 20170607-alt2%ubt
- rebuilt for ocaml 4.06

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 20170607-alt1%ubt
- updated to 20170607

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 20170101-alt2%ubt
- rebuild with ocaml 4.04.1

* Thu Mar 30 2017 Anton Farygin <rider@altlinux.ru> 20170101-alt1%ubt
- renamed to ocaml-menhir
- new version

* Mon Jun 27 2016 Andrey Bergman <vkni@altlinux.org> 20160518-alt1
- Initial release for Sisyphus.
