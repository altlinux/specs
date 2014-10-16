%define mname plonetheme
%define oname %mname.barceloneta

Name: python-module-%oname
Version: 1.6.0
Release: alt2.git20141009
Summary: The default theme for Plone 5
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plonetheme.barceloneta/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plonetheme.barceloneta.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.theming
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-unittest2

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.app.theming

%description
The default theme for Plone 5.

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
%doc *.txt *.html *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt2.git20141009
- Enabled testing

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20141009
- Initial build for Sisyphus

