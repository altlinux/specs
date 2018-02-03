%define oname functools32

%def_without python3

Name: python-module-%oname
Version: 3.2.3.2
Release: alt1.git20150711.1
Summary: Backport of the functools module from Python 3.2.3 for use on 2.7 and PyPy
License: PSF
Group: Development/Python
Url: https://pypi.python.org/pypi/functools32/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/MiCHiLU/python-functools32.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
This is a backport of the functools standard library module from Python
3.2.3 for use on Python 2.7 and PyPy. It includes new features lru_cache
(Least-recently-used cache decorator).

%if_with python3
%package -n python3-module-%oname
Summary: Backport of the functools module from Python 3.2.3 for use on 2.7 and PyPy
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is a backport of the functools standard library module from Python
3.2.3 for use on Python 2.7 and PyPy. It includes new features lru_cache
(Least-recently-used cache decorator).
%endif

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
python test_functools32.py -v
%if_with python3
pushd ../python3
python3 test_functools32.py -v
popd
%endif

%files
%doc ChangeLog *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.2.3.2-alt1.git20150711.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.3.2-alt1.git20150711
- Initial build for Sisyphus

