%define sname restkit

%def_with python3
%def_disable check

Summary: Restkit is an HTTP resource kit for Python
Name: python-module-%sname
Version: 4.2.2
Release: alt2.git20140731.1
# http://github.com/benoitc/restkit
Source0: %name-%version.tar
#Source0: http://pypi.python.org/packages/source/r/%sname/%sname-%version.tar.gz
License: BSD
Group: Development/Python
URL: http://pypi.python.org/pypi/restkit
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

#add_python_req_skip eventlet

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-http-parser python-module-socketpool
#BuildPreReq: python-module-nose python-module-webob

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-http-parser python3-module-socketpool
#BuildPreReq: python-tools-2to3 python3-module-nose python3-module-webob
%endif

%py_requires http_parser socketpool

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-enum34 python-module-pyasn1 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-enum34 python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-cryptography python-module-dns python-module-greenlet python-module-nose python-module-psycopg2 python-module-pytest python-modules-wsgiref python3-module-cryptography python3-module-dns python3-module-greenlet python3-module-nose python3-module-psycopg2 python3-module-pytest rpm-build-python3 time

%description
Restkit is an HTTP resource kit for Python. 
It allows you to easily access to HTTP resource and build objects around it. 
It's the base of couchdbkit a Python CouchDB framework.

%package -n python3-module-%sname
Summary: Restkit is an HTTP resource kit for Python
Group: Development/Python3
%py3_requires http_parser socketpool

%description -n python3-module-%sname
Restkit is an HTTP resource kit for Python. 
It allows you to easily access to HTTP resource and build objects around it. 
It's the base of couchdbkit a Python CouchDB framework.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

rm -f doc/NOTICE

%check
python setup.py test

%files
%doc README.rst THANKS LICENSE NOTICE examples/* doc/*
%_bindir/restcli
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%sname
%python_sitelibdir/%sname-%version-py*.egg-info

%if_with python3
%files -n python3-module-%sname
%doc README.rst THANKS LICENSE NOTICE examples/* doc/*
%_bindir/*.py3
%python3_sitelibdir/%sname
%python3_sitelibdir/%sname-%version-py*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.2.2-alt2.git20140731.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt2.git20140731
- Added necessary requirements

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1.git20140731
- Version 4.2.2

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.1-alt1.1
- Rebuild with Python-2.7

* Tue Nov 30 2010 Mikhail Pokidko <pma@altlinux.org> 2.3.1-alt1
- v2.3.1

* Mon Sep 20 2010 Mikhail Pokidko <pma@altlinux.org> 2.2.1-alt1
- Version up.

* Wed Aug 04 2010 Mikhail Pokidko <pma@altlinux.org> 2.1.0-alt1
- initial build


