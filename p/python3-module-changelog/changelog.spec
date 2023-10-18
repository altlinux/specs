%define  modulename changelog

Name:    python3-module-%modulename
Version: 0.6.1
Release: alt2

Summary: A Sphinx extension to generate changelog files

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/changelog
VCS:     https://github.com/sqlalchemyorg/changelog

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildArch: noarch

Source:  %name-%version.tar
Patch: remove-distutils-for-python-3.12.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.rst
%_bindir/%modulename
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Wed Oct 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt2
- Dropped dependency on distutils.

* Tue Aug 22 2023 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt1
- Automatically updated to 0.6.1.

* Wed Apr 26 2023 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- Automatically updated to 0.6.0.

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.8-alt1
- Automatically updated to 0.5.8.

* Tue Apr 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.7-alt1
- Initial build for Sisyphus.
