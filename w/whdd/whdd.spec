Name: whdd
Version: 2.2
Release: alt4

Summary: Diagnostic and recovery tool for block devices
License: GNU GPL
Group: System/Kernel and hardware
Url: https://github.com/krieger-od/whdd

Packager: Pavel Isopenko <pauli@altlinux.org>
Summary: HDD diagnostic and data recovery tool for Linux
Summary(ru_RU.UTF-8): Инструмент диагностики HDD и восстановления данных под Linux
Source: %name-%version.tar
BuildRequires(pre): cmake
# Automatically added by buildreq on Tue Nov 27 2012
# optimized out: cmake-modules libncurses-devel libstdc++-devel libtinfo-devel
BuildRequires: cmake gcc-c++ libdialog-devel libncursesw-devel

%description
WHDD is a HDD diagnostic and data recovery tool for Linux.
It is capable of testing a hard drive with reading and writing, providing intuitive visualization of the process.
Visualization or these tests is very similar to MHDD. Amongst others, there is a function for copying the device.
The copying procedure algorithms are optimized for least harm to already-defective source device.
WHDD may work with your hard drives on low level, sending ATA commands to device, the benefits are:
- no system freeze while accessing damaged device (device is soft-reset on timeout)
- better timing precision

%description -l ru_RU.UTF-8
WHDD - инструмент диагностики HDD и восстановления данных под Linux.
Предназначен для тестирования накопителей на чтение и запись, даёт наглядное представление процесса.
Визуализация тестов очень похожа на MHDD. Кроме прочего есть также функция копирования данных.
Алгоритм процедуры копирования оптимизирован на минимизацию вреда для уже имеющего дефекты устройства.
WHDD может работать с жёстким диском на низком уровне, отправляя устройству ATA-команды, это:
- исключает подвисания при доступе к повреждённому устройству (мягкий сброс по таймауту);
- лучшая точность по времени.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%attr(4711, root, root) %_sbindir/whdd*

%changelog
* Wed Nov 23 2016 Pavel Isopenko <pauli@altlinux.org> 2.2-alt4
- Fix crash caused by async call to nested function

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

