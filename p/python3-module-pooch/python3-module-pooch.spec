%define modname pooch
# tests require network access
%def_disable check

Name: python3-module-%modname
Version: 1.7.0
Release: alt1

Summary: A Python library for fetch and check data files
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/%modname

Vcs: https://github.com/fatiando/pooch.git
Source: https://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 >= 0.1.19
BuildRequires: python3-module-setuptools python3-module-setuptools_scm python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-tqdm python3-module-paramiko
BuildRequires: python3-module-xxhash python3-module-pytest-localftpserver}

%description
Pooch manages your Python library's sample data files. It automatically
downloads and stores them in a local directory, with support for
versioning and corruption checks.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
py.test3 %modname/tests

%files
%python3_sitelibdir/*
%doc README*


%changelog
* Tue Feb 28 2023 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Sat Jun 25 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- first build for Sisyphus



