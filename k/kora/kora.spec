Name:    kora
Version: 1.5.4
Release: alt1

Summary: Kora icon theme for GNU/Linux os
License: GPL-3.0
Group:   Other
Url:     https://github.com/bikass/kora

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

#BuildRequires:

%description
Kora is an SVG icon theme with lots of new icons for GNU/Linux operating systems.

%define themes kora kora-light kora-pgrey kora-light-panel

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

rm -f kora/mimetypes/scalable/application-sweethome3d.svg
rm -f kora/mimetypes/scalable/application-vnd.insync.link.drive.link.svg

%install

install -d %buildroot%_iconsdir
cp -r kora* %buildroot%_iconsdir

%changelog
* Sat Feb 04 2023 Artyom Bystrov <arbars@altlinux.org> 1.5.4-alt1
- Initial build for Sisyphus
