%define _unpackaged_files_terminate_build 1

Name: x-tile
Version: 3.3
Release: alt1

Summary: Tile selected windows in different ways
License: GPL-2.0
Group: Graphical desktop/Other
URL: https://github.com/giuspen/x-tile

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%filter_from_requires /python3(cons)/d
%filter_from_requires /python3(core)/d
%filter_from_requires /python3(globs)/d

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
X-tile is an application that allows you to select a number of
windows and tile them in different ways. Works on any X desktop.

Main features include:
* Several tiling geometries
* Undo tiling
* Invert tiling order
* Optional system tray docking and menu
* Filter to exclude windows
* Filter to include windows by default
* Command line interface

%prep
%setup -n %name-%version
%patch -p1

%build
mkdir -p build/scripts-%{__python3_version}/
%python3_build

%install
%python3_install
install -Dpm 0755 %name  %buildroot/%_bindir/%name

%find_lang %name

%files -f %name.lang
%doc license
%_bindir/%name
%_man1dir/%name.1*
%python3_sitelibdir/X_Tile-*.egg-info
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/applications/%{name}.desktop
%_datadir/icons/hicolor/*/apps/%{name}.*

%changelog
* Wed Mar 12 2025 Nikolay Strelkov <snk@altlinux.org> 3.3-alt1
- Initial build for Sisyphus
