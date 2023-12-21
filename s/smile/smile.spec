%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name smile
%define ver_major 2.9
%define rdn_name it.mijorus.smile

# <screenshot> height too large
%def_disable check

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: An emoji picker
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://github.com/mijorus/smile

%if_enabled snapshot
Vcs: https://github.com/mijorus/smile.git
Source: %_name-%version.tar
%else
Source: %url/archive/%version/%_name-%version.tar.gz
%endif

BuildArch: noarch
%add_python3_path %_datadir/%_name

%define adw_ver 1.4

Requires: dconf font(notocoloremoji)
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson /usr/bin/appstream-util desktop-file-utils

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
* Thu Dec 21 2023 Yuri N. Sedunov <aris@altlinux.org> 2.9.0-alt1
- 2.9.0

* Wed Oct 11 2023 Yuri N. Sedunov <aris@altlinux.org> 2.8.2-alt1
- first build for Sisyphus

