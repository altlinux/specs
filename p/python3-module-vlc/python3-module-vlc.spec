%define _unpackaged_files_terminate_build 1
%define oname vlc

Name: python3-module-%oname
Version: 3.0.10114
Release: alt1
Summary: Binding for the native libvlc API
License: LGPLv2.1+
Group: Development/Python3
Url: https://github.com/oaubert/python-vlc
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
Requires: libvlc-devel

%description
This module provides ctypes-based bindings for the native libvlc API of the VLC
video player. Note that it relies on an already present install of VLC.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc COPYING MANIFEST.in README.module examples/
%python3_sitelibdir/*

%changelog
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

