%define mname ztfy
%define oname %mname.media
Name: python-module-%oname
Version: 0.1.8
Release: alt1
Summary: ZTFY medias handling package
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.media/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-ZODB3
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.file
BuildPreReq: python-module-zope.app.publication
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.processlifetime
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-ztfy.extfile
BuildPreReq: python-module-ztfy.file
BuildPreReq: python-module-ztfy.jqueryui
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-ztfy.zmq
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: kino %_bindir/ffmpeg-kino
%py_requires %mname fanstatic zope.annotation zope.app.file zope.event
%py_requires zope.app.publication zope.component zope.container zmq
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent ZODB3
%py_requires zope.location zope.processlifetime zope.schema zope.site
%py_requires zope.traversing z3c.template z3c.form ztfy.extfile ztfy.zmq
%py_requires ztfy.file ztfy.jqueryui ztfy.skin ztfy.utils

%description
ztfy.media is a ZTK/ZopeApp ZTFY package used to automatically convert
and display medias files (audios, videos...).

It was developed in the context of a medias library management
application handling several kinds of medias (mainly images, videos, and
audio files), to be able to automatically display these contents in web
pages.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ztfy.media is a ZTK/ZopeApp ZTFY package used to automatically convert
and display medias files (audios, videos...).

It was developed in the context of a medias library management
application handling several kinds of medias (mainly images, videos, and
audio files), to be able to automatically display these contents in web
pages.

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
* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1
- Initial build for Sisyphus

