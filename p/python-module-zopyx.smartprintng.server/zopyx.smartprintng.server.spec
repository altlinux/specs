%define mname zopyx.smartprintng
%define oname %mname.server

%def_disable check

Name: python-module-%oname
Version: 1.1.2
Release: alt1.git20121105
Summary: ZOPYX SmartPrintNG Server
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zopyx.smartprintng.server/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopyx/zopyx.smartprintng.server.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-PasteScript python-module-pyramid-tests
BuildPreReq: python-module-pyramid_zcml python-module-pyramid_xmlrpc
BuildPreReq: python-module-uuid python-module-transaction
BuildPreReq: python-module-nose
BuildPreReq: python-module-zopyx.convert2
BuildPreReq: python-module-zope.sendmail
BuildPreReq: python-module-zope.configuration

%py_provides %oname
%py_requires %mname paste.script pyramid_zcml pyramid_xmlrpc uuid
%py_requires zopyx.convert2 zope.sendmail transaction

%description
zopyx.smartprintng.server is a Pyramid based server implementation and
implements the server side functionality of the Produce & Publish
platform. It is know as the Produce & Publish Server.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires nose zope.configuration pyramid.testing
%add_python_req_skip models

%description tests
zopyx.smartprintng.server is a Pyramid based server implementation and
implements the server side functionality of the Produce & Publish
platform. It is know as the Produce & Publish Server.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/zopyx/smartprintng
cp -fR zopyx/smartprintng/server \
	%buildroot%python_sitelibdir/zopyx/smartprintng/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc docs/source/*.rst
%python_sitelibdir/zopyx/smartprintng/server
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zopyx/smartprintng/server/test*

%files tests
%python_sitelibdir/zopyx/smartprintng/server/test*

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20121105
- Initial build for Sisyphus

