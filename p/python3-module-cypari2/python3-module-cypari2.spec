%define  modulename cypari2

Name:    python3-module-%modulename
Version: 2.1.3
Release: alt1

Summary: Python interface to the number theory library PARI/GP
License: GPL-2.0
Group:   Development/Python3
URL:     https://github.com/sagemath/cypari2

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-Cython
BuildRequires: python3-module-cysignals
BuildRequires: pari-devel
BuildRequires: pari-gp
BuildRequires: libgmp-devel

Source: %modulename-%version.tar

%description
A Python interface to the number theory library PARI/GP.

%prep
%setup -n %modulename-%version

%build
%python3_build
# Second pass for auto_paridecl.pxd generate
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Sat Nov 12 2022 Andrey Cherepanov <cas@altlinux.org> 2.1.3-alt1
- New version.

* Sat May 28 2022 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- New version.

* Mon Jun 21 2021 Andrey Cherepanov <cas@altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus
