%def_disable snapshot

%define _name time-tracker
%define __name TimeTracker
%define ver_major 1.1
%define rdn_name com.lynnmichaelmartin.%__name

%def_enable check

Name: %_name
Version: %ver_major.8
Release: alt1

Summary: Time Tracker for GNOME
License: MIT
Group: Graphical desktop/GNOME
Url: https://github.com/elvishcraftsman/time-tracker

Vcs: https://github.com/elvishcraftsman/time-tracker.git

%if_disabled snapshot
Source: https://github.com/elvishcraftsman/time-tracker/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildArch: noarch

Requires: /usr/bin/gjs dconf
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson /usr/bin/gjs
BuildRequires: typelib(Adw)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
A simple time-tracker program for GNOME.

Instead of using online-first options like Toggl and Clockify, use a
lightning-fast local-first option that is still able to sync with
multiple computers via cloud or network storage.

Time Tracker allows you to track different projects, see how much time
you've spent on each project, and sync with a local file or a file in
your own cloud storage. You can also open your sync file in spreadsheet
software (since it's a CSV file).

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/metainfo/%rdn_name.*.xml
%doc README*

%changelog
* Fri Jul 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.8-alt1
- first build for Sisyphus


