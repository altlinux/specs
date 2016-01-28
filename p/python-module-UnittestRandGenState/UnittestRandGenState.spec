%define oname UnittestRandGenState

%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt1.1
Summary: Smart random-generation state persistence for unittest
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/UnittestRandGenState/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-numpy
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-numpy
%endif

%py_provides unittest_rand_gen_state
%py_requires numpy.random

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-module-numpy python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-numpy
BuildRequires: python-devel python-module-numpy-testing python3-module-numpy-testing rpm-build-python3

%description
This library provides a simple metaclass for dropping into
unittest.TestCase that addresses this. As long as a test fails, it will
continue making the same random choices (via random or numpy.random)
each execution. Any test that passed the previous execution, will get a
fresh set of random choices.

%package -n python3-module-%oname
Summary: Smart random-generation state persistence for unittest
Group: Development/Python3
%py3_provides unittest_rand_gen_state
%py3_requires numpy.random

%description -n python3-module-%oname
This library provides a simple metaclass for dropping into
unittest.TestCase that addresses this. As long as a test fails, it will
continue making the same random choices (via random or numpy.random)
each execution. Any test that passed the previous execution, will get a
fresh set of random choices.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
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
export PYTHONPATH=$PWD
python setup.py test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus

