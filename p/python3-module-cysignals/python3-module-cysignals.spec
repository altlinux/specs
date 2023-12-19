%define  modulename cysignals

Name:    python3-module-%modulename
Version: 1.11.4
Release: alt1

Summary: cysignals: interrupt and signal handling for Cython
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/sagemath/cysignals

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython

Source: %modulename-%version.tar

Patch: remove-distutils-for-python-3.12.patch
Patch1: remove-legacy-implicit-noexcept.patch

%description
The cysignals package provides mechanisms to handle interrupts (and other
signals and errors) in Cython code.

%prep
%setup -n %modulename-%version
%patch -p1
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%_bindir/cysignals-CSI
%_datadir/cysignals/cysignals-CSI-helper.py
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Tue Dec 19 2023 Anton Vyatkin <toni@altlinux.org> 1.11.4-alt1
- New version 1.11.4.

* Fri Oct 13 2023 Grigory Ustinov <grenka@altlinux.org> 1.11.2-alt2
- Dropped dependency on distutils.

* Wed Dec 15 2021 Andrey Cherepanov <cas@altlinux.org> 1.11.2-alt1
- New version.

* Fri Nov 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.11.0-alt1
- New version.

* Mon Oct 18 2021 Grigory Ustinov <grenka@altlinux.org> 1.10.3-alt2
- Fixed FTBFS.

* Mon Jun 21 2021 Andrey Cherepanov <cas@altlinux.org> 1.10.3-alt1
- Initial build for Sisyphus
