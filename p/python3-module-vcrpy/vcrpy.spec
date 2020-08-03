%define oname vcrpy

%def_disable check

Name: python3-module-%oname
Version: 1.2.0
Release: alt2.git20150108
Summary: Automatically mock your HTTP interactions to simplify and speed up testing
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/vcrpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kevin1024/vcrpy.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-contextlib2 python3-module-html5lib python3-module-pbr python3-module-pytest-localserver python3-module-setuptools python3-module-unittest2 python3-module-wrapt python3-module-yaml rpm-build-python3

%py3_provides vcr
%py3_requires requests.packages
%add_python3_req_skip requests.packages.urllib3.connectionpool

%description
Automatically mock your HTTP interactions to simplify and speed up
testing.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Sat Aug 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2.git20150108
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1.git20150108.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20150108.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20150108.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150108
- Version 1.2.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141103
- Initial build for Sisyphus

