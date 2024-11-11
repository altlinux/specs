Name: python3-module-cached-ipaddress
Version: 0.8.0
Release: alt2

Summary: Cache construction of ipaddress objects
License: MIT
Group: Development/Python
Url: https://pypi.org/project/cached-ipaddress/

Source0: %name-%version-%release.tar

Requires: python3(propcache)

BuildRequires: rpm-build-pyproject
BuildRequires: python3(poetry-core)
BuildRequires: python3(setuptools)
BuildRequires: python3(cython)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(propcache)

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
* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.8.0-alt2
- added propcache as runtime dep

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.8.0-alt1
- 0.8.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.0-alt1
- 0.5.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released
