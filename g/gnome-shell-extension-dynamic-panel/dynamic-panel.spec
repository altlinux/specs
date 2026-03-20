%define exID dynamic-panel@velhlkj.com
%define nameU dynamic-panel
%define nameS org.gnome.shell.extensions.dynamic-panel

Name: gnome-shell-extension-dynamic-panel
Version: 4.11.1
Release: alt2

Summary: Dynamic top panel
Summary(ru_RU.UTF-8): Динамическая верхняя панель

BuildArch: noarch

License: M.W.B License
Group:  Graphical desktop/GNOME
Url: https://github.com/velade/dynamic-panel
VCS: https://github.com/velade/dynamic-panel.git

Source: %nameU-%version.tar

Requires: gnome-shell >= 47.0

%description
The design of the floating panel inspired by KDE Plasma6 presents a translucent floating bar effect 
when there is no window nearby, and a solid panel style when the window is close. Supports gnome's 
dark mode and light mode switching.

%description -l ru_RU.UTF-8
Дизайн плавающей панели, вдохновленный KDE Plasma6, представляет собой эффект полупрозрачной плавающей 
панели, когда рядом нет окна, и сплошной стиль панели, когда окно закрыто. Поддерживает переключение 
темного и светлого режимов gnome.

%prep
%setup -n %nameU-%version

subst 's|"49"|"49", "50"|' metadata.json

%build
%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -r -p locale %buildroot%_datadir/locale
install -D -p -m 0644 \
    schemas/%nameS.gschema.xml \
    %buildroot%_datadir/glib-2.0/schemas/%nameS.gschema.xml
cp -r -p icons lib %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -a *.js *.json LICENSE %buildroot%_datadir/gnome-shell/extensions/%exID/


%files
%_datadir/gnome-shell/extensions/%exID/*
%_datadir/glib-2.0/schemas/*.xml
%_datadir/locale/*/LC_MESSAGES/*.mo
%doc *.md LICENSE 

%changelog
* Fri Mar 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 4.11.1-alt2
- fixed for GNOME 50

* Wed Sep 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.11.1-alt1
- 4.11.0 -> 4.11.1

* Wed Sep 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.11.0-alt1
- 4.10.7 -> 4.11.0

* Tue Sep 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.10.7-alt1
- 4.10.6 -> 4.10.7

* Fri Aug 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.10.6-alt1
- 4.10.5 -> 4.10.6

* Fri Aug 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.10.5-alt1
- 4.10.4 -> 4.10.5 (git.b0568cce02)

* Fri Apr 11 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.10.4-alt1
- 4.10.3 -> 4.10.4

* Thu Mar 27 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.10.3-alt1
- 4.10.2 -> 4.10.3

* Tue Mar 25 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.10.2-alt1
- 4.10.1 -> 4.10.2

* Wed Mar 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.10.1-alt2
- fixed for GNOME 48

* Sun Mar 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.10.1-alt1
- Update to version 4.10.1

* Fri Mar 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.10-alt1
- Update to version 4.10

* Tue Mar 11 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.9-alt1
- Update to version 4.9

* Thu Feb 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.8.2-alt1
- Update to version 4.8.2

* Wed Jan 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.8.1-alt1
- Update to version 4.8.1

* Sun Jan 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.8-alt2
- fix %%description -l ru_RU.UTF-8

* Thu Nov 21 2024 Aleksandr Shamaraev <shad@altlinux.org> 4.8-alt1
- Update to version 4.8

* Tue Oct 15 2024 Hihin Ruslan <ruslandh@altlinux.ru> 4.6-alt1
- Update to version 4.6

* Mon Oct 14 2024 Aleksandr Shamaraev <shad@altlinux.org> 4.5-alt1
- Initial build for Sisyphus.

