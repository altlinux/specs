%define _unpackaged_files_terminate_build 1
%define nameD aiostream

Name: python3-module-aiostream
Version: 0.7.2
Release: alt1

Summary: Generator-based operators for asynchronous iteration

License: GPL-3.0-only
Group: Development/Python3

URL: https://pypi.org/project/aiostream
VCS: https://github.com/vxgmichel/aiostream

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%nameD/
%python3_sitelibdir/%{pyproject_distinfo %nameD}/

%changelog
* Wed Sep 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.2-alt1
- 0.7.1 -> 0.7.2

* Tue Oct 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt1
- 0.7.0 -> 0.7.1

* Mon Sep 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt1
- Initial build for ALT Linux.
