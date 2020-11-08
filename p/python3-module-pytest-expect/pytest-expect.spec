%define oname pytest-expect

Name: python3-module-%oname
Version: 1.1.0
Release: alt1

Summary: A py.test plugin that stores test expectations by saving the set of failing tests
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-expect/
BuildArch: noarch

# https://github.com/gsnedders/pytest-expect.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-umsgpack

%py3_provides pytest_expect
%py3_requires pytest


%description
A py.test plugin that stores test expectations by saving the set of
failing tests, allowing them to be marked as xfail when running them in
future. The tests expectations are stored such that they can be
distributed alongside the tests. However, note that test expectations
can only be reliably shared between Python 2 and Python 3 if they only
use ASCII characters in their node ids: this likely isn't a limitation
if tests are using the normal Python format, as Python 2 only allows
ASCII characters in identifiers.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- NMU: new version 1.1.0 (with rpmrb script)

* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1.git20150720.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20150720.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150720
- Initial build for Sisyphus

