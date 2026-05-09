%define _unpackaged_files_terminate_build 1

Name: symbolical
Version: 0.5.0.5
Release: alt1

Summary: Math document application
License: GPL-3.0-or-later
Group: Sciences/Mathematics
Url: https://gitlab.com/symbolical/symbolical

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-python3

Requires: fonts-ttf-google-noto-serif

%filter_from_requires /python3(gui)/d
%filter_from_requires /python3(gui.MainWindow)/d
%filter_from_requires /python3(model.Document)/d

BuildArch: noarch

%description
This is a document application that provides features for mathematics.
It is inspired by the applications MathCAD and SMath, but it is not
entirely like them. The goal of this application is to provide an
easy-to- use interface for doing mathematical expressions and
evaluations both numerically and symbolically. The Mathematical
expressions include built functions like sin, tan and log while also
providing an easy way to make new functions. There is also a Unit
feature that grants the user the ability to make their own units.

%prep
%setup
sed -i "s|join_paths(prefix, 'symbolical')|join_paths(datadir, 'symbolical')|" meson.build
sed -i "s|join_paths(get_option('prefix'), 'symbolical/src')|join_paths(datadir, 'symbolical/src')|" meson.build
sed -i "s|Categories=.*|Categories=Science;Math;|" flatpak/dk.pracedru.Symbolical.desktop

%build
%meson
%meson_build

%install
%meson_install
sed -i "s| share/symbolical/src/main.py| /usr/share/symbolical/src/main.py|" %buildroot%_bindir/symbolical

%files
%doc LICENSE README.md
%_bindir/symbolical
%_desktopdir/*.desktop
%_iconsdir/hicolor/256x256/apps/dk.pracedru.Symbolical.png
%_iconsdir/hicolor/scalable/mimetypes/symbolical-file.svg
%_datadir/metainfo/dk.pracedru.Symbolical.metainfo.xml
%_datadir/mime/packages/dk.pracedru.Symbolical.xml
%dir %_datadir/symbolical
%_datadir/symbolical/*
%exclude %_datadir/fonts/NotoSerif.ttf
%exclude %_iconsdir/hicolor/index.theme
%exclude %_datadir/licenses/symbolical

%changelog
* Sat May 09 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.0.5-alt1
- Initial build for Sisyphus
