%define _unpackaged_files_terminate_build 1
%define mname hurry
%define oname %mname.resource

%def_with check

Name: python3-module-%oname
Version: 0.10
Release: alt4
Summary: Flexible resources for web applications
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/hurry.resource/

Source: %name-%version.tar

Patch: hurry-resource-0.10-alt-zope-interface-api-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%py3_requires webob zope.interface zope.component
Requires: python3-module-%mname = %EVR

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

%package tests
Summary: Tests for hurry.resource
Group: Development/Python3
Requires: %name = %EVR

%description tests
Resources are files that are used as resources in the display of a web
page, such as CSS files, Javascript files and images. Resources packaged
together in a directory to be published as such are called a resource
library.

This package contains tests for hurry.resource.

%package -n python3-module-%mname
Summary: Core files for hurry
Group: Development/Python3
%py3_provides hurry

%description -n python3-module-%mname
Core files for hurry.

%prep
%setup

%patch -p2

# remove Python2 explicit type import as it is neither available in Python3
# types lib nor used in the module code
sed -i '/TupleType$/d' src/hurry/resource/core.py

%build
%python3_build

%install
%python3_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

touch %buildroot%python3_sitelibdir/%mname/__init__.py

%check
python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname/
%dir %python3_sitelibdir/%mname/__pycache__/
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*

%changelog
* Tue Jan 14 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.10-alt4
- NMU: Remove python2 module build
- Add unittests execution
- Fix python3 compatibility
- Add zope-interface-api-compat patch

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.10-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10-alt3.1.1
- (AUTO) subst_x86_64.

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

