%def_with check

%define  modulename distro

Name:    python3-module-%modulename
Version: 1.8.0
Release: alt1

Summary: A much more elaborate, renewed alternative implementation for Python's platform.linux_distribution()
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/nir0s/distro

BuildArch: noarch

Source:  %modulename-%version.tar

Patch: %name-1.8.0-alt-add-alt-linux-support.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest python3-module-pytest-cov
%endif

%description
%summary.

%prep
%setup -n %modulename-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -- -v

%files
%_bindir/%modulename
%python3_sitelibdir/*
%doc *.md

%changelog
* Mon Feb 20 2023 Alexander Stepchenko <geochip@altlinux.org> 1.8.0-alt1
- New version 1.8.0
- Add check section
- Add ALT Linux support

* Mon Oct 05 2020 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt2
- rename src.rpm package to python3-module-distro

* Fri Jul 03 2020 Vladimir Didenko <cow@altlinux.org> 1.5.0-alt1
- New version

* Mon Apr 08 2019 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
