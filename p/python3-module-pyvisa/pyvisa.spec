Name: python3-module-pyvisa
Version: 1.16.2
Release: alt1

Summary: Python VISA bindings for GPIB, RS232, TCPIP and USB instruments
License: MIT
Group: Development/Python
URL: https://pypi.org/project/PyVISA/
VCS: https://github.com/pyvisa/pyvisa

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
%_bindir/pyvisa-*
%python3_sitelibdir/pyvisa
%python3_sitelibdir/pyvisa-%version.dist-info

%changelog
* Sat Nov 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.16.2-alt1
- 1.16.2

