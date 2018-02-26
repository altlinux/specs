Name: mrprojext
Version: 1.3.1
Release: alt2.qa1

Summary: mrprojext - MrProject-Databasefile-Extractor and -Converter
Summary(ru_RU.KOI8-R): Программа извлечения и конвертирования данных из файлов MrProject

License: GPL
Group: Office
Url: http://sourceforge.net/projects/mrprojext/

Packager: Pavel Vainerman <pv@altlinux.ru>

Source: %name-%version.tar.bz2
Patch: %name-%version.patch

# Automatically added by buildreq on Sat Jan 15 2005
BuildRequires: gcc-c++ hostinfo libpopt-devel libstdc++-devel libxml2-devel zlib-devel

%description
Shortly spoken MrProjext is a MrProject-Databasefile-Extractor and -Converter: 
It can search the tasks belonging to a specific timeslot or recource. 
And (as converter) it can rewrite the extracted result as MrProject-, Evolution-, Yank- or Pilot-File.

%description -l ru_RU.KOI8-R
Программа извлечения и конвертирования данных из файлов MrProject. 
Умеет конвертировать в форматы MrProject-, Evolution-, Yank- or Pilot-File.

%prep
%setup -q
%patch -p0

%build
%configure
%make_build

%install
#makeinstall
%make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc ChangeLog README
%_bindir/*
%_datadir/doc/*

%changelog
* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.1-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for mrprojext
  * obsolete-call-in-post-scrollkeeper-update for mrprojext
  * postclean-05-filetriggers for spec file

* Thu Nov 06 2008 Pavel Vainerman <pv@altlinux.ru> 1.3.1-alt2
- rebuild for gcc4.3

* Wed Feb 02 2005 Pavel Vainerman <pv@altlinux.ru> 1.3.1-alt1
- rebuild for gcc3.4

* Sat Jan 15 2005 Pavel Vainerman <pv@altlinux.ru> 1.3.1-alt0.2
- add patch
- rebuild

* Thu May 27 2004 Pavel Vainerman <pv@altlinux.ru> 1.3.1-alt0.1
- first build

