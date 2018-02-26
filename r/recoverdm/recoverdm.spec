Name: recoverdm
Version: 0.19
Release: alt0.1

Summary: A tool to recover data from damaged disks
Summary (ru_RU.UTF-8): Программа для вычитывания файлов с повреждённых дисков

License: GPL
Group: File tools
Url: http://www.vanheusden.com/%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.vanheusden.com/%name/%name-%version.tar.bz2

%description
This program will help you recover disks with bad sectors.
You can recover files as well as complete devices.
If it finds unrecoverable sectors an empty sector is
written to the outputfile and extraction continues
(unlike cat/dd). While recovering a CD or DVD disk
and the program cannot read a sector cannot be read in
"normal mode", then the program tries to read it in
the "RAW mode" (without error-checking etc.).

%description -l ru_RU.UTF-8
Эта программа поможет извлечь данные с повреждённых дисков.
С её помощью можно вычитывать как отдельные файлы, так и всё
содержимое диска или раздела. Если отдельные секторы прочесть
не удаётся, то в выходной файл записывается пустой сектор и
процесс чтения продолжается (в отличие от cat/dd). Во время
чтения дисков CD или DVD программа пытается прочитать секторы
недоступные в нормальном режиме в поточном режиме "raw"
(без коррекции ошибок).

%prep
%setup -q

%build
%make_build

%install
install -p -m755 -D %name %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Sat Jan 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.19-alt0.1
- new version 0.19, do not need libfvh anymore (fix bug #10692)
- cleanup spec, set packager, fix Url, Source Url

* Fri Oct 24 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.14-alt2
- a typo fixed

* Sat Jan 11 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.14-alt1
- ALT Linux build.
