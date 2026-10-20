Name: teacher-pointer
Version: 1.4.2
Release: alt1

Summary: Teacher pointer
Summary(ru_RU.UTF-8): Учительская указка

License: GPL-3.0-only
Group: Education
Url: https://hub.mos.ru/sapik.max/teacher_pointer

# Source-url: https://hub.mos.ru/sapik.max/teacher_pointer/-/archive/49f039faa1bffa2c17a6f939c19b59d9643758d3/teacher_pointer-49f039faa1bffa2c17a6f939c19b59d9643758d3.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
A program to display a pointer image next to the mouse cursor, useful for
presentations, distance learning and demonstrations. The pointer image and
scale can be changed in the settings. To exit, use the menu of the tray icon.

%description -l ru_RU.UTF-8
Программа для отображения указки рядом с курсором мыши: для презентаций,
дистанционного обучения и демонстраций. Изображение и масштаб указки
меняются в настройках. Для выхода используйте меню значка в трее.

%prep
%setup

%build

%install
install -Dm755 pointer.py %buildroot%_bindir/%name
sed -i '1s|^#!.*|#!%__python3|' %buildroot%_bindir/%name
install -Dm644 pointer.png %buildroot%_datadir/%name/img/pointer.png
install -Dm644 tray-icon.png %buildroot%_datadir/%name/img/tray-icon.png
install -Dm644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm644 %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- initial build for Sisyphus

