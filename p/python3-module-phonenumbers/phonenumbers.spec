%define oname phonenumbers

Name: python3-module-%oname
Version: 8.12.47
Release: alt1

Summary: Python port of Google's libphonenumber

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/phonenumbers/

# Source-git: https://github.com/daviddrysdale/python-phonenumbers.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
Python version of Google's common library for parsing, formatting,
storing and validating international phone numbers.

%prep
%setup

%build
pushd python
%python3_build
popd

%install
pushd python
%python3_install
popd

%check
pushd python
%__python3 setup.py test
popd

%files
%doc *.md python/HISTORY.md
%python3_sitelibdir/*

%changelog
* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.47-alt1
- Automatically updated to 8.12.47.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 8.5.1-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 8.5.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 8.5.1-alt1
- new version 8.5.1 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 7.0.1-alt1.git20141126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.1-alt1.git20141126
- Version 7.0.1

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.0-alt1.git20141102
- Version 7.0.0

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt1.git20141026
- Initial build for Sisyphus

