%define oname tblib

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150112
Summary: Traceback fiddling library. Allows you to pickle tracebacks
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tblib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ionelmc/python-tblib.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six
%endif

%py_provides %oname
%py_requires six

%description
Traceback fiddling library. For now allows you to pickle tracebacks and
raise exceptions with pickled tracebacks in different processes. This
allows better error handling when running code over multiple processes
(imagine multiprocessing, billiard, futures, celery etc).

%package -n python3-module-%oname
Summary: Traceback fiddling library. Allows you to pickle tracebacks
Group: Development/Python3
%py3_provides %oname
%py3_requires six

%description -n python3-module-%oname
Traceback fiddling library. For now allows you to pickle tracebacks and
raise exceptions with pickled tracebacks in different processes. This
allows better error handling when running code over multiple processes
(imagine multiprocessing, billiard, futures, celery etc).

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst tests
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst tests
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150112
- Initial build for Sisyphus

