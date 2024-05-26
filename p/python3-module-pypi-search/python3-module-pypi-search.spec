%define  modulename pypi-search

Name:    python3-module-%modulename
Version: 2.0
Release: alt2

Summary: Get Information on Python Packages From PyPI
License: MIT
Group:   Development/Python3
URL:     https://github.com/asadmoosvi/pypi-search

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source:  %modulename-%version.tar

%description
pypi-search allows you to quickly query packages on PyPI. It fetches the
following information:
* Version Information
* Project Links
* Github Stats if any
* Meta Information (author, maintainer)
* Description

It quickly allows you to know what a package is all about without having to
open up the PyPI website.

%prep
%setup -n %modulename-%version

sed -i 's/os/shutil/' pypi_search/main.py

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%_bindir/pypi-search
%python3_sitelibdir/pypi_search
%python3_sitelibdir/%{pyproject_distinfo pypi_search}

%changelog
* Sun May 26 2024 Grigory Ustinov <grenka@altlinux.org> 2.0-alt2
- Fixed piping output (Closes: #45069).

* Wed Aug 23 2023 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- New version.

* Tue May 16 2023 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- New version.

* Sat Jul 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version.

* Thu Jun 10 2021 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
