Name: python3-module-cached-ipaddress
Version: 0.5.0
Release: alt1

Summary: Cache construction of ipaddress objects
License: MIT
Group: Development/Python
Url: https://pypi.org/project/cached-ipaddress/

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-pyproject
BuildRequires: python3(poetry-core)
BuildRequires: python3(setuptools)
BuildRequires: python3(cython)
BuildRequires: python3(pytest-cov)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/cached_ipaddress
%python3_sitelibdir/cached_ipaddress-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.0-alt1
- 0.5.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released
