%define oname aiomcache

%def_disable check

Name: python3-module-%oname
Version: 0.1
Release: alt2.git20140713
Summary: memcached client for asyncio
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/aiomcache/

# https://github.com/aio-libs/aiomcache.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires asyncio

BuildRequires: python3-module-nose python3-module-pytest

%description
asyncio (PEP 3156) library to work with memcached.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test
%__python3 runtests.py -v
%__python3 examples/simple.py

%files
%doc *.txt *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.1-alt2.git20140713
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt1.git20140713.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20140713.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20140713.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140713
- Initial build for Sisyphus

