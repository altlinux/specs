%define _unpackaged_files_terminate_build 1

%define appname com.github.matfantinel.reminduck

Name: reminduck
Version: 1.6.2
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
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(granite)
BuildRequires: vapi(granite)

%description
A simple reminder app made to be quick and easy - Reminduck focuses on simple
or recurrent reminders with set time and date and nothing else.

It's perfect if all you want are simple or daily/weekly/monthly reminders.
Anything more than that is not achievable by Reminduck right now - but you
can help! Open an issue or a pull request if you have any ideas or requests.

And it quacks.

%prep
%setup
sed -i "s|Categories=.*|Categories=Office;ProjectManagement;|" data/com.github.matfantinel.reminduck.desktop.in
sed -i "s|data/screenshots/||" README.md

patch -p1 < elementary-theme.patch

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md data/screenshots/Main.png
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/com.github.matfantinel.reminduck.appdata.xml

%changelog
* Tue Dec 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.6.2-alt1
- Initial build for Sisyphus
