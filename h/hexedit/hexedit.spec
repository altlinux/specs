Name: hexedit
Version: 1.2.12
Release: alt1.0

Summary: View and edit files in hexadecimal or in ASCII
Summary(ru_RU.KOI8-R): Редактор файлов в ASCII- или шестнадцатиричном режиме
License: GPL
Group: Editors
URL: http://merd.sourceforge.net/pixel/hexedit.html

Source: http://merd.sf.net/pixel/hexedit-%version.src.tgz
Patch: %name-1.2.2-rh-makefile.patch

# Automatically added by buildreq on Thu Sep 29 2005
BuildRequires: libncurses-devel libtinfo-devel

%description
hexedit shows a file both in ASCII and in hexadecimal. The file can be
a device as the file is read a piece at a time. You can modify the
file and search through it.

%description -l ru_RU.KOI8-R
hexedit отображает содержимое файла одновременно в ASCII и шестнадцатиричном
представлении. При этом не накладывается никаких ограничений на тип файла;
в частности, это может быть файл устройства. В открытом файле можно
осуществлять поиск и редактирование.

%prep
%setup -q -n %name
%patch -p1

%build
%configure
%make_build

%install
%makeinstall

%files
%doc Changes TODO
%_bindir/*
%_man1dir/*

%changelog
* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.12-alt1.0
- Automated rebuild.

* Thu Sep 29 2005 Victor Forsyuk <force@altlinux.ru> 1.2.12-alt1
- 1.2.12

* Tue Apr 12 2005 Victor Forsyuk <force@altlinux.ru> 1.2.10-alt1
- Update buildreqs.

* Mon Apr 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.2.9-alt1
- 1.2.9

* Tue Jan 27 2004 Stanislav Ievlev <inger@altlinux.org> 1.2.8-alt1
- 1.2.8

* Mon Dec 29 2003 Stanislav Ievlev <inger@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Thu Mar 27 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt1
- 1.2.4

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.3-alt2
- Rebuild with gcc3

* Fri Aug 16 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- 1.2.3

* Wed Jan 09 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Mon Jul 23 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.2.1-alt1
- new version

* Wed Apr 10 2001 Rider <rider@altlinux.ru> 1.2-alt1
- new version

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.1.2-ipl2mdk
- Automatically added BuildRequires.

* Wed Jul 19 2000 Dmitry V. Levin <ldv@fandra.org> 1.1.2-ipl1mdk
- RE adaptions.
- Russian translation for Description and Summary tags.

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 1.1.2-1mdk
- new version
- cleanup
- BM, macroization

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 1.1.1-4mdk
- new group

* Mon Nov 22 1999 Pixel <pixel@linux-mandrake.com>
- build release

* Tue Jul 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- bzip2 source

