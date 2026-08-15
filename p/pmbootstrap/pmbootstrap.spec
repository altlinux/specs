%define _unpackaged_files_terminate_build 1

Name: pmbootstrap
Version: 3.11.1
Release: alt1

Summary: Sophisticated chroot/build/flash tool to develop and install postmarketOS
License: GPL-3.0-only
Group: Development/Tools

URL: https://wiki.postmarketos.org/wiki/Pmbootstrap
VCS: https://gitlab.postmarketos.org/postmarketOS/pmbootstrap

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: python3(setuptools)

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%name
%python3_sitelibdir_noarch/pmb
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}

%changelog
* Sat Aug 15 2026 David Sultaniiazov <x1z53@altlinux.org> 3.11.1-alt1
- Initial build.
