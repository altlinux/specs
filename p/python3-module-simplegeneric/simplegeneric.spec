%define _unpackaged_files_terminate_build 1
%define pypi_name simplegeneric
%define modname %pypi_name

Name: python3-module-%modname
Version: 0.8.1
Release: alt5
Summary: Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)

Group: Development/Python3
License: Python or ZPLv2.1
Url: https://pypi.org/project/simplegeneric/
Source0: %modname-%version.zip

BuildArch: noarch
BuildRequires: unzip
BuildRequires: rpm-build-python3
# build backend and its deps
BuildRequires: python3-module-setuptools

%description
The simplegeneric module lets you define simple single-dispatch generic
functions, akin to Python's built-in generic functions like len(), iter() and
so on. However, instead of using specially-named methods, these generic
functions use simple lookup tables, akin to those used by e.g. pickle.dump()
and other generic functions found in the Python standard library.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest %modname.test_suite

%files
%doc README.txt
%python3_sitelibdir/__pycache__/%modname.cpython*
%python3_sitelibdir/%modname.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 15 2024 Stanislav Levin <slev@altlinux.org> 0.8.1-alt5
- Migrated from removed setuptools' test command (see #50996).

* Thu Mar 02 2023 Anton Vyatkin <toni@altlinux.org> 0.8.1-alt4
- (NMU) Fix BuildRequires, drop 2to3

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt3
- Fixed FTBFS.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Version 0.8.1

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.8-alt1
- First build for ALT (based on Fedora 0.8-9.fc21.src)

