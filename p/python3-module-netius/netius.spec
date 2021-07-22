%define oname netius

Name: python3-module-%oname
Version: 1.17.52
Release: alt2

Summary: Fast and readable async non-blocking network apps

License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/netius/

# https://github.com/hivesolutions/netius.git
# Source-url: https://pypi.io/packages/source/n/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
%py3_provides %oname

%description
Netius is a Python network library that can be used for the rapid
creation of asynchronous non-blocking servers and clients. It has no
dependencies, it's cross-platform, and brings some sample netius-powered
servers out of the box, namely a production-ready WSGI server.

%package tests
Summary: Tests and examples for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description tests
Netius is a Python network library that can be used for the rapid
creation of asynchronous non-blocking servers and clients. It has no
dependencies, it's cross-platform, and brings some sample netius-powered
servers out of the box, namely a production-ready WSGI server.

This package contains tests and examples for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test
%exclude %python3_sitelibdir/*/examples

%files tests
%python3_sitelibdir/*/test
%python3_sitelibdir/*/examples

%changelog
* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.17.52-alt2
- Rename package, cleanup spec.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.17.52-alt1
- new version 1.17.52 (with rpmrb script)
- python3 only

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.3-alt1.git20150202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.3-alt1.git20150202.1
- NMU: Use buildreq for BR.

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt1.git20150202
- Initial build for Sisyphus

