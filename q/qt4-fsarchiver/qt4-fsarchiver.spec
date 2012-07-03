%define subversion alt

Summary: GUI for Filesystem Archiver for Linux
Name: qt4-fsarchiver
Version: 0.6.12
Release: alt1
Url: http://www.fsarchiver.org
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name.tar
Source1: %name-pam
Source2: %name-security

License: GPLv2+
Group: Archiving/Backup


# Automatically added by buildreq on Wed Jun 29 2011
# optimized out: fontconfig libX11-devel libXext-devel libcom_err-devel libgpg-error libgpg-error-devel libqt4-core libqt4-devel libqt4-gui libstdc++-devel zlib-devel
BuildRequires: bzlib-devel gcc-c++ libattr-devel libblkid-devel libe2fs-devel libgcrypt-devel liblzma-devel liblzo2-devel libqt4-network libuuid-devel phonon-devel

%description
QT4-FSArchiver is GUI for fsarhiver.

Fsaiveris a system tool that allows you to save the contents of
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
QT4-FSArchiver это GUI для fsarhiver.

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
%setup -n %name

echo QMAKE_CXXFLAGS_RELEASE = %optflags >>  qt4-fsarchiver.pro
echo QMAKE_CFLAGS_RELEASE = %optflags >>  qt4-fsarchiver.pro

%build
export PATH=$PATH:%_qt4dir/bin

qmake QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" qt4-fsarchiver.pro

INSTALL_ROOT=%buildroot qmake qt4-fsarchiver.pro

#./configure  --prefix=/usr \
#--bindir=/usr/bin \
#--datadir=/usr/share \
#--qtdir=%_qt4dir



lrelease qt4-fsarchiver.pro

%make_build

%install
INSTALL_ROOT=%buildroot %makeinstall_std
mkdir -p %buildroot%_datadir/qt4/translations
cp translations/%{name}*.qm %buildroot%_datadir/qt4/translations
install -D -m644 %buildroot/%_pixmapsdir/harddrive.png %buildroot%_liconsdir/%name.png
rm %buildroot/%_pixmapsdir/harddrive.png


install -d -m 755 %buildroot%_bindir/

ln -s %_bindir/consolehelper %buildroot%_bindir/%name

install -pD -m640 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -pD -m640 %SOURCE2 %buildroot%_sysconfdir/security/console.apps/%name


%files
%_sbindir/%name
%_bindir/%name
%_desktopdir/qt4-fsarchiver.desktop
%_iconsdir/hicolor/*/apps/*
%_sysconfdir/pam.d/*
%_sysconfdir/security/console.apps/*
%_datadir/qt4/translations/*%{name}*.qm

%changelog
* Wed Jun 29 2011 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.12-alt1
- Initial build for ALT Linux




