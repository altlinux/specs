%define oname jsonrpcclient

Name: python3-module-%oname
Version: 2.5.2
Release: alt3

Summary: JSON-RPC 2.0 client library for Python 3
License: LGPL
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/jsonrpcclient/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest python3-module-mock
BuildRequires: python3-module-jsonschema python3(future)
BuildRequires: python3-module-requests
BuildRequires: python3(zmq) python3(tornado)
BuildRequires: python3-module-responses python3(testfixtures)

%description
JSON-RPC 2.0 client library for Python 3.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py build_ext -i
rm -fR build
PYTHONPATH=%buildroot%python3_sitelibdir py.test3

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2.5.2-alt3
- fix build (add missed mock buildrequires)

* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.5.2-alt2
- Build for python2 removed.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.2-alt1
- Updated to upstream version 2.5.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 1.1.2-alt2
- Rebuild into Sisyphus

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.12-alt1
- Version 1.0.12

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1
- Version 1.0.10

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1
- Version 1.0.7

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus

