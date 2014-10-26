%define mname collective.ptg
%define oname %mname.galleria

Name: python-module-%oname
Version: 1.3.0
Release: alt2.git20130524
Summary: galleria integration with plonetruegallery
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.ptg.galleria/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.ptg.galleria.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-collective.plonetruegallery
BuildPreReq: python-module-initgroups
BuildPreReq: python-module-unittest2

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_provides collective.plonetruegallery

%description
Basic integration of the Galleria javascript gallery with
collective.plonetruegallery.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_requires collective

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

install -p -m644 collective/ptg/__init__.py \
	%buildroot%python_sitelibdir/collective/ptg/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/collective/ptg/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/ptg/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/collective/ptg
%python_sitelibdir/collective/ptg/__init__.py*

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.git20130524
- Added necessary requirements
- Enabled testing

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20130524
- Initial build for Sisyphus

