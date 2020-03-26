%define pppconfdir %_sysconfdir/ppp
%define docdir %_datadir/chestnut-dialer/chestnut_dialer/doc
%define consolehelper %_bindir/consolehelper
%define pamdir %_sysconfdir/pam.d
%define consoleappsdir %_sysconfdir/security/console.apps

%def_disable qt
%def_enable gtk2
%def_with consolehelper

Name: chestnut-dialer
Version: 0.3.3
Release: alt8.3

Summary: A PPP dialing program written in Python
License: GPLv2+
Group: Networking/Remote access

Url: http://chestnut-dialer.sourceforge.net
Source: %name-%version.tar.bz2
Patch0: chestnut-dialer-0.3.2-alt-ttynames.patch
Patch1: chestnut-dialer-0.3.2-alt-quoting.patch
Patch2: chestnut-dialer-0.3.2-alt-ru.po.patch
Patch3: chestnut-dialer-0.3.2-cvs-pagetitles.patch
Patch4: chestnut-dialer-0.3.2-alt-230400.patch
Patch5: chestnut-dialer-0.3.3-alt-categories.patch
Patch6: chestnut-dialer-0.3.3-alt-mtu_mru.patch
Patch7: chestnut-dialer-0.3.3-alt-no_resolvconf.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: ppp
Requires: python >= 2.2
Requires: python-modules-libxml2
%{?_with_consolehelper:Requires: %consolehelper}

%py_provides chestnut_dialer
# Find chestnut_dialer and other provides
%add_python_lib_path %_datadir/chestnut-dialer/

BuildArch: noarch

BuildRequires: ppp
BuildRequires: python >= 2.2
BuildRequires: python-modules-libxml2
BuildRequires: texinfo
%{?_enable_gtk2:BuildRequires: python-module-pygtk-libglade}
%{?_enable_qt:BuildRequires: python-module-qt}
%{?_with_consolehelper:BuildRequires: %consolehelper}

Summary(ru_RU.UTF-8): Программа дозвона по протоколу PPP, написанная на Python

# Added by buildreq2 on Fri Nov 10 2006 (-bi)
BuildRequires: net-tools python-modules-libxml2

%description
Chestnut Dialer is PPP dialing program, written in Python.
Current version %version can work with GTK2, QT, and without GUI
(command line interface). Chestnut Dialer does not require root
permissions, but requires read and/or write access to some system
files (modem device etc.). Chestnut Dialer uses standard pppd
daemon to set up network interface.

%description -l ru_RU.UTF-8
Chestnut Dialer - это программа дозвона по протоколу PPP,
написанная на Python. Текущая версия (%version) может работать
с GTK2, QT, и без графического интерфейса (интерфейс командной строки).
Chestnut Dialer выполняется с привилегиями пользователя, но требует
доступ на чтение и/или на запись к некоторым системным файлам (включая
устройство модема). Chestnut Dialer использует стандартный демон pppd
для установки сетевого интерфейса.

%if_enabled gtk2
%package gtk2
Summary: GTK2 user interface for Chestnut Dialer
Summary(ru_RU.UTF-8): Интерфейс пользователя GTK2 для Chestnut Dialer
Group: Networking/Remote access
Requires: %name = %version
Requires: python-module-pygtk
Requires: python-module-pygtk-libglade

%description gtk2
This is the GTK2 user interface for Chestnut Dialer.

%description -l ru_RU.UTF-8 gtk2
Интерфейс пользователя GTK2 для Chestnut Dialer.
%endif

%if_enabled qt
%package qt
Summary: QT user interface for Chestnut Dialer
Summary(ru_RU.UTF-8): Интерфейс пользователя QT для Chestnut Dialer
Group: Networking/Remote access
Requires: %name = %version
Requires: python-module-qt

%description qt
This is the QT user interface for Chestnut Dialer.

%description -l ru_RU.UTF-8 qt
Интерфейс пользователя QT для Chestnut Dialer.
%endif

%prep
%setup
%patch0 -p1
%patch1 -p1
#patch2 -p1
#patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%configure \
	%{subst_enable gtk2} \
	%{subst_enable qt} \
	--with-pppconfdir=%pppconfdir \
	--with-docdir=%docdir \
	%{?_with_consolehelper} \
	--with-pamdir=%pamdir \
	--with-consoleappsdir=%consoleappsdir
%make
sed -i 's,/python,&2,' %name

%install
%makeinstall_std
install -dm755 %buildroot%_desktopdir
install -pm644 chestnut-dialer-gtk2.desktop %buildroot%_desktopdir/
install -pm644 chestnut-dialer-qt.desktop %buildroot%_desktopdir/

%files
%doc AUTHORS COPYING ChangeLog NEWS* README* FAQ*
%doc %docdir
%_infodir/%{name}*.info*
%_man1dir/chestnut-dialer*
%pppconfdir/peers/*
%_bindir/chestnut-dialer
%if_with consolehelper
%_sbindir/chestnut-dialer
%pamdir/chestnut-dialer
%consoleappsdir/chestnut-dialer
%endif
%_datadir/chestnut-dialer/chestnut_dialer/dobj
%_datadir/chestnut-dialer/chestnut_dialer/dockicons
%_datadir/chestnut-dialer/chestnut_dialer/importers
%_datadir/chestnut-dialer/chestnut_dialer/none_ui
%_datadir/chestnut-dialer/chestnut_dialer/*.py*
%_datadir/chestnut-dialer/chestnut_dialer/*.x*
%_datadir/locale/*/LC_MESSAGES/chestnut-dialer.mo
%_pixmapsdir/chestnut-dialer.png

%if_enabled gtk2
%files gtk2
%_datadir/chestnut-dialer/chestnut_dialer/gtk2_ui
%_desktopdir/chestnut-dialer-gtk2.desktop
%endif

%if_enabled qt
%files qt
%_datadir/chestnut-dialer/chestnut_dialer/qt_ui
%_desktopdir/chestnut-dialer-qt.desktop
%endif

# TODO
# - move from /usr/share/chestnut-dialer
#          to /usr/lib/chestnut-dialer
#   (see /usr/share/doc/rpm-build-python-0.29/policy/draft/4-Python_TOOLS.txt)
# - check ru.po

%changelog
* Thu Mar 26 2020 Michael Shigorin <mike@altlinux.org> 0.3.3-alt8.3
- clarify License:
- explicit python2
- spec cleanup (and conversion to UTF-8)

* Thu Oct 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.3-alt8.2
- Rebuilt without Qt-3.

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3-alt8.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt8.1
- Rebuilt with python 2.6

* Tue Nov 17 2009 Michael Shigorin <mike@altlinux.org> 0.3.3-alt8
- drop illegal dr^H^Hrequires
- add unneeded provides

* Thu Jul 30 2009 Michael Shigorin <mike@altlinux.org> 0.3.3-alt7
- applied repocop patch

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.3.3-alt6
- applied repocop patch

* Tue Feb 12 2008 Grigory Batalov <bga@altlinux.ru> 0.3.3-alt5
- Fix python provides.
- Use %%def_enable/%%if_enabled macros instead of ?_with_.

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 0.3.3-alt4.1
- Rebuilt with python-2.5.

* Mon Dec 24 2007 Michael Shigorin <mike@altlinux.org> 0.3.3-alt4
- fixes to defaults:
  + MTU/MRU patch wasn't actually applied, now indeed it is
  + added patch7 to disable resolv.conf modification by default
    (it's done by /etc/ppp/ip-up script just fine; the fix is
    rather cosmetic as chestnut-dialer runs unprivileged
    and would only complain into stderr)

* Tue Sep 25 2007 Michael Shigorin <mike@altlinux.org> 0.3.3-alt3
- bumped default MTU from 296 to 500 bytes, MRU from 296 to 1500

* Mon Sep 24 2007 Michael Shigorin <mike@altlinux.org> 0.3.3-alt2
- fixed desktop file categories, thanks viy@ again :)

* Sat Sep 22 2007 Michael Shigorin <mike@altlinux.org> 0.3.3-alt1
- 0.3.3
- added desktop file installation, thanks viy@
- removed ru.po patch, probably better look into it another time
- removed cvs patch (already applied, how strange)

* Tue Feb 20 2007 Michael Shigorin <mike@altlinux.org> 0.3.2-alt3
- bumped maximum port speed from 115200 to 230400 (EDGE)

* Fri Feb 16 2007 Michael Shigorin <mike@altlinux.org> 0.3.2-alt2
- added /dev/ttyACM0 and /dev/ttyUSB0
- added patch to fix assembling chat script with double-quoted
  parameter values
- tweaked russian translation for readability a bit
- applied/extended CVS fix for Qt UI two-page options empty tab names
- fixed Group:

* Fri Nov 10 2006 Michael Shigorin <mike@altlinux.org> 0.3.2-alt1
- 0.3.2
- spec cleanup
- buildreq2

* Fri Jun 03 2005 Michael Shigorin <mike@altlinux.ru> 0.2.1-alt1
- initial build

