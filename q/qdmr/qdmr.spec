
Name: qdmr
Version: 0.15.1
Release: alt1

Summary: GUI application and command-line-tool to program DMR radios
License: GPLv3+
Group: Engineering

Url: https://dm3mat.darc.de/qdmr
Vcs: https://github.com/hmatuschek/qdmr.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libusb-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-location-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-serialport-devel
BuildRequires: qt6-tools-devel

BuildRequires: findutils
BuildRequires: librsvg-utils

%description
QDMR is a friendly code-plug programming software for DMR radios.
QDMR supports radios by several vendors, and stores code-plug in
a human readable format.

%package -n libdmrconf
Summary: DMR radios programming library
Group: System/Libraries

%description -n libdmrconf
QDMR is a friendly code-plug programming software for DMR radios.
libdmrconf handles the actual programming of radios via UART and
conversion of code-plug between human readable and vendor-specific
binary formats.

%package -n libdmrconf-devel
Summary: DMR radios programming library - development files
Group: Development/KDE and QT
Requires: qt6-base-devel
Requires: libyaml-cpp-devel

%description -n libdmrconf-devel
QDMR is a friendly code-plug programming software for DMR radios.
libdmrconf handles the actual programming of radios via UART and
conversion of code-plug between human readable and vendor-specific
binary formats. This package is useful for developing software
with libdmrconf. It is not required for QDMR users.

%prep
%setup

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DINSTALL_UDEV_RULES:BOOL=ON \
  -DINSTALL_UDEV_PATH:STRING=%_udevrulesdir \
  %nil

%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_bindir/qdmr
%_bindir/dmrconf
%_udevrulesdir/*
%_datadir/icons/hicolor/*x*/apps/qdmr.png
%_datadir/applications/qdmr.desktop
%_datadir/metainfo/*.metainfo.xml

%files -n libdmrconf
%prefix/%_lib/libdmrconf.so.*

%files -n libdmrconf-devel
%prefix/%_lib/libdmrconf.so
%prefix/include/libdmrconf/*.hh
%prefix/include/libdmrconf/*.h

%changelog
* Tue Jun 23 2026 Ivan A. Melnikov <iv@altlinux.org> 0.15.1-alt1
- v0.15.1.

* Tue May 12 2026 Ivan A. Melnikov <iv@altlinux.org> 0.15.0-alt1
- v0.15.0.

* Tue Apr 07 2026 Ivan A. Melnikov <iv@altlinux.org> 0.14.1-alt1
- v0.14.1.

* Thu Mar 26 2026 Ivan A. Melnikov <iv@altlinux.org> 0.14.0-alt1
- v0.14.0.

* Tue Jan 20 2026 Ivan A. Melnikov <iv@altlinux.org> 0.13.3-alt1
- v0.13.3.

* Mon Dec 01 2025 Ivan A. Melnikov <iv@altlinux.org> 0.13.2-alt1
- v0.13.2.

* Fri Nov 28 2025 Ivan A. Melnikov <iv@altlinux.org> 0.13.1-alt1
- v0.13.1.

* Sun Jun 01 2025 Ivan A. Melnikov <iv@altlinux.org> 0.12.3-alt1
- v0.12.3.

* Fri Feb 07 2025 Ivan A. Melnikov <iv@altlinux.org> 0.12.1-alt1
- v0.12.1 (ALT#52751).

* Wed Aug 16 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.11.3-alt1
- v0.11.3, amongst other things
  + Fixed crash on missing access rights for TyT devices
  + Fixed encoding for AnyTone devices (programmable keys, mic gain, etc)

* Thu Mar 30 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.11.2-alt2
- Relocated udev rules to /lib/udev, no functional changes intended

* Wed Feb 08 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.11.2-alt1
- v0.11.2, amongst other things
  + BTECH DMR-6X2UV support
  + Call-sign DB for BTECH DM-1701, Retevis RT-84

* Wed Nov 30 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.10.4-alt1
- v0.10.3
- Amongst other things fixes detection of DM-1701

* Sun May 22 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.10.2.2-alt1
- Initial build
