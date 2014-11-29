%define mname ftw
%define oname %mname.colorbox
Name: python-module-%oname
Version: 1.2.1
Release: alt1.dev0.git20140923
Summary: An image gallery for Plone using ColorBox
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.colorbox/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.colorbox.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.registry zope.component zope.i18n zope.schema
%py_requires zope.interface zope.i18nmessageid

%description
ColorBox is a lightweight customizable lightbox plugin for jQuery.
More information about ColorBox can be found here:
http://jacklmoore.com/colorbox/

ftw.colorbox adds a new view called colorbox_view for folders and topics
which integrates ColorBox in Plone.

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

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.dev0.git20140923
- Initial build for Sisyphus

