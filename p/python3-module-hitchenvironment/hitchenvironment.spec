%define oname hitchenvironment

Name: python3-module-%oname
Version: 0.2
Release: alt2

Summary: Tool to cause tests to fail fast when the wrong environment is used to run them
License: AGPLv3+
Group: Development/Python3
Url: https://pypi.python.org/pypi/hitchenvironment/
# https://github.com/hitchtest/hitchenvironment.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
HitchEnvironment is a plugin for the Hitch testing framework that lets
you describe your environment and verify that it correct.

It is supposed to provide some measure of safety for tests that might
pass on, for example, a 64 bit machine but fail on a 32 bit machine, by
making the environment a test runs on declared explicitly.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20150621.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20150621.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150621
- Initial build for Sisyphus

