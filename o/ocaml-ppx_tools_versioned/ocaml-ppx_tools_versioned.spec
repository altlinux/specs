%set_verify_elf_method textrel=relaxed

%define oname ppx_tools_versioned
Name: ocaml-%oname
Version: 5.4.0
Release: alt2
Summary: Tools for authors of ppx rewriters and other syntactic tools
License: MIT
Group: Development/ML
Url: https://opam.ocaml.org/packages/ppx_tools_versioned/
# https://github.com/let-def/ppx_tools_versioned
Source0: %name-%version.tar
BuildRequires: ocaml-findlib ocaml-migrate-parsetree-devel ocaml-result-devel dune

%description
Tools for authors of syntactic tools (such as ppx rewriters).

This package is licensed by LexiFi under the terms of the MIT license.

The tools are installed as a findlib package called 'ppx_tools'.
Executables are thus accessible through the ocamlfind driver
(e.g.: ocamlfind ppx_tools/dumpast).

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
%dune_build -p %oname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Dec 10 2020 Anton Farygin <rider@altlinux.ru> 5.4.0-alt2
- specfile migrated to rpm-build-ocaml 1.4

* Sat Jun 27 2020 Anton Farygin <rider@altlinux.ru> 5.4.0-alt1
- 5.4.0

* Tue Apr 14 2020 Anton Farygin <rider@altlinux.ru> 5.3.0-alt1
- 5.3.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 5.2.3-alt2
- built by dune

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 5.2.3-alt1
- 5.2.3

* Thu Jun 06 2019 Anton Farygin <rider@altlinux.ru> 5.2.2-alt1
- 5.2.2

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 5.2.1-alt3
- rebuild with ocaml-migrate-parsetree 1.2.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 5.2.1-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 5.2.1-alt1
- 5.2.1

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 5.1-alt1
- first build for ALT, based on specfile from Mageia

