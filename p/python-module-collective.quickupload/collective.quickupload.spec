%define mname collective
%define oname %mname.quickupload
Name: python-module-%oname
Version: 1.6.7
Release: alt1.dev0.git20141209
Summary: Pure javascript files upload tool for Plone
License: AGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.quickupload/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.quickupload.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-ua_parser
BuildPreReq: python-module-mock
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
%py_requires %mname plone.app.dexterity

%description
This product offers a multiple files upload tool for Plone, with multi
selection, drag and drop, and progress bar. A pure javacript tool is
used on client side, with html5 file fields and ajax upload for modern
browsers, and a graceful fallback for other browsers. You can also
choose to replace the javascript with jquery.uploadify, a flashupload
based script which could be interesting in rare situations (Plone site
for MSIE client's browsers only, without http authentication in front,
and no https).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This product offers a multiple files upload tool for Plone, with multi
selection, drag and drop, and progress bar. A pure javacript tool is
used on client side, with html5 file fields and ajax upload for modern
browsers, and a graceful fallback for other browsers. You can also
choose to replace the javascript with jquery.uploadify, a flashupload
based script which could be interesting in rare situations (Plone site
for MSIE client's browsers only, without http authentication in front,
and no https).

This package contains tests for %oname.

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
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.7-alt1.dev0.git20141209
- Version 1.6.7.dev0

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt1.dev0.git20140806
- Initial build for Sisyphus

