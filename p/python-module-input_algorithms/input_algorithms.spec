%define oname input_algorithms

%def_with python3

Name: python-module-%oname
Version: 0.4.3.1
Release: alt1.git20150216
Summary: Thin DSL for creating input_algorithms
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/input_algorithms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/delfick/input_algorithms.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-delfick_error python-module-nose
BuildPreReq: python-module-mock python-module-noseOfYeti
BuildPreReq: python-module-namedlist
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-delfick_error python3-module-nose
BuildPreReq: python3-module-mock python3-module-noseOfYeti
BuildPreReq: python3-module-namedlist
%endif

%py_provides %oname
%py_requires delfick_error namedlist

%description
Thin DSL for creating yaml specifications.

%package -n python3-module-%oname
Summary: Thin DSL for creating input_algorithms
Group: Development/Python3
%py3_provides %oname
%py3_requires delfick_error namedlist

%description -n python3-module-%oname
Thin DSL for creating yaml specifications.

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
python setup.py test
./test.sh -v
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' test.sh
./test.sh -v
popd
%endif

%files
%doc *.rst docs/docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3.1-alt1.git20150216
- Version 0.4.3.1

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.git20150102
- Initial build for Sisyphus

