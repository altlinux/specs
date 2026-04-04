%define pypi_name favicon

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1

Summary: Find a website's favicon
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/favicon
Vcs: https://github.com/scottwernervt/favicon

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
%doc LICENSE *.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Apr 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt1
- Initial build for ALT Linux (git.123e431f53).

