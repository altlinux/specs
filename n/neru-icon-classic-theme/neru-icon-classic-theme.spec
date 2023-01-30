Name:    neru-icon-classic-theme
Version: 2.7
Release: alt1

Summary: Classic theme icons Neru for ROSA
License: LGPL-3.0
Group:   Other
Url:     https://github.com/chistota/neru-icon-classic-theme

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

Requires: icon-theme-neru-classic-light = %EVR
Requires: icon-theme-neru-classic-light-gray = %EVR
Requires: icon-theme-neru-classic-light-green = %EVR
Requires: icon-theme-neru-classic-light-red = %EVR
Requires: icon-theme-neru-classic-light-yellow = %EVR
Requires: icon-theme-neru-classic-dark = %EVR
Requires: icon-theme-neru-classic-dark-gray = %EVR
Requires: icon-theme-neru-classic-dark-green = %EVR
Requires: icon-theme-neru-classic-dark-red = %EVR
Requires: icon-theme-neru-classic-dark-yellow = %EVR


%description
Classic theme icons Neru for ROSA from ROSPO Design Studio

More than 3000 icons
Suitable for different environments KDE4, KDE5 Plasma, Xfce, Gnome, LXQT, Mate, etc.
For dark and light themes.

%define themes neru-classic-dark neru-classic-dark-green neru-classic-dark-yellow neru-classic-light-gray neru-classic-light-red neru-classic-dark-gray neru-classic-dark-red neru-classic-light neru-classic-light-green neru-classic-light-yellow

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

rm -f neru-classic-light/32x32/apps/pick-colour-picker.svg
rm -f neru-classic-light/32x32/apps/xfce-system.svg

%install

find . -type f -exec chmod 0644 {} \;
find . -type d -exec chmod 0755 {} \;
install -d %buildroot%_iconsdir
cp -r neru* %buildroot%_iconsdir

%changelog
* Mon Jan 30 2023 Artyom Bystrov <arbars@altlinux.org> 2.7-alt1
- Initial build for Sisyphus
