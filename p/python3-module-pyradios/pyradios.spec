Name: python3-module-pyradios
Version: 2.1.1
Release: alt1

Summary: Python client for the Radio Browser API
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pyradios
VCS: https://github.com/andreztz/pyradios

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_check_filter pytest-recording
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt

%build
%pyproject_build

%install
%pyproject_install

%check
# some tests are online
%pyproject_run_pytest -o addopts= tests ||:

%files
%python3_sitelibdir/pyradios
%python3_sitelibdir/pyradios-%version.dist-info

%changelog
* Wed Oct 22 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.1-alt1
- 2.1.1 released

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Mon Feb 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt1
- 1.0.2 released
