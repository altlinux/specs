%define APP_ID io.github.leolost2605.gradebook
%def_enable check

Name: gradebook
Version: 1.2
Release: alt1

Summary: Keep track of your grades
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/leolost2605/Gradebook
Vcs: https://github.com/leolost2605/Gradebook
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)

%description
Gradebook is a simple tool that helps you keep track of your grades. This way
you always know how you are doing in your courses.

Features:

- Support for numerical and percentage systems
- Assign your grades to categories with different weighting
- Add notes to your grades so that you later know how you could improve
- Your average is calculated automatically taking the weighting of the different
  categories into account

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %APP_ID

%check
%meson_test

%files -f %APP_ID.lang
%_bindir/%APP_ID
%_desktopdir/%APP_ID.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Wed Feb 12 2025 Oleg Shchavelev <oleg@altlinux.org> 1.2-alt1
- Initial build
