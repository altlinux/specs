%define oname unicodedata2

%def_without python3

Name: python-module-%oname
Version: 7.0.0.2
Release: alt1.git20150807.1
Summary: Unicodedata backport for python 2 updated to the latest unicode version
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/unicodedata2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mikekap/unicodedata2.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
The versions of this package match unicode versions, so
unicodedata2==7.0.0 is data from unicode 7.0.0. Additionally this
backports support for named aliases and named sequences to python2.

%if_with python3
%package -n python3-module-%oname
Summary: Unicodedata backport for python 2 updated to the latest unicode version
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The versions of this package match unicode versions, so
unicodedata2==7.0.0 is data from unicode 7.0.0. Additionally this
backports support for named aliases and named sequences to python2.
%endif

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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 7.0.0.2-alt1.git20150807.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.0.2-alt1.git20150807
- Initial build for Sisyphus

