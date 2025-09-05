%define nameD click_log

Name: python3-module-click-log
Version: 0.4.0
Release: alt1

Summary: Simple and beautiful logging for click applications

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/click-log
VCS: https://github.com/click-contrib/click-log

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
* Fri Sep 05 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.0-alt1
- Initial build for ALT Linux (git.6e9ef9835).
