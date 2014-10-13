%define oname plone.app.jquery
Name: python-module-%oname
Version: 1.9.1.3
Release: alt1.dev0.git20140923
Summary: jQuery integration for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.jquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.jquery.git
# branch: 1.9
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
%py_requires plone.app Products.CMFCore Products.GenericSetup

%description
plone.app.jquery adds jquery library to Plone.

Included is the jQuery migration plugin. You can install it by importing
the development profile.

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
%doc *.rst
%python_sitelibdir/*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1.3-alt1.dev0.git20140923
- Initial build for Sisyphus

