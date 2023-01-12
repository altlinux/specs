%define oname phonenumbers

%def_with check

Name: python3-module-%oname
Version: 8.13.4
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
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Jan 12 2023 Grigory Ustinov <grenka@altlinux.org> 8.13.4-alt1
- Automatically updated to 8.13.4.

* Thu Dec 22 2022 Grigory Ustinov <grenka@altlinux.org> 8.13.3-alt1
- Automatically updated to 8.13.3.

* Thu Dec 08 2022 Grigory Ustinov <grenka@altlinux.org> 8.13.2-alt1
- Automatically updated to 8.13.2.

* Tue Nov 29 2022 Grigory Ustinov <grenka@altlinux.org> 8.13.1-alt1
- Automatically updated to 8.13.1.

* Mon Nov 07 2022 Grigory Ustinov <grenka@altlinux.org> 8.13.0-alt1
- Automatically updated to 8.13.0.

* Mon Oct 17 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.57-alt1
- Automatically updated to 8.12.57.

* Sat Sep 24 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.56-alt1
- Automatically updated to 8.12.56.

* Mon Sep 12 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.55-alt1
- Automatically updated to 8.12.55.

* Sun Aug 21 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.54-alt1
- Automatically updated to 8.12.54.

* Fri Aug 05 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.53-alt1
- Automatically updated to 8.12.53.

* Thu Jul 21 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.52-alt1
- Automatically updated to 8.12.52.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.51-alt1
- Automatically updated to 8.12.51.

* Mon Jun 13 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.50-alt1
- Automatically updated to 8.12.50.

* Sun May 29 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.49-alt1
- Automatically updated to 8.12.49.
- Build with check.

* Thu May 12 2022 Grigory Ustinov <grenka@altlinux.org> 8.12.48-alt1
- Automatically updated to 8.12.48.

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

