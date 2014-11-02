%define mname collective.js
%define oname %mname.backbone
Name: python-module-%oname
Version: 1.0.0.3
Release: alt1.dev0.git20130818
Summary: backbone.js for plone
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.backbone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.backbone.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-collective.js.underscore

%py_provides %oname
%py_requires %mname collective.js.underscore

%description
Bundles backbone.js for use with Plone.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/collective/js/*
%python_sitelibdir/*.egg-info

%changelog
* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0.3-alt1.dev0.git20130818
- Initial build for Sisyphus

