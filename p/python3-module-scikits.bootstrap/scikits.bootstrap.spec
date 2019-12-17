%define mname scikits
%define oname %mname.bootstrap

Name: python3-module-%oname
Version: 1.0.1
Release: alt1

Summary: Bootstrap confidence interval estimation routines for SciPy
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/scikits.bootstrap/

# https://github.com/cgevans/scikits-bootstrap.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-numpy python3-module-scipy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-nose python3-module-pandas
BuildRequires: python3(pyerf)

%py3_provides %oname
%py3_requires %mname numpy scipy


%description
Scikits.bootstrap provides bootstrap confidence interval algorithms for
scipy.

At present, it is rather feature-incomplete and in flux. However, the
functions that have been written should be relatively stable as far as
results.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires pandas

%description tests
Scikits.bootstrap provides bootstrap confidence interval algorithms for
scipy.

At present, it is rather feature-incomplete and in flux. However, the
functions that have been written should be relatively stable as far as
results.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%__python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%exclude %python3_sitelibdir/%mname/*/test*
%exclude %python3_sitelibdir/%mname/*/*/test*

%files tests
%python3_sitelibdir/%mname/*/test*
%python3_sitelibdir/%mname/*/*/test*


%changelog
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt1
- version updated to 1.0.1
- build for python2 disabled

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1.1
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20150327.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20150327.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20150327
- New snapshot

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20140521
- Initial build for Sisyphus

