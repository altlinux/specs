%define  modulename cysignals

Name:    python3-module-%modulename
Version: 1.13.1
Release: alt1

Summary: cysignals: interrupt and signal handling for Cython

License: LGPL-3.0-or-later
Group:   Development/Python3
URL:     https://github.com/sagemath/cysignals

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-mesonpy
BuildRequires: meson ninja-build
BuildRequires: gcc-c++
BuildRequires: python3-module-Cython >= 3.1

Source: %modulename-%version.tar

# The debugger helper runs inside GDB, not the regular Python interpreter.
%add_python3_req_skip gdb Cython.Debugger Cython.Debugger.libcython

%description
The cysignals package provides mechanisms to handle interrupts (and other
signals and errors) in Cython code.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%_bindir/cysignals-CSI
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Fri Nov 27 2026 Vitaly Lipatov <lav@altlinux.ru> 1.13.1-alt1
- NMU: new version 1.13.1.
- Switch to the Meson build backend and drop obsolete compatibility patches.
- Added BuildRequires: meson, ninja-build, gcc-c++, python3-module-mesonpy.
- Added BuildRequires(pre): rpm-macros-python3.
- Removed BuildRequires: python3-module-setuptools, python3-module-wheel.
- Exclude GDB-only imports from regular Python dependency generation.

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
