%def_with check

Name:    thefuck
Version: 3.32
Release: alt2

Summary: Magnificent app which corrects your previous console command

License: MIT
Group:   Other
URL:     https://github.com/nvbn/thefuck

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-psutil
BuildRequires: python3-module-colorama
BuildRequires: python3-module-decorator
BuildRequires: python3-module-pyte
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest-mock
BuildRequires: /proc
%endif

BuildArch: noarch

Source:  %name-%version.tar

# replace distutils for python 3.12
Patch: dd26fb91a0fdec42fc1990bb91eab21e2c44a0a8.patch

%description
%summary.

%prep
%setup
%patch -p1

rm -v thefuck/system/win32.py

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%_bindir/fuck
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version.dist-info

%changelog
* Thu Oct 12 2023 Grigory Ustinov <grenka@altlinux.org> 3.32-alt2
- Dropped dependency on distutils.
- Build with check.

* Mon Jan 17 2022 Grigory Ustinov <grenka@altlinux.org> 3.32-alt1
- Automatically updated to 3.32.

* Fri Jun 18 2021 Grigory Ustinov <grenka@altlinux.org> 3.31-alt1
- Automatically updated to 3.31.

* Sun Mar 22 2020 Grigory Ustinov <grenka@altlinux.org> 3.30-alt1
- Automatically updated to 3.30.

* Tue May 28 2019 Grigory Ustinov <grenka@altlinux.org> 3.29-alt1
- Build new version.

* Mon Dec 03 2018 Grigory Ustinov <grenka@altlinux.org> 3.28-alt1
- Build new version.

* Tue May 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.27-alt1
- Build new version.

* Tue May 15 2018 Grigory Ustinov <grenka@altlinux.org> 3.26-alt1
- Build new version.

* Mon Feb 12 2018 Grigory Ustinov <grenka@altlinux.org> 3.25-alt2
- Change package group.

* Thu Feb 08 2018 Grigory Ustinov <grenka@altlinux.org> 3.25-alt1
- Initial build for Sisyphus.
