%define oname zope.container

%def_with python3

Name: python-module-%oname
Version: 4.0.0
Release: alt3
Summary: Zope Container
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.container/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

Requires: python-module-zope.i18nmessageid
%py_requires zope.interface zope.dottedname zope.schema zope.traversing
%py_requires zope.component zope.event zope.location zope.security
%py_requires zope.lifecycleevent zope.size zope.filerepresentation

%description
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

%package -n python3-module-%oname
Summary: Zope Container
Group: Development/Python3
Requires: python3-module-zope.i18nmessageid
%py3_requires zope.interface zope.dottedname zope.schema 
%py3_requires zope.component zope.event zope.location zope.security
%py3_requires zope.lifecycleevent

%description -n python3-module-%oname
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Container
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

This package contains tests for Zope Container.

%package tests
Summary: Tests for Zope Container
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

This package contains tests for Zope Container.

%prep
%setup

rm -fR src/*.egg-info

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
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
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Added necessary requirements

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Version 4.0.0
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a3
- Version 4.0.0a3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.0-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt2
- Added necessary requirements
- Excluded *.th

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt1
- Initial build for Sisyphus

