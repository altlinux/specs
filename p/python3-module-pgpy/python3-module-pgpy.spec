%define  modulename PGPy

Name:    python3-module-pgpy
Version: 0.6.0
Release: alt1

Summary: Pretty Good Privacy for Python
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/SecurityInnovation/PGPy

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %modulename-%version.tar

%description
PGPy is a Python library for implementing Pretty Good Privacy into Python
programs, conforming to the OpenPGP specification per RFC 4880.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/pgpy
%python3_sitelibdir/*.egg-info

%changelog
* Sun Dec 11 2022 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- New version.

* Sun Sep 18 2022 Andrey Cherepanov <cas@altlinux.org> 0.5.4-alt1
- Initial build for Sisyphus.
