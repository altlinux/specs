%define oname geocodertools

Name: python3-module-%oname
Version: 0.1.4
Release: alt2

Summary: Geo coordinates, reverse geo coding and getting city names out of coordinates
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/geocodertools/
BuildArch: noarch

# https://github.com/MartinThoma/geocodertools.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage python3-module-nose

%py3_provides %oname
%py3_requires logging msgpack


%description
Functions to work with Geo coordinates, reverse geo coding and getting
city names out of coordinates without internet.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
sed -i 's|nosetests|nosetests3|' Makefile
%make test

%files
%doc *.md docs/source/*.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt1.git20150322.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150322.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.git20150322.1
- NMU: Use buildreq for BR.

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150322
- Initial build for Sisyphus

