Name: python3-module-smbus2
Version: 0.6.1
Release: alt1

Summary: Python implementation of of the python-smbus package
License: MIT
Group: Development/Python
Url: https://pypi.org/project/smbus2
VCS: https://github.com/kplindegaard/smbus2

Source: %name-%version.tar
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
smbus2 is drop-in replacement of lm-sensors smbus package

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
%python3_sitelibdir/smbus2
%python3_sitelibdir/smbus2-%version.dist-info

%changelog
* Mon Apr 13 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6.1-alt1
- 0.6.1 released

* Thu Dec 25 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6.0-alt1
- 0.6.0 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.0-alt1
- 0.5.0 released

* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt1
- 0.4.2 released
