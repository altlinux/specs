%define APP_ID io.github.nokse22.Exhibit
# SPDX-License-Identifier: GPL-3.0-or-later

Name:    exhibit
Version: 1.5.0
Release: alt1.e08cb9b.1

Summary: 3D models viewer
License: GPL-3.0-or-later
Group:   Graphics
Url:     https://github.com/Nokse22/Exhibit
VCS:     https://github.com/Nokse22/Exhibit

BuildArch: noarch

Source: %name-%version.tar

Patch1: config_path.patch
Patch2: meson_build.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3

BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: libgtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: %_bindir/appstreamcli desktop-file-utils blueprint-compiler
BuildRequires: itstool
BuildRequires: gettext-tools

Requires: libEGL-devel


%description
View 3D models, powered by the F3D library that supports many file formats,
from digital content to scientific datasets (including glTF, USD, STL, STEP,
PLY, OBJ, FBX, Alembic).

%prep
%setup -q

%patch1 -p1
%patch2 -p1

%build
%meson
%meson_build

%install

%meson_install
%find_lang %name

%files -f %name.lang
%doc *.md
%python3_sitelibdir/%name
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/help/C/%name
%_datadir/%name
%_datadir/mime/*
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*
%_datadir/metainfo/%APP_ID.metainfo.xml


%changelog
* Mon Apr 29 2025 Valentin Sokolov <sova@altlinux.org> 1.5.0-alt1.e08cb9b.1
- Initial build for Sisyphus
