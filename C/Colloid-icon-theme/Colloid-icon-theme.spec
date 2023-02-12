Name:    Colloid-icon-theme
Version: 20230108
Release: alt1

Summary: Colloid icon theme for linux desktops
License: GPL-3.0
Group:   Other
Url:     https://github.com/vinceliuice/Colloid-icon-theme

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

%description
%summary

%define themes Colloid-light Colloid-dark Colloid Colloid-purple-light Colloid-purple-dark Colloid-purple Colloid-pink-light Colloid-pink-dark Colloid-pink Colloid-red-light Colloid-red-dark Colloid-red Colloid-orange-light Colloid-orange-dark Colloid-orange Colloid-yellow-light Colloid-yellow-dark Colloid-yellow Colloid-green-light Colloid-green-dark Colloid-green Colloid-teal-light Colloid-teal-dark Colloid-teal Colloid-grey-light Colloid-grey-dark Colloid-grey
%{expand:%(\
    for theme in %{themes}; do \
        echo -e "%%package -n icon-theme-$theme";\
        echo -e "Summary: $theme icon theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n icon-theme-$theme\n$theme icon theme.\n";\
        echo -e "%%files -n icon-theme-$theme\n%%_iconsdir/$theme/\n";\
    done\
)}

%define cursors Colloid-dark-cursors Colloid-cursors
%{expand:%(\
    for cursor in %{cursors}; do \
        echo -e "%%package -n x-cursor-theme-$cursor";\
        echo -e "Summary: $cursor cursor theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n x-cursor-theme-$cursor\n$cursor cursor theme.\n";\
        echo -e "%%files -n x-cursor-theme-$cursor\n%%_iconsdir/$cursor/\n";\
    done\
)}


%prep
%setup

sed -i '/gtk-update-icon-cache/d' install.sh
rm links/actions/32/financial-payees.svg
rm links/apps/symbolic/org.buddiesofbudgie.Settings-keyboard-symbolic.svg
rm links/mimetypes/scalable/application-x-ms-wim.svg
rm links/apps/scalable/org.gnome.Settings-keyboard-symbolic.svg
rm links/apps/symbolic/org.gnome.Settings-keyboard-symbolic.svg
rm links/apps/symbolic/org.gnome.gitlab.somas.Apostrophe-symbolic.svg

%install
./install.sh -t all -d %buildroot%_iconsdir

install -d %buildroot%_iconsdir/Colloid{-cursors,-dark-cursors}
cd cursors
cp -r dist/* "%buildroot%_iconsdir/Colloid-cursors/"
cp -r dist-dark/* "%buildroot%_iconsdir/Colloid-dark-cursors/"

%changelog
* Fri Feb 10 2023 Artyom Bystrov <arbars@altlinux.org> 20230108-alt1
- new version 20230108

* Fri Feb 10 2023 Artyom Bystrov <arbars@altlinux.org> 2023-01-08-alt1
- Initial build for Sisyphus
