%define _unpackaged_files_terminate_build 1
%define oname flake8-debugger
%def_with check

Name: python3-module-%oname
Version: 4.1.2
Release: alt1

Summary: ipdb/pdb statement checker plugin for flake8
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/flake8-debugger
BuildArch: noarch

# https://github.com/JBKahn/flake8-debugger.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-pycodestyle
BuildRequires: python3-module-flake8
%endif

%py3_provides flake8_debugger

%description
Check for pdb;idbp imports and set traces.

This module provides a plugin for ``flake8``, the Python code checker.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 4.1.2-alt1
- Build new version.

* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.1.0-alt1
- Version updated to 3.1.0
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2-alt1.git20141104.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git20141104
- Initial build for Sisyphus

