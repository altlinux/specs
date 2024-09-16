%define  modulename variantslib

Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1

Summary: OCaml variants as first class values
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/variantslib
VCS:     https://github.com/janestreet/variantslib

BuildRequires: dune
BuildRequires: ocaml-base-devel >= %version
Requires: rpm-build-ocaml >= 1.6.3

Source:  %modulename-%version.tar

%description
The Core suite of libraries is an industrial strength alternative to OCaml's
standard library that was developed by Jane Street, the
largest industrial user of OCaml.

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
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
