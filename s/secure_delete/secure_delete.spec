# SPEC-file for secure_delete
#

Name: secure_delete
Version: 3.1
Release: alt3

Summary: Utilities for secure deleting data
Summary(ru_RU.UTF-8): Утилиты для надёжного удаления данных

License: %gpl2only
Group: System/Base
Url: http://www.thc.org/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-3.1-kernel_module-alt.patch
Patch1:  %name-3.1-configure-rand-file.patch

BuildRequires(pre): rpm-build-licenses

Conflicts: srm

%description
THC Secure Delete is a set  of four utilities to perform the
following:  secure deletion of files,  secure overwriting of
the unused diskspace on the harddisk, secure overwriting and
cleaning of the swap filesystem  and secure overwriting  and
cleaning of the unused memory.

%description -l ru_RU.UTF-8
THC Secure Delete - набор четырёх утилит  для безопасного
удаления  файлов,  безопасной очистки  от остатков данных
неиспользуемого  пространства дисков,  безопасной очистки
разделов подкачки  и  безопасной  очистки  неиспользуемой
памяти.

%prep
%setup
%patch0
%patch1 -p1

%build
make sdel-lib.o srm sfill sswap smem

%install
mkdir -p -- %buildroot%_bindir
mkdir -p -- %buildroot%_man1dir

cp -- srm sfill smem sswap %buildroot%_bindir
cp -- srm.1 sfill.1 smem.1 sswap.1 %buildroot%_man1dir

%files
%doc CHANGES README usenix6-gutmann.doc secure_delete.doc the_cleaner.sh
%_bindir/*
%_mandir/man1/*

%changelog
* Mon Jul 19 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.1-alt3
- Add the configure-rand-file patch from C7.1

* Mon Jul 19 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.1-alt2
- Add conflict on srm package (Closes: 36753)
- Spec file cleanup

* Mon Sep 5 2005 Nikolay A. Fetisov <naf@altlinux.ru> 3.1-alt1
- Initial build for ALTLinux Sisyphus

* Thu Aug 11 2005 Nikolay A. Fetisov <naf@altlinux.ru> 3.1-alt0
- Initial build

