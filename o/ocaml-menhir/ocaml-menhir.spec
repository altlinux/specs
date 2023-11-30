Name: ocaml-menhir
Version: 20230608
Release: alt1
Summary: LR(1) parser generator for the OCaml programming language.

Group: Development/ML
License: QPL
Url: http://gallium.inria.fr/~fpottier/menhir/
Source: menhir-%version.tar

BuildRequires(pre): ocaml
Provides: ocaml4-menhir = %EVR
Obsoletes: ocaml4-menhir

BuildRequires: dune 

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
%dune_build --release @install

%install
%dune_install

%files
%doc LICENSE
%_bindir/*
%_man1dir/*
%dir %_libdir/ocaml/menhirLib
%dir %_libdir/ocaml/menhirSdk
%_libdir/ocaml/menhir
%_libdir/ocaml/coq-menhirlib
%_libdir/ocaml/menhirSdk/*
%_libdir/ocaml/menhirLib/*
%_libdir/ocaml/menhirSdk/*

%changelog
* Fri Nov 10 2023 Anton Farygin <rider@altlinux.ru> 20230608-alt1
- 20211230 -> 20230608

* Wed Jan 05 2022 Anton Farygin <rider@altlinux.ru> 20211230-alt1
- 20211012 -> 20211230

* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 20211012-alt1
- 20210419 -> 20211012

* Mon Aug 09 2021 Anton Farygin <rider@altlinux.ru> 20210419-alt2
- cleanup build requires

* Wed Jul 28 2021 Anton Farygin <rider@altlinux.ru> 20210419-alt1
- 20210419

* Thu Mar 11 2021 Anton Farygin <rider@altlinux.org> 20210310-alt1
- 20210310

* Sat Jun 27 2020 Anton Farygin <rider@altlinux.ru> 20200624-alt1
- 20200624

* Mon Mar 23 2020 Anton Farygin <rider@altlinux.ru> 20200211-alt1
- 20200211

* Fri Jan 31 2020 Anton Farygin <rider@altlinux.ru> 20200123-alt1
- 20200123

* Thu Oct 03 2019 Anton Farygin <rider@altlinux.ru> 20190924-alt1
- 20190924 with builtin standart menhir library

* Wed Jul 24 2019 Anton Farygin <rider@altlinux.ru> 20190620-alt2
- removed camlp4 build requires

* Mon Jun 24 2019 Anton Farygin <rider@altlinux.ru> 20190620-alt1
- 20190620

* Mon Nov 19 2018 Anton Farygin <rider@altlinux.ru> 20181113-alt1
- 20181113

* Thu Nov 01 2018 Anton Farygin <rider@altlinux.ru> 20181026-alt1
- 20181026

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 20181005-alt2
- rebuilt for ocaml-4.07.1

* Tue Oct 09 2018 Anton Farygin <rider@altlinux.ru> 20181005-alt1
- 20181005

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 20180530-alt2
- rebuilt with ocaml-4.07

* Thu May 31 2018 Anton Farygin <rider@altlinux.ru> 20180530-alt1
- 20180530 (closes: #34902)

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 20171222-alt1
- 20171222

* Tue Dec 19 2017 Anton Farygin <rider@altlinux.ru> 20170607-alt2
- rebuilt for ocaml 4.06

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 20170607-alt1
- updated to 20170607

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 20170101-alt2
- rebuild with ocaml 4.04.1

* Thu Mar 30 2017 Anton Farygin <rider@altlinux.ru> 20170101-alt1
- renamed to ocaml-menhir
- new version

* Mon Jun 27 2016 Andrey Bergman <vkni@altlinux.org> 20160518-alt1
- Initial release for Sisyphus.
