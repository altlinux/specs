%define _unpackaged_files_terminate_build 1

Name: dsview
Version: 1.3.2
Release: alt1

Summary: GUI for DreamSourceLab USB-based instruments
License: GPL-3.0
Group: Engineering
URL: http://www.dreamsourcelab.com/
VCS: https://github.com/DreamSourceLab/DSView

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: python3-devel
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: qt5-base-devel
BuildRequires: boost-devel

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
DSView is a GUI program for supporting various instruments from
DreamSourceLab, including logic analyzers, oscilloscopes, etc. 

%prep
%setup -n %name-%version
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc COPYING NEWS* README.md
%_bindir/*
%_udevrulesdir/60-dreamsourcelab.rules
%dir %_datadir/DSView
/usr/share/DSView/*
%_desktopdir/*.desktop
%dir %_datadir/libsigrokdecode4DSL
%_datadir/libsigrokdecode4DSL/*
%_pixmapsdir/*
%_iconsdir/hicolor/*/*/*

%changelog
* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus
