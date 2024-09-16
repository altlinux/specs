%define  modulename ppx_fields_conv

Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1

Summary: Generation of accessor and iteration functions for ocaml records
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_fields_conv

BuildRequires: dune 
BuildRequires: ocaml-fieldslib-devel
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-base-devel

Source:  %modulename-%version.tar

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -n %modulename-%version

%build
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 11 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Tue Nov 14 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Tue Dec 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.2-alt1
- 0.14.2
- migrated to rpm-build-ocaml 1.4

* Wed Sep 16 2020 Anton Farygin <rider@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- built as release (dune build -p) against incomplete dependencies
  in devel package

* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
