Summary: Safe and flexible file-system backup/deployment tool
Summary(ru_RU.UTF-8): Архиватор файловых систем

Name: fsarchiver
Version: 0.8.7
Release: alt1
Url: https://github.com/fdupoux/fsarchiver
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Epoch: 1

Source: %name-%version.tar
#Patch: cppcheck.patch

License: GPLv2+
Group: Archiving/Backup

# Automatically added by buildreq on Tue Oct 10 2023
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libcom_err-devel libgpg-error libgpg-error-devel perl pkg-config sh4
BuildRequires: bzlib-devel libblkid-devel libe2fs-devel libgcrypt-devel 
BuildRequires: liblz4-devel liblzma-devel liblzo2-devel libuuid-devel libzstd-devel perl-parent zlib-devel

# BEGIN SourceDeps(oneline):
BuildRequires: liblz4-devel libzstd-devel pkgconfig(com_err)
# END SourceDeps(oneline)


%description
FSArchiver is a system tool that allows you to save the contents of a
filesystem to a compressed archive file. The filesystem contents can be
restored on a device which has a different size and it can be restored on a
different filesystem. Unlike tar/dar, FSArchiver also creates the
filesystem when it extracts the data to devices. Everything is checksummed
in the archive in order to protect the data. If the archive is corrupt, you
just lose the current file, not the whole archive.

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
FSArchiver  - системная утилита, позволяющая сохранить содержимое
файловых систем в виде сжатого файла. Файловые системы могут быть
восстановлены в разделы диска, отличающиеся от исходного размером и
типом файловой системы.

FSArchiver предоставляет следующие возможности:

- сохранение атрибутов файлов;
- включение в архив нескольких файловых систем;
- сохранение атрибутов файловой системы (label, uuid, размер блока);
- поддержку атрибутов файловой системы ntfs;
- создание контрольных сумм всего, что записано в архив;
- восстановление повреждённых архивов;
- много-поточное сжатие на нескольких процессорах в различные форматы (lzo, gzip, bzip, lzma);
- максимальное сжатие с помощью lzma (более медленный, но очень эффективный алгоритм);
- разделение архива на несколько файлов заданного размера;
- шифрование архива паролем на основе blowfish, libcrypto, openssl.

%prep
%setup
#patch -p2

%build
%autoreconf
##configure --disable-lz4 \
#           --disable-zstd
%configure

%make_build

%install
%makeinstall_std

%files
%doc ChangeLog AUTHORS README README THANKS NEWS
#config %_sysconfdir/%name.conf
%_sbindir/%name
%_man8dir/*

%changelog
* Tue Oct 10 2023 Hihin Ruslan <ruslandh@altlinux.ru> 1:0.8.7-alt1
- Version 0.8.7

* Thu May 19 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1:0.8.6-alt1
- Version 0.8.6

* Sat May 02 2020 Anton Midyukov <antohami@altlinux.org> 1:0.8.5-alt1
- Version 0.8.5

* Sat Apr 29 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1:0.8.1-alt1
- Version 0.8.1

* Thu Aug 18 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:0.8.0-alt1
- Version 0.8.0

* Thu Aug 18 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:0.6.24-alt1
- Version 0.6.24

* Sat Jun 18 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:0.6.23-alt1
- Version 0.6.23

* Sat Jun 11 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:0.6.22-alt2.49af
- Update from https://github.com/fdupoux/fsarchiver to git 49af670

* Thu Apr 07 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:0.6.22-alt1
- Update from https://github.com/fdupoux/fsarchiver
- Version 0.6.22

* Tue Oct 13 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.7.0-alt3
- Correct Russian description

* Tue Oct 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt2
- update source to 0.7.0_6a7efc616
- built with libparted-3.2

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

