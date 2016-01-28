%define oname should_dsl

%def_with python3

Name: python-module-%oname
Version: 2.1.2
Release: alt1.1
Summary: Should assertions in Python as clear and readable as possible
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/should_dsl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
The goal of Should-DSL is to write should expectations in Python as
clear and readable as possible, using "almost" natural language (limited
- sometimes - by the Python language constraints).

In order to use this DSL, you need to import should and should_not
objects from should_dsl module.

%package -n python3-module-%oname
Summary: Should assertions in Python as clear and readable as possible
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The goal of Should-DSL is to write should expectations in Python as
clear and readable as possible, using "almost" natural language (limited
- sometimes - by the Python language constraints).

In order to use this DSL, you need to import should and should_not
objects from should_dsl module.

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
python run_examples.py
%if_with python3
pushd ../python3
python3 run_examples.py
popd
%endif

%files
%doc CONTRIBUTORS *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CONTRIBUTORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.2-alt1.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus

