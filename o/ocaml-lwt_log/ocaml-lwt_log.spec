Name: ocaml-lwt_log
Version: 1.1.2
Release: alt2
Summary: Lwt-friendly logger

Group: Development/ML
License: LGPL-2.1
Url: https://github.com/ocsigen/lwt_log
Source: %name-%version.tar
BuildRequires: dune ocaml-lwt
BuildPreReq: rpm-build-ocaml >= 1.6

%description
%summary.

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
%doc CHANGES README.md

%files devel -f ocaml-files.devel

%changelog
* Fri Nov 17 2023 Anton Farygin <rider@altlinux.ru> 1.1.2-alt2
- specfile cleanup

* Fri Nov 03 2023 Anton Farygin <rider@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sun Jun 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
