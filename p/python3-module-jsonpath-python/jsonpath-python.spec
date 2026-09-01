Name: python3-module-jsonpath-python
Version: 1.1.6
Release: alt1

Summary: JSONPath for Python
License: MIT
Group: Development/Python
URL: https://pypi.org/project/jsonpath-python
VCS: https://github.com/sean2077/jsonpath-python

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/jsonpath
%python3_sitelibdir/jsonpath_python-%version.dist-info

%changelog
* Fri Jul 31 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.6-alt1
- 1.1.6 released
