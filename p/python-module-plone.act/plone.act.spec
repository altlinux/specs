%define oname plone.act
Name: python-module-%oname
Version: 0.1
Release: alt1.git20130614
Summary: Acts, not words : ACceptance Testing for Plone
License: GPL
Group: Development/Python
Url: https://github.com/gotcha/plone.act
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gotcha/plone.act.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-decorator
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-robotframework-selenium2library

%py_provides %oname
%py_requires plone plone.app.testing

%description
plone.act holds robot framework resources to test Plone CMS.

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
%doc *.txt *.rst docs/*
%_bindir/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20130614
- Initial build for Sisyphus

