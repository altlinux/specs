%define oname triangle

Name: python3-module-%oname
Version: 2017.04.29
Release: alt2

Summary: Python wrapper for libtriangle

License: LGPL
Group: Development/Python
Url: http://dzhelil.info/triangle/

# https://github.com/drufat/triangle.git
Source: %name-%version.tar
Patch1: %oname-alt-docs.patch
Patch2: %oname-alt-reqs.patch

#BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: libtriangle-devel

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Cython libnumpy-py3-devel
BuildRequires: python3-module-nose
BuildRequires: python3-module-notebook python3-module-numpy-testing

%description
Python Triangle is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator
library.

%prep
%setup
%patch1 -p1

#prepare_sphinx3 .
#ln -s ../objects.inv doc/

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%check
%if_with python3
python3 setup.py build_ext -i
nosetests3 -v
%endif

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
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

