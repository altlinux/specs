%define oname tlslite

%def_without python3

Name: python-module-%oname
Version: 0.4.9
Release: alt1

Summary: Python library that implements TLS/SSL

License: Public domain
Group: Development/Python
Url: http://trevp.net/tlslite/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://trevp.net/tlslite/%oname-%version.tar.bz2

%setup_python_module %oname
BuildPreReq: /proc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python-devel python-module-setuptools-tests
%endif

%py_provides %oname

%description
TLS Lite is a free python library that implements SSL 3.0, TLS 1.0, and
TLS 1.1. TLS Lite supports non-traditional authentication methods such as
SRP, shared keys, and cryptoIDs in addition to X.509 certificates. TLS
Lite is pure Python, however it can access OpenSSL, cryptlib, pycrypto,
and GMPY for faster crypto operations. TLS Lite integrates with httplib,
xmlrpclib, poplib, imaplib, smtplib, SocketServer, asyncore, and Twisted.

%if_with python3
%package -n python3-module-%oname
Summary: Python library that implements TLS/SSL
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
TLS Lite is a free python library that implements SSL 3.0, TLS 1.0, and
TLS 1.1. TLS Lite supports non-traditional authentication methods such as
SRP, shared keys, and cryptoIDs in addition to X.509 certificates. TLS
Lite is pure Python, however it can access OpenSSL, cryptlib, pycrypto,
and GMPY for faster crypto operations. TLS Lite integrates with httplib,
xmlrpclib, poplib, imaplib, smtplib, SocketServer, asyncore, and Twisted.
%endif

%prep
%setup -n %oname-%version

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
	mv $i ${i}3
done
popd
%endif

%python_install

%check
export PYTHONPATH=$PWD
pushd tests
./httpsserver.sh &
sleep 1
python httpsclient.py
popd
killall -9 httpsserver.sh
killall -9 python
%if_with python3
pushd ../python3/tests
export PYTHONPATH=$PWD/..
sed -i 's|python|python3|' httpsserver.sh
./httpsserver.sh &
sleep 1
python3 httpsclient.py
popd
killall -9 httpsserver.sh
killall -9 python3
%endif

%files
%doc README
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1
- Version 0.4.9
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.8-alt2.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.8-alt2.1
- Rebuilt with python 2.6

* Sat Feb 21 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.8-alt2
- cleanup spec, fix build on x86_64 (thanks to Dmitry Levin)

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.8-alt1
- initial build for ALT Linux Sisyphus
