%define module_name shapely

%def_with python3

Name: python-module-%module_name
Version: 1.5.17
Release: alt1.post1.1.1

Summary: Planar geometries, predicates, and operations

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/Shapely

# https://github.com/Toblerity/Shapely.git
Source: %name-%version.tar

BuildPreReq: libgeos-devel
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-descartes python-module-sphinx-devel
BuildPreReq: python-module-matplotlib-sphinxext
BuildPreReq: python-module-packaging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-descartes
BuildPreReq: python3-module-packaging
BuildRequires: xvfb-run
%endif

%setup_python_module %module_name

%description
Planar geometries, predicates, and operations.

%package examples
Summary: Examples for %module_name
Group: Development/Python
Requires: %name = %EVR

%description examples
Planar geometries, predicates, and operations.

This package contains examples for %module_name.

%package -n python3-module-%module_name
Summary: Planar geometries, predicates, and operations
Group: Development/Python3

%description -n python3-module-%module_name
Planar geometries, predicates, and operations.

%package -n python3-module-%module_name-examples
Summary: Examples for %module_name
Group: Development/Python3
Requires: python3-module-%module_name = %EVR

%description -n python3-module-%module_name-examples
Planar geometries, predicates, and operations.

This package contains examples for %module_name.

%package pickles
Summary: Pickles for %module_name
Group: Development/Python
%add_python_req_skip figures

%description pickles
Planar geometries, predicates, and operations.

This package contains pickles for %module_name.

%package docs
Summary: Documentation for %module_name
Group: Development/Documentation
BuildArch: noarch

%description docs
Planar geometries, predicates, and operations.

This package contains documentation for %module_name.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export LC_ALL=en_US.UTF-8
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install
install -m644 %buildroot%prefix/%module_name/*.pxi \
	%buildroot%python_sitelibdir/%module_name/

%if_with python3
pushd ../python3
%python3_install
popd
install -m644 %buildroot%prefix/%module_name/*.pxi \
	%buildroot%python3_sitelibdir/%module_name/
%endif

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%module_name/

%check
export LC_ALL=en_US.UTF-8
python setup.py test
python setup.py build_ext -i
py.test -vv
%if_with python3
pushd ../python3
xvfb-run python3 setup.py test
python3 setup.py build_ext -i
py.test3 -vv
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/examples

%files examples
%python_sitelibdir/*/examples

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%module_name-examples
%python3_sitelibdir/*/examples
%endif

%changelog
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

