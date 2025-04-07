%def_enable snapshot
%define _name Adwaita-colors
%define __name adwaita-colors
%define ver_major 2.4
%define beta %nil

%def_disable check

Name: icon-theme-%__name
Version: %ver_major.1
Release: alt1%beta

Summary: Adwaita Colors Icon Theme
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://github.com/dpejoh/Adwaita-colors

Vcs: https://github.com/dpejoh/Adwaita-colors.git

BuildArch: noarch

Provides: %_name = %EVR

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

Requires(pre): icon-theme-adwaita icon-theme-adwaita-legacy

%description
Adwaita Colors enhances the Adwaita icon theme by integrating GNOME's
accent color feature, introduced in GNOME 47. This project ensures that
your Adwaita icons reflect the same accent color as your GNOME theme,
instead of the default blue, for a more cohesive and customized look.

%prep
%setup -n %_name-%version
# broken symlink com.bitwig.BitwigStudio.application-bitwig-project-folder-legacy.svg -> folder-bitwig-legacy.svg
rm -f Adwaita-blue/scalable/places/com.bitwig.BitwigStudio.application-bitwig-project-folder-legacy.svg

%install
mkdir -p %buildroot/%_iconsdir
cp -r Adwaita-* %buildroot/%_iconsdir/

%files
%_iconsdir/Adwaita-*/
%doc README*

%changelog
* Mon Feb 10 2025 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- first build for Sisyphus (v2.4.1-8-gf153417)


