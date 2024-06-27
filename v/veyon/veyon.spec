%define _unpackaged_files_terminate_build 1

Name: veyon
Version: 4.8.3
Release: alt3
Group: Education
License: GPLv2
Url: https://veyon.io/
VCS: https://github.com/veyon/veyon/

Summary: Open source computer monitoring and classroom management
Summary(ru.UTF-8): Программа с открытым кодом для контроля компьютеров и организации учебного процесса

Requires: polkit qca-qt5-ossl qt5-translations

Obsoletes: italc3

Source: %name-%version.tar
Source1: %name-%version-3rdparty-kldap.tar
Source2: %name-%version-3rdparty-kldap-qt-compat.tar
Source3: %name-%version-3rdparty-libfakekey.tar
Source4: %name-%version-3rdparty-libvncserver.tar
Source5: %name-%version-3rdparty-libvncserver-webclients-novnc.tar
Source6: %name-%version-3rdparty-qthttpserver.tar
Source7: %name-%version-3rdparty-qthttpserver-src-3rdparty-http-parser.tar
Source8: %name-%version-3rdparty-x11vnc.tar

Source100: veyon-config-dm-login.sh

Patch0: %name-%version-alt.patch
Patch1: alt-veyon-libdir.patch
Patch4: alt-fix-dm-login.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-ubt
BuildRequires: rpm-build-kf5
BuildRequires: gcc-c++ make cmake
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: libjpeg-devel
BuildRequires: zlib-devel
BuildRequires: liblzo2-devel
BuildRequires: libssl-devel
BuildRequires: libldap-devel
BuildRequires: libpam0-devel
BuildRequires: libsasl2-devel
BuildRequires: libpng-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libqca-qt5-devel
BuildRequires: libXdamage-devel
BuildRequires: libXtst-devel
BuildRequires: libfakekey-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
%if "%(rpmvercmp '%ubt_id' 'M110')" >= "0"
BuildRequires: libproc2-devel
%else
BuildRequires: libprocps-devel
%endif

%description
Veyon is a free and open source software
for computer monitoring and classroom management supporting Windows and Linux.
It enables teachers to view and control computer labs and interact with students.
Veyon is available in different languages and provides lots of useful features:

* see what's going on in computer labs in overview mode and take screenshots
* remote control computers to support and help users
* broadcast teacher's screen to students in realtime by using demo mode
(either in fullscreen or in a window)
* lock workstations for attracting attention to teacher
* send text messages to students
* powering on/off and rebooting computers remote
* remote logoff and remote execution of arbitrary commands/scripts
* home schooling - Veyon's network technology is not restricted to a subnet
and therefore students at home can join lessons via VPN connections
just by installing the Veyon service.

%description -l ru_RU.UTF-8
Veyon - это бесплатное программное обеспечение с открытым исходным кодом
для контроля компьютеров и организации учебного процесса, поддерживающее Windows и Linux.
Оно позволяет учителям просматривать и контролировать компьютерные классы
и взаимодействовать со студентами.
Veyon доступен на разных языках и предоставляет множество полезных функций:

* просмотр происходящего в компьютерных классах в режиме обзора и создание скриншотов
* удаленное управление компьютерами для поддержки и помощи пользователям
* трансляция экрана учителя ученикам в режиме реального времени,
используя демонстрационный режим (либо в полноэкранном режиме, либо в окне)
* блокировка рабочих мест для привлечения внимания к учителю
* отправка текстовых сообщений студентам
* удалённое включение / выключение и перезагрузка компьютеров
* удаленный выход из системы и удаленное выполнение произвольных команд / скриптов
* домашнее обучение - сетевые технологии Veyon не ограничиваются подсетью,
поэтому студенты могут присоединиться к урокам через VPN-подключения,
просто установив Veyon у себя на домашнем ПК.

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8

%patch0 -p1
%patch1 -p1
%patch4 -p1

# Fix: error: "_FORTIFY_SOURCE" redefined [-Werror]
# _FORTIFY_SOURCE enabled by default
sed -i -e '/-D_FORTIFY_SOURCE=2/d' CMakeLists.txt

%ifarch %e2k
sed -i "s/-Werror/-Wno-error/" cmake/modules/SetDefaultTargetProperties.cmake
# workaround of SIGILL in ecf_opt64 from LCC 1.25.23
sed -i "s/QOverload<int>::of(&QComboBox::/(void(QComboBox::*)(int))(\&QComboBox::/" \
	core/src/Configuration/UiMapping.h
%endif

%build
%cmake \
%ifarch %e2k
	-DWITH_LTO=OFF \
%endif
	-DSYSTEMD_SERVICE_INSTALL_DIR:PATH=%_unitdir \
	%nil
%cmake_build

%install
%cmakeinstall_std
%__install -D -m 0755 %SOURCE100 %buildroot%_datadir/%name/

%files
%doc COPYING README.md
%_unitdir/veyon.service
%_libdir/%name
%_libdir/*.so
%_bindir/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*
%_datadir/polkit-1/actions/*
%_datadir/pixmaps/*
%_datadir/%name

%changelog
* Thu Jun 27 2024 Ajrat Makhmutov <rauty@altlinux.org> 4.8.3-alt3
- fix FTBFS: specify the new path to the systemd services

* Mon Mar 18 2024 Ajrat Makhmutov <rauty@altlinux.org> 4.8.3-alt2
- use libprocps instead libproc2 for branches less than p11

* Thu Mar 07 2024 Ajrat Makhmutov <rauty@altlinux.org> 4.8.3-alt1
- new version 4.8.3

* Thu Oct 12 2023 Egor Ignatov <egori@altlinux.org> 4.8.2-alt2
- update BuildRequires

* Tue Oct 03 2023 Egor Ignatov <egori@altlinux.org> 4.8.2-alt1
- new version 4.8.2 (closes: #47470)

* Fri Apr 28 2023 Egor Ignatov <egori@altlinux.org> 4.8.0-alt1
- new version 4.8.0

* Mon Sep 05 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.7.4-alt2.1
- fixed build for Elbrus

* Tue Aug 09 2022 Egor Ignatov <egori@altlinux.org> 4.7.4-alt2
- fix Screen Lock and Fullscreen Demo

* Fri Jul 29 2022 Egor Ignatov <egori@altlinux.org> 4.7.4-alt1
- new version 4.7.4

* Tue Jul 19 2022 Egor Ignatov <egori@altlinux.org> 4.7.3-alt4
- cherry-pick commits from alt-fix-builtindirectory-computers-list-display patch

* Tue Jul 19 2022 Egor Ignatov <egori@altlinux.org> 4.7.3-alt3
- Use update-submodules.sh

* Mon Jul 18 2022 Egor Ignatov <egori@altlinux.org> 4.7.3-alt2
- Backport KDE open website workaround (closes: #41101)

* Fri Jun 03 2022 Egor Ignatov <egori@altlinux.org> 4.7.3-alt1
- new version 4.7.3
- 9e4b294d9 linux: runProgramAsUser set gid as well

* Thu Jun 02 2022 Egor Ignatov <egori@altlinux.org> 4.7.2-alt2
- backport upstream commit to fix build with gcc12

* Fri May 06 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.7.2-alt1.1
- fixed build for Elbrus

* Thu Mar 17 2022 Egor Ignatov <egori@altlinux.org> 4.7.2-alt1
- new version

* Tue Dec 28 2021 Egor Ignatov <egori@altlinux.org> 4.7.0-alt1
- new version

* Wed Nov 10 2021 Egor Ignatov <egori@altlinux.org> 4.6.0-alt4
- Build with downstream commits

* Wed Nov 10 2021 Egor Ignatov <egori@altlinux.org> 4.6.0-alt3
- Complete Russian translation (thanks Olesya Gerasimenko) (closes: #41183)

* Wed Oct 13 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.6.0-alt2
- fixed build for Elbrus

* Mon Sep 27 2021 Egor Ignatov <egori@altlinux.org> 4.6.0-alt1
- new version

* Fri Aug 20 2021 Egor Ignatov <egori@altlinux.org> 4.5.7-alt1
- new version

* Tue Jun 29 2021 Egor Ignatov <egori@altlinux.org> 4.5.6-alt2
- update build dependencies

* Wed Jun 02 2021 Egor Ignatov <egori@altlinux.org> 4.5.6-alt1
- new version

* Thu May 13 2021 Egor Ignatov <egori@altlinux.org> 4.5.5-alt2
- fix login with sddm and lightdm (Closes: #39892)

* Tue Apr 27 2021 Egor Ignatov <egori@altlinux.org> 4.5.5-alt1
- new version
- Import fix to #37952 as a patch

* Sat Apr 10 2021 Egor Ignatov <egori@altlinux.org> 4.5.4-alt3
- Clean up spec

* Wed Mar 24 2021 Egor Ignatov <egori@altlinux.org> 4.5.4-alt2
- Fixed:
  + ALT Education authentification error (#37960)
  + Incorrect display of the Computers list (#37952)
  + Typo in russian translation

* Wed Mar 17 2021 Egor Ignatov <egori@altlinux.org> 4.5.4-alt1
- new version

* Thu Mar 11 2021 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt2
- merge p9 git-history

* Wed Sep 02 2020 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Fri Aug 28 2020 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt2
- Fix load Qt translation

* Tue Aug 25 2020 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- New version

* Tue Apr 21 2020 Pavel Moseev <mars@altlinux.org> 4.2.5-alt3
- Fix launch of Veyon in ALT Workstation x86_64 (closes: #37950)

* Wed Jan 15 2020 Pavel Moseev <mars@altlinux.org> 4.2.5-alt2
- Fix launch of Veyon. Use pkexec instead of gksudo and kdesudo (closes: #37651)

* Tue Oct 22 2019 Pavel Moseev <mars@altlinux.org> 4.2.5-alt1
- Initial release for ALT Linux
