
Name: orca
Version: 3.4.2
Release: alt1
Summary: A screen reader that provides access to the GNOME desktop by people with visual impairments
Summary(ru_RU.UTF-8): Программа экранного доступа для людей с ограничениями по зрению 
Packager: Michael Pozhidaev <msp@altlinux.ru>
License: LGPL
Group: Accessibility
URL: http://live.gnome.org/Orca

Source0: %name-%version.tar
Source1: voiceman-server
Source2: %name.watch

Patch1: orca-3.2.1-alt-voiceman.patch
Patch2: orca-3.2.1-alt-punc.patch

%add_python_req_skip GNOME GNOME__POA

Requires: voiceman

BuildPreReq: /proc
BuildRequires: intltool >= 0.40
BuildRequires: gnome-doc-utils
BuildRequires: libgtk+3-devel >= 3.2
BuildRequires: libgtk+3-gir
BuildRequires: libat-spi2-core-devel
BuildRequires: python-module-pygobject3-devel >= 3.0
BuildRequires: python-module-dbus-devel
BuildRequires: python-module-pycairo-devel
BuildRequires: python-module-pyxdg
BuildRequires: python-module-json

%description
A flexible, scriptable, extensible screen reader for the GNOME platform
that provides access via speech synthesis, braille, and magnification.
Use gnome-default package to prepare GNOME for using with Orca. There can be problems 
if only gnome-minimal is installed.

%description -l ru_RU.UTF-8
Orca - это программа экранного доступа для людей с ограничениями по
зрению. Она предоставляет речевой интерфейс для работы в среде GNOME,
а также средства для увеличения изображения на экране.
Функциональность Orcaочень близка к возможностям популярного пакета
Jaws For Windows компании Freedom Scientific.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%__install -d -m755 %buildroot%_datadir/%name/emacspeak-servers/
echo voiceman > %buildroot%_datadir/%name/emacspeak-servers/.servers
%__install -pD -m755 %SOURCE1 %buildroot%_datadir/%name/emacspeak-servers/voiceman

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/orca
%dir %python_sitelibdir/orca
%python_sitelibdir/orca/
%_datadir/applications/*
%_datadir/icons/hicolor/*/apps/orca.png
%_datadir/icons/hicolor/scalable/apps/orca.svg
%_man1dir/*
%dir %_datadir/orca
%_datadir/orca/*
%_sysconfdir/xdg/autostart/orca-autostart.desktop

%changelog
* Wed Jun 06 2012 Paul Wolneykien <manowar@altlinux.ru> 3.4.2-alt1
- Update the sources up to v3.4.2.

* Fri Jan 06 2012 Michael Pozhidaev <msp@altlinux.ru> 3.2.2-alt1
- New version

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 25 2011 Michael Pozhidaev <msp@altlinux.ru> 3.2.1-alt1
- New version 3.2.1

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1
- new version 3.0.4

* Fri Apr 08 2011 Michael Pozhidaev <msp@altlinux.ru> 2.32.1-alt2
- Removed /etc/orca directory

* Fri Apr 08 2011 Michael Pozhidaev <msp@altlinux.ru> 2.32.1-alt1
- New version

* Tue Jun 29 2010 Michael Pozhidaev <msp@altlinux.ru> 2.30.1-alt2
- Updated for voiceman-1.5.0

* Sat Jun 12 2010 Michael Pozhidaev <msp@altlinux.ru> 2.30.1-alt1
- New version: 2.30.1

* Mon Apr 12 2010 Michael Pozhidaev <msp@altlinux.ru> 2.30.0-alt1
- Updated to 2.30

* Tue Mar 09 2010 Michael Pozhidaev <msp@altlinux.ru> 2.29.92-alt1
- Update to 2.29.92
- python-module-pygnome-desktop-devel was added to the list of build requirements

* Fri Mar 05 2010 Michael Pozhidaev <msp@altlinux.ru> 2.29.91-alt1
- Update to 2.29.91

* Thu Jan 21 2010 Michael Pozhidaev <msp@altlinux.ru> 2.28.3-alt1
- New version (closes: #22543)

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.26.1-alt1.1
- Rebuilt with python 2.6

* Tue Apr 14 2009 Michael Pozhidaev <msp@altlinux.ru> 2.26.1-alt1
- New version: 2.26.1

* Sat Nov 15 2008 Michael Pozhidaev <msp@altlinux.ru> 2.24.1-alt1
- New version (2.24.1)
- Added Russian summary and description

* Fri Sep 05 2008 Michael Pozhidaev <msp@altlinux.ru> 2.22.3-alt4
- Added voiceman support
- Added fake directory with emacspeak servers

* Sat Aug 30 2008 Michael Pozhidaev <msp@altlinux.ru> 2.22.3-alt3
- New maintaner

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 2.22.3-alt2
- fix desktop file

* Sat Jul 05 2008 Igor Zubkov <icesik@altlinux.org> 2.22.3-alt1
- 2.22.2 -> 2.22.3

* Sun Jun 01 2008 Igor Zubkov <icesik@altlinux.org> 2.22.2-alt1
- 2.19.6 -> 2.22.2

* Sat Aug 25 2007 Michael Pozhidaev <msp@altlinux.ru> 2.19.6-alt0.4
- First testing unstable AltLinux version.

* Sat Feb 03 2007 Willie Walker <william.walker@sun.com>
- Add libgail-gnome dependency.

* Thu Aug 03 2006 Willie Walker <william.walker@sun.com>
- Add orca.png and orca.desktop files.

* Tue Jul 11 2006 Willie Walker <william.walker@sun.com>
- Fix "pyborit" typo.

* Mon May 15 2006 Willie Walker <william.walker@sun.com>
- More tweaking.

* Fri May 12 2006 Willie Walker <william.walker@sun.com>
- Well, try again.  Third time is a charm?

* Thu May 04 2006 Willie Walker <william.walker@sun.com>
- One more attempt at getting the dependencies right.

* Tue Apr 25 2006 Willie Walker <william.walker@sun.com>
- Update for new preferences settings mechanism (remove orca-setup.in)

* Mon Oct 17 2005 Willie Walker <william.walker@sun.com>
- Update for 0.2.0.
