%define oname z3c.traverser

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt2.a2.1.1
Summary: Pluggable Traversers And URL handling utilities
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.traverser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-eggtestinfo python-module-zope.testrunner
#BuildPreReq: python-module-zope.interface python-module-zope.exceptions
#BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-eggtestinfo python3-module-zope.testrunner
#BuildPreReq: python3-module-zope.interface python3-module-zope.exceptions
#BuildPreReq: python3-module-six
%endif

%py_requires zope.component zope.contentprovider zope.interface
%py_requires zope.publisher zope.traversing zope.viewlet

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-mimeparse python-module-numpy python-module-pbr python-module-pyasn1 python-module-serial python-module-setuptools python-module-twisted-core python-module-unittest2 python-module-zope.exceptions python-module-zope.interface python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-setuptools python3-module-unittest2 python3-module-zope python3-module-zope.exceptions python3-module-zope.interface python3-module-zope.testing
BuildRequires: python-module-eggtestinfo python-module-zope.testrunner python3-module-eggtestinfo python3-module-html5lib python3-module-zope.testrunner rpm-build-python3

%description
This package provides the pluggable traverser mechanism allowing
developers to add new traversers to an object without altering the
original traversal implementation.

In addition to the pluggable traversers, this package contains two more
subpackages:

* viewlet - provides a way to traverse to viewlets using namespaces
* stackinfo - provides a way to consume parts of url and store them as
  attributes of the "consumer" object. Useful for urls like:
  /blog/2009/02/02/hello-world

%package -n python3-module-%oname
Summary: Pluggable Traversers And URL handling utilities
Group: Development/Python3
%py3_requires zope.component zope.contentprovider zope.interface
%py3_requires zope.publisher zope.traversing zope.viewlet

%description -n python3-module-%oname
This package provides the pluggable traverser mechanism allowing
developers to add new traversers to an object without altering the
original traversal implementation.

In addition to the pluggable traversers, this package contains two more
subpackages:

* viewlet - provides a way to traverse to viewlets using namespaces
* stackinfo - provides a way to consume parts of url and store them as
  attributes of the "consumer" object. Useful for urls like:
  /blog/2009/02/02/hello-world

%package -n python3-module-%oname-tests
Summary: Tests for Pluggable Traversers And URL handling utilities
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.securitypolicy
%py3_requires zope.app.zcmlfiles zope.testbrowser

%description -n python3-module-%oname-tests
This package provides the pluggable traverser mechanism allowing
developers to add new traversers to an object without altering the
original traversal implementation.

This package contains tests for Pluggable Traversers And URL handling
utilities.

%package tests
Summary: Tests for Pluggable Traversers And URL handling utilities
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.testbrowser

%description tests
This package provides the pluggable traverser mechanism allowing
developers to add new traversers to an object without altering the
original traversal implementation.

This package contains tests for Pluggable Traversers And URL handling
utilities.

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
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.a2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2.a2.1
- NMU: Use buildreq for BR.

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.a2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.a2
- Version 1.0.0a2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

