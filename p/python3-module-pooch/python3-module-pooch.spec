%define pypi_name pooch
# tests require network access
%def_disable check

Name: python3-module-%pypi_name
Version: 1.8.2
Release: alt1

Summary: A Python library for fetch and check data files
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/pooch

Vcs: https://github.com/fatiando/pooch.git
Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

# https://bugzilla.altlinux.org/50120
%set_python3_req_method strict

BuildRequires(pre): rpm-build-python3 >= 0.1.19
BuildRequires: python3-module-setuptools python3-module-setuptools_scm python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-tqdm python3-module-paramiko
BuildRequires: python3-module-xxhash python3-module-pytest-localftpserver}

%description
Pooch manages your Python library's sample data files. It automatically
downloads and stores them in a local directory, with support for
versioning and corruption checks.

%package tests
Summary: Tests for Pooch
Group: Development/Python3
Requires: %name = %EVR

%description tests
This packages contains tests for Pooch.


%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
py.test3 %pypi_name/tests

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%pypi_name/tests

%files tests
%python3_sitelibdir/%pypi_name/tests/

%doc README*


%changelog
* Thu Jun 06 2024 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Mon Apr 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1.1
- rebuilt with python3_req_method=strict (ALT #50120)
- split tests to separate subpackage

* Tue Feb 20 2024 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Wed Oct 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Feb 28 2023 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Sat Jun 25 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- first build for Sisyphus



