%define oname gevent_socketio2
Name: python-module-%oname
Version: 0.2.7
Release: alt1.git20141124
Summary: A gevent implementation for socketio protocol 1.0
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/gevent_socketio2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/shuoli84/gevent_socketio2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-greenlet python-module-webob
BuildPreReq: python-module-gevent-websocket python-module-pyee
BuildPreReq: python-module-requests python-module-ws4py

%py_provides socketio
%py_provides socketio_client
Conflicts: python-module-gevent-socketio
%py_requires geventwebsocket greenlet webob pyee ws4py

%description
We love socketio, implements socketio 0.7, this project intend to bring
socketio 1.0 to python(gevent) world. It started as a fork of
gevent_socketio. This project mainly is a port of socketiojs project, so
you can see EventEmitter in code. Some code not that clean due to the
port, which needs further refine.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
We love socketio, implements socketio 0.7, this project intend to bring
socketio 1.0 to python(gevent) world. It started as a fork of
gevent_socketio. This project mainly is a port of socketiojs project, so
you can see EventEmitter in code. Some code not that clean due to the
port, which needs further refine.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

cp -fR socketio_client %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc AUTHORS NOTES *.md docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test.*

%files tests
%python_sitelibdir/*/*/test.*

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt1.git20141124
- Version 0.2.7

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20141112
- Version 0.2.5

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20141111
- Version 0.2.3

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141110
- New snapshot

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141031
- Version 0.2.0

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20141027
- Initial build for Sisyphus

