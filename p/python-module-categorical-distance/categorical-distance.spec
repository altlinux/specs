%define oname categorical-distance

%def_without python3

Name: python-module-%oname
Version: 1.2
Release: alt1.git20141205
Summary: Compare categorical variables
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/categorical-distance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datamade/categorical-distance.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-numpy python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-numpy python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides categorical
%py_requires numpy

%description
Compare two categorical variables.

%package -n python3-module-%oname
Summary: Compare categorical variables
Group: Development/Python3
%py3_provides categorical
%py3_requires numpy

%description -n python3-module-%oname
Compare two categorical variables.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20141205
- Initial build for Sisyphus

