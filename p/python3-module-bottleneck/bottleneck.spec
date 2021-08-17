%define oname bottleneck

Name: python3-module-%oname
Version: 1.2.1
Release: alt5

Summary: Fast NumPy array functions written in Cython
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Bottleneck/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3

BuildRequires: python3-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-sphinx

%description
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%package tests
Summary: Tests for Bottleneck
Group: Development/Python3
Requires: %name = %EVR

%description tests
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains tests for Bottleneck.

%prep
%setup

for i in $(find %oname -type d); do
	touch $i/__init__.py
done

%prepare_sphinx3 doc
ln -s ../objects.inv doc/source/

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install
%python3_prune

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt5
- drop BR: python3-module-numpy-testing

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt4
- drop BR: libnumpy-devel

* Sat Oct 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt3
- NMU: build python3 module separately
- NMU: disable tests packaging

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.1-alt2
- Fixed build with numpy.

* Tue Apr 09 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Build new version for python3.7.
- Removed docs and pickles.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

