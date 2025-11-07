%define _unpackaged_files_terminate_build 1
%define modulename pythontk

Name:    python3-module-%modulename
Version: 0.7.30
Release: alt1

Summary: A collection of backend utilities for Python
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pythontk/
Vcs:     https://github.com/m3trik/pythontk.git

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools 
BuildRequires: python3-module-wheel
BuildRequires: python3-module-numpy
BuildRequires: python3-module-Pillow

BuildArch: noarch

Source: %name-%version.tar

%description
A collection of Python utility functions for file operations,
text processing, and basic image/video manipulation.
Provides helper classes and convenience functions for common programming tasks.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

#fix broken installation of map_converter.ui and map_packer.ui into /usr/ directory
install -D -m 644 \
 %buildroot/usr/map_converter.ui \
 %buildroot%python3_sitelibdir/%modulename/img_utils/map_converter.ui
install -D -m 644 \
 %buildroot/usr/map_packer.ui \
 %buildroot%python3_sitelibdir/%modulename/img_utils/map_packer.ui
rm -f %buildroot/usr/map_{packer,converter}.ui

%files
%doc LICENSE docs/*.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}/

%changelog
* Thu Oct 30 2025 Nikita Shmatko <nash@altlinux.org> 0.7.30-alt1
- Initial build for Sisyphus.
