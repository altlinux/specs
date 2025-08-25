%define nameD envstack

Name: python3-module-%nameD
Version: 0.9.1
Release: alt1

Summary: Stacked environment variable management system
License: BSD-3-Clause
Group: Development/Python3

Url: https://pypi.org/project/envstack
Vcs: https://github.com/rsgalloway/envstack

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
%doc LICENSE README.md
%python3_sitelibdir/%nameD/
%python3_sitelibdir/%{pyproject_distinfo %nameD}/

%changelog
* Tue Aug 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.1-alt1
- 0.9.0 -> 0.9.1

* Tue Aug 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.0-alt1
- 0.8.9 -> 0.9.0

* Tue Jul 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.8.9-alt1
- Initial build for Alt Linux.
