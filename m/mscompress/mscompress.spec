Summary: MS compress/expand-compatible (de)compressor
Summary(pl):	(De)kompresor zgodny z MS compress/expand
Name: mscompress
Version: 0.3
Release: alt1
License: GPL
Group: Archiving/Compression
Url: ftp://ftp.penguin.cz/pub/users/mhi/mscompress
Source0: ftp://ftp.penguin.cz/pub/users/mhi/mscompress/%name-%version.tar.bz2
Patch0: mscompress-0.3-LDFLAGS.diff
BuildRequires: autoconf

%description
Microsoft compress.exe/expand.exe-compatible file (de)compressor.

%description -l pl
Program kompresuj±cy i dekompresuj±cy zgodny z compress.exe/expand.exe
Microsoftu.

%prep
%setup
%patch0 -p0

%build
#autoreconf
%configure
%make

%install

install -D -m755 msexpand %buildroot%_bindir/msexpand
install -D -m755 mscompress %buildroot%_bindir/mscompress
install -D mscompress.1 %buildroot%_man1dir/mscompress.1
install -D msexpand.1 %buildroot%_man1dir/msexpand.1

%files
%doc ChangeLog README TODO format.txt
%_bindir/*
%_mandir/man1/*

%changelog
* Mon Jun 20 2011 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Importing from MDV

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-9mdv2009.1
+ Revision: 317114
- use %%optflags and %%ldflags (P0)

* Tue Jun 17 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-8mdv2009.0
+ Revision: 223323
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-6mdv2008.1
+ Revision: 153264
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 0.3-5mdv2008.0
+ Revision: 68538
- rebuild

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 19:48:03 (55069)
- rebuild

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 19:47:15 (55068)
Import mscompress

* Fri Dec 30 2005 Olivier Thauvin <nanardon@mandriva.org> 0.3-3mdk
- rebuild
- mkrel

* Fri Sep 03 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.3-2mdk
- yearly rebuild

