%define mname p01
%define oname %mname.testbrowser
Name: python-module-%oname
Version: 2.0.1
Release: alt1.1
Summary: Zope test brwoser based on webtest and wsgi app
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/p01.testbrowser/

Source: %name-%version.tar

BuildPreReq: python-module-setuptools python-test
BuildPreReq: python-module-pytz python-module-webtest
BuildPreReq: python-module-WSGIProxy2 python-module-six
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.cachedescriptors
BuildPreReq: python-module-zope.testing
BuildRequires: python-module-transaction python-module-zope.component python-module-zope.configuration python-module-z3c.json python-module-z3c.jsonrpc

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires zope.interface zope.schema zope.cachedescriptors pytz six
%py_requires webtest zope.testing

%description
This package provides a copy of the new zope.testbrowser version > 5.0.0
and is used for experiment with jsonrpc support.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

sed -i 's|\r||' $(find src -name '*.txt*')

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
py.test ||:

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.1-alt1
- Updated to upstream version 2.0.1.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1
- (AUTO) subst_x86_64.

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

