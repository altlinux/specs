%define mname yafowil
%define oname %mname.plone
Name: python-module-%oname
Version: 2.2
Release: alt1.dev0.git20140604
Summary: Plone Integration with YAFOWIL
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yafowil.plone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/yafowil.plone.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-%mname-tests
BuildPreReq: python-module-Zope2-tests python-module-yaml
BuildPreReq: python-module-interlude
BuildPreReq: python-module-Plone
BuildPreReq: python-module-yafowil
BuildPreReq: python-module-yafowil.yaml
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-openid python-module-unittest2
BuildPreReq: python-module-Products.TinyMCE

%py_provides %oname
%py_requires %mname Plone yafowil.yaml collective.js.jqueryui

%description
Addon widgets may provide custom javascripts, CSS, images and so on.

This package registers the directories containing these assets as
resource directories. Thus they can be accessed from the webbrowser. The
registration schema is ++resource++MODULENAME/....

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.dev0.git20140604
- Initial build for Sisyphus

