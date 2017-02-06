%define subversion alt
%define subver 0
%define sname qt5-fsarchiver


Summary: GUI for Filesystem Archiver for Linux
Name: qt-fsarchiver
Version: 0.8.1.%subver
Release: alt1
Url: http://www.fsarchiver.org
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:  %sname-%version-%subver.tar
Source1: %sname-pam
Source2: %sname-security
Source3: %sname.desktop
# Source4: %{sname}_ru-%version-%subver.ts

Patch: qt5-fsarchiver-0.6.19-alt-glibc-2.16.patch
Patch1: qt5-fsarchiver_qmake_pro.patch
#Patch2: qt5-fsarchiver-0.6.20-cppcheck.patch
Patch3: qt5-fsarchiver-sudo-0.6.19-21.patch
Patch4: qt5-fsarchiver-findsmb-0.8.0.patch

License: GPLv2+
Group: Archiving/Backup

Provides: qt4-fsarchiver  = %version-%release
Obsoletes: qt4-fsarchiver  <= 0.6.18
Provides: qt5-fsarchiver  = %version-%release
Conflicts: qt5-fsarchiver qt4-fsarchiver


BuildRequires(pre): rpm-macros-qt5

# Automatically added by buildreq on Sat May 14 2016
# optimized out: gcc-c++ libGL-devel libcom_err-devel libgpg-error libgpg-error-devel libqt5-core libqt5-gui libqt5-widgets libqt5-xml libstdc++-devel python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-script-devel qt5-tools qt5-webchannel-devel
BuildRequires: qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires: qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel

BuildRequires: bzlib-devel libattr-devel libblkid-devel libe2fs-devel libgcrypt-devel liblzma-devel liblzo2-devel libuuid-devel python-module-junos-eznc python3-module-zope zlib-devel

BuildRequires: libcom_err-devel libgpg-error-devel

# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libcom_err-devel libe2fs-devel libgcrypt-devel libgpg-error-devel libuuid-devel zlib-devel
# END SourceDeps(oneline)

# Requires: btrfs-progs gdisk sshpass nmap samba-client nfs-clients fuse-sshfs 
Requires: btrfs-progs gdisk nmap samba-client nfs-clients fuse-sshfs 

%description
Qt-fsarchiver - a graphical version of the application fsarchiver

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
Qt-fsarchiver это графическая версия fsarhiver.

fsarchiver  - системный инструментарий, позволяяющий вам сохранять содержимое
файловой системы в виде сжатого файла. Файловая система может быть восстановлена
в отличающемся от исходного разделе диска.

В fsarchiver уже включены следующие возможности:

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
%setup -n %sname
#%%patch2 -p2
%patch -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1

# cp %%SOURCE4 ./translations/%{sname}_ru.ts

echo QMAKE_CXXFLAGS_RELEASE = %optflags >>  qt5-fsarchiver.pro
echo QMAKE_CFLAGS_RELEASE = %optflags >>  qt5-fsarchiver.pro

%build
export PATH=$PATH:%_qt5_bindir

%qmake_qt5 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" qt5-fsarchiver.pro

INSTALL_ROOT=%buildroot %qmake_qt5 qt5-fsarchiver.pro


lrelease qt5-fsarchiver.pro

%make_build

%install
INSTALL_ROOT=%buildroot %makeinstall_std

mkdir -p %buildroot%_datadir/qt5/translations
cp translations/%{sname}*.qm %buildroot%_datadir/qt5/translations
install -d -m755 %buildroot%_liconsdir/
install -pD -m640 src/images/harddrive.png %buildroot%_liconsdir/%sname.png

install -d -m 755 %buildroot%_bindir/

ln -s %_bindir/consolehelper %buildroot%_bindir/%sname

install -pD -m640 %SOURCE1 %buildroot%_sysconfdir/pam.d/%sname
install -pD -m640 %SOURCE2 %buildroot%_sysconfdir/security/console.apps/%sname

rm -f %buildroot/%_desktopdir/*-%sname.desktop

install -pD -m640 %SOURCE3 %buildroot/%_desktopdir/%sname.desktop

%files
%doc doc/Aenderungen doc/Change doc/Liesmich doc/Readme doc/copyright

%_sbindir/*
%_bindir/%sname
%_desktopdir/qt5-fsarchiver.desktop
%_liconsdir/*
%_sysconfdir/pam.d/*
%_sysconfdir/security/console.apps/*
%_datadir/qt5/translations/*%{sname}*.qm
%exclude %_docdir/%sname
#exclude %_datadir/qt5/translations/*%{name}*.ts
%_datadir/polkit-1/actions/org.project.pkexec.run-%sname.policy

%changelog
* Mon Feb 06 2017 Hihin Ruslan <ruslandh@altlinux.ru> 0.8.1.0-alt1
- Version 0.8.1-0

* Sun Oct 23 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.8.0.03-alt1
- Version 0.8.0-3

* Wed Sep 28 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.8.0.0-alt1
- Version 0.8.0-0

* Thu Sep 22 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19.21-alt2
- Add qt5-fsarchiver-sudo-0.6.19-21.patch

* Fri Jul 22 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19-alt1.21
- Version 0.6.19-21

* Sun Jul 17 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19-alt1.20.1
- Version 0.6.19-20.1 

* Fri Jun 10 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19-alt1.19.1
- version 0.6.19-19.1 

* Sat Jun 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19-alt1.19
- version 0.6.19-19 with qt5

* Tue May 10 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19-alt1.18
- version 0.6.19-18

* Sat Apr 16 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19-alt1.16
- version 0.6.19-16
- correct russian translation

* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.19-alt1.12.qa1
- NMU: rebuilt with libgcrypt.so.11 -> libgcrypt.so.20.

* Mon Mar 16 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19-alt1.12
- new version

* Sat Feb 21 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19-alt1.2
- new subversion
- new russian translation

* Wed Feb 18 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19-alt1.1
- Fix qt4-fsarchiver.desktop

* Mon Feb 16 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.19-alt1
- New version

* Mon Dec 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.12-alt1.1
- Fixed build with glibc 2.16

* Wed Jun 29 2011 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.12-alt1
- Initial build for ALT Linux




qt5-fsarchiver-findsmb-0.8.0.patch
