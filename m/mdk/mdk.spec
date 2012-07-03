Name: mdk
Version: 1.2.5
Release: alt1

Summary: GNU MIX Development Kit
Summary(ru_RU.UTF-8): Комплект разработки для MIX

License: GPLv3
Group: Development/Other
Url: http://www.gnu.org/software/mdk/mdk.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar
Patch: %name-1.2.3.patch

# Automatically added by buildreq on Mon Oct 29 2007
BuildRequires: cvs flex guile18-devel libglade-devel libncurses-devel libreadline-devel
# FIXME:
BuildPreReq:  intltool

%description
MDK stands for MIX Development Kit, and provides tools for developing and
executing, in a MIX virtual machine, MIXAL programs.

The MIX is Donald Knuth's mythical computer, described in the first volume
of The Art of Computer Programming, which is programmed using MIXAL, the MIX
assembly language.

MDK includes a MIXAL assembler (mixasm) and a MIX virtual machine (mixvm)
with a command line interface.  In addition, a GTK+ GUI to mixvm, called
gmixvm, is provided; and, for Emacs guy, exists emacs mode, which allows
running mixvm inside an Emacs GUD buffer.


%description -l ru_RU.UTF-8
MDK -- комплект разработки для MIX, предоставляющий утилиты для разработки и
выполнения программ для виртуальной машины MIX.

MIX -- мифический компьютер Дональда Кнута, который описан в первом томе
"Искусства программирования", который программируется с использованием MIXAL
-- языка ассемблера MIX.

MDK включает в себя ассемблер MIXAL (mixasm) и виртуальную машину MIX
(mixvm) с командно-строковым интерфейсом. В добавлении к ним,
предоставляется визуальный интерфейс к mixvm на основе GTK+, который
называется gmixvm; и для любителей Emacs, есть режим, который позволяет вам
запускать mixvm внутри буфера Emacs.

%prep
%setup -q
#%patch

%build
#%autoreconf
%configure
%make_build || %make
ln -s doc/img
cd doc
make html

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/%name/samples/
install -m 644 samples/*.mixal %buildroot%_datadir/%name/samples/
mkdir -p %buildroot%_emacslispdir
mv %buildroot/%_datadir/%name/*.el  %buildroot%_emacslispdir
rm -f %buildroot%_infodir/dir

%find_lang %name

%files -f %name.lang
%doc doc/mdk.html doc/img THANKS NEWS README TODO AUTHORS ChangeLog
%_bindir/*
%_infodir/*
%_datadir/%name/
%_emacslispdir/*

%changelog
* Sat May 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt1
- new version (1.2.5) import in git
- change license to GPLv3

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for mdk
  * postclean-05-filetriggers for spec file

* Mon Oct 29 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- fix linking, enable SMP-build
- update buildreqq
- build with new gtk (disable depricated GtkTooltips)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt0.1
- new version 1.2.3 (with rpmrb script)

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt0.2
- rebuild

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt0.1
- new version

* Fri Dec 31 2004 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- fix export for libglade

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- new version (with gtk2 :) )
- update requires

* Tue Jun 15 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version ( with gtk1 :( )
- build with guile16

* Tue Jun 10 2003 Ott Alex <ott@altlinux.ru> 1.0.1-alt1
- Initial build for ALTLinux

