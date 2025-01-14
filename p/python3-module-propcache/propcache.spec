Name: python3-module-propcache
Version: 0.2.1
Release: alt1

Summary: Fast implementation of cached properties
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/propcache/

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(cython)
BuildRequires: python3(expandvars)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(pytest_codspeed)
BuildRequires: python3(xdist)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --no-cov tests

%files
%python3_sitelibdir/propcache
%python3_sitelibdir/propcache-%version.dist-info

%changelog
* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released
