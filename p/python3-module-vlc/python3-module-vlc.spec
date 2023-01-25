%define _unpackaged_files_terminate_build 1
%define modname vlc
%define pypi_name python-vlc

Name: python3-module-%modname
Version: 3.0.16120
Release: alt1
Summary: Binding for the native libvlc API
License: LGPL-2.1+
Group: Development/Python3
Url: https://github.com/oaubert/python-vlc
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

Requires: libvlc-devel

%py3_provides %pypi_name

%description
This module provides ctypes-based bindings for the native libvlc API of the VLC
video player. Note that it relies on an already present install of VLC.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modname.py
%python3_sitelibdir/*/*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc examples

%changelog
* Wed Jan 25 2023 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.16120-alt1
- Updated to version 3.0.16120
- Use pyproject macroses for build

* Tue Jun 23 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.10114-alt1
- Updated to version 3.0.10114

* Fri May 29 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.9113-alt1
- Updated to version 3.0.9113
- Changed url tag

* Fri Nov 15 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.7110-alt3
- Renamed to python3

* Mon Sep 30 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.7110-alt2
- drop python2 module

* Thu Aug 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.7110-alt1
- New version

* Sun Jul 21 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.6109-alt1
- New version

* Wed Sep 12 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.0.102-alt1
- Init build to Sisyphus

