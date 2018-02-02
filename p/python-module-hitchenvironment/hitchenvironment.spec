%define oname hitchenvironment

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git20150621.1.1
Summary: Tool to cause tests to fail fast when the wrong environment is used to run them
License: AGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/hitchenvironment/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hitchtest/hitchenvironment.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
HitchEnvironment is a plugin for the Hitch testing framework that lets
you describe your environment and verify that it correct.

It is supposed to provide some measure of safety for tests that might
pass on, for example, a 64 bit machine but fail on a 32 bit machine, by
making the environment a test runs on declared explicitly.

%if_with python3
%package -n python3-module-%oname
Summary: Tool to cause tests to fail fast when the wrong environment is used to run them
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
HitchEnvironment is a plugin for the Hitch testing framework that lets
you describe your environment and verify that it correct.

It is supposed to provide some measure of safety for tests that might
pass on, for example, a 64 bit machine but fail on a 32 bit machine, by
making the environment a test runs on declared explicitly.
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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20150621.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20150621.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150621
- Initial build for Sisyphus

