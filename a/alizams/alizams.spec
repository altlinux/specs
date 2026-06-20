%define _unpackaged_files_terminate_build 1

Name: alizams
Version: 1.10.0
Release: alt2

Summary: DICOM Viewer
License: GPL-3.0
Group: Sciences/Medicine
VCS: https://github.com/AlizaMedicalImaging/AlizaMS
Url: https://www.aliza-dicom-viewer.com/

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(opengl)
BuildRequires: pkgconfig(charls)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(bullet)
BuildRequires: pkgconfig(fmt)
BuildRequires: libitk-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-5compat-devel

%description
A 2D and 3D DICOM viewer with many tools and very fast directory scanner
and DICOMDIR support. It can consistently de-identify DICOM files.

The list of features includes:

- 2D and 3D views with many tools;
- 3D view also for non-uniform images;
- Volume Rendering;
- Multi-planar reconstruction (MPR);
- Fast directory scanner, DICOMDIR;
- Consistently de-identify DICOM, maintain integrity;
- RTSTRUCT contours;
- DICOM Study multi-view with intersection lines and side-by-side view;
- Proper measurement in Ultrasound Calibrated Regions;
- 2D+t and 3D+t animations;
- DICOM metadata viewer, DICOM 2024b dictionary;
- Encapsulated transfer syntaxes incl. HTJ2K;
- Most IODs are supported incl. Structured Reports, Key Objects
  Selection, Grayscale Softcopy Presentation State

%prep
%setup
sed -i "s|^Categories=.*|Categories=Science;MedicalSoftware;|" package/archive/usr/share/applications/alizams.desktop

%build
%cmake \
       -Wno-dev \
       -DCMAKE_BUILD_TYPE=Release \
       -DALIZA_QT_VERSION:STRING=6 \
       -DALIZA_USE_SYSTEM_BULLET:BOOL=OFF \
       -DALIZA_USE_SYSTEM_LCMS2:BOOL=ON \
       -DMDCM_USE_SYSTEM_UUID:BOOL=ON \
       -DMDCM_USE_SYSTEM_ZLIB:BOOL=ON \
       -DMDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
       -DMDCM_USE_SYSTEM_CHARLS:BOOL=ON \
%ifnarch x86_64 aarch64
       -DALIZA_DISABLE_SIMDMATH:BOOL=ON \
%endif
       -DCMAKE_INSTALL_PREFIX=%_prefix
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/*
%_man1dir/*
%_desktopdir/*
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml

%changelog
* Sat Jun 20 2026 Nikolay Strelkov <snk@altlinux.org> 1.10.0-alt2
- Fixed FTBFS.

* Mon Jun 08 2026 Nikolay Strelkov <snk@altlinux.org> 1.10.0-alt1
- New version 1.10.0.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 1.9.11-alt1
- New version 1.9.11.

* Sat Sep 06 2025 Nikolay Strelkov <snk@altlinux.org> 1.9.10-alt2
- Define DISABLE_SIMDMATH=ON only on necessary architectures.

* Wed Jul 02 2025 Nikolay Strelkov <snk@altlinux.org> 1.9.10-alt1
- Initial build for Sisyphus
