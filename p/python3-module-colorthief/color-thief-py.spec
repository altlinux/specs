Name: python3-module-colorthief
Version: 0.2.1
Release: alt1

Summary: A Python module for grabbing the color palette from an image

License: BSD
Group: Development/Python3

URL: https://pypi.org/project/colorthief
VCS: https://github.com/fengsp/color-thief-py

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
%python3_sitelibdir/*
%doc *.rst LICENSE

%changelog
* Thu Oct 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.1-alt1
- Initial build for ALT Linux.

