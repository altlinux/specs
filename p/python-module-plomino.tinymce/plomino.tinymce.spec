%define mname plomino
%define oname %mname.tinymce
Name: python-module-%oname
Version: 0.7.3
Release: alt2.git20140509
Summary: TinyMCE Plomino Embedded Plugin
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plomino.tinymce/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plomino/plomino.tinymce.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.TinyMCE
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFPlomino

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires Products.TinyMCE zope.component zope.interface
%py_requires Products.CMFPlomino

%description
Plomino TinyMCE Integration is a plugin for Plomino which allows to
manage easily Plomino objects (fields, actions and hidewhen) from
TinyMCE interface.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Plomino TinyMCE Integration is a plugin for Plomino which allows to
manage easily Plomino objects (fields, actions and hidewhen) from
TinyMCE interface.

This package contains tests for %oname.

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

touch \
	%buildroot%python_sitelibdir/%mname/tinymce/tests_windmill/__init__.py
install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt2.git20140509
- Added necessary requirements

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.git20140509
- Initial build for Sisyphus

