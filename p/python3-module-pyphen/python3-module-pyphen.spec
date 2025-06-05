%define  modulename pyphen

Name:    python3-module-%modulename
Version: 0.17.2
Release: alt1

Summary: Hyphenation in pure Python
License: GPLv2+ and LGPLv2+ and MPL 1.1
Group:   Development/Python3
URL:     https://pypi.org/project/pyphen
VCS:     https://github.com/Kozea/Pyphen

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version.dist-info
%doc README.rst

%changelog
* Thu Jun 05 2025 Grigory Ustinov <grenka@altlinux.org> 0.17.2-alt1
- Automatically updated to 0.17.2.

* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus
