Name: python3-module-aiousbwatcher
Version: 1.1.2
Release: alt1

Summary: Asyncio usb device watcher
License: MIT
Group: Development/Python
URL: https://pypi.org/project/aiousbwatcher
VCS: https://github.com/bluetooth-devices/aiousbwatcher

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
%pyproject_run_pytest -o=addopts= tests

%files
%python3_sitelibdir/aiousbwatcher
%python3_sitelibdir/aiousbwatcher-%version.dist-info

%changelog
* Tue Apr 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.2-alt1
- 1.1.2 released

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.1-alt1
- 1.1.1 released
