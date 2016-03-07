Name: ldd-requires
Version: 1.2.0
Release: alt1
Summary: Script for generate requires binary file
Summary(ru_RU.UTF-8): Скрипт для генерации зависимостей
License: GPLv3
Group: System/Base
Url: https://github.com/midyukov-anton/ldd-requires
Source: %name-%version.tar.gz
Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch

%description
Script for generate requires binary file

%description -l ru_RU.UTF-8
Скрипт определяет каких пакетов не хватает для запуска бинарного файла

%prep
%setup

%build
%make

%install
%make_install install DESTDIR=%buildroot

%find_lang %name

%files -f %name.lang
%_bindir/ldd-requires

%changelog
* Mon Mar 07 2016 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- New version.

* Thu Jul 10 2015 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt2
- Initial publish
