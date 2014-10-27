%define mname hexagonit
%define oname %mname.testing
Name: python-module-%oname
Version: 1.2.2
Release: alt1.git20120522
Summary: Plone4 test helper which uses plone.testing and manuel
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/hexagonit.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hexagonit/hexagonit.testing.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-manuel
BuildPreReq: python-module-mock python-module-unittest2
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.app.testing plone.testing

%description
This package provides useful helper methods for testing in Plone.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

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

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20120522
- Initial build for Sisyphus

