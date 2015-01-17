%define mname quintagroup
%define oname %mname.theme.sunrain
Name: python-module-%oname
Version: 6.5
Release: alt1.git20141229
Summary: Free Diazo Theme for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/quintagroup.theme.sunrain/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/quintagroup/quintagroup.theme.sunrain.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-initgroups
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-plone.app.theming
BuildPreReq: python-module-plone.app.themingplugins
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-%mname.theme = %EVR
%py_requires plone.app.theming plone.app.themingplugins
%py_requires zope.i18nmessageid

%description
SunRain free responsive diazo theme for Plone.

%package -n python-module-%mname.theme
Summary: Core files of %mname.theme
Group: Development/Python
%py_provides %mname.theme
Requires: python-module-%mname = %EVR

%description -n python-module-%mname.theme
Core files of %mname.theme.

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
install -p -m644 %mname/theme/__init__.py \
	%buildroot%python_sitelibdir/%mname/theme/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/theme/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/theme/__init__.py*

%files -n python-module-%mname.theme
%dir %python_sitelibdir/%mname/theme
%python_sitelibdir/%mname/theme/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5-alt1.git20141229
- Initial build for Sisyphus

