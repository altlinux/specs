Name: python3-module-py3rijndael
Version: 0.3.3
Release: alt1

Summary: Rijndael algorithm library for Python3
License: MIT
Group: Development/Python
URL: https://pypi.org/project/py3rijndael
VCS: https://github.com/meyt/py3rijndael

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch
Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

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
%python3_sitelibdir/py3rijndael
%python3_sitelibdir/py3rijndael-%version.dist-info

%changelog
* Thu Feb 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.3-alt1
- 0.3.3 released
