Summary: A graphical front end for scsiadd
Name: scsiaddgui
Version: 2.1
Release: alt2
License: GPL
Url: http://scsiaddgui.sourceforge.net
Requires: python, tcl-tktreectrl => 2.4.1, scsiadd
Group: System/Kernel and hardware
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

# http://www.8ung.at/klappnase/downloads/%name-%version.tar.bz2
Source: %name-%version.tar
Source1: %name-pam
Source2: %name-security
Source3: %name.desktop
Source4: %name.png


BuildArch: noarch

%description
scsiaddgui provides a GUI for the scsiadd - utility

%description -l UTF-8
scsiaddgui - графический клиент для утилиты scsiadd



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
install -d %buildroot%_sbindir

install --mode=755 scsiaddgui.py %buildroot%_datadir/scsiaddgui-%version/scsiaddgui.py

install --mode=644 help_de %buildroot%_datadir/scsiaddgui-%version/help_de
install --mode=644 help_en %buildroot%_datadir/scsiaddgui-%version/help_en
install --mode=644 help_fr %buildroot%_datadir/scsiaddgui-%version/help_fr
install --mode=644 help_ru %buildroot%_datadir/scsiaddgui-%version/help_ru

install -d %buildroot%_datadir/locale/de/LC_MESSAGES
install -v --mode=644 locale/de.gmo %buildroot%_datadir/locale/de/LC_MESSAGES/scsiaddgui.mo
install -d %buildroot%_datadir/locale/fr/LC_MESSAGES
install -v --mode=644 locale/fr.gmo %buildroot%_datadir/locale/fr/LC_MESSAGES/scsiaddgui.mo
install -d %buildroot%_datadir/locale/ru/LC_MESSAGES
install -v --mode=644 locale/ru.gmo %buildroot%_datadir/locale/ru/LC_MESSAGES/scsiaddgui.mo

ln -s %_datadir/%name-%version/%name.py %buildroot%_sbindir/%name
ln -s %_bindir/consolehelper %buildroot%_bindir/%name

install -pD -m640 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -pD -m640 %SOURCE2 %buildroot%_sysconfdir/security/console.apps/%name
install -pD -m644 %SOURCE3 %buildroot/%_desktopdir/%name.desktop
install -D -m644 %SOURCE4 %buildroot%_niconsdir/%name.png

%find_lang %name

%files -f %name.lang
%doc doc/{ChangeLog,README}
%_sbindir/%name
%_bindir/%name
%dir %_datadir/%name-%version
%_desktopdir/%name.desktop
%_niconsdir/*
%_sysconfdir/pam.d/*
%_sysconfdir/security/console.apps/*
%_datadir/%name-%version/*.py
%_datadir/%name-%version/help_de
%_datadir/%name-%version/help_en
%_datadir/%name-%version/help_fr
%_datadir/%name-%version/help_ru

%dir %_datadir/scsiaddgui-%version/TkTreectrl
%_datadir/scsiaddgui-%version/TkTreectrl/*


%changelog
* Sun Jul 16 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2.1-alt2
- Add desktop and pam files

* Wed Nov 18 2015 Hihin Ruslan <ruslandh@altlinux.ru> 2.1-alt1
- Version 2.1-alt1

* Sun Mar 29 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.6-alt2
- Add desktop and pam files

* Tue Mar 24 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.6-alt1
- New version

* Mon Mar 23 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.5-alt1
- initial build for ALT Linux Sisyphus

