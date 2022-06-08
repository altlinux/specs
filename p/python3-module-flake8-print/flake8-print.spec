%define _unpackaged_files_terminate_build 1
%define oname flake8-print

Name: python3-module-%oname
Version: 5.0.0
Release: alt1

Summary: Print statement checker plugin for flake8

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/flake8-print/

Source0: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flake8

BuildArch: noarch

%py3_provides flake8_print

%description
Check for Print statements in python files.

This module provides a plugin for ``flake8``, the Python code checker.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Wed Jun 08 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Build new version.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1
- automated PyPI update

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.git20141104
- Fixed build

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141104
- Initial build for Sisyphus

