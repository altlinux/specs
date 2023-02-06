Name:    Zafiro-icons
Version: 1.3
Release: alt1

Summary: icon pack flat with light colors
License: GPL-3.0
Group:   Other
Url:     https://github.com/zayronxio/Zafiro-icons

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

#BuildRequires:

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

%install
install -d %buildroot%_iconsdir

mv Light Zafiro-icons-Light
mv Dark Zafiro-icons-Dark
cp -r Zafiro-icons-Light %buildroot%_iconsdir
cp -r Zafiro-icons-Dark %buildroot%_iconsdir

%changelog
* Mon Feb 06 2023 Artyom Bystrov <arbars@altlinux.org> 1.3-alt1
- new version 1.3

* Mon Feb 06 2023 Artyom Bystrov <arbars@altlinux.org> 0.9-alt1
- Initial build for Sisyphus
