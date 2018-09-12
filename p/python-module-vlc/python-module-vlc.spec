%define oname vlc

Name: python-module-%oname
Version: 3.0.102
Release: alt1

Summary: Binding for the native libvlc API.
License: GPL
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

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc COPYING MANIFEST.in README.module examples/
%python_sitelibdir/*

%files -n python3-module-%oname
%doc COPYING MANIFEST.in README.module examples/
%python3_sitelibdir/*


%changelog
* Wed Sep 12 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.0.102-alt1
- Init build to Sisyphus

