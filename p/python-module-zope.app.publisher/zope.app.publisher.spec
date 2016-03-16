%define oname zope.app.publisher

%def_with python3

Name: python-module-%oname
Version: 3.10.2
Release: alt4.1
Summary: Implementations and means for configuration of Zope 3-style views and resources
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.publisher/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.browsermenu zope.browserpage zope.browserresource
%py_requires zope.component zope.configuration zope.datetime
%py_requires zope.interface zope.location zope.ptresource
%py_requires zope.publisher zope.schema zope.security
%py_requires zope.componentvocabulary zope.app

%description
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package used to provide browser page, resource and menu classes for
use with zope.publisher object publishing framework, as well as some
other useful utilities and adapters, but most of things was factored out
to separate packages, leaving here only backward-compatibility imports.

%package -n python3-module-%oname
Summary: Implementations and means for configuration of Zope 3-style views and resources
Group: Development/Python3
%py3_requires zope.browsermenu zope.browserpage zope.browserresource
%py3_requires zope.component zope.configuration zope.datetime
%py3_requires zope.interface zope.location zope.ptresource
%py3_requires zope.publisher zope.schema zope.security
%py3_requires zope.componentvocabulary zope.app

%description -n python3-module-%oname
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package used to provide browser page, resource and menu classes for
use with zope.publisher object publishing framework, as well as some
other useful utilities and adapters, but most of things was factored out
to separate packages, leaving here only backward-compatibility imports.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.publisher
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.app.testing zope.app.zcmlfiles
%py3_requires zope.container zope.securitypolicy zope.site zope.login

%description -n python3-module-%oname-tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package used to provide browser page, resource and menu classes for
use with zope.publisher object publishing framework, as well as some
other useful utilities and adapters, but most of things was factored out
to separate packages, leaving here only backward-compatibility imports.

This package contains tests for zope.app.publisher.

%package tests
Summary: Tests for zope.app.publisher
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.app.testing zope.app.zcmlfiles
%py_requires zope.container zope.securitypolicy zope.site zope.login

%description tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package used to provide browser page, resource and menu classes for
use with zope.publisher object publishing framework, as well as some
other useful utilities and adapters, but most of things was factored out
to separate packages, leaving here only backward-compatibility imports.

This package contains tests for zope.app.publisher.

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
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests
%exclude %python3_sitelibdir/*/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%python3_sitelibdir/*/*/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.10.2-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.10.2-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt2
- Excluded *.pth
- Added necessary requirements

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt1
- Initial build for Sisyphus

