%define oname affinegap

Name: python3-module-%oname
Version: 1.11
Release: alt1

Summary: A Cython implementation of the affine gap string distance

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/affinegap/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Cython

%description
A Cython implementation of the affine gap penalty string distance also
known as the Smith-Waterman algorithm.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
#python3 setup.py test build_ext -i
#nosetests3 -v

%files
%python3_sitelibdir/*

%changelog
* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- new version 1.11 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt3
- build python3 module separately

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10-alt2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10-alt2
- Updated build dependencies

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.git20150304.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt1.git20150304.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150304
- Version 1.1

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141119
- Initial build for Sisyphus

