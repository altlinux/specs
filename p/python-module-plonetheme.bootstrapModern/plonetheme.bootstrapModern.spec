%define mname plonetheme
%define oname %mname.bootstrapModern
Name: python-module-%oname
Version: 0.46
Release: alt2
Summary: An installable theme for Plone 4
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plonetheme.bootstrapModern/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-PasteScript
BuildPreReq: python-module-plone.app.z3cform python-module-unittest2
BuildPreReq: python-module-zLOG python-module-initgroups
BuildPreReq: python-module-Zope2-tests python-module-nose
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
%py_requires %mname plone.app.z3cform

%description
An installable theme for Plone 4.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-Zope2-tests
%py_requires zope.component.testing zope.security.testing
%py_requires Products.PloneTestCase

%description tests
An installable theme for Plone 4.

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

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%check
python setup.py test
nosetests

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.46-alt2
- Applied python-module-plonetheme.bootstrapModern-0.46-alt1.diff

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.46-alt1
- Initial build for Sisyphus

