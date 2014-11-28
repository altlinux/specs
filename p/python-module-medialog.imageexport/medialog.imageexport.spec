%define mname medialog
%define oname %mname.imageexport
Name: python-module-%oname
Version: 0.4
Release: alt1.git20141127
Summary: Export all images (or a scale) from a folder
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/medialog.imageexport/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/espenmn/medialog.imageexport.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires Products.CMFPlone Products.PythonScripts Products.CMFCore
%py_requires plone.namedfile plone.dexterity zope.interface zope.schema
%py_requires zope.component zope.app.component zope.i18nmessageid

%description
Adds a browser view to export all images from a folder as a zip file.

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
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141127
- Initial build for Sisyphus

