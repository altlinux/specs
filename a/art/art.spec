%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: art
# NOTE: run
#       ./tools/generateReleaseInfo
#       on each update
Version: 1.26.6
Release: alt1

Summary: Advanced raw photo development program
License: GPL-3.0-or-later
Group: Graphics
Url: https://artraweditor.github.io
Vcs: https://github.com/artpixls/ART

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(lensfun)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libturbojpeg)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(mimalloc)
BuildRequires: pkgconfig(libraw_r)
BuildRequires: pkgconfig(OpenColorIO)
BuildRequires: pkgconfig(OpenEXR)

Requires: art-data

%description
ART, a free, open-source, raw image processing program. ART
is a derivative of the popular RawTherapee, trading a bit of
customization and control over various processing parameters for
a simpler and (hopefully) easier to use interface, while still
maintaining the power and quality of RawTherapee.

%package data
Summary: Advanced raw photo development program - data files
Group: Graphics
BuildArch: noarch

%description data
ART, a free, open-source, raw image processing program. ART
is a derivative of the popular RawTherapee, trading a bit of
customization and control over various processing parameters for
a simpler and (hopefully) easier to use interface, while still
maintaining the power and quality of RawTherapee.

This package contains the architecture independent data files.

%prep
%setup
%patch -p1
sed -i "s/sisyphus/master/" ReleaseInfo.cmake

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %{name}.lang
%doc README.md
%_bindir/ART
%_bindir/ART-cli
%_desktopdir/ART.desktop
%_iconsdir/hicolor/*/apps/ART.png
%_man1dir/ART.1.*
%_datadir/metainfo/us.pixls.art.ART.metainfo.xml

%files data
%dir %_datadir/ART
%_datadir/ART/*
%_datadir/doc/ART/AUTHORS.txt
%_datadir/doc/ART/AboutThisBuild.txt
%_datadir/doc/ART/LICENSE.txt
%_datadir/doc/ART/RELEASE_NOTES.txt

%changelog
* Tue Jun 16 2026 Nikolay Strelkov <snk@altlinux.org> 1.26.6-alt1
- New version 1.26.6.

* Sat May 30 2026 Nikolay Strelkov <snk@altlinux.org> 1.26.5-alt1
- New version 1.26.5.

* Fri May 01 2026 Nikolay Strelkov <snk@altlinux.org> 1.26.4-alt1
- New version 1.26.4.

* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 1.26.3-alt1
- New version 1.26.3.

* Tue Feb 24 2026 Nikolay Strelkov <snk@altlinux.org> 1.26.2-alt1
- Initial build for Sisyphus
