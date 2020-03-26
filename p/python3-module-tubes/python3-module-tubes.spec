%define  modulename tubes

Name:    python3-module-%modulename
Version: 0.2.0
Release: alt2

Summary: A series of tubes.
License: MIT
Group:   Development/Python3
URL:     https://github.com/twisted/tubes

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

Patch1: 0001-remove-unnecessary-dependency.patch

%description
%summary

%prep
%setup -n %modulename-%version
%patch1 -p1

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc README.rst LICENSE

%changelog
* Thu Mar 26 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.0-alt2
- Remove unnecessary dependency from setup.py

* Tue Mar 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
