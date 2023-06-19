%define _wallpapersdir %_datadir/wallpapers

Name:    gtk-themes-Graphite
Version: 20230517
Release: alt2

Summary: Graphite - set of themes for XFCE, MATE, Gnome, Cinnamon desktop environment
License: GPL-3.0
Group:   Other
Url:     https://github.com/vinceliuice/Graphite-gtk-theme

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source2: wave-Dark-Basealt.png
Source3: wave-Dark-nord-Basealt.png
Source4: wave-Dark-nord-SL.png
Source5: wave-Dark-SL.png
Source6: wave-Light-Basealt.png
Source7: wave-Light-SL.png
Source8: wave-nord-Light-Basealt.png
Source9: wave-nord-Light-SL.png
Source10: wave-Dark-ALT-nord.png
Source11: wave-Dark-ALT.png
Source12: wave-Light-ALT-nord.png
Source13: wave-Light-ALT.png

BuildRequires: sassc libgtk-engine-murrine
Requires: Tela-icon-theme gnome-themes-extra

BuildArch: noarch

%description
Graphite is set of GTK themes for XFCE, MATE, Gnome, Cinnamon desktop environments. Note: Light theme will not work in the MATE...

Themes for XFCE, besides the colors, dividing by the type of pixel density:
* regular - just for regular displays;
* hdpi - for displays with hight pixel density;
* xhdpi - for displays with hight pixel density, multiplied by 2

%define themes Graphite Graphite-Dark Graphite-Dark-hdpi Graphite-Dark-xhdpi Graphite-hdpi Graphite-Light Graphite-Light-hdpi Graphite-Light-xhdpi Graphite-xhdpi
%{expand:%(\
    for theme in %{themes}; do \
        echo -e "%%package -n gtk-theme-$theme";\
        echo -e "Summary: $theme GTK theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n gtk-theme-$theme\n$theme gtk theme for XFCE, MATE, Gnome, Cinnamon desktop environment.\n";\
        echo -e "%%files -n gtk-theme-$theme\n%%_datadir/themes/$theme/\n";\
    done\
)}

%define themes_blue Graphite-blue Graphite-blue-Dark Graphite-blue-Dark-hdpi Graphite-blue-Dark-xhdpi Graphite-blue-hdpi Graphite-blue-Light Graphite-blue-Light-hdpi Graphite-blue-Light-xhdpi Graphite-blue-xhdpi
%{expand:%(\
    for theme in %{themes_blue}; do \
        echo -e "%%package -n gtk-theme-$theme";\
        echo -e "Summary: $theme GTK theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n gtk-theme-$theme\n$theme gtk theme for XFCE, MATE, Gnome, Cinnamon desktop environment.\n";\
        echo -e "%%files -n gtk-theme-$theme\n%%_datadir/themes/$theme/\n";\
    done\
)}

%define themes_green Graphite-green Graphite-green-Dark Graphite-green-Dark-hdpi Graphite-green-Dark-xhdpi Graphite-green-hdpi Graphite-green-Light Graphite-green-Light-hdpi Graphite-green-Light-xhdpi Graphite-green-xhdpi
%{expand:%(\
    for theme in %{themes_green}; do \
        echo -e "%%package -n gtk-theme-$theme";\
        echo -e "Summary: $theme GTK theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n gtk-theme-$theme\n$theme gtk theme for XFCE, MATE, Gnome, Cinnamon desktop environment.\n";\
        echo -e "%%files -n gtk-theme-$theme\n%%_datadir/themes/$theme/\n";\
    done\
)}

%define themes_pink Graphite-pink Graphite-pink-Dark Graphite-pink-Dark-hdpi Graphite-pink-Dark-xhdpi Graphite-pink-hdpi Graphite-pink-Light Graphite-pink-Light-hdpi Graphite-pink-Light-xhdpi Graphite-pink-xhdpi
%{expand:%(\
    for theme in %{themes_pink}; do \
        echo -e "%%package -n gtk-theme-$theme";\
        echo -e "Summary: $theme GTK theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n gtk-theme-$theme\n$theme gtk theme for XFCE, MATE, Gnome, Cinnamon desktop environment.\n";\
        echo -e "%%files -n gtk-theme-$theme\n%%_datadir/themes/$theme/\n";\
    done\
)}

%define themes_orange Graphite-orange Graphite-orange-Dark Graphite-orange-Dark-hdpi Graphite-orange-Dark-xhdpi Graphite-orange-hdpi Graphite-orange-Light Graphite-orange-Light-hdpi Graphite-orange-Light-xhdpi Graphite-orange-xhdpi
%{expand:%(\
    for theme in %{themes_orange}; do \
        echo -e "%%package -n gtk-theme-$theme";\
        echo -e "Summary: $theme GTK theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n gtk-theme-$theme\n$theme gtk theme for XFCE, MATE, Gnome, Cinnamon desktop environment.\n";\
        echo -e "%%files -n gtk-theme-$theme\n%%_datadir/themes/$theme/\n";\
    done\
)}

%define themes_purple Graphite-purple Graphite-purple-Dark Graphite-purple-Dark-hdpi Graphite-purple-Dark-xhdpi Graphite-purple-hdpi Graphite-purple-Light Graphite-purple-Light-hdpi Graphite-purple-Light-xhdpi Graphite-purple-xhdpi
%{expand:%(\
    for theme in %{themes_purple}; do \
        echo -e "%%package -n gtk-theme-$theme";\
        echo -e "Summary: $theme GTK theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n gtk-theme-$theme\n$theme gtk theme for XFCE, MATE, Gnome, Cinnamon desktop environment.\n";\
        echo -e "%%files -n gtk-theme-$theme\n%%_datadir/themes/$theme/\n";\
    done\
)}

%define themes_red Graphite-red Graphite-red-Dark Graphite-red-Dark-hdpi Graphite-red-Dark-xhdpi Graphite-red-hdpi Graphite-red-Light Graphite-red-Light-hdpi Graphite-red-Light-xhdpi Graphite-red-xhdpi
%{expand:%(\
    for theme in %{themes_red}; do \
        echo -e "%%package -n gtk-theme-$theme";\
        echo -e "Summary: $theme GTK theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n gtk-theme-$theme\n$theme gtk theme for XFCE, MATE, Gnome, Cinnamon desktop environment.\n";\
        echo -e "%%files -n gtk-theme-$theme\n%%_datadir/themes/$theme/\n";\
    done\
)}

%define themes_teal Graphite-teal Graphite-teal-Dark Graphite-teal-Dark-hdpi Graphite-teal-Dark-xhdpi Graphite-teal-hdpi Graphite-teal-Light Graphite-teal-Light-hdpi Graphite-teal-Light-xhdpi Graphite-teal-xhdpi
%{expand:%(\
    for theme in %{themes_teal}; do \
        echo -e "%%package -n gtk-theme-$theme";\
        echo -e "Summary: $theme GTK theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n gtk-theme-$theme\n$theme gtk theme for XFCE, MATE, Gnome, Cinnamon desktop environment.\n";\
        echo -e "%%files -n gtk-theme-$theme\n%%_datadir/themes/$theme/\n";\
    done\
)}

%define themes_yellow Graphite-yellow Graphite-yellow-Dark Graphite-yellow-Dark-hdpi Graphite-yellow-Dark-xhdpi Graphite-yellow-hdpi Graphite-yellow-Light Graphite-yellow-Light-hdpi Graphite-yellow-Light-xhdpi Graphite-yellow-xhdpi
%{expand:%(\
    for theme in %{themes_yellow}; do \
        echo -e "%%package -n gtk-theme-$theme";\
        echo -e "Summary: $theme GTK theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n gtk-theme-$theme\n$theme gtk theme for XFCE, MATE, Gnome, Cinnamon desktop environment.\n";\
        echo -e "%%files -n gtk-theme-$theme\n%%_datadir/themes/$theme/\n";\
    done\
)}


%package -n wallpapers-Graphite
Summary:Set of wallpapers for Graphite GTK theme
Group: Graphics
%description -n wallpapers-Graphite
Set of wallpapers for Graphite GTK theme

%package -n grub-theme-Graphite
Summary: Graphite theme for GRUB menu
Group: Graphics
%description -n grub-theme-Graphite
Graphite theme for GRUB menu

%prep
%setup

%install

mkdir -p %buildroot%_datadir/themes/Graphite
mkdir -p %buildroot%_wallpapersdir/Graphite
./install.sh -t all -d %buildroot%_datadir/themes

for wallpaper in %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9 wallpaper/Graphite-nord/wave-Light-nord.png wallpaper/Graphite-nord/wave-Dark-nord.png wallpaper/Graphite/wave-Dark.png wallpaper/Graphite/wave-Light.png; do
install -m 0644 $wallpaper %buildroot%_wallpapersdir/Graphite
done

%files -n wallpapers-Graphite
%_wallpapersdir/Graphite/*.png

%changelog
* Mon Jun 19 2023 Artyom Bystrov <arbars@altlinux.org> 20230517-alt2
- Add wallpapers with ALT Linux Community logo

* Thu May 18 2023 Artyom Bystrov <arbars@altlinux.org> 20230517-alt1
- New version 20230517.

* Mon Apr 10 2023 Artyom Bystrov <arbars@altlinux.org> 220902-alt2
- Fix description and name of package.
- Add new su

* Fri Apr 07 2023 Artyom Bystrov <arbars@altlinux.org> 220902-alt1
- New version 220902.

* Fri Apr 07 2023 Artyom Bystrov <arbars@altlinux.org> 2022-09-02-alt1
- Initial build for Sisyphus
