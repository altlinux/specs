%define oname zope.sendmail

%def_with python3

Name: python-module-%oname
Version: 4.0.1
Release: alt1
Summary: Zope sendmail
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.sendmail/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
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
%ifarch x86_64
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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
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

