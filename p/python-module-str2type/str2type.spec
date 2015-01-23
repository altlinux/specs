%define oname str2type

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20150123
Summary: Convert a Python string representation of int, float, etc. to its native type
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/str2type/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/geowurster/str2type.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coverage python-module-nose
BuildPreReq: python-modules-json python-tools-pep8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coverage python3-module-nose
BuildPreReq: python3-tools-pep8
%endif

%py_provides %oname
%py_requires json

%description
Convert a string representation of an int, float, None, True, False, or
JSON to its native type. For None, True, and False, case is irrelevant.

The user can also specify which JSON library to use for decoding should
they know they will be encountering a lot of JSON, in which case a
different library is probably more appropriate than this function.

%package -n python3-module-%oname
Summary: Convert a Python string representation of int, float, etc. to its native type
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Convert a string representation of an int, float, None, True, False, or
JSON to its native type. For None, True, and False, case is irrelevant.

The user can also specify which JSON library to use for decoding should
they know they will be encountering a lot of JSON, in which case a
different library is probably more appropriate than this function.

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
* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150123
- Initial build for Sisyphus

