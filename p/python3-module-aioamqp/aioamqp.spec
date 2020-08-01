%define oname aioamqp

Name: python3-module-%oname
Version: 0.13.0
Release: alt2

Summary: AMQP implementation using asyncio

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/aioamqp/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Polyconseil/aioamqp.git
# Source-url: https://pypi.io/packages/source/a/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pamqp
BuildRequires: pylint-py3 python3-module-coverage python3-module-nose python3-module-setuptools rpm-build-python3

%py3_provides %oname
%py3_requires asyncio

%description
aioamqp library is a pure-Python implementation of the AMQP 0.9.1
protocol.

Built on top on Python's asynchronous I/O support introduced in PEP
3156, it provides an API based on coroutines, making it easy to write
highly concurrent applications.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst docs/*.rst examples
%python3_sitelibdir/*

%changelog
* Sat Aug 01 2020 Grigory Ustinov <grenka@altlinux.org> 0.13.0-alt2
- Drop python2 support.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20141217.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1.git20141217.1
- NMU: Use buildreq for BR.

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141217
- Initial build for Sisyphus

