%define module_name tornado

%def_with python3

Name: python-module-%module_name
Version: 2.1.1
Release: alt1.1
Summary: Scalable, non-blocking web server and tools

License: Apache
Group: Development/Python
Url: http://www.tornadoweb.org

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif
Requires: python-module-simplejson
Requires: ca-certificates

%description
Tornado is an open source version of the scalable, non-blocking web
server and tools.

The framework is distinct from most mainstream web server frameworks
(and certainly most Python frameworks) because it is non-blocking and
reasonably fast. Because it is non-blocking and uses epoll, it can
handle thousands of simultaneous standing connections, which means it is
ideal for real-time web services.

%if_with python3
%package -n python3-module-%module_name
Summary: Scalable, non-blocking web server and tools (Python 3)
Group: Development/Python3
Requires: ca-certificates
%add_python3_req_skip MySQLdb pycurl

%description -n python3-module-%module_name
Tornado is an open source version of the scalable, non-blocking web
server and tools.

The framework is distinct from most mainstream web server frameworks
(and certainly most Python frameworks) because it is non-blocking and
reasonably fast. Because it is non-blocking and uses epoll, it can
handle thousands of simultaneous standing connections, which means it is
ideal for real-time web services.
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
%python3_build
popd
%endif

%install
%python_install
pushd %buildroot%python_sitelibdir/%module_name
rm -rf ca-certificates.crt
ln -sf /usr/share/ca-certificates/ca-bundle.crt ca-certificates.crt
popd

%if_with python3
pushd ../python3
%python3_install
pushd %buildroot%python3_sitelibdir/%module_name
rm -rf ca-certificates.crt
ln -sf /usr/share/ca-certificates/ca-bundle.crt ca-certificates.crt
popd
%endif

%files
%python_sitelibdir/%module_name
%exclude %python_sitelibdir/*.egg-*

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.egg-*
%endif

%changelog
* Fri Jun 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.1
- Added module for Python 3

* Wed Nov 23 2011 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- initial build for ALT Linux Sisyphus

