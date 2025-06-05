%define  modulename tubes

Name:    python3-module-%modulename
Version: 0.2.1
Release: alt1

Summary: A series of tubes.
License: MIT
Group:   Development/Python3
URL:     https://github.com/twisted/tubes

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-intro >= 2.2.4
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
%python3_prune

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc README.rst LICENSE

%changelog
* Thu Jun 05 2025 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt1
- Automatically updated to 0.2.1.

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt3
- don't pack tests

* Thu Mar 26 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.0-alt2
- Remove unnecessary dependency from setup.py

* Tue Mar 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
