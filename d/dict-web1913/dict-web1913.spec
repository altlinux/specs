%define wrongversion 1.4+0.47pd

Name: dict-web1913
Version: 1.4_0.47pd
Release: alt1
Epoch: 1

Summary: Webster dictionary in dict format
License: GPL, Public Domain
Group: Text tools

Source: %name-%wrongversion.tar.bz2
Source1: webster-sedscript
Source2: debian-copyright
Patch: debian-webster.patch.bz2

BuildArchitectures: noarch
# Automatically added by buildreq on Sun Oct 19 2003
BuildRequires: dict-tools flex libltdl tetex-core tetex-dvips tetex-latex transfig
BuildRequires: dict-tools
PreReq: dictd

Summary(ru_RU.KOI8-R): Словарь Вебстера в формате dict

%description
This is the most full english dictionary by Webster published in 1913.
It is free because all copyrights ended due to the time. But it is still
very helpful in work.

%description -l ru_RU.KOI8-R
Это наиболее полный английский словарь, созданный Вебстером и опубликованный
в 1913 году. Он стал свободным из-за того, что прошло много времени
с его опубликования. Однако он до сих пор сохраняет свою актуальность
и помогает в работе.

%prep
%setup -q -n %name-%wrongversion
%patch0 -p1
cp %SOURCE1 ./sedfile

%build
sed -i "s|__FUNCTION__|__FILE__|g" libmaa/*.c
%configure
export LANG=C
#NO SMP
%make
%make db

%install
mkdir rpmdoc
cp -a ChangeLog README rpmdoc
cp -a %SOURCE2 rpmdoc/LICENSE
mkdir -p %buildroot%_datadir/dictd
export LANG=C
%make dictdir=%buildroot%_datadir/dictd install

%post
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%postun
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%files
%_datadir/dictd/*
%doc rpmdoc/*

%changelog
* Wed Feb 20 2008 Michael Shigorin <mike@altlinux.org> 1:1.4_0.47pd-alt1
- alt1
- spec macro abuse cleanup

* Tue May 24 2005 Michael Shigorin <mike@altlinux.ru> 1.4_0.47pd-ipl6.1
- fixed build; thanks to Vitaly Lipatov (lav@) for the workaround

* Sun Oct 19 2003 Michael Shigorin <mike@altlinux.ru> 1.4_0.47pd-ipl6
- updated buildrequires
- rebuild (Alexey asked to temporarily take care of the package)

* Wed Jan 29 2003 Alexey Dyachenko <alexd@altlinux.ru> 1.4_0.47pd-ipl5
- fixed bug #0001708: service dictd condreload would be more appropriate
	than condrestart

* Tue Oct 15 2002 Alexey Dyachenko <alexd@altlinux.ru> 1.4_0.47pd-ipl4
- fixed bug #0001350:  missing PreReq: dictd
- spec cleanup

* Wed Apr 17 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4_0.47pd-ipl3
- removed illegal symbol from version

* Wed Feb 21 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> ipl2
- Added /usr/sbin/ before dictdconfig in case use hasn't /usr/sbin in
$path.

* Mon Feb  5 2001 Peter 'Nidd' Novodvorsky ipl1
- initial release

