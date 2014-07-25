%define oname z3wingdbg

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt2
Summary: Wing IDE debugger integration for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3wingdbg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires(pre): python-tools-2to3
%endif

%py_requires zope.traversing zope.security zope.location zope.interface
%py_requires zope.i18n zope.publisher zope.component
%py_requires zope.app.publication zope.app.component zope.app.appsetup
%py_requires zope.event zope.schema zope.app.generations
%py_requires zope.cachedescriptors zope.app.applicationcontrol
%py_requires zope.app.twisted zope.app.wsgi zope.app.container

%description
Zope3 package providing debug integration with the Wing IDE, allowing
you to run Zope3 applications under the control of the Wing debugger.

%package -n python3-module-%oname
Summary: Wing IDE debugger integration for Zope3
Group: Development/Python3
%py3_requires zope.traversing zope.security zope.location zope.interface
%py3_requires zope.i18n zope.publisher zope.component
%py3_requires zope.app.publication zope.app.component zope.app.appsetup
%py3_requires zope.event zope.schema zope.app.generations
%py3_requires zope.cachedescriptors zope.app.applicationcontrol
%py3_requires zope.app.twisted zope.app.wsgi zope.app.container

%description -n python3-module-%oname
Zope3 package providing debug integration with the Wing IDE, allowing
you to run Zope3 applications under the control of the Wing debugger.

%package -n python3-module-%oname-tests
Summary: Tests for Wing IDE debugger integration for Zope3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing

%description -n python3-module-%oname-tests
Zope3 package providing debug integration with the Wing IDE, allowing
you to run Zope3 applications under the control of the Wing debugger.

This package contains tests for Wing IDE debugger integration for Zope3.

%package tests
Summary: Tests for Wing IDE debugger integration for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
Zope3 package providing debug integration with the Wing IDE, allowing
you to run Zope3 applications under the control of the Wing debugger.

This package contains tests for Wing IDE debugger integration for Zope3.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt1.1
- Rebuild with Python-2.7

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

