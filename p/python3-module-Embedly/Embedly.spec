%define oname Embedly

%def_disable check

Name: python3-module-%oname
Version: 0.5.0
Release: alt2.git20141215
Summary: Python Library for Embedly
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Embedly/

# https://github.com/embedly/embedly-python.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides embedly
%py3_requires httplib2 json

BuildRequires: python3-module-httplib2 python3-module-pbr python3-module-pytest python3-module-unittest2

%description
Python library for interacting with Embedly's API. To get started sign
up for a key at https://app.embed.ly/signup

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Python library for interacting with Embedly's API. To get started sign
up for a key at https://app.embed.ly/signup

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*

%changelog
* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt2.git20141215
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5.0-alt1.git20141215.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20141215.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.git20141215.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141215
- Initial build for Sisyphus

