# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

# %%docdir set
%define docdir %_defaultdocdir/%name-%version
%define confdir %_sysconfdir/%name
%define keysdir %confdir/keys
%define xinitdir %_sysconfdir/X11/xinit.d

%define master_group %{name}master

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

Name: italc
Version: 1.0.13
Release: %branch_release alt1.1

Summary: Didactical software for teachers etc
Summary(de_DE.UTF-8): Didaktische Software fuer Lehrer usw
Summary(ru_RU.UTF-8): Управление компьютерным классом
License: %gpl2plus
Group: Networking/Remote access

Url: http://italc.sourceforge.net/
Packager: Aleksey Avdeev <solo@altlinux.ru>

Source0: %name-%version.tar
Patch10: %name-%version-ubuntu.patch

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: automake
BuildPreReq: GraphicsMagick

# Automatically added by buildreq on Sat Aug 08 2009 (-bi)
BuildRequires: gcc-c++ imake libICE-devel libXdamage-devel libXext-devel libXinerama-devel libXrandr-devel libXrender-devel libXtst-devel libjpeg-devel libqt4-devel xorg-inputproto-devel

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
Requires: italc = %version-%release

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
Requires: italc-client = %version-%release
# for filetriggers use
%ifdef rpm_min_ver
Requires: rpm >= %rpm_min_ver
%endif
%ifdef menu_min_ver
Requires: menu >= %menu_min_ver
%endif

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
%make -f Makefile.svn
%configure --docdir=%docdir --disable-pixmaps-files --disable-menu-files
%make_build

%install
%makeinstall_std
install -pD %name.spec %buildroot%docdir/%name.origin.spec
mkdir -p %buildroot%xinitdir
ln -snf $(relative %buildroot%_bindir/ica-launcher %buildroot%xinitdir/ica-launcher) %buildroot%xinitdir/ica-launcher
find %buildroot%keysdir -mindepth 2 -maxdepth 2 -type d -print0 \
	| xargs -r0 -i touch "{}/key"
%find_lang %name

%pre client
%_sbindir/groupadd -r -f %master_group 2>/dev/null ||:

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
%_libdir/italc/libitalc_core.so
%_man1dir/ica.1.gz
%_bindir/ica-launcher
%xinitdir/ica-launcher
%dir %confdir
%dir %keysdir
%attr(2750,root,%master_group) %dir %keysdir/private
%attr(2755,root,%master_group) %dir %keysdir/public
%attr(2750,root,%master_group) %dir %keysdir/private/teacher
%attr(2750,root,%master_group) %dir %keysdir/private/admin
%attr(2750,root,%master_group) %dir %keysdir/private/supporter
%attr(2750,root,%master_group) %dir %keysdir/private/other
%attr(2755,root,%master_group) %dir %keysdir/public/teacher
%attr(2755,root,%master_group) %dir %keysdir/public/admin
%attr(2755,root,%master_group) %dir %keysdir/public/supporter
%attr(2755,root,%master_group) %dir %keysdir/public/other
%ghost %attr(0440,root,%master_group) %config(noreplace) %keysdir/private/teacher/key
%ghost %attr(0440,root,%master_group) %config(noreplace) %keysdir/private/admin/key
%ghost %attr(0440,root,%master_group) %config(noreplace) %keysdir/private/supporter/key
%ghost %attr(0440,root,%master_group) %config(noreplace) %keysdir/private/other/key
%ghost %attr(0444,root,%master_group) %config(noreplace) %keysdir/public/teacher/key
%ghost %attr(0444,root,%master_group) %config(noreplace) %keysdir/public/admin/key
%ghost %attr(0444,root,%master_group) %config(noreplace) %keysdir/public/supporter/key
%ghost %attr(0444,root,%master_group) %config(noreplace) %keysdir/public/other/key

%files master
%_bindir/italc
%_bindir/italc-launcher
%_man1dir/italc.1.gz
%_desktopdir/italc.desktop
%icons128x128dir/italc.png
%icons64x64dir/italc.png
%icons48x48dir/italc.png
%icons32x32dir/italc.png
%icons16x16dir/italc.png

%changelog
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
