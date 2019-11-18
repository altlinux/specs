%define oname jsonm

Name: python3-module-%oname
Version: 1.0.11
Release: alt2

Summary: Python object to (json + redis)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/jsonm/
# https://github.com/dantezhu/jsonm.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires json


%description
Python object to (json + redis).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md examples
%python3_sitelibdir/*


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.11-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.11-alt1.git20150126.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.11-alt1.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.11-alt1.git20150126.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11-alt1.git20150126
- Version 1.0.11

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150122
- Initial build for Sisyphus

