%define _unpackaged_files_terminate_build 1
%define oname dev.mohfy.quizbite

Name: quizbite
Version: 2.0.9
Release: alt1

Summary: Informative quizzes, bite sized
License: GPL-3.0-or-later
Group: Education

Url: https://github.com/mohfy/quizbite
Vcs: https://github.com/mohfy/quizbite

BuildArch: noarch
AutoProv: nopython3

Source: %name-%version.tar

%add_python3_path %_datadir/%name/%name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson pkgconfig(gtk4) pkgconfig(libadwaita-1) typelib(Adw)
BuildRequires: blueprint-compiler /usr/bin/appstreamcli

%description
%summary.

Features:
Create quizzes with multiple choice questions.
add images to question.
Import and export .quiz files.
Import Flashcards and play them.
Export a quiz or flashcards to PDF.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang --all-name %name

%files -f %name.lang
%doc *.md COPYING
%_bindir/%name
%_desktopdir/%oname.desktop
%_datadir/dbus-1/services/%oname.service
%_datadir/glib-2.0/schemas/%oname.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%oname.metainfo.xml
%_datadir/%name

%changelog
* Mon Jul 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.0.9-alt1
- Initial build for ALT Linux.

