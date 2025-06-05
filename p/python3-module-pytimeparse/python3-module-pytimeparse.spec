%define  modulename pytimeparse

Name:    python3-module-%modulename
Version: 1.1.8
Release: alt1

Summary: A small Python module to parse various kinds of time expressions.
License: MIT
Group:   Development/Python3
URL:     https://github.com/wroberts/pytimeparse

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Jun 05 2025 Grigory Ustinov <grenka@altlinux.org> 1.1.8-alt1
- Automatically updated to 1.1.8.

* Wed Feb 07 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.7-alt1
- Initial build for Sisyphus
