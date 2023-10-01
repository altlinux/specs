%define oversion %(echo %version | sed -e "s|\\.|_|g")

Name: iozone
Version: 3.506
Release: alt1

Summary: IOzone Filesystem Benchmark
Summary(ru_RU.UTF-8): Эталонный тест файловой подсистемы IOzone

License: Freeware
Group: File tools
Url: http://www.iozone.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source0-url: http://www.iozone.org/src/current/%name%oversion.tar
Source0: %name-%version.tar
Source1: %name-graphs

# for convert doc document to txt
BuildPreReq: catdoc

%description
IOzone is a filesystem benchmark tool. The benchmark generates and
measures a variety of file operations. Iozone has been ported
to many machines and runs under many operating systems.

Iozone is useful for performing a broad filesystem analysis of a vendors
computer platform. The benchmark tests file I/O performance for the following
operations: Read, write, re-read, re-write, read backwards, read strided,
fread, fwrite, random read, pread, mmap, aio_read, aio_write.

%description -l ru_RU.UTF-8
IOzone - это инструмент для эталонного тестирования
производительности файловой подсистемы. Этот тест производит
различные операции над файлами и выполняет тестовые замеры.
Iozone портирована на различные машины и запускается под многими
операционными системами.

Iozone полезна для выполнения обширного анализа файловых подсистем
поставщиков компьютерных платформ. Этот тест исследует
производительность файлового ввода-вывода для следующих операций:
чтение, запись, повторное чтение, повторная запись,
чтение назад, чтение с большим шагом, выполнение функций fread и fwrite,
случайное чтение, выполнение pread, mmap, aio_read, aio_write

Запускайте iozone-graphs для получения графиков в каталоге,
расположенном на тестируемой файловой системе. Учтите, что в ходе тестирования
будет занято до 550 мегабайт, и результаты тестирования будут записаны
в текущем каталоге. Также можно указать iozone-graphs файл, полученный
в результате выполнения любым способом iozone -a.
ВНИМАНИЕ! Тест может выполняться десятки минут, столько требуется для
передачи нескольких десятков гигабайт.

%prep
%setup

%build
cd src/current
# Forgot to mention.  If you have Little Endian 64bit compiler,
# then the make target for linux-AMD64 should work fine,
# and produce a 64 bit version. :-)
%ifarch x86_64 aarch64 riscv64 %e2k
%make_build linux-AMD64
%else
%ifarch ppc64le
%make_build linux-powerpc64
%else
%ifarch armh
%make_build linux-arm
%else
%make_build linux
%endif
%endif
%endif

%install
cd src/current
%define iozonebin %buildroot%_bindir
install -D -m755 %name %iozonebin/%name
install -D -m755 %SOURCE1 %iozonebin/%name-graphs
install -D -m755 gengnuplot.sh %iozonebin/%name-gnuplot.sh

install -D gnu3d.dem %buildroot%_datadir/%name/gnu3d.dem

cd ../../docs
install -D iozone.1 %buildroot%_man1dir/iozone.1
catdoc Run_rules.doc >Run_rules.txt

%files
%doc src/current/Gnuplot.txt docs/IOzone_msword_98.pdf docs/Run_rules.txt
%_bindir/iozone
%_bindir/iozone-graphs
%_bindir/iozone-gnuplot.sh
%_man1dir/*
%_datadir/%name/

%changelog
* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 3.506-alt1
- new version 3.506 (with rpmrb script)

* Wed Mar 31 2021 Vitaly Lipatov <lav@altlinux.ru> 3.490-alt1
- new version 3.490 (with rpmrb script)

* Mon Jul 13 2020 Michael Shigorin <mike@altlinux.org> 3.489-alt3
- 64-bit LE arches may use linux-AMD64 target (Don's advice again)

* Sun Jul 12 2020 Michael Shigorin <mike@altlinux.org> 3.489-alt2
- e2k build fix kindly provided by Don Capps himself

* Sun Jul 12 2020 Michael Shigorin <mike@altlinux.org> 3.489-alt1
- new version 3.489
- drop long-unneeded spec bits
- somewhat more involved arch handling

* Sat Mar 24 2018 Vitaly Lipatov <lav@altlinux.ru> 3.471-alt1
- new version 3.471 (with rpmrb script)

* Wed Aug 24 2016 Vitaly Lipatov <lav@altlinux.ru> 3.465-alt1
- new version 3.465 (with rpmrb script)

* Sat Aug 22 2015 Vitaly Lipatov <lav@altlinux.ru> 3.430-alt1
- new version 3.430 (with rpmrb script)

* Sat Nov 22 2014 Vitaly Lipatov <lav@altlinux.ru> 3.429-alt1
- new version (3.429) with rpmgs script
- recode spec to utf-8
- cleanup spec

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.303-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 3.303-alt1
- new version 3.303 (with rpmrb script)

* Mon Feb 26 2007 Vitaly Lipatov <lav@altlinux.ru> 3.283-alt1
- new version 3.283 (with rpmrb script)
- add patch against buffer overflow (thanks kas@)

* Fri Feb 16 2007 Vitaly Lipatov <lav@altlinux.ru> 3.281-alt1
- new version

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 3.271-alt1
- new version (3.271)
- fix build

* Sat Apr 15 2006 Vitaly Lipatov <lav@altlinux.ru> 3.263-alt1
- new version (3.263)

* Sat Feb 04 2006 Vitaly Lipatov <lav@altlinux.ru> 3.259-alt1
- new version
- fix spec: use man1dir, rewrite doc packaging

* Fri Nov 11 2005 Vitaly Lipatov <lav@altlinux.ru> 3.257-alt1
- new version

* Fri Jan 28 2005 Vitaly Lipatov <lav@altlinux.ru> 3.228-alt1
- new version

* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 3.226-alt1
- new version
- spec cleanup

* Mon Jun 07 2004 Vitaly Lipatov <lav@altlinux.ru> 3.218-alt1
- first build for Sisyphus

