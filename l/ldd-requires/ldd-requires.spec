Name: ldd-requires
Version: 1.1.1
Release: alt2

Summary: Script for generate requires binary file
License: GPLv3
Group: System/Base

Url: https://github.com/midyukov-anton/ldd-requires
Source: %name-%version.tar.gz

BuildArch: noarch

%description
Script for generate requires binary file

%description -l ru_RU.UTF8
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
* Thu Jul 10 2015 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt2
- Initial publish

