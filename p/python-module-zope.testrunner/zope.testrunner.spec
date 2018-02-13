%define _unpackaged_files_terminate_build 1
%define oname zope.testrunner

%def_with check

Name: python-module-%oname
Version: 4.8.1
Release: alt1%ubt

Summary: Zope testrunner script
License: ZPLv2.1
Group: Development/Python
# Source-git: https://github.com/zopefoundation/zope.testrunner.git
Url: http://pypi.python.org/pypi/zope.testrunner

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-zope.interface
BuildRequires: python-module-zope.testing
BuildRequires: python-module-six
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-six
%endif

%py_requires zope.exceptions zope.interface

%description
This package provides a flexible test runner with layer support.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides a flexible test runner with layer support.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Zope testrunner script (Python 3)
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
This package provides a flexible test runner with layer support.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip zope.testrunner.huh

%description -n python3-module-%oname-tests
This package provides a flexible test runner with layer support.

This package contains tests for %oname.

%prep
%setup
rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd

mv %buildroot%_bindir/zope-testrunner \
	%buildroot%_bindir/zope-testrunner3

%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
        %buildroot%python3_sitelibdir/
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
        %buildroot%python_sitelibdir/
%endif

%check
python setup.py test -v

pushd ../python3
python3 setup.py test -v
popd

%files
%doc *.rst
%_bindir/zope-testrunner
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%files -n python3-module-%oname
%doc *.rst
%_bindir/zope-testrunner3
%python3_sitelibdir/*

%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests

%changelog
* Mon Feb 12 2018 Stanislav Levin <slev@altlinux.org> 4.8.1-alt1%ubt
- v4.4.9 -> v4.8.1

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.9-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.9-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.4.9-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.9-alt1
- Version 4.4.9

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.6-alt1
- Version 4.4.6

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.5-alt1
- Version 4.4.5

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt1
- Version 4.4.4

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.3-alt1
- Version 4.4.3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1-alt1
- Version 4.4.1

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1
- Version 4.3.3

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.4-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Added module for Python 3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.3-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Initial build for Sisyphus

