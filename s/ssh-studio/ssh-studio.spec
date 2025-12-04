%define _unpackaged_files_terminate_build 1
%define app_id io.github.BuddySirJava.SSH-Studio

Name: ssh-studio
Version: 1.3.1
Release: alt1
Summary: GUI SSH config editor and validator.
Group: Networking/Remote access
License: GPL-3.0-or-later
Url: https://github.com/BuddySirJava/SSH-Studio
Vcs: https://github.com/BuddySirJava/SSH-Studio

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rpm-build-python3
BuildRequires: blueprint-compiler
BuildRequires: libgtksourceview5-devel

%description
Easy, GUI SSH config editor and validator built with Python,
GTK 4 and libadwaita.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install	
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir/ssh_studio/*
%_datadir/%app_id/ssh-studio-resources.gresource
%_datadir/applications/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/scalable/apps/%app_id.svg
%_iconsdir/hicolor/*x*/apps/%app_id.png

%changelog
* Thu Nov 27 2025 Vladislav Petrukhin <vladp@altlinux.org> 1.3.1-alt1
- Initial build.
