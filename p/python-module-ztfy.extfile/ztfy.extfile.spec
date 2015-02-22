%define mname ztfy
%define oname %mname.extfile

Name: python-module-%oname
Version: 0.2.14
Release: alt2
Summary: ZTFY package used to handle external files storage in Zope3
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.extfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-paramiko
BuildPreReq: python-module-libmagic python-module-pytz
BuildPreReq: python-module-ZODB3
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-hurry.query
BuildPreReq: python-module-zc.catalog
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.app.file
BuildPreReq: python-module-zope.app.generations
BuildPreReq: python-module-zope.app.publication
BuildPreReq: python-module-zope.catalog
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.processlifetime
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-ztfy.file

%py_provides %oname
Requires: python-module-libmagic
%py_requires %mname ztfy.utils fanstatic hurry.query paramiko pytz ZODB3
%py_requires zc.catalog zope.annotation zope.app.component zope.app.file
%py_requires zope.app.generations zope.app.publication zope.catalog
%py_requires zope.component zope.configuration zope.container zope.event
%py_requires zope.dublincore zope.interface zope.intid zope.location
%py_requires zope.lifecycleevent zope.processlifetime zope.schema

%description
ztfy.extfile is a package which allows storing File and Image objects
data outside of the Zope database (ZODB), into 'external' files. Files
can be stored in the local file system, or remotely via protocols like
SFTP or NFS (even HTTP is possible) ; an efficient cache system allows
to store local copies of the remote files locally.

Finally, external files can be stored via Blob objects, provided by the
latest versions of the ZODB.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing
%py_requires ztfy.file

%description tests
ztfy.extfile is a package which allows storing File and Image objects
data outside of the Zope database (ZODB), into 'external' files. Files
can be stored in the local file system, or remotely via protocols like
SFTP or NFS (even HTTP is possible) ; an efficient cache system allows
to store local copies of the remote files locally.

Finally, external files can be stored via Blob objects, provided by the
latest versions of the ZODB.

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

%files
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.14-alt2
- Added necessary requirements
- Enabled testing

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.14-alt1
- Initial build for Sisyphus

