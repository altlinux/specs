%set_verify_elf_method textrel=relaxed
Name: ocaml-xml-light
Version: 2.5
Release: alt1
Summary: Minimal XML parser and printer for OCaml

Group: Development/ML
License: LGPLv2+
Url: https://opam.ocaml.org/packages/xml-light/
Source0: %name-%version.tar

BuildRequires: ocaml-odoc ocaml-findlib dune rpm-build-ocaml

%description
Xml-Light is a minimal XML parser & printer for OCaml. It provides
functions to parse an XML document into an OCaml data structure, work
with it, and print it back to an XML document. It support also DTD
parsing and checking, and is entirely written in OCaml, hence it does
not require additional C library.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build --release @install @doc

%install
%dune_install

%files -f ocaml-files.runtime
%doc CHANGES* README*

%files devel -f ocaml-files.devel
%doc _build/default/_doc/*

%changelog
* Sat Jun 03 2023 Ildar Mulyukov <ildar@altlinux.ru> 2.5-alt1
- new version

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 2.4-alt7
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.4-alt6
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 2.4-alt5
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 2.4-alt4
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 2.4-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 2.4-alt2
- rebuild with ocaml 4.04.1

* Wed Apr 12 2017 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- new version
- build for ocaml-4.04

* Tue Dec 27 2011 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1.1
- rebuild with new ocaml

* Thu Nov 12 2009 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- first build for Sisyphus, based on Fedora specfile
