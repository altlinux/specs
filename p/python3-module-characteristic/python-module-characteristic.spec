%define oname characteristic

Name: python3-module-%oname
Version: 14.3.0
Release: alt2

Summary: Python library that eases the chores of implementing attributes

License: MIT
Group: Development/Python3
Url: https://github.com/hynek/characteristic

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/c/characteristic/characteristic-0.1.0.tar.gz
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-python3

%description
characteristic is an MIT-licensed Python package with class decorators that ease the chores of
implementing the most common attribute-related object protocols.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS.rst CONTRIBUTING.rst README.rst
%python3_sitelibdir/%oname.py
%python3_sitelibdir/test_%oname.py
%python3_sitelibdir/*.egg-*
%exclude %python3_sitelibdir/__pycache__/

%changelog
* Wed Jul 14 2021 Grigory Ustinov <grenka@altlinux.org> 14.3.0-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 14.3.0-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 14.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 14.3.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Jun 29 2015 Vladimir Didenko <cow@altlinux.ru> 14.3.0-alt1
- new version

* Thu Jul 31 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.0-alt1
- initial build for Sisyphus
