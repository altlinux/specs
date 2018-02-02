%define oname jsonobject

%def_without python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1.git20150130.1
Summary: A library for dealing with JSON as python objects
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonobject/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dimagi/jsonobject.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-couchdbkit python-module-unittest2
BuildPreReq: python-module-argparse python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-couchdbkit python3-module-unittest2
BuildPreReq: python3-module-argparse python3-module-six
%endif

%py_provides %oname

%description
A python library for handling deeply nested JSON objects as
well-schema'd python objects.

%if_with python3
%package -n python3-module-%oname
Summary: A library for dealing with JSON as python objects
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A python library for handling deeply nested JSON objects as
well-schema'd python objects.
%endif

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
export LC_ALL=en_US.UTF-8
python setup.py test
python -m unittest test.test_couchdbkit
%if_with python3
pushd ../python3
python3 setup.py test
python3 -m unittest test.test_couchdbkit
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1.git20150130.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150130
- New snapshot

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141126
- Initial build for Sisyphus

