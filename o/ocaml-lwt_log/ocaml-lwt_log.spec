Name: ocaml-lwt_log
Version: 1.1.2
Release: alt4
Summary: Lwt-friendly logger

Group: Development/ML
License: LGPL-2.1
Url: https://github.com/ocsigen/lwt_log
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune ocaml-lwt-devel
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
%patch0 -p1

%build
%dune_build

%install
%dune_install

%files -f ocaml-files.runtime
%doc CHANGES README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Mar 10 2026 Anton Farygin <rider@altlinux.org> 1.1.2-alt4
- fixed build with lwt > 5.7.0: removed reference to Lwt_main.exit_hooks
  which was dropped in newer versions of Lwt

* Wed Jan 22 2025 Anton Farygin <rider@altlinux.ru> 1.1.2-alt3
- changed BR - use ocaml-lwt-devel instead of the ocaml-lwt

* Fri Nov 17 2023 Anton Farygin <rider@altlinux.ru> 1.1.2-alt2
- specfile cleanup

* Fri Nov 03 2023 Anton Farygin <rider@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sun Jun 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
