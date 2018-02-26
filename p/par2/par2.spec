Name: par2
Version: 0.4
Release: alt3

Summary: File verification and repair tool
Summary(ru_RU.CP1251): ”тилита дл€ проверки и восстановлени€ файлов

License: GPL
Group: Archiving/Other
Url: http://parchive.sourceforge.net/

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: http://dl.sf.net/parchive/par2cmdline-%version.tar.bz2
Patch0:     par2cmdline-reedsolomon.cpp.patch
Patch1:     par2cmdline-packed.patch
Patch2:     par2cmdline-Makefile.am.patch

# Automatically added by buildreq on Mon Mar 05 2007
BuildRequires: gcc-c++

%description
%name is a program for creating and using PAR2 files to detect
damage in data files and repair them if necessary.

%description -l ru_RU.CP1251
%name --- это программа дл€ создани€ и использовани€ файлов PAR2,
позвол€ющих находить ошибки в файлах данных и исправл€ть их.

%prep
%setup -q -n par2cmdline-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1


chmod a-x NEWS ChangeLog

%build
%configure
%make_build
%__make check

%install
%makeinstall

%files
%doc NEWS README PORTING ROADMAP ChangeLog
%_bindir/*

%changelog
* Mon Mar 05 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4-alt3
- Recovery from orphaned
- Update buildreq
- Add make check
- Add patches
  + par2cmdline-reedsolomon.cpp.patch
  + par2cmdline-packed.patch
  + par2cmdline-Makefile.am.patch

* Sat Jan 28 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- NMU: fix bug #7990
- add URL to Source

* Tue Feb 22 2005 Andrey Astafiev <andrei@altlinux.ru> 0.4-alt1
- First version of RPM package for Sisyphus.
