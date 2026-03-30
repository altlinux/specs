Name: python3-module-aiohasupervisor
Version: 0.4.3
Release: alt1

Summary: Client Library for Home Assistant Supervisor
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/aiohasupervisor
VCS: https://github.com/home-assistant-libs/python-supervisor-client

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_check_filter codespell
%pyproject_builddeps_build
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check

%description
%summary

%prep
%setup
sed -ri '/^version\s+=/ s,"[^"]+","%version",' pyproject.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o=addopts= tests

%files
%python3_sitelibdir/aiohasupervisor
%python3_sitelibdir/aiohasupervisor-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.3-alt1
- 0.4.3 released

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.3.3-alt1.1
- Demodernized packaging.

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.3-alt1
- 0.3.3 released

* Wed Jan 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.2-alt1
- 0.2.2 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released
