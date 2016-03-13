%define oname tabulate

%def_with python3

Name: python-module-%oname
Version: 0.7.3
Release: alt1.1.1
Summary: Pretty-print tabular data
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tabulate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose python-module-funcsigs
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-module-funcsigs
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pluggy python-module-py python-module-setuptools python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python-module-funcsigs python-module-nose python-module-pytest python3-module-nose python3-module-pytest rpm-build-python3 time

%description
Pretty-print tabular data in Python.

%package -n python3-module-%oname
Summary: Pretty-print tabular data
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Pretty-print tabular data in Python.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus

