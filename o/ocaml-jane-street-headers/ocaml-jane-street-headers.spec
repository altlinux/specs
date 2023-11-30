%define  modulename jane-street-headers

Name:    ocaml-%modulename
Version: 0.16.0
Release: alt1
Summary: Jane Street header files
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/jane-street-headers
BuildRequires: dune ocaml
BuildRequires: rpm-build-ocaml >= 1.4
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
%doc README.org

%files devel -f ocaml-files.devel
%_ocamldir/%modulename/*.h

%changelog
* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Wed Jan 05 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Thu Oct 15 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- migrated to rpm-build-ocaml 1.4

* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
