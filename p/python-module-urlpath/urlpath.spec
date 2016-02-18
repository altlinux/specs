%define oname urlpath

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 1.0.4
Release: alt1.git20150127.1
Summary: Object-oriented URL from `urllib.parse` and `pathlib`
License: PSFL
Group: Development/Python
Url: https://pypi.python.org/pypi/urlpath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/chrono-meter/urlpath.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pathlib python-module-webob
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pathlib python3-module-webob
%endif

%py_provides %oname
%py_requires pathlib webob

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python3-module-pathlib python3-module-pytest python3-module-webob rpm-build-python3 time

%description
urlpath provides URL manipulator class that extends pathlib.PurePath.

%package -n python3-module-%oname
Summary: Object-oriented URL from `urllib.parse` and `pathlib`
Group: Development/Python3
%py3_provides %oname
%py3_requires pathlib webob

%description -n python3-module-%oname
urlpath provides URL manipulator class that extends pathlib.PurePath.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
export PYTHONPATH=$PWD
py.test -vv
%endif
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%if_with python2
%files
%doc *.txt
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1.git20150127.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.git20150127
- Version 1.0.4

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150123
- Initial build for Sisyphus

