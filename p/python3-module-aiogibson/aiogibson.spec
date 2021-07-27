%define oname aiogibson

%def_disable check

Name: python3-module-%oname
Version: 0.1.3
Release: alt1.git20150210.2
Summary: asyncio (PEP 3156) Gibson cache support
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/aiogibson/

# https://github.com/jettify/aiogibson.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires asyncio

BuildRequires: python3-module-coverage python3-module-flake8 python3-module-nose

%description
aiogibson is a library for accessing a gibson cache database from the
asyncio (PEP-3156/tulip) framework.

%prep
%setup

sed -i 's|flake8|python3-flake8|' Makefile
sed -i 's|nosetests|nosetests3|' Makefile

%build
%python3_build

%install
%python3_install

rm -f requirements.txt

%check
python3 setup.py test
%make test FLAGS=-v

%files
%doc *.txt *.rst docs/*.rst examples
%python3_sitelibdir/*

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.3-alt1.git20150210.2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.3-alt1.git20150210.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.git20150210.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1.git20150210.1
- NMU: Use buildreq for BR.

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150210
- Version 0.1.3

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150101
- Initial build for Sisyphus

