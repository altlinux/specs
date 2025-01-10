%define APP_ID io.github.diegoivanme.flowtime
#Validate appstream file FAIL
%def_disable check

Name: flowtime
Version: 6.5
Release: alt1

Summary: Spend your time wisely
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/Diego-Ivan/Flowtime
Vcs: https://github.com/Diego-Ivan/Flowtime
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libportal-gtk4)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libgio
%endif

%description
The Pomodoro technique is efficient for tasks you find boring, but having
to take a break when you are 100 percent concentrated in something you like
might be annoying. That's why the Flowtime technique exists: take appropriate
breaks without losing your flow.

Instead of strict work and break times, you work as long as you wish and your
break is a portion of how long you worked (by default, 20 percent). For example,
if you work for an hour, your break is 12 minutes. This lets you concentrate
on your work and take appropriate breaks when convenient without a rigid
schedule.

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
%_datadir/appdata/%APP_ID.appdata.xml
%_desktopdir/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg

%changelog
* Wed Jan 08 2025 Oleg Shchavelev <oleg@altlinux.org> 6.5-alt1
- Initial build
