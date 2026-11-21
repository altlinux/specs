Name: python3-module-pyvisa-py
Version: 0.8.1
Release: alt1

Summary: Pure Python implementation of a VISA library.
License: MIT
Group: Development/Python
URL: https://pypi.org/project/PyVISA-py/
VCS: https://github.com/pyvisa/pyvisa-py

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/pyvisa_py
%python3_sitelibdir/pyvisa_py-%version.dist-info

%changelog
* Sat Nov 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.8.1-alt1
- 0.8.1

