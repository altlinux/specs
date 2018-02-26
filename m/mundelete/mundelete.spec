Name: mundelete
Version: 1.0
Release: alt1

Summary: mundelete is a program to undelete files from MsDos/Windows disks (FAT filesystems)
Summary(ru_RU.KOI8-R): mundelete -- программа для восстановления удалённых файлов с файловых систем DOS/Windows (FAT)

License: GPL
Group: File tools
Url: http://sourceforge.net/projects/mundelete

Packager: Yury Aliaev <mutabor@altlinux.ru>

Source: http://dl.sourceforge.net/sourceforge/%name.tar.gz
Patch: %name-newgcc-alt.patch

%description
mundelete is a program to undelete files from MsDos/Windows disks. It
supports FAT12/FAT16/FAT32 and vfat extensions. It works under Unix
systems.

WARNING!!! Carefully read man page before usage and select the working
directory if possible. Otherwise the storage can be filled with old waste
and file system may be corrupted.

%description -l ru_RU.KOI8-R

mundelete -- программа для восстановления удалённых файлов с файловых
систем DOS/Windows (FAT). Поддерживает файловые системы
FAT12/FAT16/FAT32 и vfat. Работает под операционными системами Unix.

ВНИМАНИЕ!!! Обязательно прочитайте страницу руководства (man) перед
использованием программы и по возможности указывайте рабочую директорию.
В противном случае возможно засорение накопителя старым мусором и порча
файловой системы.

%prep
%setup -q -n %name
%patch -p1

%build
rm -rf {mundelete,bin/*}
%make_build CFLAGS="%optflags"

%install
mkdir -p {%buildroot/%_bindir,%buildroot/%_man1dir}
install -pD -m755 bin/%name %buildroot/%_bindir
install -pD -m644 man/%name.1 %buildroot/%_man1dir

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Wed Sep 03 2008 Yury Aliaev <mutabor@altlinux.ru> 1.0-alt1
- first build for ALT Linux Sisyphus
