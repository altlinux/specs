%set_verify_elf_method textrel=relaxed
Name: ocaml-cmdliner
Version: 1.2.0
Release: alt2
Summary: Declarative definition of command line interfaces for OCaml
License: ISC
Url: https://github.com/dbuenzli/cmdliner/
Source0: %name-%version.tar
Group: Development/ML

BuildRequires: ocaml
BuildRequires: dune
BuildRequires: ocaml-result-devel

%description
Cmdliner allows the declarative definition of command line
interfaces for OCaml.

It provides a simple and compositional mechanism to convert
command line arguments to OCaml values and pass them to your
functions. The module automatically handles syntax errors,
help messages and UNIX man page generation. It supports
programs with single or multiple commands and respects
most of the POSIX and GNU conventions.

Cmdliner has no dependencies and is distributed under
the ISC license.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build --release @install

%install
%dune_install

%files -f ocaml-files.runtime
%doc README.md CHANGES.md

%files devel -f ocaml-files.devel

%changelog
* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 1.2.0-alt2
- cleanup buildrequires
- build without docs to avoid cycles in rebuild order

* Wed Aug 23 2023 Ildar Mulyukov <ildar@altlinux.ru> 1.2.0-alt1
- new version

* Thu Mar 24 2022 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt5
- fixed the version repesentation for ocaml findlib

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt4
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt3
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt2
- rebuilt for ocaml 4.06.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- first build for ALT, based on RH spec

