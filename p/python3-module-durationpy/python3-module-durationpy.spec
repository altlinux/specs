%define  modulename durationpy

Name:     python3-module-%modulename
Version:  0.9
Release:  alt1

Summary:  Module for converting between datetime.timedelta and Go's Duration strings
License:  MIT
Group:    Other
Url:      https://github.com/icholy/durationpy
Vcs:      https://github.com/icholy/durationpy.git
BuildArch:  noarch

Source:   %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%python3_sitelibdir/*

%changelog
* Thu Oct 03 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.9-alt1
- 0.9

* Wed Oct 02 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.8-alt1
- 0.8

* Tue Sep 24 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.7-alt1
- Initial build for ALT

