%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname pytest-remove-stale-bytecode

%def_with python3

Name: python-module-%oname
Version: 2.1
Release: alt1.1
Summary: py.test plugin to remove stale byte code files
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-remove-stale-bytecode
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/3d/29/8389e329a55beb7b752d94fc28e9acaf6c3e6791f17cec86736a47853294/%{oname}-%{version}.zip
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%description
This plugin removes all stale bytecode files before running tests. This
makes sure that removed python files are no longer visible for the test
runner as their bytecode file (*.pyc, *.pyo) is removed as well.

%package -n python3-module-%oname
Summary: py.test plugin to remove stale byte code files
Group: Development/Python3

%description -n python3-module-%oname
This plugin removes all stale bytecode files before running tests. This
makes sure that removed python files are no longer visible for the test
runner as their bytecode file (*.pyc, *.pyo) is removed as well.

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
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

