%define pack zisofs-tools

Name: mkzftree
Version: 1.0.7
Release: alt1

Summary: Create a zisofs/RockRidge compressed file tree
Summary(ru_RU.CP1251): Подготовка сжатого дерева файлов
License: GPL
Url: ftp://ftp.kernel.org/pub/linux/utils/fs/zisofs/
Group: Archiving/Cd burning
Packager: Eugene Ostapets <eostapets@altlinux.ru>

Source: ftp://ftp.kernel.org/pub/linux/utils/fs/zisofs/%pack-%version.tar.bz2
Patch1: mkzftree-1.0.3-patch

# Automatically added by buildreq on Mon Dec 02 2002
BuildRequires: zlib-devel

%description
%name takes an input file tree and create a corresponding compressed file
tree that can be used with an appropriately patched mkisofs to create
a transparent-compression ISO9660/RockRidge filesystem using
the "ZF" compression records.

%description -l ru_RU.CP1251
%name подготавливает сжатое дерево файлов, которое может быть
использовано утилитой mkisofs для создания прозрачно декомпрессируемой
файловой системы ISO9660/RockRidge.

%prep
%setup -q -n %pack-%version
%patch1 -p1
%configure

%build
%make

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc README CHANGES

%changelog
* Thu Nov 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Mon Dec 02 2002 Andrei Astafiev <andrei@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Mon Dec 17 2001 Andrei Astafiev <andrei@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Nov 08 2001 Andrei Astafiev <andrei@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Oct 12 2001 Andrei Astafiev <andrei@altlinux.ru> 1.0.1-alt1
- First version of RPM package
