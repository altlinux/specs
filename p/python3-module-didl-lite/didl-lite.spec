Name: python3-module-didl-lite
Version: 1.5.0
Release: alt1

Summary: DIDL-Lite (Digital Item Declaration Language) tools for Python
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/python-didl-lite
VCS: https://github.com/StevenLooman/python-didl-lite

Provides: python3-module-python-didl-lite = %EVR

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch
Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject >= 0.2.0
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
%pyproject_run_pytest -o addopts=

%files
%python3_sitelibdir/didl_lite
%python3_sitelibdir/python_didl_lite-%version.dist-info

%changelog
* Tue Feb 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.0-alt1
- 1.5.0 released

* Wed Jul 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.1-alt2
- provide pep503 name

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.1-alt1
- 1.4.1 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.2-alt1
- 1.3.2 released

* Tue Oct 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Thu Apr 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.6-alt1
- 1.2.6 released

* Tue Jan 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.4-alt1
- initial
