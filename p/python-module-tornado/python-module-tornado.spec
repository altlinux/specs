%define module_name tornado

%def_with python3

Name: python-module-%module_name
Version: 4.4.2
Release: alt2
Summary: Scalable, non-blocking web server and tools

License: Apache
Group: Development/Python
Url: http://www.tornadoweb.org

# https://github.com/tornadoweb/tornado.git
Source: %name-%version.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: ca-certificates elfutils python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-devel python3-module-setuptools rpm-build-python3

#BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
%endif
Requires: python-module-simplejson
Requires: ca-certificates
# required by tornado/netutil.py for Python2 version.
Requires: python-module-backports.ssl_match_hostname python-module-certifi
# required by tornado/gen.py
Requires: python-module-singledispatch
# required by tornado/gen.py
Requires: python-module-backports_abc

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
Requires: ca-certificates python3-module-certifi
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
# remove shebang from files
sed -i.orig -e '/^#!\//, 1d' *py tornado/*.py tornado/*/*.py

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
%python_sitelibdir/*.egg-*

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/*
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Mon Nov 21 2016 Lenar Shakirov <snejok@altlinux.ru> 4.4.2-alt2
- Requires: python-module-certifi added

* Tue Oct 18 2016 Vladimir Didenko <cow@altlinux.org> 4.4.2-alt1
- update version
- update requires for Python 2 version

* Thu Sep 08 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 4.4.1-alt1.1.1
- (NMU) update version

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.1-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.2.1-alt1.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Dec 1 2014 Vladimir Didenko (REAL) <cow@altlinux.org> 4.0.2-alt2
- Add dependency to python-module-backports.ssl_match_hostname

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Sat Mar 02 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Fri Jun 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.1
- Added module for Python 3

* Wed Nov 23 2011 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- initial build for ALT Linux Sisyphus
