Name: python3-module-stringcase
Version: 1.2.1
Release: alt2

Summary: Convert string cases between camel case, pascal case, snake case etc
License: MIT
Group: Development/Python
Url: https://pypi.org/project/stringcase
VCS: https://github.com/okunishinishi/python-stringcase

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
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest stringcase_test.py

%files
%python3_sitelibdir/stringcase.*
%python3_sitelibdir/*/stringcase.*
%python3_sitelibdir/stringcase-%version.dist-info

%changelog
* Tue Dec 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.1-alt2
- moved to pyproject

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- initial
