%def_with check

%define  modulename parsedatetime

Name:    python3-module-%modulename
Version: 2.6
Release: alt1

Summary: Parse human-readable date/time strings
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/bear/parsedatetime

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Tue Feb 24 2026 Grigory Ustinov <grenka@altlinux.org> 2.6-alt1
- Automatically updated to 2.6.

* Thu Feb 08 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.4-alt1
- Separate build for Sisyphus
