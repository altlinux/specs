%define oname zope.contentprovider

%def_with python3

Name: python-module-%oname
Version: 4.0.0
Release: alt3
Summary: Content Provider Framework for Zope Templates
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.contentprovider/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.component zope.event zope.interface zope.location
%py_requires zope.publisher zope.schema zope.tales

%description
This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content
provider objects are dynamically looked up based on the
setup/configuration of the application.

%package -n python3-module-%oname
Summary: Content Provider Framework for Zope Templates
Group: Development/Python3
%py3_requires zope zope.component zope.event zope.interface zope.location
%py3_requires zope.publisher zope.schema zope.tales

%description -n python3-module-%oname
This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content
provider objects are dynamically looked up based on the
setup/configuration of the application.

%package -n python3-module-%oname-tests
Summary: Tests for zope.contentprovider
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.browserpage zope.testing

%description -n python3-module-%oname-tests
This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content
provider objects are dynamically looked up based on the
setup/configuration of the application.

This package contains tests for zope.contentprovider.

%package tests
Summary: Tests for zope.contentprovider
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.browserpage zope.testing

%description tests
This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content
provider objects are dynamically looked up based on the
setup/configuration of the application.

This package contains tests for zope.contentprovider.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Initial build for Sisyphus

