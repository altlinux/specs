%set_verify_elf_method textrel=relaxed
Name: ocaml-mew_vi
Version: 0.5.0
Release: alt2
Summary: Modal editing witch, VI interpreter

Group: Development/ML
License: MIT
Url: https://github.com/kandu/mew_vi
Source: %name-%version.tar

BuildRequires: dune ocaml-react ocaml-mew-devel
BuildPreReq: rpm-build-ocaml >= 1.1

%description
This is a vi-like modal editing engine generator.

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
%dune_build

%install
%dune_install

%files -f ocaml-files.runtime
%doc CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.5.0-alt2
- fixed BuildRequires
- simplified spec

* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
