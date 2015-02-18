%define oname clint

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20150109
Summary: Python Command-line Application Tools
License: ISCL
Group: Development/Python
Url: https://pypi.python.org/pypi/clint/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kennethreitz/clint.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-args
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-args
%endif

%py_provides %oname
%py_requires args

%description
Clint is a module filled with a set of awesome tools for developing
commandline applications.

%package -n python3-module-%oname
Summary: Python Command-line Application Tools
Group: Development/Python3
%py3_provides %oname
%py3_requires args
%add_python3_req_skip UserDict

%description -n python3-module-%oname
Clint is a module filled with a set of awesome tools for developing
commandline applications.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Clint is a module filled with a set of awesome tools for developing
commandline applications.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Clint is a module filled with a set of awesome tools for developing
commandline applications.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
python setup.py test
python test_clint.py -v
%if_with python3
pushd ../python3
python3 setup.py test
python3 test_clint.py -v
popd
%endif

%files
%doc AUTHORS HACKING LICENSE NOTICE *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS HACKING LICENSE NOTICE *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150109
- Initial build for Sisyphus

