%define oname gevent-websocket

%def_with python3

Name: python-module-%oname
Version: 0.3.6
Release: alt1.hg20120423
Summary: Websocket handler for the gevent pywsgi server, a Python network library
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/gevent-websocket/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/Jeffrey/gevent-websocket
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires gevent greenlet

%description
gevent-websocket is a websocket library for the gevent networking
library.

%if_with python3
%package -n python3-module-%oname
Summary: Websocket handler for the gevent pywsgi server, a Python 3 network library
Group: Development/Python3
%py3_provides %oname
%py3_requires gevent greenlet

%description -n python3-module-%oname
gevent-websocket is a websocket library for the gevent networking
library.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc LICENSE README.rst AUTHORS CHANGELOG
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst AUTHORS CHANGELOG
%python3_sitelibdir/*
%endif

%changelog
* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.hg20120423
- Version 0.3.6
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.3-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus

