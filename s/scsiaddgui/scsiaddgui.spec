Summary: A graphical front end for scsiadd
Name: scsiaddgui
Version: 2.1
Release: alt1
License: GPL
Url: http://scsiaddgui.sourceforge.net
Requires: python, tcl-tktreectrl => 2.4.1, scsiadd
Group: System/Kernel and hardware
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: scsiaddgui-2.1.tar

BuildArch: noarch

%description
scsiaddgui provides a GUI for the scsiadd - utility

%description -l UTF-8
scsiaddgui GUI для утилиты scsiadd



%prep
%setup

%build
%__subst 's!/usr/local/share!%_datadir!g' *.py
pushd locale

for file in *.po
do
 fil=$(basename $file .po)
 msgfmt $fil.po -o $fil.gmo
done
popd


%install
install -d %buildroot%_datadir/scsiaddgui-%version
install -d %buildroot%_datadir/scsiaddgui-%version/TkTreectrl
install -v --mode=644 TkTreectrl/* %buildroot%_datadir/scsiaddgui-%version/TkTreectrl
install -d %buildroot%_bindir
install --mode=755 scsiaddgui.py %buildroot%_datadir/scsiaddgui-%version/scsiaddgui.py

install --mode=644 help_de %buildroot%_datadir/scsiaddgui-%version/help_de
install --mode=644 help_en %buildroot%_datadir/scsiaddgui-%version/help_en
install --mode=644 help_fr %buildroot%_datadir/scsiaddgui-%version/help_fr
install --mode=644 help_fr %buildroot%_datadir/scsiaddgui-%version/help_ru

install -d %buildroot%_datadir/locale/de/LC_MESSAGES
install -v --mode=644 locale/de.gmo %buildroot%_datadir/locale/de/LC_MESSAGES/scsiaddgui.mo
install -d %buildroot%_datadir/locale/fr/LC_MESSAGES
install -v --mode=644 locale/fr.gmo %buildroot%_datadir/locale/fr/LC_MESSAGES/scsiaddgui.mo
install -d %buildroot%_datadir/locale/ru/LC_MESSAGES
install -v --mode=644 locale/ru.gmo %buildroot%_datadir/locale/ru/LC_MESSAGES/scsiaddgui.mo

(cd %buildroot
ln -s %_datadir/scsiaddgui-%version/scsiaddgui.py ./%_bindir/scsiaddgui
)
%find_lang %name

%files -f %name.lang
%doc doc/{ChangeLog,README}
%_bindir/scsiaddgui
%dir %_datadir/scsiaddgui-%version
%_datadir/scsiaddgui-%version/scsiaddgui.py
%_datadir/scsiaddgui-%version/help_de
%_datadir/scsiaddgui-%version/help_en
%_datadir/scsiaddgui-%version/help_fr
%_datadir/scsiaddgui-%version/help_ru
%dir %_datadir/scsiaddgui-%version/TkTreectrl
%_datadir/scsiaddgui-%version/TkTreectrl/*

%changelog
* Wed Nov 18 2015 Hihin Ruslan <ruslandh@altlinux.ru> 2.1-alt1
- New version

* Sun Mar 29 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.6-alt2
- add desktop and pam files

* Tue Mar 24 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.6-alt1
- New version

* Mon Mar 23 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.5-alt1
- initial build for ALT Linux Sisyphus

* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.5-6mdv2010.0
+ Revision: 433634
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-5mdv2009.0
+ Revision: 260582
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-4mdv2009.0
+ Revision: 252220
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5-2mdv2008.1
+ Revision: 140776
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 16:49:58 (54906)
- rebuild

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 16:48:47 (54905)
Import scsiaddgui

* Tue Apr 11 2006 Lenny Cartier <lenny@mandriva.com> 1.5-1mdk
- 1.5

* Tue Aug 09 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.4-1mdk
- 1.4
- %%mkrel
- be sure to wipe out buildroot at the beginning of %%install

* Mon Nov 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.3-1mdk
- 1.3

* Thu Jul 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2-1mdk
- 1.2

* Wed Jan 07 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1-2mdk
- fix DIRM

* Sun Nov 02 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1-1mdk
- 1st (real) mdk spec

* Fri Oct 31 2003 Michael Lange<klappnase@8ung.at>
- added Control.py as a replacement for the Tix.Control widget,
  so now Tix is not needed anymore, added optionDB(v.1.1)

* Mon Sep 15 2003 Michael Lange<klappnase@8ung.at>
- a little code cleanup, maybe this is the final version (v. 1.0)
