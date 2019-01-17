%define _unpackaged_files_terminate_build 1
%define oname process-tests

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1
Summary: Tools for testing processes
License: BSD
Group: Development/Python
Url: https://pypi.org/project/process-tests/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ionelmc/python-process-tests.git
Source: https://files.pythonhosted.org/packages/43/6e/c4bd9605036e3c883c42e4f9ce79aede9101bd95f09055ae946a60b63b9e/%name-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Testcase classes and assertions for testing processes.

%package -n python3-module-%oname
Summary: Tools for testing processes
Group: Development/Python3

%description -n python3-module-%oname
Testcase classes and assertions for testing processes.

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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 1.2.1 -> 2.0.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20150618.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150618
- Version 1.0.0

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20140725
- Initial build for Sisyphus

