%define _unpackaged_files_terminate_build 1

%define oname shapely

%def_without check
# Need module numpydoc and bootstrapped package
%def_without doc

Name: python3-module-%oname
Version: 2.0.1
Release: alt1

Summary: Planar geometries, predicates, and operations
License: BSD
Group: Development/Python3

Url: http://pypi.python.org/pypi/Shapely
# https://github.com/Toblerity/Shapely.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx3
BuildRequires: libgeos-devel
BuildRequires: python3-module-Cython libnumpy-py3-devel
BuildRequires: python3-module-descartes
BuildRequires: python3-module-packaging
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy-testing
BuildRequires: xvfb-run
%if_with doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinxcontrib-websupport
BuildRequires: python3(matplotlib.sphinxext)
BuildRequires: %name = %version
%endif

%description
Planar geometries, predicates, and operations.

%package examples
Summary: Examples for %oname
Group: Development/Python3
Requires: %name = %EVR

%description examples
Planar geometries, predicates, and operations.

This package contains examples for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3
%add_python3_req_skip figures

%description pickles
Planar geometries, predicates, and operations.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Planar geometries, predicates, and operations.

This package contains documentation for %oname.

%prep
%setup

%if_with doc
%prepare_sphinx3 .
ln -s ../objects.inv docs/
sed -i 's/sphinx-apidoc/sphinx-apidoc-3/' docs/Makefile
%endif

%build
export LC_ALL=en_US.UTF-8
%add_optflags -fno-strict-aliasing

%python3_build

%install
export LC_ALL=en_US.UTF-8

%python3_install

%if_with doc
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%if_with check
%check
export LC_ALL=en_US.UTF-8

xvfb-run python3 setup.py test
python3 setup.py build_ext -i
py.test3 -vv
%endif

%files
%python3_sitelibdir/*
%if_with doc
%exclude %python3_sitelibdir/*/pickle
%endif

%if_with doc
%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%changelog
* Mon Jan 30 2023 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version.

* Mon Dec 12 2022 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Fri Oct 14 2022 Andrey Cherepanov <cas@altlinux.org> 1.8.5-alt1
- New version.

* Thu Aug 18 2022 Andrey Cherepanov <cas@altlinux.org> 1.8.4-alt1
- New version.

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 1.8.2-alt2
- Fixed FTBFS.

* Wed May 04 2022 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1
- New version.

* Thu Feb 17 2022 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version.

* Fri Feb 04 2022 Grigory Ustinov <grenka@altlinux.org> 1.8.0-alt2
- Enable check back.

* Thu Feb 03 2022 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version.

* Fri Jan 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt4
- Disable check for python3.10.

* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt3
- Fixed building docs with python3.

* Sun Jul 18 2021 Michael Shigorin <mike@altlinux.org> 1.7.1-alt2
- Introduce doc knob (on by default).

* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt1
- Automatically updated to 1.7.1.
- Enable check.
- Drop python2 support.

* Sun Feb 14 2021 Grigory Ustinov <grenka@altlinux.org> 1.7-alt2.b1
- Disable check for building python3.9.

* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7-alt1.b1
- Updated to upstream version 1.7b1 (Closes: #37910)

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.5.17-alt1.post1.1.1.1.1
- Added missing dep on `numpy.testing`.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.17-alt1.post1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.17-alt1.post1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 1.5.17-alt1.post1.1
- Build without geos support

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.17-alt1.post1
- Updated to upstream version 1.5.17.post1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.10-alt1.git20150820.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.10-alt1.git20150820
- Version 1.5.10

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20150202
- New snapshot

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20150104
- Version 1.5.2

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.git20141102
- Version 1.4.4

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1.git20141031
- Version 1.4.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2b6-alt2.1
- Rebuild with Python-2.7

* Tue Apr 13 2010 Denis Klimov <zver@altlinux.org> 1.2b6-alt2
- add build require to python-module-setuptools

* Tue Apr 13 2010 Denis Klimov <zver@altlinux.org> 1.2b6-alt1
- Initial build for ALT Linux

