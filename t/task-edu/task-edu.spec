Name:    task-edu
Version: 1.5.9
Release: alt8
License: GPL-3.0+
URL:     https://www.altlinux.org/Education
Group:   Education

# Education (base part)
Requires: task-edu-lite = %EVR
%ifarch x86_64 aarch64
Requires: blender
%endif
Requires: clamav
Requires: clamav-db
Requires: clamtk
Requires: dosbox
%ifarch %ix86 x86_64
Requires: freebasic
Requires: fpc
Requires: fpc-ide
Requires: pascalabcnet
Requires: kchmviewer
%endif
Requires: brasero
%ifarch %ix86 x86_64 %e2k
Requires: veyon
%endif
# Big educational software
%ifarch %ix86 x86_64
Requires: lazarus
Requires: gambas-full
%endif

Summary(ru_RU.UTF-8): Базовый образовательный комплект
Summary: Educational software (base set)
%description
%{summary}.

%package lite
Summary(ru_RU.UTF-8): Базовый набор образовательного ПО, облегчённый для rootfs
Summary: Basic set of educational software, lightweight for rootfs
Group: Education
# Education (base part)
Requires: audacity
Requires: bluefish
Requires: codeblocks
Requires: codeblocks-contrib
Requires: dia
Requires: fbreader
%ifnarch %e2k
Requires: goldendict
%else
Requires: stardict
%endif
Requires: dict-mueller7-utf8
Requires: gcc
Requires: inkscape
Requires: gimp
Requires: gimp-help-ru
Requires: gimp-plugin-gutenprint
Requires: gimp-plugin-refocus-it
Requires: java-devel
Requires: kdenlive
Requires: scribus
%ifnarch %e2k
Requires: shotwell
%endif
Requires: logisim
Requires: basic256
Requires: geany
Requires: geany-themes
%ifnarch %e2k
Requires: geany-plugins
%else
Requires: freemind
%endif
Requires: gnome-games-klotski
Requires: gnome-games-mahjongg
%ifnarch %e2k
Requires: gnome-games-aisleriot
%endif
Requires: xsane
Requires: xsane-gimp2
Requires: xsane-doc-ru
Requires: simple-scan
%ifnarch armh
Requires: imagination
%endif
Requires: connector
%ifarch x86_64 aarch64
Requires: chromium
%endif
Requires: fonts-otf-mozilla-fira
Requires: itest
Requires: kumir2
# Big educational software
Requires: octave
Requires: gnuplot-qt
%ifnarch ppc64le
Requires: wxMaxima
%endif
# OCR
Requires: gimagereader-gtk
Requires: tesseract
Requires: tesseract-langpack-ru
Requires: tesseract-langpack-en
# KDE5 localization and profile
Requires: kde5-profile
Requires: qt5-translations
%ifnarch %e2k
Requires: kde5-khelpcenter
%endif
# Content filter and antivirus
Requires: netpolice-filter
Requires: netpolice-main
# For Skydns
%ifnarch %e2k
Requires: ddclient
%endif
Requires: perl-IO-Socket-SSL
# For search exercises
Requires: docx2txt odt2txt
# Mass management and remote assistance
%ifnarch %e2k
Requires: puppet
%endif
%ifarch x86_64 aarch64
Requires: x11spice
Requires: openssh-server
%endif
# LibreOffice
%ifnarch %e2k
%define lo_name LibreOffice-still
%else
%define lo_name LibreOffice
%endif
%ifnarch armh
Requires: %{lo_name}-extensions
Requires: %{lo_name}-integrated
Requires: %{lo_name}-gtk3
Requires: %{lo_name}-langpack-ru
Requires: libreoffice-languagetool
%endif
Requires: mythes-ru
Requires: hyphen-ru
Requires: gst-plugins-bad
Requires: gst-plugins-ugly
Requires: pentaho-reporting-flow-engine
Requires: perl-DBD-mysql
Requires: postgresql-jdbc
Requires: mysql-connector-java
# Mozilla
%ifnarch armh
Requires: thunderbird
%endif
%description lite
%{summary}.

%package tools
Summary(ru_RU.UTF-8): Вспомогательные программы для Альт Образование
Summary: Utilities for ALT Education
Group: Other
%ifnarch %e2k armh
Requires: grub-customizer
%endif
# Electronic board support
%ifarch %ix86 x86_64
Requires: starboard-preinstall
%endif
%ifarch %ix86 x86_64
Requires: bumblebee
%endif
%ifarch %ix86 x86_64
Requires: virtualbox-guest-utils
Requires: xorg-dri-intel
%endif
%ifnarch armh
Requires: adp
%endif
%ifarch %e2k
Requires: rtc
%endif
%description tools
%{summary}.

%package preschool
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (дошкольное образование)
Summary: Educational software (preschool)
Group: Education
Requires: gcompris-qt
Requires: gcompris-qt-voices-ru
# wait for python3 version
#Requires: childsplay
#Requires: childsplay-alphabet_sounds_ru
Requires: tuxpaint
Requires: kde5-khangman
Requires: kde5-kanagram
# KDE5 localization and profile
Requires: kde5-profile
Requires: qt5-translations
%ifnarch %e2k
Requires: kde5-khelpcenter
%endif
%description preschool
%{summary}.

%package gradeschool
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (начальная школа)
Summary: Educational software (gradeschool)
Group: Education
Requires: task-edu
Requires: kde5-profile
Requires: kde5-kolourpaint
Requires: kde5-ktouch
Requires: gcompris-qt
Requires: gcompris-qt-voices-ru
Requires: trikStudio
Requires: trikStudio-data
Requires: kde5-kbruch
Requires: abiword
Requires: python3-tools
Requires: python3-module-pygame
Requires: python3-module-pygame-doc
Requires: python3-modules-curses
Requires: afce
# KDE5 localization and profile
Requires: kde5-profile
Requires: qt5-translations
%ifarch %e2k
Requires: scratch
%endif
%ifarch %ix86 x86_64
Requires: scratch-desktop
%endif
%ifnarch %e2k
Requires: kde5-khelpcenter
Requires: trikStudioJunior
%endif
%description gradeschool
%{summary}.

%package highschool
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (cредняя школа)
Summary: Educational software (highschool)
Group: Education
Requires: task-edu
Requires: kumir2
Requires: codeblocks
Requires: kde5-profile
Requires: kde5-kolourpaint
%ifarch %ix86 x86_64
Requires: lazarus
Requires: openscad
%endif
%ifarch %ix86 x86_64 %e2k
Requires: synfigstudio
%endif
Requires: dia
Requires: trikStudio
#Requires: kde5-marble
%ifnarch ppc64le
Requires: wxMaxima
%endif
Requires: bluefish
Requires: afce
# KDE5 localization and profile
Requires: kde5-profile
Requires: qt5-translations
%ifarch %e2k
Requires: scratch
%endif
%ifarch %ix86 x86_64
Requires: scratch-desktop
%endif
%ifnarch %e2k
Requires: qcad
Requires: kde5-khelpcenter
%endif
%ifarch %ix86 x86_64 aarch64 ppc64le
Requires: freecad
%endif
Requires: python3-tools
Requires: pip
%description highschool
%{summary}.

%package secondary-vocational
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (среднее профессиональное образование)
Summary: Educational software (secondary vocational)
Group: Education
Requires: codeblocks
%ifarch %ix86 x86_64
Requires: lazarus
Requires: scilab
%endif
%ifnarch %e2k armh
Requires: freecad
Requires: qcad
%endif
%ifnarch ppc64le
Requires: wxMaxima
%endif
Requires: octave
Requires: gnuplot-qt
%ifnarch %e2k %ix86 armh
Requires: qt-creator
Requires: qt-creator-doc
%endif
Requires: cmake
Requires: ninja-build
Requires: qt5-base-devel
Requires: qt5-base-doc
#Requires: Eclipse
#Requires: Texmacs
Requires: logisim
Requires: fritzing
Requires: projectlibre
Requires: python3-tools
Requires: python3-module-pygame
Requires: python3-module-pygame-doc
Requires: python3-modules-curses
Requires: pip
%description secondary-vocational
%{summary}.

%package university
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (высшее образование)
Summary: Educational software (university)
Group: Education
Requires: codeblocks
%ifnarch %e2k %ix86 armh
Requires: qt-creator
Requires: qt-creator-doc
%endif
Requires: cmake
Requires: ninja-build
Requires: qt5-base-devel
Requires: qt5-base-doc
#Requires: Eclipse
%ifarch %ix86 x86_64
Requires: lazarus
Requires: gambas-full
Requires: monodevelop
Requires: openscad
Requires: scilab
%endif
Requires: swi-prolog
#Requires: Texmacs
%ifnarch ppc64le
Requires: wxMaxima
%endif
Requires: octave
Requires: gnuplot-qt
%ifnarch %e2k
Requires: qcad
%endif
%ifnarch %e2k armh
Requires: freecad
#Requires: qgis3
#Requires: qgis3-grass
#Requires: qgis3-python
%endif
Requires: projectlibre
Requires: openmpi
Requires: fritzing
Requires: python3-tools
Requires: python3-module-pygame
Requires: python3-module-pygame-doc
Requires: python3-modules-curses
Requires: pip
%description university
%{summary}.

%package kde5
Summary(ru_RU.UTF-8): Среда KDE5 для Альт Образование
Summary: KDE5 for Alt Education
Group: Education
Requires: kde5
Requires: kf5-plasma-workspace
Requires: kde5-network-manager-nm
Requires: libqimageblitz5
Requires: kde5-krfb
%ifnarch ppc64le
Requires: kde5-parley
%endif
Requires: kde5-kanagram
Requires: kde5-khangman
Requires: kde5-kwordquiz
Requires: kde5-kturtle
#Requires: kde5-marble
Requires: kde5-step
#Requires: kde5-kstars
Requires: kde5-kig
Requires: kde5-kmplot
Requires: kde5-kalgebra
Requires: kde5-cantor
Requires: kde5-rocs
Requires: kde5-kbruch
#Requires: kde5-kgeography
Requires: kde5-ktouch
Requires: kde5-minuet
Requires: kde5-runtime
Requires: kde5-printing
Requires: kde5-scanning
Requires: kde5-connect
%ifnarch armh
Requires: %{lo_name}-kde5
%endif
%ifnarch %e2k ppc64le
Requires: nextcloud-client-kde5
%endif
Requires: branding-alt-education-kde-settings
%description kde5
%{summary}.

%package teacher
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (для учителей)
Summary: Software for teachers
Group: Education
%ifnarch armh
Requires: veyon
%endif
Requires: itest-server
Requires: ansible
%ifnarch %e2k armh
Requires: semaphore
%endif
Requires: virt-viewer
Requires: OpenBoard
Requires: touchegg
%description teacher
%{summary}.

%package server-apps
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (серверные приложения)
Summary: Server applications for education
Group: Education
%ifnarch %e2k armh
Requires: semaphore
%endif
Requires: mariadb-server
Requires: mariadb-client
Requires: nano
Requires: dansguardian
Requires: perl-DBD-mysql
#Requires: ejudge
Requires: ejabberd
Requires: alterator-datetime
Requires: alterator-console
Requires: apache2
Requires: apache2-httpd-worker
#Requires: installed-db-office-server-mediawiki
Requires: installed-db-office-server-nextcloud
Requires: installed-db-office-server-moodle
Requires: moodle-qtype_coderunner
Requires: alt-domain-server
Requires: alterator-fbi
#Requires: alterator-bacula
Requires: alterator-ca
Requires: alterator-ddns
Requires: alterator-dhcp
Requires: alterator-firsttime
Requires: alterator-kdc
Requires: alterator-ldap-groups
Requires: alterator-ldap-users
Requires: alterator-mirror
Requires: alterator-net-domain
Requires: alterator-net-eth
Requires: alterator-net-pppoe
Requires: alterator-net-pptp
%ifarch %ix86 x86_64
Requires: alterator-netinst
%endif
Requires: alterator-net-openvpn
Requires: alterator-net-routing
Requires: alterator-net-bond
Requires: alterator-net-bridge
Requires: alterator-net-iptables
Requires: alterator-openldap
Requires: alterator-openvpn-server
Requires: alterator-squid
Requires: alterator-squidmill
Requires: alterator-quota
Requires: alterator-trust
Requires: alterator-vsftpd
Requires: alterator-xinetd
Requires: alterator-postfix-dovecot
Requires: alterator-ulogd
Requires: anonftp
Requires: samba4
Requires: xauth
# Terminal services
Requires: xrdp
Requires: pulseaudio-module-xrdp
%ifarch %ix86 x86_64
Requires: docker-ce
Requires: lsb
%endif
Requires: tcpdump
%description server-apps
%{summary}.

%package video-conferencing
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (сервер видеоконференций)
Summary: Video-conferencing server for education
Group: Education
Requires: prosody
Requires: jitsi-meet-doc
Requires: jitsi-meet-prosody
Requires: jitsi-meet-web
Requires: jitsi-meet-web-config
Requires: jitsi-videobridge
%ifarch x86_64
Requires: jicofo
%endif
%description video-conferencing
%{summary}.

%package school
Summary(ru_RU.UTF-8): Образовательное программное обеспечение для школ
Summary: Complete list of education software for schools
Group:   Education
Requires: task-edu
Requires: task-edu-gradeschool
Requires: task-edu-highschool
Requires: task-edu-teacher
%description school
%{summary}.

%files

%files lite

%files tools

%files preschool

%files gradeschool

%files highschool
 
%files secondary-vocational

%files university

%ifnarch %e2k
%files kde5
%endif

%files teacher

%files server-apps

%ifnarch %e2k %ix86 armh
%files video-conferencing
%endif

%files school

%changelog
* Thu Mar 30 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt8
- Do not require qt-creator for i586 and armh.

* Mon Mar 20 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt7
- Do not build task-edu-video-conferencing for 32-bit architectures and e2k.

* Wed Dec 21 2022 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt6
- Exclude applications with old map of Russia.

* Wed Oct 05 2022 Anton Midyukov <antohami@altlinux.org> 1.5.9-alt5
- Make the task-edu-lite subpackage the base for task-edu
- Fix description of lite subpackage
- Fix Group field of task-edu-lite subpackage (Other -> Education)
- Fix typo in URL field

* Tue Oct 04 2022 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt4
- Delete deprecated freeplane.

* Sun Oct 02 2022 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt3
- Add kchmviewer as help viewer for IDE for pascalabcnet.

* Tue Aug 23 2022 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt2
- Remove mediawiki from task-edu-server-apps because it does not support PHP 8.0.

* Tue Jul 26 2022 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt1
- Used pip instead of python3-module-pip.
- Added python3-tools to task-edu-highschool.

* Sat May 28 2022 Andrey Cherepanov <cas@altlinux.org> 1.5.8-alt1
- Excluded chromium for i586.

* Fri Feb 04 2022 Sergey V Turchin <zerg@altlinux.org> 1.5.7-alt3
- Update requires for qt-creator.

* Thu Feb 03 2022 Sergey V Turchin <zerg@altlinux.org> 1.5.7-alt2
- Update requires for qt-creator and nextcloud-client.

* Thu Nov 11 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.7-alt1
- Add moodle-qtype_coderunner to server-apps.

* Tue Nov 09 2021 Dmitry Terekhin <jqt4@altlinux.org> 1.5.6-alt2
- Add basic set of educational software, lightweight for RPi4.
  Some applications added by the task-edu package are unnecessary
  or do not work on RPi4.

* Wed Nov 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.6-alt1
- Use gimagereader-gtk instead of gimagereader-qt5 due completely translation.

* Tue Nov 02 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.5-alt1
- Add pascalabcnet to task-edu.

* Thu Oct 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.4-alt1
- Move scilab from school group to secondary-vocational and university.

* Wed Oct 27 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.3-alt1
- server-apps: add apache2 metapackage.

* Tue Oct 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt1
- Remove puppetserver and puppetdb from task-edu-server-apps.

* Tue Oct 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- Add gnuplot-qt for octave.

* Thu Oct 14 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt2
- LibreOffice was not built on armh.

* Mon Sep 20 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- Move utilities to distribution profile and package task-edu-tools.

* Thu Aug 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.6-alt3
- Thunderbird do not build for armh.

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.6-alt2
- NMU: temp. disable childsplay (was python2 only)

* Thu Aug 05 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.6-alt1
- Return scilab.

* Wed Jul 21 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.5-alt1
- Remove vlan-utils.

* Wed Jul 07 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1
- Remove python2 modules.

* Tue Jun 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.3-alt3
- Replaced openfire with ejabberd.

* Tue May 11 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt2
- Do not require thunderbird on ppc64le.

* Wed Apr 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt1
- Add touchegg to task-edu-teacher.

* Tue Apr 27 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- Add pulseaudio-module-xrdp, alterator-net-bond, alterator-net-bridge
  and alterator-net-iptables to task-edu-server-apps.

* Fri Apr 23 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- Update for Sisyphus.
- Move from qgis to qgis3.
- Completely remove documentation for pip.
- Add xsane-doc-ru.
- Remove python3-modules-nis.

* Mon Apr 12 2021 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- Replace italc3 to veyon.

* Sun Apr 11 2021 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- Remove documentation for pip.

* Wed Apr 07 2021 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Use java-devel instead of java-1.8.0-openjdk-devel.
- Add trikStudioJunior to task-edu-gradeschool.
- Add pip both for Python and Python3 for task-edu-highschool,
  task-edu-secondary-vocational and task-edu-university.

* Sat Apr 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Remove installer-feature* packages.

* Thu Apr 01 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt3
- Initial build for Sisyphus.
