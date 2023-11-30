%define  modulename ppx_here

Name:    ocaml-%modulename
Version: 0.16.0
Release: alt1
Summary: Expands [%%here_str] into its location
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_here
Source:  %modulename-%version.tar
BuildRequires: ocaml >= 4.10
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-base-devel
BuildRequires: dune

%description
A ppx rewriter that defines an extension node whose value is its source
position.

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
%dune_build -p ppx_here

%install
%dune_install

%files -f ocaml-files.runtime
%doc LICENSE.md

%files devel -f ocaml-files.devel
%doc README.md CHANGES.md

%changelog
* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Wed Sep 09 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- migrated to rpm-build-ocaml 1.4

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
