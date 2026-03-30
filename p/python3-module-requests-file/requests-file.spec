%def_with check

Name: python3-module-requests-file
Version: 3.0.1
Release: alt1.1

Summary: Local filesystem access for Requests module
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/requests-file
VCS: https://codeberg.org/dashea/requests-file

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-requests
%endif

%description
%summary

%prep
%setup
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/requests_file
%python3_sitelibdir/requests_file-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1.1
- Demodernized packaging.

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.1-alt1
- 3.0.1 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- initial
