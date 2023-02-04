Name:    Tela-circle-icon-theme
Version: 20230129
Release: alt1

Summary: A flat, colorful icon theme
License: GPLv3
Group:   Other
Url:     https://github.com/vinceliuice/Tela-circle-icon-theme

Packager: Artyom Bystrov <arbars@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

#BuildRequires:

%description
%summary


%define themes Tela-circle Tela-circle-green Tela-circle-yellow Tela-circle-orange Tela-circle-grey Tela-circle-red Tela-circle-blue Tela-circle-brown Tela-circle-black Tela-circle-pink Tela-circle-purple Tela-circle-manjaro Tela-circle-ubuntu Tela-circle-dracula Tela-circle-nord Tela-circle-dark Tela-circle-green-dark Tela-circle-yellow-dark Tela-circle-orange-dark Tela-circle-grey-dark Tela-circle-red-dark Tela-circle-blue-dark Tela-circle-brown-dark Tela-circle-black-dark Tela-circle-pink-dark Tela-circle-purple-dark Tela-circle-manjaro-dark Tela-circle-ubuntu-dark Tela-circle-dracula-dark Tela-circle-nord-dark
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

sed -i '/gtk-update-icon-cache/d' install.sh
%install
./install.sh -a -d %buildroot%_iconsdir

%changelog
* Sat Feb 04 2023 Artyom Bystrov <arbars@altlinux.org> 20230129-alt1
- new version 20230129

* Fri Feb 03 2023 Artyom Bystrov <arbars@altlinux.org> 2023-01-29-alt1
- Initial build for Sisyphus
