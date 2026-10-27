Name: python3-module-gpsoauth
Version: 2.0.0
Release: alt1

Summary: Python API for google play services oauth
License: MIT
Group: Development/Python
URL: https://pypi.org/project/gpsoauth/
VCS: https://github.com/simon-weber/gpsoauth

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
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/gpsoauth
%python3_sitelibdir/gpsoauth-%version.dist-info

%changelog
* Tue Oct 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.0-alt1
- 2.0.0 released

* Mon Jun 10 2024 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.0 -> 1.1.1.

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- NMU: Modernized packaging (fixes FTBFS due to poetry-core 1.1.0).

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- initial
