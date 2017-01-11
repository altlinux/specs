%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.app.testing

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 3.10.0
#Release: alt1.dev.git20141223.1
Summary: Zope Application Testing Support
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/b7/72/f62c1c79d691260235f1ebe48f954d2fdffc253bcb14623550e242a366dd/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.annotation zope.app.appsetup
%py_requires zope.processlifetime zope.app.debug zope.app.dependable
%py_requires zope.app.publication zope.component zope.container
%py_requires zope.i18n zope.interface zope.password zope.publisher
%py_requires zope.schema zope.security zope.site zope.testing
%py_requires zope.testbrowser zope.traversing
%py_requires ZODB3 zope.app.authentication zope.app.zcmlfiles zope.login
%py_requires zope.publisher zope.securitypolicy
Requires: python-module-zope.app = %EVR

%description
This package provides testing support for Zope 3 applications. Besides
providing numerous setup convenience functions, it implements a testing
setup that allows the user to make calls to the publisher allowing to
write functional tests.

%package -n python3-module-%oname
Summary: Zope Application Testing Support
Group: Development/Python3
%py3_requires zope.annotation zope.app.appsetup
%py3_requires zope.processlifetime zope.app.debug zope.app.dependable
%py3_requires zope.app.publication zope.component zope.container
%py3_requires zope.i18n zope.interface zope.password zope.publisher
%py3_requires zope.schema zope.security zope.site zope.testing
%py3_requires zope.testbrowser zope.traversing
%py3_requires ZODB3 zope.app.authentication zope.app.zcmlfiles zope.login
%py3_requires zope.publisher zope.securitypolicy
Requires: python3-module-zope.app = %EVR

%description -n python3-module-%oname
This package provides testing support for Zope 3 applications. Besides
providing numerous setup convenience functions, it implements a testing
setup that allows the user to make calls to the publisher allowing to
write functional tests.

%package -n python3-module-zope.app
Summary: Core files for zope.app
Group: Development/Python3
Requires: python3-module-zope
%py3_provides zope.app

%description -n python3-module-zope.app
This package provides testing support for Zope 3 applications. Besides
providing numerous setup convenience functions, it implements a testing
setup that allows the user to make calls to the publisher allowing to
write functional tests.

This package contains core files for zope.app.

%package -n python-module-zope.app
Summary: Core files for zope.app
Group: Development/Python
Requires: python-module-zope
%py_provides zope.app

%description -n python-module-zope.app
This package provides testing support for Zope 3 applications. Besides
providing numerous setup convenience functions, it implements a testing
setup that allows the user to make calls to the publisher allowing to
write functional tests.

This package contains core files for zope.app.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|rfc822|rfc822py3|g' $(find ./ -name '*.py')
%python3_build
popd
%endif

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif
touch %buildroot%python_sitelibdir/zope/app/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/zope/app/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zope/app/__init__.py*

%files -n python-module-zope.app
%python_sitelibdir/zope/app/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/app/__init__.py
%exclude %python3_sitelibdir/zope/app/__pycache__/__init__.*

%files -n python3-module-zope.app
%python3_sitelibdir/zope/app/__init__.py
%python3_sitelibdir/zope/app/__pycache__/__init__.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.10.0-alt1
- automated PyPI update

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:3.9.1-alt1.dev.git20141223.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:3.9.1-alt1.dev.git20141223.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.9.1-alt1.dev.git20141223
- Updated from github

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt1
- Version 3.10.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Initial build for Sisyphus

