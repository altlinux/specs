%define ver_major 43
%define beta %nil

Name: orca
Version: %ver_major.1
Release: alt1%beta

Summary: A screen reader that provides access to the GNOME desktop by people with visual impairments
Summary(ru_RU.UTF-8): Программа экранного доступа для людей с ограничениями по зрению
Group: Accessibility
License: LGPL-2.1
Url: http://wiki.gnome.org/Projects/Orca

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
Source1: voiceman-server
Source2: %name.watch
Source3: orca-autostart.desktop
#Source4: ru.po

#Patch1: orca-3.2.1-alt-voiceman.patch
Patch2: orca-3.2.1-alt-punc.patch

Requires: typelib(Gtk) = 3.0
#Requires: voiceman

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildPreReq: /proc
BuildRequires: libgtk+3-devel >= 3.2
BuildRequires: libgtk+3-gir
BuildRequires: libat-spi2-core-devel >= 2.26
BuildRequires: at-spi2-atk-devel
BuildRequires: python3-module-pygobject3-devel >= 3.18
BuildRequires: python3-module-dbus-devel
BuildRequires: python3-module-pycairo-devel
BuildRequires: python3-module-pyxdg
BuildRequires: python3-base
BuildRequires: yelp-tools
BuildRequires: python3-module-speechd
BuildRequires: python3-module-brlapi
BuildRequires: gstreamer1.0-devel

Requires: python3-module-speechd

%description
A flexible, scriptable, extensible screen reader for the GNOME platform
that provides access via speech synthesis, braille, and magnification.
Use gnome-default package to prepare GNOME for using with Orca. There can be problems 
if only gnome-minimal is installed.

%description -l ru_RU.UTF-8
Orca - это программа экранного доступа для людей с ограничениями по
зрению. Она предоставляет речевой интерфейс для работы в среде GNOME,
а также средства для увеличения изображения на экране.
Функциональность Orca очень близка к возможностям популярного пакета
Jaws For Windows компании Freedom Scientific.

%prep
%setup -n %name-%version%beta
#%patch1 -p1
%patch2 -p1
#cp -f %SOURCE4 po/ru.po

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std pyexecdir=%python3_sitelibdir

#%__install -d -m755 %buildroot%_datadir/%name/emacspeak-servers/
#echo voiceman > %buildroot%_datadir/%name/emacspeak-servers/.servers
#%__install -pD -m755 %SOURCE1 %buildroot%_datadir/%name/emacspeak-servers/voiceman

install -D -m0644 %SOURCE3 %buildroot%_datadir/gdm/greeter/autostart/orca-autostart.desktop

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/%name
%python3_sitelibdir/%name/
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/symbolic/apps/%name-symbolic.svg
%_man1dir/*
%_datadir/%name/
%_sysconfdir/xdg/autostart/%name-autostart.desktop
%_datadir/gdm/greeter/autostart/%name-autostart.desktop

%changelog
* Sun Jan 08 2023 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Fri Sep 23 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Thu Jul 07 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Fri Jul 01 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Tue May 17 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Tue Mar 22 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Fri Mar 11 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc
- 42.rc

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Thu Dec 02 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Tue Dec 22 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Thu Dec 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Mon Aug 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.6-alt1
- 3.36.6

* Thu Aug 20 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.5-alt1
- 3.36.5

* Mon Jun 01 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Thu Apr 23 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Tue Jan 28 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Fri Feb 01 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Thu Jan 10 2019 Ivan Razzhivin <underwit@altlinux.org> 3.30.1-alt3
- update russian translation

* Wed Nov 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.30.1-alt2
- requires fixed (closes: #35221)

* Fri Oct 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Tue Sep 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.29.92-alt1
- 3.29.92

* Fri Jun 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Sat Apr 21 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Fri Sep 15 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Fri Sep 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.92-alt1
- 3.21.92

* Wed Jul 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Mon May 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.18.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Nov 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Fri May 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 3.16.1-alt1
- Fresh up to v3.16.1 with the help of cronbuild and update-source-functions.

* Sat Mar 28 2015 Cronbuild Service <cronbuild@altlinux.org> 3.16.0-alt1
- Fresh up to v3.16.0 with the help of cronbuild and update-source-functions.

* Sat Dec 06 2014 Cronbuild Service <cronbuild@altlinux.org> 3.14.3-alt1
- Fresh up to v3.14.3 with the help of cronbuild and update-source-functions.

* Sun Nov 16 2014 Paul Wolneykien <manowar@altlinux.org> 3.14.2-alt1
- Fresh up to v3.14.2 with the help of cronbuild and update-source-functions.

* Tue Sep 30 2014 Paul Wolneykien <manowar@altlinux.org> 3.14.0-alt1
- Fresh up to v3.14.0 with the help of cronbuild and update-source-functions.

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 3.12.2-alt1
- Fresh up to v3.12.2 with the help of cronbuild and update-source-functions.

* Thu Apr 17 2014 Paul Wolneykien <manowar@altlinux.org> 3.12.1-alt1
- Fresh up to v3.12.1 with the help of cronbuild and update-source-functions.

* Mon Apr 14 2014 Paul Wolneykien <manowar@altlinux.org> 3.12.0-alt1
- Fresh up to v3.12.0 with the help of cronbuild and update-source-functions.

* Tue Dec 17 2013 Paul Wolneykien <manowar@altlinux.org> 3.10.2-alt2
- Cronbuild: do not build unstable branches.

* Thu Nov 14 2013 Cronbuild Service <cronbuild@altlinux.org> 3.10.2-alt1
- Fresh up to v3.10.2 with the help of cronbuild and update-source-functions.

* Fri Oct 25 2013 Paul Wolneykien <manowar@altlinux.ru> 3.10.1-alt1
- Fresh up to v3.10.1 with the help of cronbuild and update-source-functions.

* Tue Sep 17 2013 Cronbuild Service <cronbuild@altlinux.org> 3.9.92-alt1
- Fresh up to v3.9.92 with the help of cronbuild and update-source-functions.

* Wed Sep 04 2013 Cronbuild Service <cronbuild@altlinux.org> 3.9.91-alt1
- Fresh up to v3.9.91 with the help of cronbuild and update-source-functions.

* Fri Aug 23 2013 Cronbuild Service <cronbuild@altlinux.org> 3.9.90-alt1
- Fresh up to v3.9.90 with the help of cronbuild and update-source-functions.

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 3.9.5-alt1
- Fresh up to v3.9.5 with the help of cronbuild and update-source-functions.

* Fri Jul 12 2013 Paul Wolneykien <manowar@altlinux.ru> 3.9.4-alt1
- Remove the upstream applied patch: reset-family.patch.
- Fresh up to v3.9.4 with the help of cronbuild and update-source-
  functions.

* Wed Jul 03 2013 Paul Wolneykien <manowar@altlinux.ru> 3.9.3-alt1
- Fix erroneously downloaded orca-autostart.desktop.
- Build the package noarch.
- Minor fix in the Russian description.
- Use the default locale for the default voice if none is specified
  (patch).
- Restore plain srcdir packaging.
- Fresh up to v3.9.3 with the help of cronbuild and
  update-source-functions.

* Wed May 29 2013 Paul Wolneykien <manowar@altlinux.ru> 3.9.2-alt1
- new version 3.9.2

* Mon May 13 2013 Paul Wolneykien <manowar@altlinux.org> 3.8.1-alt2
- Add the desktop file to auto-start from GDM.

* Sat May 11 2013 Paul Wolneykien <manowar@altlinux.org> 3.8.1-alt1
- Fix duplicate topdir in 3.8.1.
- New version: 3.8.1.

* Wed Apr 10 2013 Paul Wolneykien <manowar@altlinux.ru> 3.8.0-alt1
- Upstream version 3.8.0.

* Tue Dec 18 2012 Paul Wolneykien <manowar@altlinux.ru> 3.6.3-alt1
- Upstream version 3.6.3.

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
