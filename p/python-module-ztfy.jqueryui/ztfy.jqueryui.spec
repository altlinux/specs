%define mname ztfy
%define oname %mname.jqueryui
Name: python-module-%oname
Version: 0.7.12
Release: alt1
Summary: JQuery, JQuery UI, JQuery Tools and a small set of JQuery plugins
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.jqueryui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: repocop-test-hint.binary.ztfy.jqueryui.resources

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname fanstatic

%description
ztfy.jqueryui is a set of javascript resources (and their dependencies)
allowing any application to easily use a set of JQuery plug-ins; when
possible, all CSS and JavaScript resources are already minified via
Yahoo 'yui-compressor' tool.

Most of these plug-ins are used by default ZTFY skins and packages.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ztfy.jqueryui is a set of javascript resources (and their dependencies)
allowing any application to easily use a set of JQuery plug-ins; when
possible, all CSS and JavaScript resources are already minified via
Yahoo 'yui-compressor' tool.

Most of these plug-ins are used by default ZTFY skins and packages.

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
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.12-alt1
- Initial build for Sisyphus

