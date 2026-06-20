%define pypi_name exejs

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: Run JavaScript code from Python
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/exejs
Vcs: https://github.com/UlionTse/exejs

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md
%python3_sitelibdir/*

%changelog
* Sat Jun 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.0-alt1
- automatic build: 0.0.7.1 -> 1.0.0

* Wed Jun 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.0.7.1-alt1
- Initial build for ALT Linux.

