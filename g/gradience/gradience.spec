%def_disable snapshot
# /usr/share/locale/zh_Hans/LC_MESSAGES/gradience.mo
#%%define _unpackaged_files_terminate_build 1

%define _name Gradience
%define ver_major 0.4
%define beta %nil
%define rdn_name com.github.GradienceTeam.Gradience

Name: gradience
Version: %ver_major.1
Release: alt1%beta

Summary: GNOME ecosystem customizer
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://github.com/GradienceTeam/Gradience

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version%beta.tar.gz
%else
Vcs: https://github.com/GradienceTeam/Gradience.git
Source: %_name-%version.tar
%endif

BuildArch: noarch

%add_python3_path %_datadir/%name

%define gtk4_ver 4.5.0
%define adwaita_ver 1.2
%define pygobject_ver 3.42.0
%define soup3_ver 3.2.0

Requires: dconf
Requires: typelib(Gtk) = 4.0
Requires: typelib(Adw) = 1
Requires: typelib(Soup) = 3.0
Requires: gtk3-theme-adw-gtk3

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler sassc
BuildRequires: desktop-file-utils /usr/bin/appstream-util
BuildRequires: libgtk4-gir-devel >= %gtk4_ver
BuildRequires: libadwaita-gir-devel >= %adwaita_ver
BuildRequires: python3-module-pygobject3-devel >= %pygobject_ver python3-module-lxml

%description
With Gradience, you can easily change colors of your desktop with a real
time preview. You can also export your configuration as preset and share
with others. With plugins, you can extend the application and customize
more things.

%prep
%setup -n %_name-%version%beta

%build
%meson -Dbuildtype=release
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-cli
%python3_sitelibdir_noarch/%name/
%_datadir/%name/
%_datadir/applications/%rdn_name.desktop
%_iconsdir/hicolor/*/*/*.*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*

%changelog
* Mon Mar 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Sun Dec 04 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Mon Nov 21 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2-8-g1b7c089

* Sat Oct 08 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1-27-gc3eb085

* Mon Oct 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first build for Sisyphus


