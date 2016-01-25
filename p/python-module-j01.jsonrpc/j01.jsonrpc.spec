%define mname j01
%define oname %mname.jsonrpc
%def_disable check

Name: python-module-%oname
Version: 2.0.0
Release: alt2
Summary: JSON-RPC helpers based on JQuery, z3c.form and z3c.jsonrpc for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/j01.jsonrpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildRequires: python-module-cjson python-module-nose python-module-p01.checker python-module-p01.testbrowser python-module-pytest python-module-z3c.coverage python-module-z3c.form python-module-z3c.jsonrpc python-module-z3c.macro python-module-z3c.pagelet python-module-zc.sourcefactory python-module-zope.app.testing python-module-zope.testrunner

#BuildPreReq: python-module-setuptools-tests python-module-nose
#BuildPreReq: python-module-cjson
#BuildPreReq: python-module-z3c.form-tests
#BuildPreReq: python-module-z3c.jsonrpc-tests
#BuildPreReq: python-module-z3c.pagelet
#BuildPreReq: python-module-z3c.template
#BuildPreReq: python-module-zope.browserresource
#BuildPreReq: python-module-zope.component-tests
#BuildPreReq: python-module-zope.i18n
#BuildPreReq: python-module-zope.i18nmessageid
#BuildPreReq: python-module-zope.interface
#BuildPreReq: python-module-zope.location
#BuildPreReq: python-module-zope.publisher
#BuildPreReq: python-module-zope.schema
#BuildPreReq: python-module-zope.site
#BuildPreReq: python-module-zope.traversing-tests
#BuildPreReq: python-module-p01.checker
#BuildPreReq: python-module-p01.testbrowser
#BuildPreReq: python-module-z3c.macro
#BuildPreReq: python-module-zope.container
#BuildPreReq: python-module-zope.pagetemplate
#BuildPreReq: python-module-zope.password-tests
#BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
#%py_requires zope.site zope.traversing
#%py_requires zope.interface zope.location zope.publisher zope.schema
#%py_requires z3c.form z3c.jsonrpc z3c.pagelet z3c.template zope.i18n
#%py_requires zope.browserresource zope.component zope.i18nmessageid

%description
This package provides some JQuery based JSON-RPC form handling using the
z3c.jsonrpc and z3c.form libraries for Zope3.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#%py_requires p01.checker p01.testbrowser z3c.form.tests z3c.macro
#%py_requires z3c.jsonrpc.tests zope.container zope.pagetemplate
#%py_requires zope.password zope.testing zope.traversing.testing
#%py_requires zope.component.testing zope.password.testing

%description tests
This package provides some JQuery based JSON-RPC form handling using the
z3c.jsonrpc and z3c.form libraries for Zope3.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

sed -i 's|\r||' $(find src -name '*.txt')

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test
nosetests -v

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 2.0.0-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus

