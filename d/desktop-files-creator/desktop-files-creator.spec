%def_enable snapshot

%define _name desktop-files-creator
%define ver_major 1.2
%define rdn_name com.github.alexkdeveloper.%name

# bad appdata
%def_disable check

Name: %_name
Version: %ver_major.7
Release: alt1

Summary: Desktop Files Creator
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/alexkdeveloper/desktop-files-creator

Vcs: https://github.com/alexkdeveloper/desktop-files-creator.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

%define adw_ver 1.0.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils /usr/bin/glib-compile-schemas}

%description
The application allows you to create desktop files in GNU/Linux distributions.

%prep
%setup -n %{?_enable_snapshot:%name}%{?_disable_snapshot:%_name}-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*


%changelog
* Tue Jul 02 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.7-alt1
- first build for Sisyphus (1.2.7-3-gdfd0ff8)


