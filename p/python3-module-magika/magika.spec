%define nameD magika

Name: python3-module-%nameD
Version: 1.0.3
Release: alt1

Summary: Fast and accurate AI powered file content types detection
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/magika

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling python3-module-wheel

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
%doc *.md
%_bindir/%{nameD}*
%python3_sitelibdir/%nameD
%python3_sitelibdir/%{pyproject_distinfo %nameD}

%changelog
* Tue Aug 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.3-alt1
- 1.0.2 -> 1.0.3

* Tue Aug 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.2-alt1
- Initial build for ALT Linux.

