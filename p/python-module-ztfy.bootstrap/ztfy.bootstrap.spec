%define mname ztfy
%define oname %mname.bootstrap
Name: python-module-%oname
Version: 0.1.6
Release: alt1
Summary: Bootstrap based ZTFY skin
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.bootstrap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-ztfy.blog
BuildPreReq: python-module-ztfy.jqueryui
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname zope.component zope.i18nmessageid zope.interface
%py_requires ztfy.skin ztfy.utils ztfy.blog ztfy.jqueryui fanstatic

%description
ZTFY.bootstrap is mainly a new set of Fanstatic resources for Twitter
Bootstrap (including Glypicons set of icons and CSS for responsive
design).

It also defines a new browser layer, and a set of forms templates to be
used with this skin, which also relies on ZTFY.skin package.

Finally, ZTFY.bootstrap provides a new basic skin for ZTFY.blog (but
because of conditional includes, usage of ZTFY.blog is not mandatory to
use ZTFY.bootstrap package).

%package tests
Summary: tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ZTFY.bootstrap is mainly a new set of Fanstatic resources for Twitter
Bootstrap (including Glypicons set of icons and CSS for responsive
design).

It also defines a new browser layer, and a set of forms templates to be
used with this skin, which also relies on ZTFY.skin package.

Finally, ZTFY.bootstrap provides a new basic skin for ZTFY.blog (but
because of conditional includes, usage of ZTFY.blog is not mandatory to
use ZTFY.bootstrap package).

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
rm -fR build
py.test -vv

%files
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1
- Initial build for Sisyphus

