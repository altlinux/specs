%define _unpackaged_files_terminate_build 1
%define oname flake8-print

%def_without python3

Name: python-module-%oname
Version: 2.0.2
Release: alt1.1
Summary: Print statement checker plugin for flake8
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/flake8-print/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/JBKahn/flake8-print.git
Source0: https://pypi.python.org/packages/b8/ce/b253acf4da0ea69bedbeec0e62c066be7962057a27ab552638d757201ea7/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-flake8 python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-flake8 python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides flake8_print

%description
Check for Print statements in python files.

This module provides a plugin for ``flake8``, the Python code checker.

%if_with python3
%package -n python3-module-%oname
Summary: Print statement checker plugin for flake8
Group: Development/Python3
%py3_provides flake8_print

%description -n python3-module-%oname
Check for Print statements in python files.

This module provides a plugin for ``flake8``, the Python code checker.
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1
- automated PyPI update

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.git20141104
- Fixed build

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141104
- Initial build for Sisyphus

