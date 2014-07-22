%define oname z3c.jbot

%def_with python3

Name: python-module-%oname
Version: 0.7.2
Release: alt1
Summary: Drop-in template overrides
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.jbot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.pagetemplate zope.component zope.configuration
%py_requires zope.security zope.publisher

%description
The z3c.jbot (or "Just a bunch of templates") package allows easy
customization of existing templates and images. It works on Zope 2 and
Zope 3.

%package -n python3-module-%oname
Summary: Drop-in template overrides
Group: Development/Python3
%py3_requires zope.pagetemplate zope.component zope.configuration
%py3_requires zope.security zope.publisher

%description -n python3-module-%oname
The z3c.jbot (or "Just a bunch of templates") package allows easy
customization of existing templates and images. It works on Zope 2 and
Zope 3.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.jbot
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%add_python3_req_skip Testing

%description -n python3-module-%oname-tests
The z3c.jbot (or "Just a bunch of templates") package allows easy
customization of existing templates and images. It works on Zope 2 and
Zope 3.

This package contains tests for z3c.jbot.

%package tests
Summary: Tests for z3c.jbot
Group: Development/Python
Requires: %name = %version-%release

%description tests
The z3c.jbot (or "Just a bunch of templates") package allows easy
customization of existing templates and images. It works on Zope 2 and
Zope 3.

This package contains tests for z3c.jbot.

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Version 0.7.2
- Added module for Python 3

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Version 0.7.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.3-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus

