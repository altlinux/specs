%define _unpackaged_files_terminate_build 1
%define pypi_name nvchecker

Name:    python3-module-%pypi_name
Version: 2.17
Release: alt1

Summary: New version checker for software releases
License: MIT
Group:   Development/Python3
Url:     https://github.com/lilydjwg/nvchecker
Vcs:     https://github.com/lilydjwg/nvchecker.git

Provides: %pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel 
BuildRequires: python3-module-setuptools 
BuildRequires: python3-module-wheel

%py3_requires pycurl tornado curses

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

%description
nvchecker (short for new version checker) is for checking if a new version of some software has been released.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/nvchecker
%_bindir/nvchecker-ini2toml
%_bindir/nvchecker-notify
%_bindir/nvcmp
%_bindir/nvtake
%python3_sitelibdir/%{pypi_name}/
%python3_sitelibdir/%{pypi_name}_source/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Mar 16 2025 Maxim Slipenko <maks1ms@altlinux.org> 2.17-alt1
- 2.17

* Sat Feb 22 2025 Maxim Slipenko <maks1ms@altlinux.org> 2.16-alt1
- Initial build
