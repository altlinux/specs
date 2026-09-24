%define edu_programming_reqs \
Requires: gcc \
Requires: java-devel \
Requires: codeblocks \
Requires: codeblocks-contrib \
Requires: bluefish \
Requires: geany >= 2.1 \
%ifnarch %e2k \
Requires: geany-plugins \
%endif \
Requires: logisim \
Requires: basic256 \
Requires: kumir2 \
%ifarch %ix86 x86_64 \
Requires: freebasic \
Requires: fpc \
Requires: fpc-ide \
%ifarch %_dotnet_archlist \
Requires: pascalabcnet \
%endif \
Requires: kchmviewer \
%endif \
%ifnarch %e2k loongarch64 \
Requires: lazarus \
%endif \
Requires: gambas-full \
%{nil}

%define edu_graphics_reqs \
Requires: gimp \
Requires: gimp-help-ru \
Requires: inkscape \
Requires: scribus \
Requires: dia \
%ifnarch %e2k \
Requires: shotwell \
%endif \
Requires: imagination \
Requires: shutter \
%ifarch x86_64 aarch64 \
Requires: blender \
%endif \
%{nil}

%define edu_av_editing_reqs \
Requires: audacity \
Requires: kdenlive \
Requires: cheese \
Requires: gst-plugins-bad \
Requires: gst-plugins-ugly \
%{nil}

%define edu_math_reqs \
Requires: octave \
Requires: gnuplot-qt \
Requires: wxMaxima \
%{nil}

%define edu_reference_reqs \
%ifnarch %e2k %ix86 \
Requires: calibre \
Requires: goldendict-ng \
%else \
Requires: stardict \
%endif \
Requires: dict-mueller7-utf8 \
%ifarch x86_64 aarch64 \
Requires: freeplane \
%endif \
%ifarch %e2k \
Requires: freemind \
%endif \
Requires: connector \
%{nil}

%define edu_content_filter_reqs \
Requires: netpolice-filter \
Requires: netpolice-main \
# For Skydns \
%ifnarch %e2k \
Requires: ddclient \
%endif \
Requires: perl-IO-Socket-SSL \
%{nil}

%define edu_db_connectors_reqs \
Requires: perl-DBD-mysql \
Requires: postgresql-jdbc \
Requires: mysql-connector-java \
%{nil}

%define edu_l10n_reqs \
Requires: qt5-translations \
%ifnarch %e2k %not_qt6_qtwebengine_arches \
Requires: khelpcenter \
%endif \
Requires: mythes-ru \
Requires: hyphen-ru \
Requires: aspell-ru-lebedev \
Requires: hunspell-ru-lebedev \
Requires: man-pages-ru \
%{nil}

%define edu_scanning_reqs \
Requires: xsane \
Requires: xsane-doc-ru \
Requires: simple-scan \
Requires: sane \
Requires: sane-airscan \
Requires: hplip-sane \
Requires: gimagereader-gtk \
Requires: tesseract \
Requires: tesseract-langpack-ru \
Requires: tesseract-langpack-en \
%{nil}

%define edu_fonts_reqs \
Requires: fonts-ttf-liberation \
Requires: fonts-ttf-dejavu \
Requires: fonts-ttf-google-droid-sans \
Requires: fonts-ttf-google-droid-sans-mono \
Requires: fonts-ttf-google-droid-serif \
Requires: fonts-ttf-ubuntu-font-family \
Requires: fonts-ttf-gost \
Requires: fonts-ttf-xorg \
Requires: fonts-ttf-PTAstra \
Requires: fonts-ttf-XO \
Requires: fonts-ttf-google-noto-sans \
Requires: fonts-ttf-google-crosextra-caladea \
Requires: fonts-ttf-google-crosextra-carlito \
Requires: fonts-ttf-wqy-zenhei \
Requires: fonts-ttf-unifont \
Requires: fonts-otf-mozilla-fira \
%{nil}

%define edu_desktop_search_reqs \
Requires: recoll \
Requires: recoll-extras \
Requires: perl-Image-ExifTool \
Requires: antiword \
Requires: unrtf \
Requires: wv \
Requires: xpdf-utils \
Requires: aspell \
Requires: python3-module-pychm \
Requires: python3-module-lxml \
# For search exercises \
Requires: docx2txt \
Requires: odt2txt \
%{nil}

%define edu_alterator_reqs \
Requires: altcenter \
Requires: alterator-browser-qt6 \
Requires: alterator-fbi \
Requires: alterator-standalone \
Requires: alterator-notes-base \
Requires: alterator-auth \
Requires: alterator-control \
Requires: alterator-datetime \
Requires: alterator-gpupdate \
Requires: alterator-groups \
Requires: alterator-grub \
Requires: alterator-logs \
Requires: alterator-net-eth \
Requires: alterator-net-general \
Requires: alterator-net-openvpn \
Requires: alterator-net-pppoe \
Requires: alterator-net-pptp \
Requires: alterator-net-wifi \
Requires: alterator-net-vlan \
Requires: alterator-osec \
Requires: alterator-packages \
Requires: alterator-ports-access \
Requires: alterator-printers \
Requires: alterator-root \
Requires: alterator-services \
Requires: alterator-sslkey \
Requires: alterator-sysconfig \
Requires: alterator-sysinfo \
Requires: alterator-updates \
Requires: alterator-usbguard \
Requires: alterator-usbmount \
Requires: alterator-users \
Requires: alterator-xkb \
Requires: alterator-zram-swap \
Requires: alterator-kopidel \
Requires: alterator-update-kernel \
Requires: alterator-net-iptables \
Requires: alterator-limits \
%{nil}

%define edu_games_reqs \
Requires: gnome-games-klotski \
Requires: gnome-games-mahjongg \
%ifnarch %e2k \
Requires: gnome-games-aisleriot \
%endif \
%ifnarch %e2k \
Requires: gnome-games-mines \
Requires: gnome-games-tetravex \
%endif \
Requires: dosbox \
%{nil}

%define edu_remote_management_reqs \
%ifnarch %e2k \
Requires: puppet \
%endif \
%ifarch x86_64 aarch64 \
Requires: x11spice \
Requires: openssh-server \
%endif \
Requires: freerdp3-server \
Requires: veyon \
%{nil}

%define edu_software_management_reqs \
Requires: gnome-software \
Requires: gnome-software-plugin-stplr \
Requires: packagekit \
Requires: rpminstall \
Requires: stplr-repo-aides \
Requires: flatpak \
%ifnarch %e2k \
Requires: flatpak-repo-flathub \
%endif \
Requires: apt-updatecache \
%{nil}

%define edu_printing_reqs \
Requires: cups \
Requires: cups-filters \
Requires: cups-pdf \
Requires: cups-browsed \
Requires: system-config-printer \
Requires: system-config-printer-udev \
Requires: printer-drivers-base \
Requires: gutenprint-cups-ppds \
Requires: hplip-hpijs \
Requires: printer-driver-oki \
Requires: bluez-cups \
Requires: printer-testpages \
Requires: ipp-usb \
%ifnarch %e2k \
Requires: printer-driver-brlaser \
Requires: epson-inkjet-printer-escpr \
%endif \
%{nil}

%define edu_antivirus_reqs \
Requires: clamav \
Requires: clamav-db \
Requires: clamtk \
%{nil}

%define edu_burning_reqs \
Requires: brasero \
%{nil}

%define edu_mail_reqs \
%ifarch %thunderbird_arches \
Requires: thunderbird \
%endif \
%{nil}

%define edu_base_reqs \
%edu_programming_reqs \
%edu_graphics_reqs \
%edu_av_editing_reqs \
%edu_math_reqs \
%edu_reference_reqs \
%edu_content_filter_reqs \
%edu_db_connectors_reqs \
%edu_l10n_reqs \
%edu_scanning_reqs \
%edu_fonts_reqs \
%edu_desktop_search_reqs \
%edu_alterator_reqs \
%edu_games_reqs \
%edu_remote_management_reqs \
%edu_software_management_reqs \
%edu_printing_reqs \
%edu_antivirus_reqs \
%edu_burning_reqs \
%edu_mail_reqs \
%{nil}

%define edu_python_reqs \
Requires: python3-tools \
Requires: pip \
Requires: python3-module-pygame \
Requires: python3-module-pygame-doc \
Requires: python3-modules-curses \
%{nil}

%define edu_professional_reqs \
%edu_python_reqs \
Requires: inkscape \
Requires: gimp \
Requires: gimp-help-ru \
%ifarch x86_64 aarch64 %e2k \
Requires: blender \
%endif \
Requires: scribus \
Requires: codeblocks \
%ifnarch %e2k loongarch64 \
Requires: lazarus \
%endif \
%ifarch x86_64 aarch64 \
Requires: freecad \
%endif \
%ifnarch %e2k \
Requires: qcad \
%endif \
Requires: wxMaxima \
Requires: octave \
Requires: gnuplot-qt \
%ifnarch %e2k %ix86 \
Requires: qt-creator \
Requires: qt-creator-doc \
%endif \
%ifnarch %ix86 \
Requires: projectlibre \
%endif \
Requires: cmake \
Requires: ninja-build \
Requires: qt5-base-devel \
Requires: qt5-base-doc \
Requires: fritzing \
%{nil}

%define edu_desktop_common_reqs \
Requires: desktop-screensaver-modules-xscreensaver \
Requires: desktop-screensaver-modules-xscreensaver-gl \
Requires: altlinux-freedesktop-menu-shallow-menu \
Requires: altlinux-freedesktop-menu-mate-like-menu \
Requires: altlinux-freedesktop-menu-icon-theme-default \
%ifarch %e2k \
# better optimized for 8C \
Requires: mplayer \
%endif \
%ifarch x86_64 \
Requires: libva-driver-intel \
Requires: libva-intel-media-driver \
%endif \
Requires: simplescreenrecorder \
Requires: quick-usb-formatter \
Requires: xorg-conf-libinput-touchpad \
%{nil}

%define edu_highschool_own_reqs \
Requires: kolourpaint \
Requires: openscad \
Requires: synfigstudio \
Requires: trikStudio \
Requires: marble \
Requires: afce \
%ifarch x86_64 aarch64 \
Requires: scratch-desktop \
%endif \
%ifnarch %e2k \
Requires: qcad \
Requires: trikStudioJunior \
%endif \
%ifarch x86_64 aarch64 \
Requires: freecad \
%endif \
%edu_python_reqs \
Requires: gcompris-qt \
Requires: gcompris-qt-voices-ru \
Requires: ktouch \
Requires: kbruch \
Requires: parley \
Requires: kanagram \
Requires: khangman \
Requires: kwordquiz \
Requires: kturtle \
Requires: step \
Requires: kig \
Requires: kmplot \
Requires: kalgebra \
Requires: cantor \
Requires: rocs \
Requires: kgeography \
Requires: minuet \
Requires: abiword \
# stellarium is ExcludeArch: %%ix86 (translation encoding problems) \
%ifnarch %ix86 \
Requires: stellarium \
%endif \
%{nil}

%define edu_teacher_reqs \
Requires: veyon \
Requires: ansible \
%ifnarch %e2k \
Requires: semaphore \
%endif \
Requires: virt-viewer \
%ifnarch %not_qt6_qtwebengine_arches \
Requires: OpenBoard \
%endif \
%{nil}

Name: task-edu
Version: 1.9.1
Release: alt1

Summary(ru_RU.UTF-8): Базовый образовательный комплект
Summary: Educational software (base set)
License: GPL-3.0+
Group: Education
Url: http://altlinux.org/education

BuildRequires(pre): rpm-macros-thunderbird
BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires(pre): rpm-macros-dotnet

Provides: %name-lite = %EVR
Obsoletes: %name-lite < %EVR
%edu_base_reqs

%description
%{summary}.

%package tools
Summary(ru_RU.UTF-8): Вспомогательные программы для Альт Образование
Summary: Utilities for ALT Education
Group: Other
%ifnarch %e2k
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
Requires: adp
%ifarch %e2k
Requires: rtc
%endif
Requires: touchegg
Requires: xfburn
Requires: xorg-drv-wacom
Requires: zenity
Requires: yelp
%description tools
%{summary}.

%package preschool
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (дошкольное образование)
Summary: Educational software (preschool)
Group: Education
Requires: gcompris-qt
Requires: gcompris-qt-voices-ru
Requires: tuxpaint
Requires: khangman
Requires: kanagram
Requires: qt5-translations
%ifnarch %e2k %not_qt6_qtwebengine_arches
Requires: khelpcenter
%endif
%description preschool
%{summary}.

%package highschool
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (cредняя школа)
Summary: Educational software (highschool)
Group: Education
Provides: %name-gradeschool = %EVR
Obsoletes: %name-gradeschool < %EVR
%edu_base_reqs
%edu_highschool_own_reqs
%description highschool
%{summary}.

%package secondary-vocational
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (среднее профессиональное образование)
Summary: Educational software (secondary vocational)
Group: Education
%edu_professional_reqs
Requires: logisim
%description secondary-vocational
%{summary}.

%package university
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (высшее образование)
Summary: Educational software (university)
Group: Education
%edu_professional_reqs
Requires: gambas-full
Requires: openscad
Requires: swi-prolog
%ifnarch %e2k %ix86
Requires: qgis
Requires: qgis-grass
Requires: qgis-python
%endif
Requires: openmpi
%description university
%{summary}.

%package xfce
Summary(ru_RU.UTF-8): Среда XFCE для Альт Образование
Summary: XFCE for Alt Education
Group: Education
Requires: xfce4-default
Requires: pavucontrol
Requires: xfce-polkit
Requires: xfce4-clipman-plugin
Requires: xfce4-pulseaudio-plugin
Requires: xfwm4-themes
Requires: orage
Requires: xfce4-screenshooter
Requires: xarchiver
Requires: ristretto
Requires: parole
Requires: catfish
Requires: xfce4-panel-profiles
Requires: xfce4-battery-plugin
Requires: xfce4-calculator-plugin
Requires: xfce4-cpufreq-plugin
Requires: xfce4-cpugraph-plugin
Requires: xfce4-diskperf-plugin
Requires: xfce4-docklike-plugin
Requires: xfce4-eyes-plugin
Requires: xfce4-fsguard-plugin
Requires: xfce4-generic-slider-plugin
Requires: xfce4-genmon-plugin
Requires: xfce4-mailwatch-plugin
Requires: xfce4-mount-plugin
Requires: xfce4-netload-plugin
Requires: xfce4-notes-plugin
Requires: xfce4-notification-plugin
Requires: xfce4-places-plugin
Requires: xfce4-sensors-plugin
Requires: xfce4-smartbookmark-plugin
Requires: xfce4-stopwatch-plugin
Requires: xfce4-systemload-plugin
Requires: xfce4-time-out-plugin
Requires: xfce4-timer-plugin
Requires: xfce4-verve-plugin
Requires: xfce4-wavelan-plugin
Requires: xfce4-weather-plugin
Requires: xfce4-whiskermenu-plugin
Requires: xfce4-xkb-plugin
Requires: thunar-shares-plugin
Requires: xfce4-screensaver
Requires: libcanberra-gtk2
Requires: alacarte
Requires: screenkey
Requires: atril-gtk
Requires: atril-gtk-djvu
Requires: atril-gtk-pixbuf
Requires: atril-gtk-xps
%edu_desktop_common_reqs
Requires: vlc-maxi
%ifnarch %e2k
Requires: nextcloud-client
%endif
Requires: branding-alt-education-xfce-settings
Requires: xdg-user-dirs-gtk
Requires: libgtk2-engine-adwaita
Requires: parted
Requires: xorg-drv-synaptics
Requires: xorg-conf-synaptics
Requires: xinput
Requires: xorg-drv-libinput
%ifnarch %not_qt5_qtwebengine_arches
Requires: mousepad
%endif
%description xfce
%{summary}.

%package kde
Summary(ru_RU.UTF-8): Среда KDE для Альт Образование
Summary: KDE for Alt Education
Group: Education
Requires: kinfocenter-maxi
Requires: kde-network-manager-nm
Requires: kde
Requires: krfb
Requires: kde6-runtime
Requires: kde-printing
Requires: kde-scanning
Requires: kdeconnect
# Plasma weather applet (systray, enabled by default); arch-limited by package
%ifarch x86_64 aarch64
Requires: plasma-addon-alt-weather
%endif
%ifnarch %e2k
Requires: nextcloud-client-kde
%endif
Requires: branding-alt-education-kde-settings
%edu_desktop_common_reqs
%description kde
%{summary}.

%package teacher
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (для учителей)
Summary: Software for teachers
Group: Education
%edu_teacher_reqs
%description teacher
%{summary}.

%package server-apps
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (серверные приложения)
Summary: Server applications for education
Group: Education
%ifnarch %e2k
Requires: semaphore
%endif
Requires: mariadb-server
Requires: mariadb-client
Requires: postgresql16-server
Requires: postgresql16-contrib
Requires: nano
Requires: dansguardian
Requires: perl-DBD-mysql
#Requires: ejudge
#Requires: ejabberd
Requires: alterator-datetime
Requires: alterator-console
Requires: apache2
Requires: apache2-httpd-worker
Requires: installed-db-office-server-mediawiki
Requires: installed-db-office-server-nextcloud
Requires: installed-db-office-server-moodle
Requires: moodle-qtype_coderunner
Requires: alterator-fbi
#Requires: alterator-bacula
Requires: alterator-ca
Requires: alterator-bind
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
Requires: anonftp
Requires: samba4
Requires: xauth
# Terminal services
Requires: xrdp
Requires: pulseaudio-module-xrdp
%ifarch x86_64
Requires: docker-ce
Requires: lsb
%endif
Requires: tcpdump
%description server-apps
%{summary}.

%package school
Summary(ru_RU.UTF-8): Образовательное программное обеспечение для школ
Summary: Complete list of education software for schools
Group: Education
%edu_base_reqs
%edu_highschool_own_reqs
%edu_teacher_reqs
%description school
%{summary}.

%files

%files tools

%files preschool

%files highschool

%files secondary-vocational

%files university

%files xfce

%ifnarch %e2k
%files kde
%endif

%files teacher

%files server-apps

%files school

%changelog
* Thu Sep 24 2026 Pavel Petrykin <silverducks@altlinux.org> 1.9.1-alt1
- Add xorg-conf-libinput-touchpad to edu_desktop_common_reqs.

* Wed Sep 23 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.9.0-alt1
- Take over the packages the ALT Education profile
  used to list by hand in its misc and misc-base lists.
- Fold lite into task-edu (Provides/Obsoletes task-edu-lite).
- Drop the video-conferencing subpackage: Jitsi Meet is out of the product.
- Drop every subpackage-to-subpackage requirement:
  a subpackage now requires leaf packages only.
- Require gambas-full, openscad, synfigstudio, lazarus
  and veyon on every architecture they are built for.
- university: Require blender on e2k, where it is built.
- Require octave unconditionally: the fortran
  bcond it hung on was never defined.
- highschool: Drop scratch and the requirements the base set already carries.
- preschool: Drop the commented-out childsplay requirements.
- Drop the arch conditions for armh, ppc64le and riscv64.
- Spec cleanup.

* Mon Sep 14 2026 Ivan Khanas <xeno@altlinux.org> 1.8.5-alt1
- lite: add alterator-limits.

* Thu Sep 03 2026 Ivan Khanas <xeno@altlinux.org> 1.8.4-alt1
- lite: add alterator-net-iptables.

* Tue Jul 07 2026 Arseniy Kostevich <faux@altlinux.org> 1.8.3-alt1
- lite: Add freeplane.

* Thu Jul 02 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.8.2-alt1
- kde: Add plasma-addon-alt-weather.
- server-apps: Add postgresql16 alongside mariadb.
- highschool: Add stellarium.
- lite: Drop geany-themes, require geany >= 2.1 (themes now part of geany).

* Thu Jun 04 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.8.1-alt1
- Move touchegg from teacher to tools.

* Sun May 31 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.8.0-alt1
- Remove LibreOffice (lite, xfce, kde) and pentaho-reporting-flow-engine
  to make the office suite optional for ALT Education users.
- Remove altcenter-education (xfce, kde).
- Fix macro expansion in 1.7.15-alt2 changelog.

* Sat Apr 25 2026 Ivan Khanas <xeno@altlinux.org> 1.7.15-alt3
- Add kinfocenter-maxi to unlock systeminfo/graphics features.

* Wed Apr 22 2026 Ivan Khanas <xeno@altlinux.org> 1.7.15-alt2
- Exclude %%ix86 for projectlibre.

* Wed Feb 18 2026 Andrey Cherepanov <cas@altlinux.org> 1.7.15-alt1
- server-apps: removed alterator-ulogd and ejabberd.

* Tue Dec 09 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.14-alt1
- Adapted for pascalabcnet 3.11 using dotnet.

* Tue Nov 11 2025 Vladimir Didenko <cow@altlinux.org> 1.7.13-alt3
- don't require docker on ix86 platform

* Sat Nov 08 2025 Anton Midyukov <antohami@altlinux.org> 1.7.13-alt2
- teacher: depends on OpenBoard for %%qt6_qtwebengine_arches only.

* Sun Oct 19 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.7.13-alt1
- server-apps: Stop requiring alt-domain-server.

* Sat Oct 18 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.12-alt1
- Removed vulkan-amdgpu (ALT #56017).

* Wed Oct 08 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.7.11-alt1
- xfce: Replace the requirement from xfce4-full to xfce4-default.
- xfce: Get rid of xfce4-dict.

* Tue Jun 17 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.10-alt1
- server-apps: return mediawiki.
- highschool: restore kdeedu from task-edu-kde.

* Mon Jun 09 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.9-alt1
- kde: removed kdeedu packages.

* Mon Jun 09 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.8-alt1
- Required altcenter-education.
- xfce: added mousepad.

* Wed Jun 04 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.7.7-alt1
- Use the thunderbird_arch macro for the thunderbird requirement.

* Thu May 29 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.6-alt1
- Replaced kde-runtime by kde6-runtime (ALT #54486).

* Wed May 21 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1
- Remove synaptic.

* Mon Mar 10 2025 Constantin Sunzow <protvin@altlinux.org> 1.7.4-alt1
- Remove unsupported itest.

* Tue Feb 25 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.3-alt1
- Replace unsupported fbreader by calibre.
- Replace unsupported goldendict by goldendict-ng.

* Wed Feb 12 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.2-alt1
- Remove gimp plugins.

* Tue Feb 11 2025 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1.2
- NMU: remove xsane-gimp2

* Thu Jan 23 2025 Ivan A. Melnikov <iv@altlinux.org> 1.7.1-alt1.1
- NMU: rpm-macros-qt5-webengine to determine altcenter presence
  (fixes build on loongarch64)

* Thu Jan 23 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- task-edu-kde, task-edu-xfce: add altcenter

* Tue Jan 21 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- Add task-edu-xfce metapackage.

* Mon Dec 16 2024 Andrey Cherepanov <cas@altlinux.org> 1.6.5-alt1
- Remove chromium from requrements.

* Thu Dec 12 2024 Andrey Cherepanov <cas@altlinux.org> 1.6.4-alt1
- Adapt for KDE6.

* Tue Dec 10 2024 Andrey Cherepanov <cas@altlinux.org> 1.6.3-alt1
- task-edu-kde5: remove unsupported LibreOffice-still-kde5.

* Tue Nov 12 2024 Andrey Cherepanov <cas@altlinux.org> 1.6.2-alt1
- Do not use qgis for i586.

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 1.6.1-alt3.1
- NMU: update KDE requries

* Fri Aug 09 2024 Ivan A. Melnikov <iv@altlinux.org> 1.6.1-alt3
- NMU: drop OpenBoard and kde5-parley on loongarch64,
  as they require qt5-webengine.

* Sun Jun 30 2024 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt2
- NMU: task-edu-teacher: do not require OpenBoard on ppc64le

* Tue May 07 2024 Andrey Cherepanov <cas@altlinux.org> 1.6.1-alt1
- Merge task-edu-highschool and task-edu-gradeschool.

* Fri Apr 19 2024 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt2
- Remove unworking jitsi-meet and scilab.
- Do not use freecad for i586.

* Sun Feb 25 2024 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- Removed task-edu from school profiles.
- Removed monodevelop (this project has not been built nor maintained since January 2020).
- task-edu-video-conferencing was not built for ppc64le.

* Mon Nov 27 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt13
- Used old scratch for i586 and e2k, modern scratch-desktop for x86_64 and aarch64.
- freecad was not built for ppc64le.

* Thu Oct 12 2023 Michael Shigorin <mike@altlinux.org> 1.5.9-alt12
- E2K-specific/related dependency tweaks.
- Minor spec cleanup.

* Mon Oct 09 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt11
- Removed kde5-kstars.

* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt10
- Returned qgis3, kde5-marble, kde5-kstars and kde5-kgeography.
- Added image editors for secondary-vocational and university.

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
