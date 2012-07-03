# SPEC file for cryptsetup utility: setup crypto disks using
# /dev/mapper interface in 2.6.x kernels

%define _root_sbindir /sbin

Name: cryptsetup
Version: 1.4.2
Release: alt1

Summary: utility to setup a encrypted disks with LUKS support
Summary(ru_RU.UTF-8): утилита управления зашифрованными дисковыми разделами с поддержкой LUKS

License: %gpl2only
Group: System/Kernel and hardware
URL: http://code.google.com/p/cryptsetup/

Source0: %name-%version.tar
Source1: %name.README.ALT.utf-8
Patch0: %name-%version-%release.patch

Requires: lib%name = %version-%release

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Sun Nov 15 2009
BuildRequires: libdevmapper-devel libgcrypt-devel libpopt-devel libuuid-devel
BuildRequires: libudev-devel libselinux-devel

# Rename package from cryptsetup-luks-1.0.6-alt0.pre2 to cryptsetup-1.0.6-alt1
Provides:  cryptsetup-luks = %version
Obsoletes: cryptsetup-luks < %version-%release

%description
LUKS ( Linux Unified Key Setup ) is the upcoming standard for 
Linux disk encryption. By providing a standard on-disk-format, 
it does not only facilitate compatibility among distributions,
but also provide secure management of multiple user passwords.
In contrast to existing solution,  LUKS stores all  necessary 
setup information  in the partition header, enabling the user
to transport or migrate his data seamlessly.

This package contains cryptsetup utility to setup a encrypted 
disks based on  dm-crypt  module for 2.6 kernel, with support 
for LUKS infrastructure. Also cryptsetup can handle old 2.4.x
cryptoloop devices.

%description -l ru_RU.UTF-8
LUKS ( Linux Unified Key Setup ) - разрабатываемый стандарт 
для шифрования дисков в Linux. Определяя стандартный формат
хранения  информации на дисках,  он не только  способствует 
совместимости  между различными  дистрибутивами,  но  также 
предоставляет возможность управлять безопасностью доступа к 
данным  путём  использования  нескольких   пользовательских
паролей. По сравнению с существующими решениями, в LUKS вся
необходимая  информация по  настройке параметров шифрования 
хранится в заголовке  раздела диска, облегчая пользователям
перемещение или миграцию данных.

Данный пакет содержит  утилиту  cryptsetup  для  управления 
зашифрованными  дисками, основанными на модуле dm-crypt для
ядер Linux 2.6.x,  с поддержкой  инфраструктуры LUKS. Также 
cryptsetup может  управлять старыми дисками,  использующими 
модуль cryptoloop ядер 2.4.x. 

%package -n lib%name
Group: System/Libraries
Summary: Cryptsetup shared library

%description -n lib%name
This package contains the cryptsetup shared library, libcryptsetup.

%package -n lib%name-devel
Summary: development files for cryptsetup-luks
Summary(ru_RU.UTF-8): файлы для разработки программ с использованием cryptsetup-luks
Group: Development/C
Requires: lib%name = %version-%release
Provides:  %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release

%description -n lib%name-devel
LUKS ( Linux Unified Key Setup ) is the upcoming standard for 
Linux disk encryption. By providing a standard on-disk-format, 
it does not only facilitate compatibility among distributions,
but also provide secure management of multiple user passwords.
In contrast to existing solution,  LUKS stores all  necessary 
setup information  in the partition header, enabling the user
to transport or migrate his data seamlessly.

This package includes  the  development libraries  and header 
files needed for developing applications  that use LUKS.  You
need it only  if  You  plan to  develop or  compile some LUKS 
applications.

%description -n lib%name-devel -l ru_RU.UTF-8
LUKS ( Linux Unified Key Setup ) - разрабатываемый стандарт 
для шифрования дисков в Linux. Определяя стандартный формат
хранения  информации на дисках,  он не только  способствует 
совместимости  между различными  дистрибутивами,  но  также 
предоставляет возможность управлять безопасностью доступа к 
данным  путём  использования  нескольких   пользовательских
паролей. По сравнению с существующими решениями, в LUKS вся
необходимая  информация по  настройке параметров шифрования 
хранится в заголовке  раздела диска, облегчая пользователям
перемещение или миграцию данных.

Данный  пакет  содержит  библиотеки  и  заголовочные  файлы,
необходимые для разработки использующих LUKS приложений.  Он
необходим Вам  только  если Вы планируете  разрабатывать или
компилировать какие-либо приложения с поддержкой LUKS.

%prep
%setup -n %name-%version
%patch0 -p1

cp -- %SOURCE1 README.ALT.utf-8

# Replacing license file with reference
mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
NOCONFIGURE=1 ./autogen.sh
%configure --sbindir=%_root_sbindir --libdir=/%_lib
%make

%install
%make DESTDIR=%buildroot install
# move libcryptsetup.so to %%_libdir
pushd %buildroot/%_lib
rm libcryptsetup.so
mkdir -p %buildroot/%_libdir
ln -s ../../%_lib/$(ls libcryptsetup.so.?.?.?) %buildroot/%_libdir/libcryptsetup.so
mv %buildroot/%_lib/pkgconfig %buildroot/%_libdir
popd
mkdir -p %buildroot/%_sbindir
ln -s ../../sbin/%name %buildroot/%_sbindir/%name

%find_lang %name


%files -f %name.lang
%doc docs/*
%doc AUTHORS FAQ README
%doc --no-dereference COPYING
%doc README.ALT.utf-8
%_root_sbindir/%name
%_sbindir/%name
%_man8dir/*

%files -n lib%name
/%_lib/lib%name.so.*

%files -n lib%name-devel
%_includedir/lib%name.h
%_libdir/lib%name.so
%_pkgconfigdir/*

%changelog
* Mon May 21 2012 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Mon Apr 02 2012 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Mon Oct 31 2011 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Jun 07 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon Feb 14 2011 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0
- cleanup spec
- move lib to /%%_lib, sbin to /sbin
- add lib subpackage
- disabled patches 5,7,9,10 (need review)
- add patches 12,13 for fix build
- drop Werror
- rename package cryptosetup-devel to libcryptosetup-devel

* Sun Nov 15 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.7-alt1
- New version 1.0.7
- Fix Requies/Obsoletes

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.6-alt2
- Remove %%post_ldconfig calls
- Man page typos fixed

* Fri Mar 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.6-alt1
- New version 1.0.6
- Rename package back from cryptsetup-luks to cryptsetup following upstream

* Sun Mar 02 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.6-alt0.pre2
- New version 1.0.6-pre2
  - Now cryptsetup will fail when trying to create two mappings for a single device
  - Remove O_EXCL requirement for certain LUKS operations
  - Deprecate 'reload' action
  - No password retry for I/O errors
  - A lot of bug fixes

* Fri Mar 23 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.4-alt2.svn26
- Fix build with -Werror on x86_64

* Thu Mar 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.4-alt1.svn26
- Current developer version svn26
 -- Fix segfaults with unsupported keysize
 -- Fix a sector size error
 -- Prevents password retrying with I/O errors
 -- Allow hashing of keys passed through stdin
 -- Other bugfixes and code improvements
- Adding several patches for build with -Werror
- Spec file cleanup
- Adding README.ALT (fix FR # 8300)

* Mon Jan 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.4-alt0
- New version 1.0.4
 -- Fix getline problem for 64-bit archs
 -- Fix 64 bit compiler warning issues
 -- Add support for reading binary keys from stdin using the "-" as key file
 -- Add support to allow user selection of key slot
  
* Mon Jul 10 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.3-alt1
- New version 1.0.3
 -- Fix sector size of the temporary mapping to be an integral 
    of the block's sector size.
 -- Add LUKS key copy cmd: luksKeyCopy
 -- Add option to supply a master key directly for LUKS commands:
    luksFormat, luksOpen and luksAddKey.
 -- More verbose error logging; meaningful exit codes
 -- Other small bugfixes, see CHANGELOG for details
- Adding numerous patches from Debian, most significant is:
 -- Fix the terminal status after a timeout
 -- Fixes standard input to allow more than 32 characters password

* Sun Feb 26 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.3-alt0.1
- New version 1.0.3-rc2
  * Work with libdevmapper 1.02.02
  * Add LUKS key copy cmd: luksKeyCopy
  * Add option to supply a master key directly for LUKS commands:
    luksFormat, luksOpen and luksAddKey.
	 
* Fri Jan 27 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.1-alt2
- Fix incompatibility with libdevmapper 1.02.02
- SPEC file cleanup

* Mon Sep 05 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.1-alt1
- Initial build for ALT Linux Sisyphus

* Thu Jul 21 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.1-alt0
- Initial build


