%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name smile
%define ver_major 2.12
%define rdn_name it.mijorus.smile

# <screenshot> height too large
%def_disable check

Name: %_name
Version: %ver_major.3
Release: alt1

Summary: An emoji picker
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/mijorus/smile

Vcs: https://github.com/mijorus/smile.git

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: %url/archive/%version/%_name-%version.tar.gz
%endif

BuildArch: noarch
%add_python3_path %_datadir/%_name

%define adw_ver 1.8

Requires: python3-module-pygobject3
Requires: dconf font(notocoloremoji)
Requires: typelib(Adw) = 1
Requires: /usr/bin/wl-copy

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson
BuildRequires: libgio-devel
BuildRequires: /usr/bin/glib-compile-resources /usr/bin/gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils /usr/bin/glib-compile-schemas}

%description
An emoji picker for linux, with custom tags support and localization.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
ln -sf ../../fonts/ttf/google-noto-emoji/NotoColorEmoji.ttf \
%buildroot%_datadir/%name/assets/NotoColorEmoji.ttf

%find_lang %name

%check
%__meson_test -v

%files -f %name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*

%changelog
* Thu Apr 23 2026 Yuri N. Sedunov <aris@altlinux.org> 2.12.3-alt1
- 2.12.3

* Thu Apr 09 2026 Yuri N. Sedunov <aris@altlinux.org> 2.12.2-alt1
- 2.12.2

* Fri Apr 03 2026 Yuri N. Sedunov <aris@altlinux.org> 2.12.1-alt1
- 2.12.1

* Fri Dec 19 2025 Yuri N. Sedunov <aris@altlinux.org> 2.11.0-alt1
- 2.11.0

* Wed Sep 10 2025 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt1
- 2.10.2

* Fri Jan 03 2025 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- 2.10.1

* Tue May 07 2024 Yuri N. Sedunov <aris@altlinux.org> 2.9.5-alt1
- 2.9.5

* Fri Apr 05 2024 Yuri N. Sedunov <aris@altlinux.org> 2.9.4-alt1
- 2.9.4

* Sun Mar 10 2024 Yuri N. Sedunov <aris@altlinux.org> 2.9.2-alt1
- 2.9.2

* Wed Mar 06 2024 Yuri N. Sedunov <aris@altlinux.org> 2.9.1-alt1
- 2.9.1

* Thu Dec 21 2023 Yuri N. Sedunov <aris@altlinux.org> 2.9.0-alt1
- 2.9.0

* Wed Oct 11 2023 Yuri N. Sedunov <aris@altlinux.org> 2.8.2-alt1
- first build for Sisyphus

