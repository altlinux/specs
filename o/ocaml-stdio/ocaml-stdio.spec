%define oname stdio
Name: ocaml-%oname
Version: 0.17.0
Release: alt1
Summary: Standard IO library for OCaml
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: dune
BuildRequires: ocaml-base  >= 0.17.1

%description
Stdio implements simple input/output functionalities for OCaml.

It re-exports the input/output functions of the OCaml standard
libraries using a more consistent API.

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
%doc README.md LICENSE.md

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 03 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- devel parts moved to the ocaml-stdio-devel package

* Tue Jun 16 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt4
- fixed install with dune 1.4.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt2
- rebuilt with ocaml 4.07

* Thu May 17 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT, based on Mageia spec

