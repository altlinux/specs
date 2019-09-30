%define oname vlc

Name: python-module-%oname
Version: 3.0.7110
Release: alt2

Summary: Binding for the native libvlc API.
License: LGPLv2.1+
Group: Development/Python
Url: https://wiki.videolan.org/PythonBinding
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools

Requires: libvlc-devel


%description
This module provides ctypes-based bindings for the native libvlc API of the VLC
video player. Note that it relies on an already present install of VLC.

%package -n python3-module-%oname
Summary: Binding for the native libvlc API.
Group: Development/Python3
Requires: libvlc-devel

%description -n python3-module-%oname
This module provides ctypes-based bindings for the native libvlc API of the VLC
video player. Note that it relies on an already present install of VLC.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files -n python3-module-%oname
%doc COPYING MANIFEST.in README.module examples/
%python3_sitelibdir/*

%changelog
* Mon Sep 30 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.7110-alt2
- drop python2 module

* Thu Aug 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.7110-alt1
- New version

* Sun Jul 21 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.6109-alt1
- New version

* Wed Sep 12 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.0.102-alt1
- Init build to Sisyphus

