%define mname haufe
%define oname %mname.requestmonitoring
Name: python-module-%oname
Version: 0.4.0.1
Release: alt1.git20150113
Summary: Zope 2 request monitoring
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/haufe.requestmonitoring/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/haufe.requestmonitoring.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.app.appsetup
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.event

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires zope.app.appsetup zope.component zope.publisher zope.event
%py_requires zope.interface

%description
haufe.requestmonitoring implements a detailed request logging
functionality on top of the publication events as introduced with Zope
2.12.

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
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0.1-alt1.git20150113
- Initial build for Sisyphus

