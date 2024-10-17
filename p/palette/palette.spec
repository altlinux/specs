%define APP_ID org.gnome.design.Palette
%def_enable check

Name: palette
Version: 2.0.3
Release: alt1

Summary: Color Palette tool
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/World/design/palette
Vcs: https://gitlab.gnome.org/World/design/palette
Source0: %name-%version.tar
# Merge the submodule HIG-app-icons with application icons
# Vcs: https://gitlab.gnome.org/Teams/Design/HIG-app-icons
Source1: HIG-app-icons.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: rpm-build-gir
BuildRequires: rpm-build-vala
BuildRequires: pkgconfig(libadwaita-1)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
%endif

%description
Tool for viewing the GNOME color palette as defined by the design guidelines.

%prep
%setup -a1

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %APP_ID

%check
%__meson_test

%files -f %APP_ID.lang
%_bindir/%APP_ID
%_desktopdir/%APP_ID.desktop
%_datadir/dbus-1/services/%APP_ID.service
%_datadir/icons/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%{APP_ID}.metainfo.xml

%changelog
* Tue Oct 15 2024 Oleg Shchavelev <oleg@altlinux.org> 2.0.3-alt1
- Initial build
