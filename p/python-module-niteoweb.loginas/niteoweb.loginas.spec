%define mname niteoweb
%define oname %mname.loginas
Name: python-module-%oname
Version: 0.3
Release: alt1.dev.git20120516
Summary: Hacked niteoweb.loginas to allow "sudo" on Plone site
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/niteoweb.loginas/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/miohtama/niteoweb.loginas.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires zope.i18nmessageid

%description
Allow administrator to login as another user (useful for debugging).

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python

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
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev.git20120516
- Initial build for Sisyphus

