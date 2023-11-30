%define  modulename ppx_custom_printf

Name:    ocaml-%modulename
Version: 0.16.0
Release: alt1

Summary: Printf-style format-strings for user-defined string conversion
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_custom_printf
BuildRequires: dune
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires(pre): rpm-build-ocaml >= 1.6
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
%dune_install %modulename

%check
%dune_check -p %modulename

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.1-alt1
- 0.14.1

* Tue Dec 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- specfile migrated to rpm-build-ocaml 1.4

* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
