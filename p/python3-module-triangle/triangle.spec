%define oname triangle

%def_with check

Name: python3-module-%oname
Version: 2022.02.02
Release: alt1

Summary: Python wrapper for libtriangle

License: LGPL-3.0
Group: Development/Python3
Url: https://rufat.be/triangle/
Vcs: https://github.com/drufat/triangle.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-numpy
BuildRequires: python3-module-pytest
%endif

%description
Python Triangle is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator
library.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v tests

%files
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Wed May 03 2023 Anton Vyatkin <toni@altlinux.org> 2022.02.02-alt1
- New version 2022.02.02

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 2017.04.29-alt2
- build python3 module

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.04.29-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2017.04.29-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.04.29-alt1
- Updated to upstream version 20170429.
- Updated build dependencies.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2013.04.05-alt1.git20141030.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2013.04.05-alt1.git20141030.1
- NMU: Use buildreq for BR.

* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.04.05-alt1.git20141030
- Initial build for Sisyphus

