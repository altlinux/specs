%define oname cached-property
%define modname cached_property

Name: python3-module-%oname
Version: 1.5.2
Release: alt1

Summary: A decorator for caching properties in classes.

License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/pydanny/cached-property

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description
A decorator for caching properties in classes.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE AUTHORS.rst README.rst HISTORY.rst CONTRIBUTING.rst
%python3_sitelibdir/%modname.*
%python3_sitelibdir/*.egg-*
%python3_sitelibdir/__pycache__/*

%changelog
* Sun Sep 27 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.2-alt1
- Automatically updated to 1.5.2.
- Drop python2 support.

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt2
- NMU: Fix license.

* Tue Dec 4 2018 Vladimir Didenko <cow@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 1.3.0-alt1
- 1.3.0
