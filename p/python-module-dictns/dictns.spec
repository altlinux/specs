%define oname dictns

%def_with python3

Name: python-module-%oname
Version: 1.4
Release: alt1.git20141214
Summary: Simple class that merges dictionary and object API
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dictns/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tardyp/dictns.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Simple class that merges dictionary and object API.

This Namespace objects work in a similar way as javascript objects.

%package -n python3-module-%oname
Summary: Simple class that merges dictionary and object API
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Simple class that merges dictionary and object API.

This Namespace objects work in a similar way as javascript objects.

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
export PYTHONPATH=$PWD
py.test -vv
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
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
* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.git20141214
- Initial build for Sisyphus

