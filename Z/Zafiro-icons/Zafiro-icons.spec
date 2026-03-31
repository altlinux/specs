Name:    Zafiro-icons
Version: 1.3
Release: alt2

Summary: icon pack flat with light colors
License: GPL-3.0
Group:   Other
Url:     https://github.com/zayronxio/Zafiro-icons
BuildArch: noarch

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: /proc

%description
%summary


%define themes Zafiro-icons-Dark Zafiro-icons-Light
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

for icons in Light Dark; do
mv $icons/apps/scalable/βTORRENT.svg $icons/apps/scalable/TORRENT.svg
done

%install
install -d %buildroot%_iconsdir

mv Light Zafiro-icons-Light
mv Dark Zafiro-icons-Dark
cp -r Zafiro-icons-Light %buildroot%_iconsdir
cp -r Zafiro-icons-Dark %buildroot%_iconsdir

%changelog
* Mon Mar 30 2026 Artyom Bystrov <arbars@altlinux.org> 1.3-alt2
- add rename for icon with non-ASCII character in name
- change arch to noarch

* Mon Feb 06 2023 Artyom Bystrov <arbars@altlinux.org> 1.3-alt1
- new version 1.3

* Mon Feb 06 2023 Artyom Bystrov <arbars@altlinux.org> 0.9-alt1
- Initial build for Sisyphus
