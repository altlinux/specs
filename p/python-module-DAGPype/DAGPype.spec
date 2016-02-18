%define oname DAGPype

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.5.1
Release: alt1.1
Summary: Low-footprint flexible data-processing and data-preparation pipelines
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/DAGPype/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: gcc-c++ swig xvfb-run
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-matplotlib libnumpy-devel
#BuildPreReq: python-module-UnittestRandGenState
#BuildPreReq: python-module-nose python-module-pygobject3
#BuildPreReq: python-module-pycairo
#BuildPreReq: python-modules-xml
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-matplotlib libnumpy-py3-devel
#BuildPreReq: python3-module-UnittestRandGenState
#BuildPreReq: python3-module-nose python3-module-pygobject3
#BuildPreReq: python3-module-pycairo
%endif

%py_provides dagpype
%py_requires numpy matplotlib xml
# for tests:
%py_requires unittest_rand_gen_state

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils libnumpy-devel libstdc++-devel python-base python-devel python-module-numpy python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-dev python3-module-numpy
BuildRequires: gcc-c++ libnumpy-py3-devel python-module-numpy-testing python3-module-numpy-testing rpm-build-python3

%description
This is a Python framework for scientific data-processing and
data-preparation DAG (directed acyclic graph) pipelines.

It is designed to work well within Python scripts or IPython, provide an
in-Python alternative for sed, awk, perl, and grep, and complement
libraries such as NumPy/SciPy, SciKits, pandas, MayaVi, PyTables, and so
forth. Those libraries process data once it has been assembled. This
library is for flexible data assembly and quick exploration, or for
aggregating huge data which cannot be reasonably assembled.

%if_with python3
%package -n python3-module-%oname
Summary: Low-footprint flexible data-processing and data-preparation pipelines
Group: Development/Python3
%py3_provides dagpype
%py3_requires numpy matplotlib xml

%description -n python3-module-%oname
This is a Python framework for scientific data-processing and
data-preparation DAG (directed acyclic graph) pipelines.

It is designed to work well within Python scripts or IPython, provide an
in-Python alternative for sed, awk, perl, and grep, and complement
libraries such as NumPy/SciPy, SciKits, pandas, MayaVi, PyTables, and so
forth. Those libraries process data once it has been assembled. This
library is for flexible data assembly and quick exploration, or for
aggregating huge data which cannot be reasonably assembled.
%endif

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This is a Python framework for scientific data-processing and
data-preparation DAG (directed acyclic graph) pipelines.

It is designed to work well within Python scripts or IPython, provide an
in-Python alternative for sed, awk, perl, and grep, and complement
libraries such as NumPy/SciPy, SciKits, pandas, MayaVi, PyTables, and so
forth. Those libraries process data once it has been assembled. This
library is for flexible data assembly and quick exploration, or for
aggregating huge data which cannot be reasonably assembled.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py build_ext -i
xvfb-run python setup.py performance_test
xvfb-run nosetests -v
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
xvfb-run python3 setup.py performance_test
xvfb-run nosetests3 -v
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%files docs
%doc docs/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.1.5.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5.1-alt1
- Initial build for Sisyphus

