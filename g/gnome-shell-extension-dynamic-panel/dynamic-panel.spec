%define exID dynamic-panel@velhlkj.com
%define nameU dynamic-panel

Name: gnome-shell-extension-dynamic-panel
Version: 4.6
Release: alt1

Summary: Dynamic top panel
Summary(ru_RU.UTF-8): Динамическая верхняя панель

BuildArch: noarch

License: M.W.B License
Group:  Graphical desktop/GNOME
Url: https://github.com/velade/dynamic-panel

Source: %nameU-%version.tar

Requires: gnome-shell >= 47.0

%description
The design of the floating panel inspired by KDE Plasma6 presents a translucent floating bar effect when there is no window nearby, and a solid panel style when the window is close. Supports gnome's dark mode and light mode switching.

%description -l ru_RU.UTF8
Дизайн плавающей панели, вдохновленный KDE Plasma6, представляет собой эффект полупрозрачной плавающей панели, когда рядом нет окна, и сплошной стиль панели, когда окно закрыто. Поддерживает переключение темного и светлого режимов gnome.

%prep
%setup -n %nameU-%version

%build
%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -R locale %buildroot%_datadir/gnome-shell/extensions/%exID/locale
cp -R schemas %buildroot%_datadir/gnome-shell/extensions/%exID/schemas
cp -R icons %buildroot%_datadir/gnome-shell/extensions/%exID/icons
cp *.js %buildroot%_datadir/gnome-shell/extensions/%exID/
cp LICENSE %buildroot%_datadir/gnome-shell/extensions/%exID/LICENSE
cp metadata.json %buildroot%_datadir/gnome-shell/extensions/%exID/metadata.json

%files
%_datadir/gnome-shell/extensions/%exID/*
%doc *.md LICENSE 

%changelog
* Tue Oct 15 2024 Hihin Ruslan <ruslandh@altlinux.ru> 4.6-alt1
- Update to version 4.6

* Mon Oct 14 2024 Aleksandr Shamaraev <shad@altlinux.org> 4.5-alt1
- Initial build for Sisyphus.
