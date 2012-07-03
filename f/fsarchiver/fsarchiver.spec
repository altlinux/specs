Summary: Filesystem Archiver for Linux
Name: fsarchiver
Version: 0.7.0
Release: alt1
Url: http://www.fsarchiver.org
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar.bz2
License: GPLv2+
Group: Archiving/Backup

# Automatically added by buildreq on Tue Nov 29 2011
# optimized out: libcom_err-devel libgpg-error libgpg-error-devel pkg-config
BuildRequires: bzlib-devel libattr-devel libblkid-devel libe2fs-devel libgcrypt-devel liblzma-devel liblzo2-devel libparted-devel libuuid-devel zlib-devel

BuildRequires: libe2fs-devel libgcrypt-devel liblzma-devel liblzo2-devel libuuid-devel zlib-devel

%description
FSArchiver is a system tool that allows you to save the contents of
a file-system to a compressed archive file. The file-system can be
restored on a partition which has a different size and it can be
restored on a different file-system.

The following features have already been implemented in the current version:

-Support for basic file attributes (permissions, owner, ...)
-Support for multiple file-systems per archive
-Support for extended attributes (they are used by SELinux)
-Support the basic file-system attributes (label, uuid, block-size) for all
 linux file-systems
-Support for ntfs filesystems (ability to create flexible clones of
 windows partitions)
-Checksumming of everything which is written in the archive
 (headers, data blocks, whole files)
-Ability to restore an archive which is corrupt (it will just skip the
 current file)
-Multi-threaded lzo, gzip, bzip2, lzma compression: if you have a
 dual-core / quad-core it will use all the power of your cpu
-Lzma compression (slow but very efficient algorithm) to make your
 archive smaller.
-Support for splitting large archives into several files with a fixed
 maximum size
-Encryption of the archive using a password. Based on blowfish from libcrypto
 from openssl.

%description -l ru_RU.UTF8
FSArchiver  - системный инструментарий, позволяяющий вам сохранять содержимое
файловой системы в виде сжатого файла. Файловая система может быть восстановлена
в отличающемся от исходного разделе диска.

В FSArchiver уже включены следующие возможности:

- поддерживает сохранеие атрибутов файлов файловой системы;
- подеерживает включение в архив нескольких файловых систем;
- поодерживает сохранение атрибутув файлой системы (label, uuid, размер блока);
- поддерживает атрибуты ntfs (позволяет создать изменяемый клон раздела Виндоус);
- создаёт контрольные суммы всего, что записано в архив;
- позволяет восстанавливать повреждённые архивы;
- мултипотоковая компрессия на нескольких процессорах в различных форматах (lzo, gzip, bzip, lzma);
- максимальное сжатие с помощью lzma (более медленный, но очень эффективный алгоритм);
- поддержка разбиения архива на несколько файлов заданного размера;
- шифрование архива паролём на основе blowfish, libcrypto, openssl.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%makeinstall_std

%files
%doc COPYING ChangeLog AUTHORS README
%_sbindir/%name
%_man8dir/*

%changelog
* Tue Nov 29 2011 Hihin Ruslan <ruslandh@altlinux.ru> 0.7.0-alt1
- Major feature: implemented savept, restpt, showpt (save and restore partition tables)
- Added configuration file: /etc/fsarchiver.conf (it currently only supports "exclude_restpt")
- Implemented error correction based on Forward Error Correction (FEC) (cf: option -y)
- File format more robust when corruptions / insertions / deletions happen in the archive


* Sat Mar 26 2011 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.12-alt1
- Initial release for ALT Linux

* Sun Dec 26 2010 Texstar <texstar at gmail.com> 0.6.12-1pclos2010
- 0.6.12

* Mon Dec 06 2010 Texstar <texstar at gmail.com> 0.6.11-1pclos2010
- 0.6.11

* Fri Nov 27 2009 maik3531 <maik3531 at yahoo.de> 0.6.1-1pclos2010
- Initial release for PCLinuxOS
