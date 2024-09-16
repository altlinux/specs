%define  modulename ppx_optcomp
Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1

Summary: Optional compilation for OCaml
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_optcomp
BuildRequires: dune
BuildRequires: ocaml-base-devel ocaml-stdio-devel ocaml-ppxlib-devel
Source:  %modulename-%version.tar
Patch0: %name-%version-%release.patch

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
%patch0 -p1

%build
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 10 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Wed Nov 03 2021 Anton Farygin <rider@altlinux.ru> 0.14.3-alt1
- 0.14.3

* Mon Aug 16 2021 Anton Farygin <rider@altlinux.ru> 0.14.2-alt1
- 0.14.2

* Sun Mar 28 2021 Anton Farygin <rider@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.0-alt3
- simplified specfile with macros from rpm-build-ocaml 1.4
- added upstream fix against ppxlib 0.22

* Wed Sep 09 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- added ocaml-stdio-devel to BuildRequires

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
