Name: python3-module-bracex
Version: 2.4
Release: alt1
Summary: Bash style brace expansion for Python
License: MIT
Group: Development/Python3
Url: https://github.com/facelessuser/bracex.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= 3.8
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling >= 0.21.1

# for tests
BuildRequires: python3-module-pytest

%description
Bracex is a brace expanding library (a la Bash) for Python.
Brace expanding is used to generate arbitrary strings.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE.md README.md
%python3_sitelibdir/*

%changelog
* Tue Jan 30 2024 Alexey Shabalin <shaba@altlinux.org> 2.4-alt1
- Initial build.

