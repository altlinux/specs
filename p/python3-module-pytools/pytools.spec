%define oname pytools

Name: python3-module-%oname
Version: 2017.4
Release: alt2
Summary: A collection of tools for Python
License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/pytools

# https://github.com/inducer/pytools.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-appdirs python3-module-decorator
BuildPreReq: python3-module-six
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-pytest
BuildArch: noarch

%add_python3_req_skip mpi4py.rc

%description
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of my other software
packages, and is probably of little interest to you unless you use
those.

%package tests
Summary: Test for Pytools
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of my other software
packages, and is probably of little interest to you unless you use
those.

This package contains test for Pytools.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
PYTHONPATH=%buildroot%python3_sitelibdir py.test3

%files
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test.py*
%exclude %python3_sitelibdir/%oname/__pycache__/test*

%files tests
%python3_sitelibdir/%oname/test.py*
%python3_sitelibdir/%oname/__pycache__/test*

%changelog
* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 2017.4-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2017.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.4-alt1
- Updated to upstream version 2017.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2014.3.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.3.5-alt1
- Version 2014.3.5

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.3.4-alt1
- Version 2014.3.4
- Enabled testing

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.3-alt1
- Version 2014.3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.5.7-alt1
- Version 2013.5.7

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.5.6-alt1
- Version 2013.5.6

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1-alt1
- Version 2012.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2011.5-alt2.1
- Rebuild with Python-3.3

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.5-alt2
- Added module for Python 3

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.5-alt1
- Initial build for Sisyphus

