%define _unpackaged_files_terminate_build 1

Name:    epsonscan2
Version: 6.7.66.0
Release: alt1

Summary: Simple Image Acquisition for Epson scanners and MFP
License: GPL-3.0+
Group:   Publishing
Url:     https://support.epson.net/linux/en/epsonscan2.php

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version-1.src.tar.gz
Source1: %name.watch
Patch1: epsonscan2-alt-return-type.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-interprocess-devel
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: libpng-devel
BuildRequires: libsane-devel
BuildRequires: rapidjson
BuildRequires: libusb-devel
BuildRequires: qt5-base-devel

%description
This software provides applications to easily turn hard-copy documents and
imagery into formats that are more amenable to computer processing.

Included are a native driver for a number of EPSON scanners and a compatibility
driver to interface with software built around the SANE standard.

%prep
%setup -n %name-%version-1
%patch1 -p2
subst 's|${EPSON_INSTALL_ROOT}/lib/udev|%_udevdir|' CMakeLists.txt

%build
%cmake -GNinja \
       -Wno-dev \
       -DCMAKE_SKIP_RPATH=OFF \
       -DCMAKE_SKIP_INSTALL_RPATH=OFF

%ninja_build  -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
# Remove copy of documentation
rm -rf %buildroot%_defaultdocdir/epsonscan2-1.0.0.0-1

%files
%doc AUTHORS NEWS README
%_bindir/epsonscan2
%_libdir/epsonscan2
%config(noreplace) %_sysconfdir/sane.d/dll.d/epsonscan2
%_udevrulesdir/60-epsonscan2.rules

%changelog
* Thu Sep 12 2024 Andrey Cherepanov <cas@altlinux.org> 6.7.66.0-alt1
- New version.

* Wed Jun 19 2024 Andrey Cherepanov <cas@altlinux.org> 6.7.65.0-alt1
- New version (ALT #49660).

* Fri Mar 17 2023 Andrey Cherepanov <cas@altlinux.org> 6.7.43.0-alt1
- New version.

* Sat Feb 04 2023 Andrey Cherepanov <cas@altlinux.org> 6.7.42.0-alt1
- New version.

* Tue Nov 22 2022 Andrey Cherepanov <cas@altlinux.org> 6.7.0.0-alt1
- New version.

* Sun Jul 10 2022 Andrey Cherepanov <cas@altlinux.org> 6.6.42.0-alt1
- New version.

* Sun Jun 05 2022 Andrey Cherepanov <cas@altlinux.org> 6.6.41.0-alt1
- New version.

* Wed May 11 2022 Andrey Cherepanov <cas@altlinux.org> 6.6.40.0-alt1
- Initial build in Sisyphus (ALT #42634).
