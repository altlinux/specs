# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20150613.1.1.1
%define oname zope.sendmail

%def_with python3

Name: python-module-%oname
Version: 4.0.2
#Release: alt1.dev0.git20150613.1
Summary: Zope sendmail
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.sendmail/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.sendmail.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-transaction python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema python-module-zope.configuration
BuildPreReq: python-module-zope.security python-module-zope.testing
BuildPreReq: python-module-zope.component-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-transaction python3-module-zope.i18nmessageid
BuildPreReq: python3-module-zope.schema python3-module-zope.configuration
BuildPreReq: python3-module-zope.security python3-module-zope.testing
BuildPreReq: python3-module-zope.component-tests
%endif

%py_requires zope transaction zope.i18nmessageid zope.interface
%py_requires zope.schema zope.component zope.configuration

%description
zope.sendmail is a package for email sending from Zope 3 applications.

%package -n python3-module-%oname
Summary: Zope sendmail
Group: Development/Python3
%py3_requires zope transaction zope.i18nmessageid zope.interface
%py3_requires zope.schema zope.component zope.configuration

%description -n python3-module-%oname
zope.sendmail is a package for email sending from Zope 3 applications.

%package -n python3-module-%oname-tests
Summary: Tests for Zope sendmail
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.security zope.component

%description -n python3-module-%oname-tests
zope.sendmail is a package for email sending from Zope 3 applications.

This package contains tests for Zope sendmail.

%package tests
Summary: Tests for Zope sendmail
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.security zope.component

%description tests
zope.sendmail is a package for email sending from Zope 3 applications.

This package contains tests for Zope sendmail.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.2-alt1.dev0.git20150613.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev0.git20150613.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev0.git20150613.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.dev0.git20150613
- Version 4.0.2.dev0
- Enabled check

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a2
- Version 4.0.0a2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt1
- Initial build for Sisyphus

