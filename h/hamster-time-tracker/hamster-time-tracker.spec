%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%def_with check

Name: hamster-time-tracker
Version: 3.0.3
Release: alt1

Summary: time tracking application for GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
URL: https://github.com/projecthamster/hamster

BuildRequires(pre): rpm-build-python3

BuildRequires: waf
BuildRequires: intltool
BuildRequires: itstool

%if_with check
BuildRequires: /usr/bin/glib-compile-schemas
BuildRequires: /usr/bin/dbus-run-session
BuildRequires: /usr/bin/xvfb-run
BuildRequires: python3(gi)
BuildRequires: python3(dbus)
BuildRequires: libgtk+3-gir-devel
%endif

BuildArch: noarch

Source: %name-%version.tar

# sync with version 3.0.3-3 from Debian unstable
Patch: %name-%version-%release.patch

%description
Project Hamster helps you to keep track of how much time you spend on various
activities during the day.  Whenever you move from one task to another, you
can change your current activity, or you can record time spent afterwards.

It can present graphical statistics of how long you have spent on each task,
and may be useful for project management or keeping employee timesheets.

This package contains the background daemon and GNOME application.

%prep
%setup
%patch -p1
sed -i "s/Categories=.*/Categories=GNOME;GTK;Office;ProjectManagement;/" data/org.gnome.Hamster.GUI.desktop.in

%build
%__python3 ./waf configure --prefix=%{_prefix} --libdir=%{_libdir} --skip-gsettings --skip-icon-cache-update
%__python3 ./waf build

%install
%__python3 ./waf install --destdir=%{buildroot}

install -Dm644 -t %buildroot%_datadir/glib-2.0/schemas ./data/org.gnome.hamster.gschema.xml

%find_lang %name --all-name

%check
export XDG_RUNTIME_DIR="%buildroot"
export GSETTINGS_SCHEMA_DIR="%buildroot%_datadir/glib-2.0/schemas"
install -Dm644 -t %buildroot%_datadir/glib-2.0/schemas ./data/org.gnome.hamster.gschema.xml
glib-compile-schemas "%buildroot%_datadir/glib-2.0/schemas"
dbus-run-session xvfb-run %__python3 -m unittest

rm -rfv %buildroot/dconf/user
rm -rfv %buildroot%_datadir/glib-2.0/schemas/gschemas.compiled

%files -f %{name}.lang
%doc AUTHORS COPYING MAINTAINERS NEWS.md README.md screenshot.png
%_bindir/hamster
%_desktopdir/org.gnome.Hamster.GUI.desktop
%dir %_libexecdir/hamster
%_libexecdir/hamster/hamster-service
%_libexecdir/hamster/hamster-windows-service
%_datadir/bash-completion/completions/hamster.bash
%_datadir/dbus-1/services/org.gnome.Hamster.GUI.service
%_datadir/dbus-1/services/org.gnome.Hamster.WindowServer.service
%_datadir/dbus-1/services/org.gnome.Hamster.service
%_datadir/glib-2.0/schemas/org.gnome.hamster.gschema.xml
%_datadir/metainfo/org.gnome.Hamster.metainfo.xml
%_iconsdir/hicolor/16x16/apps/org.gnome.Hamster.GUI.png
%_iconsdir/hicolor/22x22/apps/org.gnome.Hamster.GUI.png
%_iconsdir/hicolor/24x24/apps/org.gnome.Hamster.GUI.png
%_iconsdir/hicolor/32x32/apps/org.gnome.Hamster.GUI.png
%_iconsdir/hicolor/48x48/apps/org.gnome.Hamster.GUI.png
%_iconsdir/hicolor/scalable/apps/org.gnome.Hamster.GUI.svg
%python3_sitelibdir/hamster/
%dir %_datadir/hamster
%dir %_datadir/hamster/art
%_datadir/hamster/*
%dir %_datadir/help/C/hamster/
%_datadir/help/C/hamster/*
%dir %_datadir/help/cs/hamster/
%_datadir/help/cs/hamster/*
%dir %_datadir/help/da/hamster/
%_datadir/help/da/hamster/*
%dir %_datadir/help/de/hamster/
%_datadir/help/de/hamster/*
%dir %_datadir/help/el/hamster/
%_datadir/help/el/hamster/*
%dir %_datadir/help/es/hamster/
%_datadir/help/es/hamster/*
%dir %_datadir/help/fa/hamster/
%_datadir/help/fa/hamster/*
%dir %_datadir/help/fr/hamster/
%_datadir/help/fr/hamster/*
%dir %_datadir/help/gl/hamster/
%_datadir/help/gl/hamster/*
%dir %_datadir/help/hu/hamster/
%_datadir/help/hu/hamster/*
%dir %_datadir/help/pl/hamster/
%_datadir/help/pl/hamster/*
%dir %_datadir/help/pt_BR/hamster/
%_datadir/help/pt_BR/hamster/*
%dir %_datadir/help/ro/hamster/
%_datadir/help/ro/hamster/*
%dir %_datadir/help/ru/hamster/
%_datadir/help/ru/hamster/*
%dir %_datadir/help/sl/hamster/
%_datadir/help/sl/hamster/*
%dir %_datadir/help/te/hamster/
%_datadir/help/te/hamster/*
%dir %_datadir/help/zh_CN/hamster/
%_datadir/help/zh_CN/hamster/*
%dir %_datadir/help/zh_HK/hamster/
%_datadir/help/zh_HK/hamster/*
%dir %_datadir/help/zh_TW/hamster/
%_datadir/help/zh_TW/hamster/*

%changelog
* Sat Dec 06 2025 Nikolay Strelkov <snk@altlinux.org> 3.0.3-alt1
- Initial build for Sisyphus
