Name:    Tela-icon-theme
Version: 20230203
Release: alt2

Summary: A flat colorful Design icon theme
License: GPL-3.0
Group:   Other
Url:     https://github.com/vinceliuice/Tela-icon-theme

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source2: uav-quadcopter_22x22.svg
Source3: uav-quadcopter_24x24.svg
Source4: user-desktop.svg

Requires: icon-theme-Tela = %EVR
Requires: icon-theme-Tela-dark = %EVR
Requires: icon-theme-Tela-black = %EVR
Requires: icon-theme-Tela-black-dark = %EVR
Requires: icon-theme-Tela-blue = %EVR
Requires: icon-theme-Tela-blue-dark = %EVR
Requires: icon-theme-Tela-brown = %EVR
Requires: icon-theme-Tela-brown-dark = %EVR
Requires: icon-theme-Tela-green = %EVR
Requires: icon-theme-Tela-green-dark = %EVR
Requires: icon-theme-Tela-grey = %EVR
Requires: icon-theme-Tela-grey-dark = %EVR
Requires: icon-theme-Tela-orange = %EVR
Requires: icon-theme-Tela-orange-dark = %EVR
Requires: icon-theme-Tela-pink = %EVR
Requires: icon-theme-Tela-pink-dark = %EVR
Requires: icon-theme-Tela-purple = %EVR
Requires: icon-theme-Tela-purple-dark = %EVR
Requires: icon-theme-Tela-red = %EVR
Requires: icon-theme-Tela-red-dark = %EVR
Requires: icon-theme-Tela-yellow = %EVR
Requires: icon-theme-Tela-yellow-dark = %EVR
Requires: icon-theme-Tela-manjaro = %EVR
Requires: icon-theme-Tela-manjaro-dark = %EVR
Requires: icon-theme-Tela-ubuntu = %EVR
Requires: icon-theme-Tela-ubuntu-dark = %EVR
Requires: icon-theme-Tela-dracula = %EVR
Requires: icon-theme-Tela-dracula-dark = %EVR
Requires: icon-theme-Tela-nord = %EVR
Requires: icon-theme-Tela-nord-dark = %EVR

%description
%summary


%define themes Tela Tela-green Tela-yellow Tela-orange Tela-grey Tela-red Tela-blue Tela-brown Tela-black Tela-pink Tela-purple Tela-manjaro Tela-ubuntu Tela-dracula Tela-nord Tela-dark Tela-green-dark Tela-yellow-dark Tela-orange-dark Tela-grey-dark Tela-red-dark Tela-blue-dark Tela-brown-dark Tela-black-dark Tela-pink-dark Tela-purple-dark Tela-manjaro-dark Tela-ubuntu-dark Tela-dracula-dark Tela-nord-dark
%{expand:%(\
    for theme in %{themes}; do \
        echo -e "%%package -n icon-theme-$theme";\
        echo -e "Summary: $theme icon theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n icon-theme-$theme\n$theme icon theme.\n";\
        echo -e "%%files -n icon-theme-$theme\n%%_iconsdir/$theme/\n";\
    done\
)}

%prep
%setup
cp %SOURCE2 src/22/devices/uav-quadcopter.svg
cp %SOURCE3 src/24/devices/uav-quadcopter.svg
cp %SOURCE4 src/24/panel/user-desktop.svg

sed -i '/gtk-update-icon-cache/d' install.sh
%install
./install.sh -a -d %buildroot%_iconsdir

%changelog
* Mon Feb 06 2023 Artyom Bystrov <arbars@altlinux.org> 20230203-alt2
- fix missing icons

* Sat Feb 04 2023 Artyom Bystrov <arbars@altlinux.org> 20230203-alt1
- new version 20230203

* Sat Feb 04 2023 Artyom Bystrov <arbars@altlinux.org> 2023-02-03-alt1
- Initial build for Sisyphus
