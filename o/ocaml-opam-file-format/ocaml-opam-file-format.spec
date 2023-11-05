Name: ocaml-opam-file-format
Version: 2.1.6
Release: alt1
Summary: Parser and printer for the opam file syntax
Group: Development/ML
%global libname %(echo %name | sed -e 's/^ocaml-//')
License: LGPLv2 with OCaml-LGPL-linking-exception
Url: https://github.com/ocaml/opam-file-format/
Source0: %name-%version.tar
BuildRequires: ocaml dune

%description
Parser and printer for the opam file syntax.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature
files for developing applications that use %name.

%prep
%setup

%build
%dune_build -p %libname

%install
%dune_install

%files -f ocaml-files.runtime
%doc LICENSE

%files devel -f ocaml-files.devel
%doc LICENSE

%changelog
* Sat Nov 04 2023 Anton Farygin <rider@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Tue Aug 03 2021 Anton Farygin <rider@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Tue Mar 23 2021 Anton Farygin <rider@altlinux.org> 2.1.2-alt1
- 2.1.2

* Mon Oct 12 2020 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.1.0
- switch to dune build system

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 2.0.0-alt4
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt3
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt2
- up to 2.0.0 release

* Wed May 23 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1.rc2
- first build for ALT, based on RH spec

