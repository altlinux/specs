%define oname radar

Name: python3-module-%oname
Version: 0.3
Release: alt2

Summary: Random date generation
License: GPLv2.0/LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/radar/
BuildArch: noarch

# https://github.com/barseghyanartur/radar.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
Generate random date(time).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires simple_timer

%description tests
Generate random date(time).

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD/src
%__python3 setup.py test
sed -i 's|python|python3|' test.sh
./test.sh

%files
%doc *.rst docs/*.rst example
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%doc *.rst docs/*.rst example


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.git20131211.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.git20131211.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20131211.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20131211
- Initial build for Sisyphus

