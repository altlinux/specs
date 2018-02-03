%define _unpackaged_files_terminate_build 1
%define oname flake8-debugger

%def_with python3

Name: python-module-%oname
Version: 1.4.0
Release: alt1.1
Summary: ipdb/pdb statement checker plugin for flake8
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/flake8-debugger/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/JBKahn/flake8-debugger.git
Source0: https://pypi.python.org/packages/d1/3f/0dd096c996c9c34acc5bc66c6b60895accc635e832e4e696446f12424348/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-flake8 python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-flake8 python3-module-nose
%endif

%py_provides flake8_debugger

%description
Check for pdb;idbp imports and set traces.

This module provides a plugin for ``flake8``, the Python code checker.

%package -n python3-module-%oname
Summary: ipdb/pdb statement checker plugin for flake8
Group: Development/Python3
%py3_provides flake8_debugger

%description -n python3-module-%oname
Check for pdb;idbp imports and set traces.

This module provides a plugin for ``flake8``, the Python code checker.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2-alt1.git20141104.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git20141104
- Initial build for Sisyphus

