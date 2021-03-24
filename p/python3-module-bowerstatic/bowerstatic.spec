%define oname bowerstatic

Name: python3-module-%oname
Version: 0.9
Release: alt3

Summary: A Bower-centric static file server for WSGI
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/bowerstatic/

# https://github.com/faassen/bowerstatic.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-mock
BuildRequires: python3-module-webtest
BuildRequires: python3-module-sphinx

%py3_provides %oname


%description
BowerStatic is a WSGI-based framework that you can integrate with your
WSGI-using web application or framework to help it serve static
resources.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
BowerStatic is a WSGI-based framework that you can integrate with your
WSGI-using web application or framework to help it serve static
resources.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
BowerStatic is a WSGI-based framework that you can integrate with your
WSGI-using web application or framework to help it serve static
resources.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
BowerStatic is a WSGI-based framework that you can integrate with your
WSGI-using web application or framework to help it serve static
resources.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test
rm -fR build
py.test3

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*


%changelog
* Wed Mar 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.9-alt3
- Fixed BuildRequires (fixed FTBFS).

* Mon Feb 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9-alt1
- Updated to upstream version 0.9.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8-alt1.dev0.git20141115.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8-alt1.dev0.git20141115.1
- NMU: Use buildreq for BR.

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.dev0.git20141115
- Version 0.8.dev0

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.dev0.git20141111
- Initial build for Sisyphus

