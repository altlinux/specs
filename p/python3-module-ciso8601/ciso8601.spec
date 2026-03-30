Name: python3-module-ciso8601
Version: 2.3.3
Release: alt2

Summary: ISO8601/RFC3339 date time strings converter
License: MIT
Group: Development/Python
Url: https://pypi.org/project/ciso8601
VCS: https://github.com/closeio/ciso8601

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_tox tox.ini testenv

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%python3_sitelibdir/ciso8601
%python3_sitelibdir/ciso8601.*.so
%python3_sitelibdir/ciso8601-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.3-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.3.3-alt1.1
- Demodernized packaging.

* Fri Sep 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.3-alt1
- 2.3.3 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.2-alt1
- 2.3.2 released

* Thu Jul 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt2
- drop deps on now retired nose

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- 2.3.0 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.3-alt1
- initial
