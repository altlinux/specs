Name: python3-module-esp-pylib
Version: 1.1.4
Release: alt1

Summary: Espressif Systems pythol library
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/esp-pylib
VCS: https://github.com/espressif/esp-pylib

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra serial
%pyproject_builddeps_metadata_extra cli

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
%pyproject_run_pytest tests

%files
%python3_sitelibdir/esp_pylib
%python3_sitelibdir/esp_pylib-%version.dist-info

%changelog
* Fri Sep 04 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.4-alt1
- 1.1.4 released

