%define mname ecreall.helpers
%define oname %mname.testing
Name: python-module-%oname
Version: 1.8
Release: alt1.dev0.git20140217
Summary: Helpers for testing often used at Ecreall
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ecreall.helpers.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tdesvenain/ecreall.helpers.testing.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.app.testing

%description
Various base classes and methods ecreall uses to test and debug
projects.

%package -n python-module-ecreall
Summary: Core files of ecreall
Group: Development/Python

%description -n python-module-ecreall
Core files of ecreall.

%package -n python-module-%mname
Summary: Core files of %mname.
Group: Development/Python
Requires: python-module-ecreall = %EVR

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/ecreall/__init__.py \
	%buildroot%python_sitelibdir/ecreall/
install -p -m644 src/ecreall/helpers/__init__.py \
	%buildroot%python_sitelibdir/ecreall/helpers/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/ecreall/helpers/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/ecreall/helpers/__init__.py*

%files -n python-module-ecreall
%dir %python_sitelibdir/ecreall
%python_sitelibdir/ecreall/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/ecreall/helpers
%python_sitelibdir/ecreall/helpers/__init__.py*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.dev0.git20140217
- Initial build for Sisyphus

