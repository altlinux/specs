%define oname smmap

Name: python3-module-%oname
Version: 5.0.0
Release: alt1

Summary:  Sliding window memory map manager

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/smmap

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-coverage python3-module-nosexcover

%description
A pure python implementation of a sliding window memory map manager

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A pure python implementation of a sliding window memory map manager

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
python3 setup.py test

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- new version 5.0.0 (with rpmrb script)

* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version (4.0.0) with rpmgs script
- build python3 module separately
- switch to build from tarball

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt2
- NMU: remove %ubt from release

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.3-alt1%ubt
- Updated to upstream version 2.0.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1.git20150107.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.git20150107.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150107.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150107
- Version 0.9.0

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20141113
- Version 0.8.3

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20140714
- New snapshot
- Added module for Python 3

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1
- initial
