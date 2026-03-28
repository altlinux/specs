%define _unpackaged_files_terminate_build 1

%define appname io.github.ellie_commons.reminduck

Name: reminduck
Version: 2.3.1.5
Release: alt1

Summary: Remember your stuff in an adorably annoying way
License: GPL-3.0-or-later
Group: Office
Url: https://github.com/ellie-commons/reminduck

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libportal)

%description
A simple reminder app made to be quick and easy - Reminduck focuses on simple
or recurrent reminders with set time and date and nothing else.

It's perfect if all you want are simple or daily/weekly/monthly reminders.
Anything more than that is not achievable by Reminduck right now - but you
can help! Open an issue or a pull request if you have any ideas or requests.

And it quacks.

%prep
%setup
sed -i "s|data/icons/hicolor/128.png|/usr/share/icons/hicolor/128x128/apps/%{appname}.png|" README.md
sed -i "s|Categories=.*|Categories=Office;ProjectManagement;|" data/reminduck.desktop.in
sed -i "s|data/screenshots/||" README.md

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md data/screenshots/Welcome.png
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{name}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.png
%_iconsdir/scalable/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sat Mar 28 2026 Nikolay Strelkov <snk@altlinux.org> 2.3.1.5-alt1
- New version 2.3.1.5.

* Thu Jan 15 2026 Nikolay Strelkov <snk@altlinux.org> 2.3.1-alt1
- New version 2.3.1.

* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 2.3.0-alt1
- New version 2.3.0.

* Fri Dec 26 2025 Nikolay Strelkov <snk@altlinux.org> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Tue Dec 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.6.2-alt1
- Initial build for Sisyphus
