# Name Upstream release  0.1.4.2-Gx
Name: printer-driver-foo2capt

Version: 0.1.4.2
Release: alt1.git_1_8ecc3cd 

Source: %name-%version.tar

Summary: Driver for Canon CAPT printers
URL: https://github.com/mounaiban/captdriver
License: GPL-3.0-or-later
Group: System/Configuration/Printing

BuildRequires: libcups-devel

%description
Captdriver an alternative driver for Canon laser printers that only support the proprietary
CAPT communications protocol and associated data stream formats.
It aims to be a portable and reliable driver that can extend the service life of existing
CAPT-only printers by extending support to more platforms and newer operating systems.

Wiki -  https://github.com/mounaiban/captdriver/wiki

The following printer-host-operating system combinations have been found to work:

 LBP2900
 LBP3000
 LBP3010
 LBP3100/3108/3150
 LBP6000/6018

%description -l ru_Ru.utf8 
Captdriver - это альтернативный драйвер для лазерных принтеров Canon,
которые поддерживает только проприетарные принтеры с Протокололом связи CAPT
и связанными с ним форматом потоков данных.
Он призван быть портативным и надежным драйвером, способным продлить срок службы существующих принтеров,
поддерживаемых только CAPT, за счет поддержки на большее количество платформ и операционных систем.

Драайвера разработаны на основе методов обратной инженерии, но могут не тестироваться на реальной аппаратуре

Руководство по работе с драйвером принтеры -  https://github.com/mounaiban/captdriver/wiki

Имеется информация, что поддерживаются в разной степени следующие принтеры:

 LBP2900
 LBP3000
 LBP3010
 LBP3100/3108/3150
 LBP6000/6018

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
install -Dm0755 -t  %buildroot%_libexecdir/cups/filter/ src/rastertocapt
install -Dm644  -t %buildroot%_datadir/cups/model/foo2capt/ *.ppd

%files
%_datadir/cups/model/foo2capt/
%_libexecdir/cups/filter/rastertocapt

%changelog
* Sat Jul 22 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.1.4.2-alt1.git_1_8ecc3cd
- Fix ppd driver location

* Thu Jul 06 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.1.4.2-alt1.git_0_8ecc3cd
- Update Version

* Wed Jun 15 2022 Hihin Ruslan <ruslandh@altlinux.ru> 0.1.0-alt2.git_0_5208e72
- Update Version

* Fri Nov 1 2019 Grigory Maksimov <zacat@altlinux.org> 0.1.0-alt1.git94b2bf2
- Initial build for ALT
