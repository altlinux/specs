%define _unpackaged_files_terminate_build 1
%define mname dominate

Name: python3-module-%mname
Version: 2.7.0
Release: alt1
Summary: Library for creating and manipulating HTML documents using an elegant DOM API
License: LGPLv3
Group: Development/Python3
Url: https://github.com/Knio/dominate
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Dominate is a Python library for creating and manipulating HTML documents using
an elegant DOM API. It allows you to write HTML pages in pure Python very
concisely, which eliminates the need to learn another template language, and
lets you take advantage of the more powerful features of Python.

%package -n %name-tests
Summary: Tests for %name
Group: Development/Python3
BuildArch: noarch
Requires: %name

%description -n %name-tests
This package contains tests for %name.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%python3_sitelibdir/%mname/tests
install -m 0644 tests/* %buildroot%python3_sitelibdir/%mname/tests

%files
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version.dist-info
%exclude %python3_sitelibdir/%mname/tests
%doc LICENSE.txt README.md

%files -n %name-tests
%python3_sitelibdir/%mname/tests

%changelog
* Fri Oct 07 2022 Alexander Makeenkov <amakeenk@altlinux.org> 2.7.0-alt1
- Updated to version 2.7.0

* Sun Mar 08 2020 Alexander Makeenkov <amakeenk@altlinux.org> 2.5.1-alt1
- New version

* Sat Feb 29 2020 Alexander Makeenkov <amakeenk@altlinux.org> 2.5.0-alt1
- New version
- Move tests in separate package

* Wed Oct 02 2019 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.0-alt1
- Initial build for ALT
