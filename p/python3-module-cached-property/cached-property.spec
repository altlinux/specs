%define oname cached-property
%define modname cached_property

%def_with check

Name: python3-module-%oname
Version: 2.0.1
Release: alt1

Summary: A decorator for caching properties in classes.

License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/cached-property
VCS: https://github.com/pydanny/cached-property

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-distribute

%if_with check
BuildRequires: python3-module-freezegun
%endif

%description
A decorator for caching properties in classes.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/%modname.*
%python3_sitelibdir/%modname-%version.dist-info
%python3_sitelibdir/__pycache__/*

%changelog
* Sat Oct 26 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Automatically updated to 2.0.1.
- Built with check.

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
