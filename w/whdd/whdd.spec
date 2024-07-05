Name: whdd
Version: 3.1
Release: alt1

Summary: Diagnostic and recovery tool for block devices
License: GPL-3
Group: System/Kernel and hardware
Url: https://github.com/whdd/whdd

Packager: Pavel Isopenko <pauli@altlinux.org>
Summary: HDD diagnostic and data recovery tool for Linux
Summary(ru_RU.UTF-8): Инструмент диагностики HDD и восстановления данных под Linux
Source: %name-%version.tar
Patch1: %name-remove-nested.patch

BuildRequires: gcc-c++ libdialog-devel libncursesw-devel

%description
WHDD is a HDD diagnostic and data recovery tool for Linux.
It is capable of testing a hard drive with reading and writing, providing intuitive visualization of the process.
Visualization or these tests is very similar to MHDD. Amongst others, there is a function for copying the device.
The copying procedure algorithms are optimized for least harm to already-defective source device.
WHDD may work with your hard drives on low level, sending ATA commands to device, the benefits are:
- no system freeze while accessing damaged device (device is soft-reset on timeout)
- better timing precision

%description -l ru_RU.UTF-8
WHDD - инструмент диагностики HDD и восстановления данных для Linux.
Предназначен для тестирования накопителей на чтение и запись. Даёт наглядное представление процесса,
визуализация тестов весьма похожа на MHDD. Кроме прочего, имеется функция копирования данных.
Алгоритм процедуры копирования оптимизирован на минимизацию вреда для уже имеющего дефекты устройства.
WHDD может работать с жёстким диском на низком уровне, отправляя устройству ATA-команды, что:
- исключает подвисания при доступе к повреждённому устройству (сброс устройства по таймауту);
- даёт лучшую точность по времени.

%prep
%setup
%ifarch %e2k
# EDG frontend doesn't support nested functions
%patch1 -p1
%endif

%build
%make_build

%install
%make_install install DESTDIR=%buildroot/usr
%find_lang %name

%files  -f %name.lang
%doc README LICENSE COPYING doc/README.developer
%attr(4711, root, root) %_bindir/%name

%changelog
* Fri Jul 05 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.1-alt1
- new version whdd 3.1

* Fri Sep 24 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.0-alt3
- e2k: removed nested function

* Wed Jun 20 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt2
- rebuild with libdialog.so.14

* Mon May 29 2017 Pavel Isopenko <pauli@altlinux.org> 3.0-alt1
- new version 3.0
- change destination directory to /usr/bin
- change build system to automake

* Tue Nov 08 2016 Pavel Isopenko <pauli@altlinux.org> 2.2-alt4
- Upstream update (Add back explicit def of _GNU_SOURCE)

* Sun Oct 16 2016 Pavel Isopenko <pauli@altlinux.org> 2.2-alt3
- Description fix (ALT #32556)

* Sat Apr 25 2015 Pavel Isopenko <pauli@altlinux.org> 2.2-alt2
- Correction of the description (ALT #30854)

* Fri Jan 09 2015 Pavel Isopenko <pauli@altlinux.org> 2.2-alt1
- new version whdd 2.2

* Thu Sep 19 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1-alt1
- New version

* Mon Nov 26 2012 Pavel Isopenko <pauli@altlinux.org> 1.1-alt1
- Initial build for Sisyphus
- Add ncursesw to target_link_libraries()

