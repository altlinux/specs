%define oname hurry.resource

%def_with python3

Name: python-module-%oname
Version: 0.10
Release: alt3.1
Summary: Flexible resources for web applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/hurry.resource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires hurry webob zope.interface zope.component

%description
Resources are files that are used as resources in the display of a web
page, such as CSS files, Javascript files and images. Resources packaged
together in a directory to be published as such are called a resource
library.

When a resource is included in the head section of a HTML page, we call
this a resource inclusion. An inclusion is of a particular resource in a
particular library. There are two forms of this kind of inclusion in
HTML: javascript is included using the script tag, and CSS (and KSS) are
included using a link tag.

Inclusions may depend on other inclusions. A javascript resource may for
instance be built on top of another javascript resource. This means both
of them should be loaded when the page displays.

Page components may actually require a certain inclusion in order to be
functional. A widget may for instance expect a particular Javascript
library to loaded. We call this an inclusion requirement of the
component.

hurry.resource provides a simple API to specify resource libraries,
inclusion and inclusion requirements.

%package -n python3-module-%oname
Summary: Flexible resources for web applications
Group: Development/Python3
%py3_requires hurry webob zope.interface zope.component

%description -n python3-module-%oname
Resources are files that are used as resources in the display of a web
page, such as CSS files, Javascript files and images. Resources packaged
together in a directory to be published as such are called a resource
library.

When a resource is included in the head section of a HTML page, we call
this a resource inclusion. An inclusion is of a particular resource in a
particular library. There are two forms of this kind of inclusion in
HTML: javascript is included using the script tag, and CSS (and KSS) are
included using a link tag.

Inclusions may depend on other inclusions. A javascript resource may for
instance be built on top of another javascript resource. This means both
of them should be loaded when the page displays.

Page components may actually require a certain inclusion in order to be
functional. A widget may for instance expect a particular Javascript
library to loaded. We call this an inclusion requirement of the
component.

hurry.resource provides a simple API to specify resource libraries,
inclusion and inclusion requirements.

%package -n python3-module-%oname-tests
Summary: Tests for hurry.resource
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Resources are files that are used as resources in the display of a web
page, such as CSS files, Javascript files and images. Resources packaged
together in a directory to be published as such are called a resource
library.

This package contains tests for hurry.resource.

%package tests
Summary: Tests for hurry.resource
Group: Development/Python
Requires: %name = %version-%release

%description tests
Resources are files that are used as resources in the display of a web
page, such as CSS files, Javascript files and images. Resources packaged
together in a directory to be published as such are called a resource
library.

This package contains tests for hurry.resource.

%package -n python-module-hurry
Summary: Core files for hurry
Group: Development/Python
%py_provides hurry

%description -n python-module-hurry
Core files for hurry.

%package -n python3-module-hurry
Summary: Core files for hurry
Group: Development/Python3
%py3_provides hurry

%description -n python3-module-hurry
Core files for hurry.

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
touch %buildroot%python_sitelibdir/hurry/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/hurry/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/hurry/__init__.py*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%files -n python-module-hurry
%python_sitelibdir/hurry/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/hurry/__init__.py
%exclude %python3_sitelibdir/hurry/__pycache__/__init__.*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-hurry
%python3_sitelibdir/hurry/__init__.py
%python3_sitelibdir/hurry/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt2
- Added necessary requirements
- Excludes *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1
- Initial build for Sisyphus

