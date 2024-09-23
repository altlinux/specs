%define variant alt-kworkstation
%define Variant ALT KWorkstation

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 10.4
Release: alt2

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Conflicts: %(for n in %variants ; do [ "$n" = %name ] || echo -n "$n "; done)

Provides: docs-kworkstation = 8.0-alt1
Obsoletes: docs-kworkstation <= 8.0

BuildRequires(pre):rpm-build-licenses
BuildRequires: publican
BuildRequires: perl-podlators
BuildRequires: libwebp-tools

%description
%Variant documentation.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docsinstalldir install
ln -s $(relative %_docsinstalldir %_documentationdir) %buildroot%_documentationdir
sed -i 's/src="images\/\(.*\).png"/src="images\/\1.webp"/g' %buildroot%_docsinstalldir/ru-RU/index.html
for file in %buildroot%_docsinstalldir/ru-RU/images/*.png; do cwebp $file -o %buildroot%_docsinstalldir/ru-RU/images/$(basename $file .png).webp -quiet && rm $file; done

%files
%_docsinstalldir
%_documentationdir

%changelog
* Mon Sep 23 2024 Elena Mishina <lepata@altlinux.org> 10.4-alt2
- typo fixes, small improvements (closes #51469, #51473, #51470)

* Thu Sep 05 2024 Elena Mishina <lepata@altlinux.org> 10.4-alt1
- update to ALT Kworkstation 10.4

* Tue Mar 19 2024 Elena Mishina <lepata@altlinux.org> 10.3-alt3
- update screenshots
- small improvements

* Tue Mar 05 2024 Elena Mishina <lepata@altlinux.org> 10.3-alt2
- update discover (closes #49520, #49524, #49522)
- update samba (closes #49561)
- add krfb (closes #49554)
- small improvement (closes #49461, #49462, #49480, #49466, #49469)

* Mon Feb 19 2024 Elena Mishina <lepata@altlinux.org> 10.3-alt1
- update to ALT Kworkstation 10.3

* Wed Sep 27 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt10
- discover: deleted double (closes #47747)
- synaptic: fixed typos (closes #47746)
- fixed boot-disk (closes #47748)

* Tue Sep 12 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt9
- small improvement (closes #47662)
- update kfind screenshots (closes #47650)
- fix discover screenshot (closes #47649)

* Tue Sep 12 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt8
- fix Discover to dist upgrade

* Tue Sep 05 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt7
- update screenshots
- small improvements

* Thu Aug 31 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt6
- update to ALT Kworkstation 10.2RC2

* Tue Aug 15 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt5
- update screenshots
- small improvements

* Fri Jun 30 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt4
- typo fixes, small improvements

* Fri Jun 16 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt3
- update to ALT Kworkstation 10.2RC1

* Thu Jun 01 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt2
- update to ALT Kworkstation 10.2beta3
- system-management: add userpasswd, alt-customize-branding
- desktop-software: skanpage, haruna

* Wed Mar 29 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt1
- update to ALT Kworkstation 10.2beta

* Thu Oct 13 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt5
- update to ALT Kworkstation 10.1

* Tue Sep 13 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt4
- update to ALT Kworkstation 10.1rc1

* Wed Aug 03 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt3
- update to ALT Kworkstation 10.1beta2

* Wed Jul 13 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt2
- fix typos (closes: #43144, #43151, #43143)

* Fri Jun 24 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt1
- update to ALT Kworkstation 10.1beta

* Wed Apr 06 2022 Elena Mishina <lepata@altlinux.org> 10.0-alt4
- update screenshots
- small improvements

* Thu Mar 17 2022 Elena Mishina <lepata@altlinux.org> 10.0-alt3
- update to ALT Kworkstation 10.0RC2

* Fri Feb 18 2022 Elena Mishina <lepata@altlinux.org> 10.0-alt2
- update to ALT Kworkstation 10.0RC1

* Tue Jan 18 2022 Elena Mishina <lepata@altlinux.org> 10.0-alt1
- update to ALT Kworkstation 10.0beta

* Fri Aug 20 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt2
- server-network delete alterator-net-domain, squid, squidmill, dhcp, ulogd
- update screenshots
- typo fixes, small improvements

* Wed Jul 07 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt1
- update to ALT Kworkstation 9.2

* Tue Jul 06 2021 Artem Zolochevskiy <azol@altlinux.org> 9.1-alt5
- reduce package size

* Tue Apr 06 2021 Elena Mishina <lepata@altlinux.org> 9.1-alt4
- fix some typos
- update screenshots
- update info: network-configuration

* Tue Mar 02 2021 Elena Mishina <lepata@altlinux.org> 9.1-alt3
- update to ALT Kworkstation 9.1RC3
- system-management: add CUPS web-interface, group policy
- desktop-software: add search files (dolhin)
- functional: add alt-csp-cryptopro, luks password
- install-packages-advanced: add epm

* Tue Dec 15 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt2
- update to ALT Kworkstation 9.1RC1
- add OEM-mode

* Wed Sep 09 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt1
- update to ALT Kworkstation 9.1Beta
- add fleet-commander

* Tue Jul 21 2020 Elena Mishina <lepata@altlinux.org> 9.0-alt3
- update restrictions section
- update screenshots
- fix some typos

* Mon Jun 29 2020 Elena Mishina <lepata@altlinux.org> 9.0-alt2
- system-management add FreeIPA, sambadc server, autostart/save sessions
- starting-os add qtvirtualkeyboard
- server-network add alterator
- restrictions add altha, kiosk
- functionl add openvpn-gost, openssh-gost

* Thu Apr 09 2020 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to ALT Kworkstation 9.0

* Mon Mar 02 2020 Elena Mishina <lepata@altlinux.org> 8.90-alt6
- desktop-software add ark
- desktop-software add dolhin hash, encrypt GOST
- system-management add kde5-kcm-grub2
- system-management add sessions (sddm, krdc, alt-app-starter)

* Wed Feb 05 2020 Elena Mishina <lepata@altlinux.org> 8.90-alt5
- update to 8.95
- update desktop-software section

* Thu Jan 16 2020 Elena Mishina <lepata@altlinux.org> 8.90-alt4
- desktop-software add discover
- desktop-software add ksysguard
- update screenshots

* Mon Dec 23 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt3
- updated to latest public distr

* Tue Aug 13 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt2
Beta version of ALT Kworkstation 9.0

* Mon Aug 05 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
Alpha version of ALT Kworkstation 9.0

* Mon Nov 19 2018 Elena Mishina <lepata@altlinux.org> 8.3-alt1
- Version fix

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- update documentation

* Tue Aug 29 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- Version fix

* Wed May 31 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt5
- renamed docs-kworkstation->docs-alt-kworkstation

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt4
- fix typo
- update doc

* Fri Feb 10 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt3
- update Conflicts list

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt2
- updated to latest public distr

* Fri Jan 13 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt1
- renamed to alt-kworkstation

* Sat Sep 24 2016 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt1
- initial kworkstation doc

* Sat Mar 5 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt3
- fix changelog

* Sat Mar 5 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt2
- rebuild with publclian4

* Sat Jan 23 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt1
- update to 7.0.5

* Tue Aug 19 2014 Artem Zolochevskiy <azol@altlinux.ru> 7.0.3-alt1
- update doc
- switch to publican

* Sat Jul 13 2013 Alexandr Boltris <alex@altlinux.org> 7.0.0-alt2
- Version fix

* Wed Jul 10 2013 Alexandr Boltris <alex@altlinux.org> 7.0.0-alt1
- Add info about support *.docx in app libreOffice
  (thx Nickolay Rogalskiy)
- add 11 step to "install-guide" This step is about setting up
  password for LUKS partition(s) (thx Nickolay Rogalskiy)
- desktop-software/internet/im: telepathy replaces kopete
- desktop-software/multimedia/kde: remove Dragonplayer
- install-guide: added section for RAID, LVM and LUSK setup
- install-guide: update installation from USB flash
- support/index.txt: add more Community/Company links
  (thx Artem Zolochevskiy)
- whatis-alt: added text about platform (p7)
- update screenshots
- spellcheck

* Tue Jun 25 2013 Artem Zolochevskiy <azol@altlinux.ru> 6.0.2-alt1
- update dvd- usb-burn section

* Mon Mar 19 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0.1-alt1
- update for 6.0.1

* Fri Mar 09 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt14
- fix some typos

* Tue Mar 08 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt13
- improve sumode section
- add docs-lxdesktop, docs-lxdesktop-lite to conflicts list

* Fri Oct 21 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt9
- update documentation
- closes bug: #26457

* Mon Aug 29 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt8
- fix some typos

* Fri Aug 26 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt7
- update

* Fri Aug 19 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt6
- fix previous changelog entry

* Fri Aug 18 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt5
- update

* Thu Aug 18 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt4
- update

* Fri Jul 01 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt3
- some rephrasings / typo fixes

* Fri Jun 09 2011 Alexandr Boltris <alex@altlinux.ru> 6.0-alt2
- system-management: add initial network section
- kde-quickstart: update system-tray description
- add packages section
- desktop-software: update software descriptions
- some rephrasings / typo fixes
- update screenshots

* Mon Jun 06 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt1
- update for ALT Linux 6.0 KDesktop

* Mon Mar 07 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt8
- update Conflicts list

* Fri Feb 26 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt7
- install-guide: fix info on RAID creation during install
- whatis-alt: fix 'Le Mythe de Sisyphe' link
- add docs-school-terminal to Conflicts list

* Mon Feb 22 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt6
- simplify datetime section (#19084)
- typo and punctuation fixes
- small rephrasings

* Fri Jan 29 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt5
- typo fixes, small improvements

* Wed Dec 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt4
- update screenshots (thx Sergey V Turchin)

* Fri Dec 18 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt3
- add initial 'applications' section

* Fri Nov 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt2
- add dolphin section

* Thu Nov 26 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt1
- initial build for Sisyphus
  + based on docs-desktop-5.0-alt8 package
