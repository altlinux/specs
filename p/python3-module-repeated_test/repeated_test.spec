%define _unpackaged_files_terminate_build 1
%define oname repeated_test

%def_with check

Name: python3-module-%oname
Version: 2.3.3
Release: alt2

Summary: A quick unittest-compatible framework for repeating a test function over many fixtures

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/repeated-test
VCS: https://github.com/epsy/repeated_test

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(wheel)

# PEP503 normalized name
%py3_provides repeated-test
Provides: python3-module-repeated-test = %EVR

%description
A quick unittest-compatible framework for repeating a test function over many fixtures.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

# strip tests
rm -r %buildroot%python3_sitelibdir/%oname/tests/

%check
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 2.3.3-alt2
- Build new version.

* Sun Jan 28 2024 Grigory Ustinov <grenka@altlinux.org> 2.1.3-alt2
- Moved on modern pyproject macros.

* Tue Mar 29 2022 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1
- 1.0.1 -> 2.1.3.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt2
- Drop python2 support.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Sisyphus

