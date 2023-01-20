%define  modulename pyinstaller-hooks-contrib

Name:    python3-module-%modulename
Version: 2022.13
Release: alt2

Summary: Community maintained hooks for PyInstaller
License: Apache-2.0 and GPL-2.0
Group:   Development/Python3
URL:     https://github.com/pyinstaller/pyinstaller-hooks-contrib

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%filter_from_requires /python3(nltk)/d

%description
The PyInstaller community hooks repository. This repository is a collection of
hooks for many packages, and allows PyInstaller to work with these packages
seamlessly.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install
# Remove tests
rm -rf %buildroot%python3_sitelibdir/_pyinstaller_hooks_contrib/tests

%files
%doc *.md
%python3_sitelibdir/_pyinstaller_hooks_contrib/
%python3_sitelibdir/*.egg-info

%changelog
* Fri Jan 20 2023 Andrey Cherepanov <cas@altlinux.org> 2022.13-alt2
- Removed autorequires nltk module.

* Wed Nov 09 2022 Andrey Cherepanov <cas@altlinux.org> 2022.13-alt1
- New version.

* Sat Nov 05 2022 Andrey Cherepanov <cas@altlinux.org> 2022.12-alt1
- New version.

* Sun Oct 30 2022 Andrey Cherepanov <cas@altlinux.org> 2022.11-alt1
- New version.

* Sun Sep 18 2022 Andrey Cherepanov <cas@altlinux.org> 2022.10-alt1
- Initial build for Sisyphus.
