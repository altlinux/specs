Name:    OpenComposite
Version: 1.0.1521
Release: alt1

Summary: Reimplementation of OpenVR, translating calls to OpenXR
License: BSD-2-Clause
Group:   Games/Other
Url:     https://gitlab.com/znixian/OpenOVR

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libvulkan-devel libglvnd-devel

ExclusiveArch: x86_64

%description
OpenComposite OpenXR (previously known as OpenOVR - OpenVR for OculusVR - but
renamed due to confusion with OpenVR) is an implementation of SteamVR's API - OpenVR,
forwarding calls directly to the OpenXR runtime. Think of it as a backwards version
of ReVive, for the OpenXR compatible headsets.
This allows you to play SteamVR-based games on an OpenXR compatible headset as though
they were native titles, without the use of SteamVR!

%prep
%setup -a1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo

%cmake_build

%install
%cmake_install

mkdir -p %buildroot%_libdir/OpenComposite/
mv -v %buildroot/usr/OpenComposite/bin/linux64/vrclient.so %buildroot%_libdir/OpenComposite/vrclient.so
rm -rf %buildroot/usr/OpenComposite/bin/version.txt
rm -rf %buildroot/usr/OpenComposite/openvrpaths.vrpath

%files
%doc LICENCE* LICENSE* README.*
%dir %_libdir/%name/
%_libdir/%name/vrclient.so

%changelog
* Tue May 26 2026 Sergey Palcheh <minergenon@altlinux.org> 1.0.1521-alt1
- new version (1.0.1521)

* Sat Mar 15 2025 Sergey Palcheh <minergenon@altlinux.org> 1.0.1506-alt1
- initial build for ALT Sisyphus

