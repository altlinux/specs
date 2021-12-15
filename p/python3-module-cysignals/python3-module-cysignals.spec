%define  modulename cysignals

Name:    python3-module-%modulename
Version: 1.11.2
Release: alt1

Summary: cysignals: interrupt and signal handling for Cython
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/sagemath/cysignals

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-Cython

Source: %modulename-%version.tar

%description
The cysignals package provides mechanisms to handle interrupts (and other
signals and errors) in Cython code.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%_bindir/cysignals-CSI
%_datadir/cysignals/cysignals-CSI-helper.py
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Wed Dec 15 2021 Andrey Cherepanov <cas@altlinux.org> 1.11.2-alt1
- New version.

* Fri Nov 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.11.0-alt1
- New version.

* Mon Oct 18 2021 Grigory Ustinov <grenka@altlinux.org> 1.10.3-alt2
- Fixed FTBFS.

* Mon Jun 21 2021 Andrey Cherepanov <cas@altlinux.org> 1.10.3-alt1
- Initial build for Sisyphus
