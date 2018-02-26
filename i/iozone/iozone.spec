Name: iozone
%define minor 303
Version: 3.%minor
Release: alt1

Summary: IOzone Filesystem Benchmark
Summary(ru_RU.KOI8-R): Эталонный тест файловой подсистемы IOzone

License: Freeware
Group: File tools
Url: http://www.iozone.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.iozone.org/src/current/%{name}3_%minor.tar.bz2
Source1: %name-graphs
Patch: %name.patch

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

%description -l ru_RU.KOI8-R
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
в текущем каталоге. Также можно указать iozone-graphs файл, полученный в результате
выполнения любым способом iozone -a.
ВНИМАНИЕ! Тест может выполняться десятки минут, столько требуется для
передачи нескольких десятков гигабайт.

%prep
%setup -n %{name}3_%minor/src/current -q
%patch

%build
%make_build linux

# fix hard xrange
#%__subst "s/set xrange/#set xrange/" $RPM_BUILD_DIR/src/current/gnu3d.dem

%install
%define iozonebin %buildroot%_bindir
install -D -m755 %name %iozonebin/%name
install -D -m755 %SOURCE1 %iozonebin/%name-graphs
install -D -m755 gengnuplot.sh %iozonebin/%name-gnuplot.sh

install -D gnu3d.dem %buildroot%_datadir/%name/gnu3d.dem

cd ../../docs
install -D iozone.1 %buildroot%_man1dir/iozone.1
catdoc Run_rules.doc >Run_rules.txt

%files
%doc Gnuplot.txt ../../docs/IOzone_msword_98.pdf ../../docs/Run_rules.txt
%_bindir/iozone
%_bindir/iozone-graphs
%_bindir/iozone-gnuplot.sh
%_man1dir/*
%_datadir/%name/

%changelog
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

