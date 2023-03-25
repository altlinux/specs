Name:    sevi-icon-theme
Version: 20230324
Release: alt1

Summary: A colorful Design Rectangle icon theme for linux desktops
License: GPL-3.0
Group:   Other
Url:     https://github.com/yeyushengfan258/Reversal-icon-theme

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: gtk4-update-icon-cache

Requires: icon-theme-Sevi = %EVR
Requires: icon-theme-Sevi-dark = %EVR
Requires: icon-theme-Sevi-black = %EVR
Requires: icon-theme-Sevi-black-dark = %EVR
Requires: icon-theme-Sevi-blue = %EVR
Requires: icon-theme-Sevi-blue-dark = %EVR
Requires: icon-theme-Sevi-brown = %EVR
Requires: icon-theme-Sevi-brown-dark = %EVR
Requires: icon-theme-Sevi-green = %EVR
Requires: icon-theme-Sevi-green-dark = %EVR
Requires: icon-theme-Sevi-grey = %EVR
Requires: icon-theme-Sevi-grey-dark = %EVR
Requires: icon-theme-Sevi-orange = %EVR
Requires: icon-theme-Sevi-orange-dark = %EVR
Requires: icon-theme-Sevi-pink = %EVR
Requires: icon-theme-Sevi-pink-dark = %EVR
Requires: icon-theme-Sevi-purple = %EVR
Requires: icon-theme-Sevi-purple-dark = %EVR
Requires: icon-theme-Sevi-red = %EVR
Requires: icon-theme-Sevi-red-dark = %EVR

%description
%summary

%define themes Sevi Sevi-green Sevi-orange Sevi-grey Sevi-red Sevi-blue Sevi-brown Sevi-black Sevi-pink Sevi-purple Sevi-dark Sevi-green-dark Sevi-orange-dark Sevi-grey-dark Sevi-red-dark Sevi-blue-dark Sevi-brown-dark Sevi-black-dark Sevi-pink-dark Sevi-purple-dark
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

%install
mkdir -p %buildroot%_iconsdir
./install.sh -a -d %buildroot%_iconsdir

rm -rf %buildroot%_datadir/icons/Sevi*/apps/scalable/libreoffice7.3-chart.svg

%changelog
* Fri Mar 24 2023 Artyom Bystrov <arbars@altlinux.org> 20230324-alt1
- Initial build for Sisyphus
