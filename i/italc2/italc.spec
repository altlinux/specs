# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

# %%docdir set
%define docdir %_defaultdocdir/%name-%version
%define confdir %_sysconfdir/italc
%define keysdir %confdir/keys
%define xinitdir %_sysconfdir/X11/xinit.d

%define program_name %(echo '%name'|sed -r 's/^(.*[^0-9]+)[0-9]+$/\\1/')
%define master_group %{program_name}master

# set %%{program_name}-* groups
%define admin_group %{program_name}-admins
%define supporter_group %{program_name}-supporters
%define teacher_group %{program_name}-teachers
%define other_group %{program_name}-others

# macros for icons
%define iconshicolordir %_iconsdir/hicolor
%define icons128x128dir %iconshicolordir/128x128/apps
%define icons64x64dir %iconshicolordir/64x64/apps
%define icons48x48dir %iconshicolordir/48x48/apps
%define icons32x32dir %iconshicolordir/32x32/apps
%define icons16x16dir %iconshicolordir/16x16/apps

# for filetriggers use
%if "%{?branch_switch}" == "" || "%{?branch_switch}" == "M50"
%define filetriggers yes
%define rpm_min_ver 4.0.4-alt96.11
%define menu_min_ver 2.1.41-alt4
%else
%if "%{?branch_switch}" == "M41"
%define filetriggers yes
%define rpm_min_ver 4.0.4-alt95.M41.7
%define menu_min_ver 2.1.41-alt3.M41.1
%else
%undefine filetriggers
%endif
%endif

Name: italc2
Version: 2.0.1
Release: %branch_release alt6

Summary: Didactical software for teachers etc
Summary(de_DE.UTF-8): Didaktische Software fuer Lehrer usw
Summary(ru_RU.UTF-8): Управление компьютерным классом
License: %gpl2plus
Group: Networking/Remote access

Url: http://italc.sourceforge.net/
Packager: Aleksey Avdeev <solo@altlinux.ru>

Source0: %name-%version.tar
Source10: iTALC.conf
Patch10: %name-alt-all.patch

Conflicts: %program_name < 2.0.0

BuildRequires(pre): rpm-macros-branch
BuildPreReq: /proc
BuildPreReq: rpm-build-licenses
BuildPreReq: cmake
BuildPreReq: rpm-macros-cmake
BuildPreReq: GraphicsMagick-ImageMagick-compat
BuildPreReq: icoutils

# Automatically added by buildreq on Sat May 12 2012 (-bi)
# optimized out: cmake-modules elfutils fontconfig java libICE-devel libSM-devel libX11-devel libXau-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXtst-devel libXv-devel libpng-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libssl-devel libstdc++-devel pkg-config python-base tzdata tzdata-java xorg-inputproto-devel xorg-kbproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: cmake gcc-c++ java-devel libXdamage-devel libjpeg-devel libpam-devel phonon-devel

%description
iTALC is a use- and powerful didactical tool for teachers. It lets you view
and control other computers in your network in several ways. It supports Linux
and Windows 2000/XP/Vista.

Features:

* see what's going on in computer-labs by using overview mode and
  make snapshots
* remote-control computers to support and help other people
* show a demo (either in fullscreen or in a window) - the teacher's screen
  is shown on all student's computers in realtime
* lock workstations for moving undivided attention to teacher
* send text-messages to students
* powering on/off and rebooting computers per remote
* remote logon and logoff and remote execution of arbitrary commands/scripts
* home-schooling - iTALC's network-technology is not restricted to a subnet
  and therefore students at home can join lessons via VPN-connections just
  by installing iTALC client

Furthermore iTALC is optimized for usage on multi-core systems (by making
heavy use of threads). No matter how many cores you have, iTALC can make use
of all of them.

%description -l de_DE.UTF-8
iTALC ist ein nuetzliches und leistungsfaehiges didaktisches Werkzeug für
Lehrer, mit dem man andere Computer im Netzwerk auf verschiedene Art und Weise
beobachten und fernsteuern kann.

iTALC unterstuetzt derzeit Linux und Windows 2000/XP/Vista.

Funktionen:

* sehen, was in Computerkabinetten los ist (Uebersichtsmodus) und
  Schnapsschuesse erstellen
* Computern fernsteuern, um anderen Leuten zu unterstuetzen
* eine Demo zeigen (entweder als Vollbild oder in einem Fenster) -
  der Lehrer-Bildschirm wird auf alle Schuelercomputer in Echtzeit uebertragen
* Schuelercomputer sperren um Aufmerksamkeit zu erlangen
* Textnachrichten an Schueler senden
* Computer uebers Netzwerk an- und ausschalten sowie neustarten
* Remote-Anmeldung sowie Ausfuehrung beliebiger Befehle/Skripte
* Anbindung zu Hause sitzender Schueler ueber VPN moeglich

Weiterhin ist iTALC optimiert auf die Nutzung auf Mehrkern-Systemen 
(indem es in grossen Umfang Threads benutzt). Egal wie viele Kerne sie haben,
iTALC kann von allen Gebrauch machen.

%description -l ru_RU.UTF-8
iTALC - мощная программа для учителей работающих в компьютеризированных
классах. Она позволяет различными способами контролировать компьютеры
учащихся входящих в состав сети. iTALC поддерживает Linux
и Windows 2000/XP/Vista а также может использоваться в смешанных сетях.

Возможности:

* просмотр и запись происходящего на компьютерах учеников
* удаленный контроль компьютеров входящих в сеть, для поддержки и помощи
  учащимся
* показ учебных материалов (в режиме полного экрана или в отдельном окне)
  на всех компьютерах сети
* блокировка рабочих станций для привлечения большего внимания к изложению
  материала
* пересылка текстовых сообщений учащимся
* включение и выключение всех компьютеров сети
* удаленный вход и выход и запуск команд и скриптов
* обучение на расстоянии. iTALC может работать не только в локальных сетях -
  с помощью соединений VPN можно организовать преподавание и в домашних
  условиях

Следует отметить что iTALC оптимизирован для работы с многоядерными системами.
Не важно сколько ядер вы имеете - iTALC может использовать все.

%package client
Summary: Software for iTALC-clients
Summary(de_DE.UTF-8): Software fuer iTALC-Clients
Summary(ru_RU.UTF-8): iTALC-клиент
Group: Networking/Remote access
Requires: %name = %version-%release
Conflicts: %program_name-client < 2.0.0


%description client
This package contains the software, needed by iTALC-clients.

See /usr/share/italc/doc/INSTALL for details on how to install and setup iTALC
in your network.

%description client -l de_DE.UTF-8
Dieses Paket beinhaltet die Software, die auf iTALC-Clients benoetigt wird.

Weitere Details ueber die Installation und Einrichtung von iTALC in Ihrem
Netzwerk finden Sie in /usr/share/italc/doc/INSTALL.

%description -l ru_RU.UTF-8
Этот пакет содержит программное обеспечение, необходимое для организации
iTALC-клиента.

Более подробную информацию о установке и настройке iTALC в вашей сети
см. в /usr/share/italc/doc/INSTALL.

%package master
Summary: iTALC master software
Summary(de_DE.UTF-8): iTALC-Master-Software
Summary(ru_RU.UTF-8): iTALC-мастер
Group: Networking/Remote access
Requires: %name-client = %version-%release
# for filetriggers use
%ifdef rpm_min_ver
Requires: rpm >= %rpm_min_ver
%endif
%ifdef menu_min_ver
Requires: menu >= %menu_min_ver
%endif
Conflicts: %program_name-master < 2.0.0

Requires: %icons128x128dir
Requires: %icons64x64dir
Requires: %icons48x48dir
Requires: %icons32x32dir
Requires: %icons16x16dir

%description master
This package contains the actual master-software for accessing clients.

See /usr/share/italc/doc/INSTALL for details on how to install and setup iTALC
in your network.

%description master -l de_DE.UTF-8
Dieses Paket beinhaltet die eigentliche Master-Software, um auf Clients
zuzugreifen.

Weitere Details ueber die Installation und Einrichtung von iTALC in Ihrem
Netzwerk finden Sie in /usr/share/italc/doc/INSTALL.

%description -l ru_RU.UTF-8
Этот пакет содержит программное обеспечение, необходимое для организации
мастер-доступа к iTALC-клиентам.

Более подробную информацию о установке и настройке iTALC в вашей сети
см. в /usr/share/italc/doc/INSTALL.

%prep
%setup
%patch10 -p1

%build
%cmake -DCMAKE_INSTALL_DOCDIR:PATCH='%docdir'
%cmake_build update-locales # VERBOSE=1
%cmake_build finalize-locales # VERBOSE=1
%cmake_build # VERBOSE=1

%install
%cmakeinstall_std
pushd BUILD
install -m 644 -pD italc.spec %buildroot%docdir/%name.origin.spec
popd

# Install iTALC.conf
install -m 644 -pD %SOURCE10 "%buildroot%_sysconfdir/xdg/iTALC Solutions/iTALC.conf"
ln -snf "$(relative "%buildroot%_sysconfdir/xdg/iTALC Solutions" %buildroot%_sysconfdir/xdg/iTALC)" %buildroot%_sysconfdir/xdg/iTALC

# Create key dirs
mkdir -p %buildroot%keysdir/private/teacher
mkdir -p %buildroot%keysdir/private/admin
mkdir -p %buildroot%keysdir/private/supporter
mkdir -p %buildroot%keysdir/private/other
mkdir -p %buildroot%keysdir/public/teacher
mkdir -p %buildroot%keysdir/public/admin
mkdir -p %buildroot%keysdir/public/supporter
mkdir -p %buildroot%keysdir/public/other

mkdir -p %buildroot%xinitdir
ln -snf $(relative %buildroot%_bindir/ica-launcher %buildroot%xinitdir/ica-launcher) %buildroot%xinitdir/ica-launcher
find %buildroot%keysdir -mindepth 2 -maxdepth 2 -type d -print0 \
	| xargs -r0 -i touch "{}/key"

# Move JavaViewer to %%docdir
mv %buildroot%_datadir/italc/JavaViewer %buildroot%docdir/

%find_lang %name

%pre client
%_sbindir/groupadd -r -f %master_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %admin_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %supporter_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %teacher_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %other_group 2>/dev/null ||:

%ifndef filetriggers
%post master
%update_menus

%postun master
%clean_menus
%endif

%files -f %name.lang
%doc %docdir

%files client
%_bindir/ica
%attr(4711,root,root) %_bindir/italc_auth_helper
%_man1dir/italc_auth_helper.1.gz
%_libdir/*.so
%_man1dir/ica.1.gz
#%%_bindir/ica-launcher
#%%xinitdir/ica-launcher
%dir %confdir
%dir %keysdir
%attr(0770,root,%master_group) %dir %keysdir/private
%attr(0775,root,%master_group) %dir %keysdir/public
%attr(2770,root,%teacher_group) %dir %keysdir/private/teacher
%attr(2770,root,%admin_group) %dir %keysdir/private/admin
%attr(2770,root,%supporter_group) %dir %keysdir/private/supporter
%attr(2770,root,%other_group) %dir %keysdir/private/other
%attr(2775,root,%teacher_group) %dir %keysdir/public/teacher
%attr(2775,root,%admin_group) %dir %keysdir/public/admin
%attr(2775,root,%supporter_group) %dir %keysdir/public/supporter
%attr(2775,root,%other_group) %dir %keysdir/public/other
%ghost %attr(0660,root,%teacher_group) %config(noreplace) %keysdir/private/teacher/key
%ghost %attr(0660,root,%admin_group) %config(noreplace) %keysdir/private/admin/key
%ghost %attr(0660,root,%supporter_group) %config(noreplace) %keysdir/private/supporter/key
%ghost %attr(0660,root,%other_group) %config(noreplace) %keysdir/private/other/key
%ghost %attr(0664,root,%teacher_group) %config(noreplace) %keysdir/public/teacher/key
%ghost %attr(0664,root,%admin_group) %config(noreplace) %keysdir/public/admin/key
%ghost %attr(0664,root,%supporter_group) %config(noreplace) %keysdir/public/supporter/key
%ghost %attr(0664,root,%other_group) %config(noreplace) %keysdir/public/other/key
%dir %config(noreplace) "%_sysconfdir/xdg/iTALC Solutions"
%config(noreplace) %attr(0664,root,%master_group)  "%_sysconfdir/xdg/iTALC Solutions/iTALC.conf"
%_sysconfdir/xdg/iTALC

%files master
%_bindir/imc
%_bindir/italc
#%%_bindir/italc-launcher
%_man1dir/imc.1.gz
%_man1dir/italc.1.gz
%_desktopdir/italc.desktop
%icons128x128dir/italc.png
%icons128x128dir/imc.png
%icons64x64dir/italc.png
%icons48x48dir/italc.png
%icons48x48dir/imc.png
%icons32x32dir/italc.png
%icons32x32dir/imc.png
%icons16x16dir/italc.png
%icons16x16dir/imc.png

%changelog
* Mon Jul 09 2012 Aleksey Avdeev <solo@altlinux.ru> 2.0.1-alt6
- Add conflicts for italc < 2.0.0
- Add JavaViewer to %%docdir

* Sun Jul 08 2012 Aleksey Avdeev <solo@altlinux.ru> 2.0.1-alt5
- Fix permissions for:
  + key dirs and key files
  + %%_sysconfdir/xdg/iTALC Solutions/iTALC.conf file
- Fix %%{program_name}-* groups names
- Fix Exec in italc.desktop file

* Thu Jul 05 2012 Aleksey Avdeev <solo@altlinux.ru> 2.0.1-alt4
- Fix %%other_group name

* Thu Jul 05 2012 Aleksey Avdeev <solo@altlinux.ru> 2.0.1-alt3
- Fix name italc master group
- Set setuid for italc_auth_helper
- Create %%{program_name}-* groups:
  + %%admin_group
  + %%supporter_group
  + %%teacher_group
  + %%other_group
- Sets %%{program_name}-* groups for %%keysdir subdirs
- Use Debian patches:
  + 002_use-v4l-videodev2.patch
  + 004_x2go-nx-noxdamage.patch
  + 011_qt-signals.patch
  + 021_man-page-patch-in.patch
- Add %%_sysconfdir/xdg/iTALC Solutions/iTALC.conf config file
- Add:
  + italc.desktop
  + man pages for ica, italc, imc and italc_auth_helper

* Tue Jun 19 2012 Aleksey Avdeev <solo@altlinux.ru> 2.0.1-alt2
- Add icons for:
  + italc
  + imc

* Tue May 29 2012 Aleksey Avdeev <solo@altlinux.ru> 2.0.1-alt1
- Version 2.0.1 build
- Not done:
  + italc-launcher
  + ica-launcher
  + italc.desktop
  + icons

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.13-alt1.1
- Rebuild with Python-2.7

* Fri Jan 21 2011 Aleksey Avdeev <solo@altlinux.ru> 1.0.13-alt1
- Version 1.0.13 build

* Tue Mar 02 2010 Aleksey Avdeev <solo@altlinux.ru> 1.0.9.1.6-alt2
- Move docs to %%_defaultdocdir/%%name-%%version
- Fix shutting down of clients using KDE4 (Closes: #23033) (thanks to
  Flavio Moringa <flavio.moringa caixamagica pt>)

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9.1.6-alt1.1
- Rebuilt with python 2.6

* Tue Sep 22 2009 Aleksey Avdeev <solo@altlinux.ru> 1.0.9.1.6-alt1
- Add multiX use to ica-launcher

* Tue Sep 01 2009 Aleksey Avdeev <solo@altlinux.ru> 1.0.9.1.5-alt3
- Fix permissions: keys generation root only

* Tue Sep 01 2009 Aleksey Avdeev <solo@altlinux.ru> 1.0.9.1.5-alt2
- Fix keys permissions

* Sat Aug 29 2009 Aleksey Avdeev <solo@altlinux.ru> 1.0.9.1.5-alt1
- Add %%xinitdir/ica-launcher for autostarting ica
- Fix %%name-client installation: move createting %%master_group to this %%pre

* Tue Aug 18 2009 Aleksey Avdeev <solo@altlinux.ru> 1.0.9.1.3-alt1
- Add key dirs
  %%_sysconfdir/%%name/keys/{private,public}/{teacher,admin,supporter,other}
- Create %%{name}master group, for master using

* Thu Aug 13 2009 Aleksey Avdeev <solo@altlinux.ru> 1.0.9.1.2-alt1
- Support Freedesktop menu only

* Sat Aug 08 2009 Aleksey Avdeev <solo@altlinux.ru> 1.0.9.1.1-alt1
- Version 1.0.9 build

* Fri Apr 25 2008 Denis Medvedev <nbr@altlinux.ru> 1.0.7-alt4
 - %post changed to fix

* Fri Apr 25 2008 Denis Medvedev <nbr@altlinux.ru> 1.0.7-alt3
 - Russian translation, icon paths changed, some spec cleanup, .desktop

* Thu Apr 24 2008 Denis Medvedev <nbr@altlinux.ru> 1.0.7-alt2
 - X86_64 fixes

* Thu Mar 27 2008 Denis Medvedev <nbr@altlinux.ru> 1.0.7-alt1
- Initial ALT release
