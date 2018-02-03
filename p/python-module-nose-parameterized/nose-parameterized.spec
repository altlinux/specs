%define oname nose-parameterized

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1.git20150806.2.1
Summary: Decorator for parameterized testing with Nose
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-parameterized/

# https://github.com/wolever/nose-parameterized.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
%endif

%py_provides nose_parameterized

%description
nose-parameterized is a decorator for parameterized testing with nose.

%package -n python3-module-%oname
Summary: Decorator for parameterized testing with Nose
Group: Development/Python3
%py3_provides nose_parameterized

%description -n python3-module-%oname
nose-parameterized is a decorator for parameterized testing with nose.

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
export LC_ALL=en_US.UTF-8
nosetests
%if_with python3
pushd ../python3
nosetests3
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1.git20150806.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1.git20150806.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150806.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150806
- Version 0.5.0

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20141105
- Initial build for Sisyphus

