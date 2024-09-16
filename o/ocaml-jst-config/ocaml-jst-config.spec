%define  modulename jst-config
Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1
Summary: Compile-time configuration for Jane Street libraries
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/jst-config
BuildRequires: ocaml-dune-configurator-devel ocaml-ppx_assert-devel
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-stdio-devel ocaml-base-devel

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
%_libdir/ocaml/%{modulename}*/*.h

%changelog
* Tue Sep 10 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Wed Jan 05 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Wed Nov 03 2021 Anton Farygin <rider@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Thu Mar 18 2021 Anton Farygin <rider@altlinux.org> 0.14.0-alt4
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt3
- cleanup build dependencies

* Wed Sep 16 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- migrated to rpm-build-ocaml-1.4
- added ocaml-stdio-devel to BuildRequires

* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
