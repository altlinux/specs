Name: unace
Version: 1.2b
Release: alt3

Summary: ACE unarchiver
License: Freely distributable
Group: Archiving/Compression

Url: http://www.winace.com
Source: %name-%version.tar.gz
Patch0: unace-1.2b-CAN-2005-0160-CAN-2005-0161.patch
Patch1: unace-1.2b-64bit.patch

Summary(ru_RU.UTF-8): Распаковщик архивов ACE 1.x

%description
The %name utility is a freeware program, distributed with source
code and developed for extracting and viewing the contents of
archives created with the ACE archiver v1.x. ACE archiver is
developed by "ACE Compression Software".

%description -l ru_RU.UTF-8
Программа %name предназначена для распаковки и просмотра содержимого
архивов, сжатых архиватором ACE версий 1.х. Архиватор ACE разработан
фирмой "ACE Compression Software".

%prep
%setup
%patch0 -p0
%patch1 -p1

%build
make clean
make dep
make

%install
install -pDm755 %name %buildroot%_bindir/%name

%files
%doc readme.txt file_id.diz
%_bindir/*

# 2.5 is closed source and known insecure (#24907)

%changelog
* Fri Jan 28 2011 Michael Shigorin <mike@altlinux.org> 1.2b-alt3
- applied patch from Gentoo to fix CAN-2005-0160, CAN-2005-0161
  (closes: #24907)
- applied unace-1.2b-64bit.patch from Gentoo as well

* Sun Jun 15 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.2b-alt2
- build fix (make clean)

* Thu Mar 20 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.2b-1
- ALTLinux build
