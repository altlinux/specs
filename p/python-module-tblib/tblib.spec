%define _unpackaged_files_terminate_build 1
%define oname tblib

%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1.1
Summary: Traceback fiddling library. Allows you to pickle tracebacks
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tblib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ionelmc/python-tblib.git
Source0: https://pypi.python.org/packages/52/aa/aefcbf6b2976fc91d5c32c4014f40e2202654279654cc509b613d7cf5568/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-six
%endif

%py_provides %oname
%py_requires six

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

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
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.git20150727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.git20150727.1
- NMU: Use buildreq for BR.

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20150727
- Version 1.1.0

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150112
- Initial build for Sisyphus

