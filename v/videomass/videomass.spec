%define _unpackaged_files_terminate_build 1

Name: videomass
Release: alt1
Version: 6.1.20

Summary: Videomass is a free, open source and cross-platform GUI for FFmpeg
Group: Video
License: GPL-3.0-or-later
Url: https://jeanslack.github.io/Videomass
VCS: https://github.com/jeanslack/Videomass

Requires: ffmpeg
Requires: ffplay

BuildArch: noarch

# Source-url: https://github.com/jeanslack/Videomass/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-babel
BuildRequires: python3-module-distutils-extra
BuildRequires: python3-module-hatchling

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%__mv %buildroot%_desktopdir/{io.github.jeanslack.videomass.desktop,%name.desktop}

%check
%pyproject_run_pytest -Wignore --ignore=tests/test_display_GUI.py

%files
%doc AUTHORS CHANGELOG INSTALL README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/*.png
%_liconsdir/*.xpm
%_iconsdir/hicolor/**/**/*.png
%_iconsdir/hicolor/**/**/*.svg
%_pixmapsdir/%name.png
%_man1dir/%name.1*
%_datadir/metainfo/*.xml
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}

%changelog
* Sat Nov 01 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 6.1.20-alt1
- initial build for ALT Linux
