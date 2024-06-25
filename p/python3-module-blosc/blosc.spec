%define _unpackaged_files_terminate_build 1
%define oname blosc

%def_with check
%def_without docs

Name: python3-module-%oname
Version: 1.11.2
Release: alt1

Summary: A Python wrapper for the extremely fast Blosc compression library
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/blosc
Vcs: https://github.com/Blosc/python-blosc.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: libblosc-devel
BuildRequires: python3-module-scikit-build
%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-numpydoc
%endif
%if_with check
BuildRequires: python3-module-numpy-testing
%endif

%py3_provides %oname


%description
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

This package contains tests for %oname.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

This package contains pickles for %oname.
%endif

%prep
%setup
rm -rf blosc/c-blosc

sed -i "s|.*blosc.test.*||" blosc/__init__.py

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile
%endif

%build
export USE_SYSTEM_BLOSC=1
%pyproject_build

%install
%pyproject_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m blosc.test

%files
%doc *.rst
%if_with docs
%doc doc/_build/html
%endif
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%if_with docs
%exclude %python3_sitelibdir/*/pickle
%endif
%exclude %python3_sitelibdir/*/test*

%files tests
%python3_sitelibdir/*/test*

%if_with docs
%files pickles
%python3_sitelibdir/*/pickle
%endif


%changelog
* Tue Jun 25 2024 Anton Vyatkin <toni@altlinux.org> 1.11.2-alt1
- New version 1.11.2.

* Fri Oct 13 2023 Anton Vyatkin <toni@altlinux.org> 1.11.1-alt1
- New version 1.11.1.

* Thu Dec 09 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt5
- Build without docs for python3.10.

* Mon Nov 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt4
- NMU: disable tests packing, fix build

* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.5.1-alt3
- build for python2 disabled

* Tue May 08 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt2
- fixed build on non-x86

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.1-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.1-alt1
- Updated to upstream version 1.5.1.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.6-alt1.dev.git20150415.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt1.dev.git20150415.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.dev.git20150415
- Initial build for Sisyphus

