%define APP_ID net.kirgroup.confy
%def_enable check

Name: confy
Version: 0.8.0
Release: alt1

Summary: Conference schedules viewer
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://confy.kirgroup.net
Vcs: https://git.sr.ht/~fabrixxm/confy
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: blueprint-compiler
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libgio
%endif

BuildArch: noarch

%description
Confy lets you browse conference schedules.

Browse talks by day, track or room. Select the talks you are interested
in and receive notification when they are about to start. View when
two or more talks you are interested in overlap.

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
%python3_sitelibdir_noarch/%name
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/%name
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Sat Jan 11 2025 Oleg Shchavelev <oleg@altlinux.org> 0.8.0-alt1
- Initial build
