%def_without check

Summary: Twm based window manager for the X Window System
Summary(ru_RU): Основанный на twm оконный менеджер для X Window System
Name: ctwm
Version: 4.0.3.691
Epoch: 1
Release: alt1

Source: %name-%version.tar.xz
Url: http://www.ctwm.org/index.html

Source1: startctwm
Source2: %name.wmsession
Source3: %name.icon64x64.xpm
Source4: %name.desktop
Source5: %name-systemd.desktop
Source6: %name-session-target
Source7: %name.service
Source8: %name-session.target
Source9: %name.target

Patch: ctwm-3.8.2-GetFont.patch
License: BSD
Group: Graphical desktop/Other

# Automatically added by buildreq on Wed Jun 29 2022
# optimized out: asciidoc cmake-modules docbook-dtds docbook-style-xsl glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXau-devel libXrender-devel libXt-devel libcrypt-devel libgpg-error libsasl2-3 libxcb-devel python3 python3-base sh4 xml-common xml-utils xorg-proto-devel xsltproc xz
BuildRequires: asciidoc-a2x cmake ctags doxygen flex graphviz libXext-devel libXmu-devel libXpm-devel libXrandr-devel libjpeg-devel

%description
Ctwm is a window manager for the X Window System.  It provides
titlebars, shaped windows, virtual screens (workspaces), several forms
of icon management, user-defined macro functions, click-to-type and
pointer-driven keyboard focus, and user-specified key and pointer
button bindings.  It is actually twm (Tab Window Manager) from the MIT
X11 distribution slightly modified to accommodate the use of several
virtual screens (workspaces). It is heavily inspired from the
Hewlett-Packard vuewm window manager.  In addition, ctwm can use
coloured, shaped icons and background root pixmaps in XPM format [from
Arnaud Le Hors], any format understood by the imconv package [from the
San Diego Supercomputer Center] and xwd files.  Ctwm can be compiled
to use both, either or none of the above icon/pixmap formats.

%description -l ru-RU
Ctwm -- оконный менеждер для X Windows System, основанный на одном из
старейших  оконных менеджеров для X11 -- twm (Tab Window Manager) из
дистрибутива Mit X11. Под влиянием vuewm от Hewlett-Packard в ctwm
добавлена поддержка "трёхмерных" заголовков, рамоки меню, виртуальные
экраны и многое другое. Ctwm поддерживает макросы в настройках,
разнообразные стили перемещения фокуса, заливку фона и т. д., а также
имеет несколько уникальных функций, например movepush, когда окно,
перемещаемое по экрану, расталкивает прочие окна в стороны.

%package docs
BuildArch: noarch
Summary: Developmeatn documentation for %name
Group: Graphical desktop/Other
%description docs
%summary

%package systemd
BuildArch: noarch
Summary: Systemd services ans scripts for %name
Group: Graphical desktop/Other
Requires: %name = %version-%release
%description systemd
%summary

%prep
%setup
#patch -p1
sed -ri 's/(#define[[:space:]]+MAX_BUTTONS[[:space:]]+).*/\1 24/' ctwm.h
%cmake \
    -DETCDIR=%_sysconfdir/X11/ctwm \
    -DDOCDIR=%_defaultdocdir/%name-%version \
    -DEXAMPLEDIR=%_defaultdocdir/%name-%version \
    -DMANUAL_BUILD_HTML=True -DENABLE_ASCIIDOC_HTML=True
    # unmaintained -DDO_CLIENT=ON

%build
%cmake_build -t all -t doxygen
(cd doc/devman; for N in *adoc; do asciidoc -atoc -anumbered $N; done)

%install
%cmakeinstall_std
install -d %buildroot%_datadir/xsessions
install %SOURCE4 %buildroot%_datadir/xsessions/
install %SOURCE5 %buildroot%_datadir/xsessions/
install -D %SOURCE3 %buildroot/%_iconsdir/hicolor/64x64/apps/%name.xpm
install -D %SOURCE1 %buildroot/%_sysconfdir/X11/wmsession.d/07%name
install -D system.ctwmrc %buildroot/%_sysconfdir/X11/%name/system.ctwmrc
install -D %SOURCE1 %buildroot/%_bindir/startctwm
install -D %SOURCE6 %buildroot%_prefix/libexec/%name-session-target
install -d %buildroot%_user_unitdir
install -D %SOURCE7 %buildroot%_user_unitdir/
install -D %SOURCE8 %buildroot%_user_unitdir/
install -D %SOURCE9 %buildroot%_user_unitdir/
install -D %_cmake__builddir/ctwm.1 %buildroot%_man1dir/ctwm.1

%files
%doc %_defaultdocdir/%name-%version
%_iconsdir/hicolor/64x64/apps/*
%_bindir/*
%_mandir/man1/*
%config(noreplace) %_sysconfdir/X11/%name/system.ctwmrc
%_sysconfdir/X11/wmsession.d/*
%_datadir/%name/
%_datadir/xsessions/%name.desktop

%files docs
%doc %_cmake__builddir/doxygen/html
%doc doc/devman/*.html doc/devman/static

%files systemd
%_user_unitdir/*
%_prefix/libexec/*
%_datadir/xsessions/%name-systemd.desktop

%if_with check
%check
%cmake_build -t test
%endif

%changelog
* Wed Jun 29 2022 Fr. Br. George <george@altlinux.org> 1:4.0.3.691-alt1
- Update to revision 691
- Separate systemd-avare subpackage

* Tue Nov 09 2021 Fr. Br. George <george@altlinux.ru> 1:4.0.3-alt3
- Introduce systemd --user session startup

* Mon Nov 01 2021 Igor Vlasenko <viy@altlinux.org> 1:4.0.3-alt2
- NMU: WM packaging policy 2.0: added xsessions desktop

* Sat Oct 26 2019 Fr. Br. George <george@altlinux.ru> 1:4.0.3-alt1
- Autobuild version bump to 4.0.3

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 1:4.0.1-alt1
- Autobuild version bump to 4.0.1

* Mon May 29 2017 Fr. Br. George <george@altlinux.ru> 1:4.0.0-alt1
- Autobuild version bump to 4.0.0

* Wed Sep 21 2016 Fr. Br. George <george@altlinux.ru> 1:3.8.2-alt2
- Fix fonset usage

* Mon Jul 14 2014 Fr. Br. George <george@altlinux.ru> 1:3.8.2-alt1
- Autobuild version bump to 3.8.2
- Clean up spec

* Thu Aug 29 2013 Fr. Br. George <george@altlinux.ru> 1:3.8.1-alt1
- Update to current mtn
- Introducing epoch (version switched back to 3.8.*)

* Mon Mar 14 2011 Fr. Br. George <george@altlinux.ru> 3.9devel-alt2
- Buildreq regenerated

* Mon Feb 14 2011 Fr. Br. George <george@altlinux.ru> 3.9devel-alt1
- Version up to MTN development

* Sat Nov 21 2009 Repocop Q. A. Robot <repocop@altlinux.org> 3.8a-alt1.qa2
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for ctwm
  * postclean-05-filetriggers for spec file

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.8a-alt1.qa1.1
- NMU:
  * updated build dependencies
  * removed obsolete %%update_wms/%%clean_wms calls

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 3.8a-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_wms for ctwm

* Wed Apr 18 2007 Fr. Br. George <george@altlinux.ru> 3.8a-alt1
- version up
- another strcpy() without \0 fix
- MAX_BUTTONS is 24 now

* Mon Dec 11 2006 Fr. Br. George <george@altlinux.ru> 3.7-alt5
- Poor strcpy() bugfix

* Thu Nov 16 2006 Fr. Br. George <george@altlinux.ru> 3.7-alt4
- Bug 10256 closed (/usr/X11R6 -> /usr)

* Thu Sep 14 2006 Fr. Br. George <george@altlinux.ru> 3.7-alt3
- GEAR tuning

* Sun Oct 09 2005 Fr. Br. George <george@altlinux.ru> 3.7-alt2
- Trivial description bugs fixed, russian description added

* Thu Aug 25 2005 Fr. Br. George <george@altlinux.ru> 3.7-alt1
- Version upping
- Upstream changed

* Fri Jul 01 2005 Fr. Br. George <george@altlinux.ru> 3.6-alt3
- Change startctwm to be used both with or without m4

* Mon Jul 26 2004 Fr. Br. George <george@altlinux.ru> 3.6-alt2
- Add startctwm simple script, move pixmaps out of /etc/X11

* Fri Oct 17 2003 Fr. Br. George <george@altlinux.ru> 3.6-alt1
- First time ported under ALT Linux

