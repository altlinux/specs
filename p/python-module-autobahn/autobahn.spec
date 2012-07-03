%define oname autobahn

%def_with python3

Name: python-module-%oname
Version: 0.5.1
Release: alt1.git20120523
Summary: WebSocket & WAMP for Python/Twisted
License: Apache License 2.0
Group: Development/Python
Url: https://github.com/tavendo/AutobahnPython
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tavendo/AutobahnPython.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.

%package pickles
Summary: Pickles for Autobahn
Group: Development/Python

%description pickles
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.

This package contains pickles for Autobahn.

%package docs
Summary: Documentation and examples for Autobahn
Group: Development/Documentation

%description docs
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.

This package contains documentation and examples for Autobahn.

%if_with python3
%package -n python3-module-%oname
Summary: WebSocket & WAMP for Python3/Twisted
Group: Development/Python3

%description -n python3-module-%oname
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/python/

%build
pushd %oname
%python_build_debug
popd

%if_with python3
pushd ../python3/%oname
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build_debug
popd
%endif

pushd doc/python
%make pickle
%make html
popd

%install
pushd %oname
%python_install
popd

cp -fR doc/python/_build/pickle \
	%buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3/%oname
%python3_install
popd
%endif

%files
%doc README* doc/rfc
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/python/_build/html examples

%if_with python3
%files -n python3-module-%oname
%doc README* doc/rfc
%python3_sitelibdir/*
%endif

%changelog
* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20120523
- Initial build for Sisyphus

