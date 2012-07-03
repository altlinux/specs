# SPEC-file for secure_delete
#
#

%define version 3.1
%define release alt1

Name: secure_delete
Version: %version
Release: %release

Summary: Utilities for secure deleting data
Summary(ru_RU.KOI8-R): Утилиты для надёжного удаления данных

License: GPL
Group: System/Base
Url: http://www.thc.org/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar.gz
Patch0:  %name-3.1-kernel_module-alt.patch

#Requires: 

%description
THC Secure Delete is a set  of four utilities to perform the 
following:  secure deletion of files,  secure overwriting of 
the unused diskspace on the harddisk, secure overwriting and
cleaning of the swap filesystem  and secure overwriting  and 
cleaning of the unused memory.

%description -l ru_RU.KOI8-R
THC Secure Delete - набор четырёх утилит  для безопасного
удаления  файлов,  безопасной очистки  от остатков данных
неиспользуемого  пространства дисков,  безопасной очистки 
разделов подкачки  и  безопасной  очистки  неиспользуемой 
памяти.

%prep
%setup
%patch0

%build
%__make sdel-lib.o srm sfill sswap smem

%install
%__mkdir -p -- %buildroot%_bindir
%__mkdir -p -- %buildroot%_man1dir

%__cp srm sfill smem sswap %buildroot%_bindir
%__cp srm.1 sfill.1 smem.1 sswap.1 %buildroot%_man1dir

%files
%_bindir/*
%_mandir/man1/*
%doc CHANGES README usenix6-gutmann.doc secure_delete.doc the_cleaner.sh

%changelog
* Mon Sep 5 2005 Nikolay A. Fetisov <naf@altlinux.ru> 3.1-alt1
- Initial build for ALTLinux Sisyphus

* Thu Aug 11 2005 Nikolay A. Fetisov <naf@altlinux.ru> 3.1-alt0
- Initial build

