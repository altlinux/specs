Name: python3-module-zeep
Version: 4.3.3
Release: alt1

Summary: A fast and modern Python SOAP client
License: MIT
Group: Development/Python
URL: https://pypi.org/project/python-zeep
VCS: https://github.com/mvantellingen/python-zeep

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
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
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/zeep
%python3_sitelibdir/zeep-%version.dist-info

%changelog
* Wed Jun 24 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.3.3-alt1
- 4.3.3 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.3.2-alt1
- 4.3.2 released

* Fri Dec 13 2024 Grigory Ustinov <grenka@altlinux.org> 4.3.1-alt1
- 4.3.1 released (nessesary update for python3.13)

* Wed Jan 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.1-alt1
- 4.2.1 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.0-alt1
- 4.1.0 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.0-alt1
- initial
