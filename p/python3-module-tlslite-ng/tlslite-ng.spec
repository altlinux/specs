%define _unpackaged_files_terminate_build 1

%define mname tlslite
%define oname %mname-ng

Name: python3-module-%oname
Version: 0.7.5
Release: alt2

Summary: Pure python implementation of SSL and TLS
License: BSD & LGPLv2
Group: Development/Python3
Url: https://pypi.org/project/tlslite-ng/

BuildArch: noarch

# https://github.com/tomato42/tlslite-ng.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx
BuildRequires: python3(ecdsa)

Conflicts: python3-module-%mname < %EVR
Provides: python3-module-%mname = %EVR

%description
tlslite-ng is a pure python implementation of SSLv3.0, TLS 1.0, TLS 1.1
and TLS 1.2 protocols.

It can use pycrypto, m2crypto and gmp for acceleration of cryptographic
operations but is not dependant upon them.

tlslite-ng aims to be a drop-in replacement for tlslite while providing
more comprehensive set of features and more secure defautls.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
tlslite-ng is a pure python implementation of SSLv3.0, TLS 1.0, TLS 1.1
and TLS 1.2 protocols.

It can use pycrypto, m2crypto and gmp for acceleration of cryptographic
operations but is not dependant upon them.

tlslite-ng aims to be a drop-in replacement for tlslite while providing
more comprehensive set of features and more secure defautls.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|&-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

%make docs

%check
%if 0
pushd tests/
export PYTHONPATH=$PWD/..
sed -i 's|python|python3|' httpsserver.sh
./httpsserver.sh &
sleep 1
%__python3 httpsclient.py
popd
killall -9 httpsserver.sh
killall -9 python3
%__python3 -m unittest discover -v
%endif

%files
%doc LICENSE README*
%_bindir/*
%python3_sitelibdir/*

%files docs
%doc docs/*

%changelog
* Wed Apr 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.5-alt2
- Build for python2 disabled.

* Mon Sep 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.5-alt1
- Updated to upstream version 0.7.5.
- Built modules for python3.

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.5.0-alt2.beta4.git20150724
- cleanup buildreq

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.beta4.git20150724
- Initial build for Sisyphus

