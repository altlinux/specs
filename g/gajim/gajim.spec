%global appid org.gajim.Gajim

# reduce an amount of overabundant dependencies
%filter_from_requires /^python3(gajim.gui/d

Name: gajim
Version: 1.6.1
Release: alt1

Summary: a Jabber client written in PyGTK
License: GPL-3.0-only
Group: Networking/Instant messaging
Url: http://gajim.org
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: https://gajim.org/downloads/1.3/gajim-%version.tar.gz
Patch1: gajim-1.2.2-alt-fix-egg-requires.patch

# https://gajim.org/post/2023-01-07-gajim-1.6.0-released/
Requires: python3 >= 3.10

# typelib(Avahi)
%filter_from_requires /^typelib(Avahi)/d

Requires: libgtk+3-gir libgtksourceview4-gir
%py3_requires cssutils
%py3_requires keyring
%py3_requires precis_i18n
%py3_requires nbxmpp
%py3_requires precis_i18n
%py3_requires OpenSSL
%py3_requires cairo

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: libgtk+3-devel python3-devel python3-module-setuptools libsoup-gir-devel libgtksourceview4-gir-devel
BuildRequires: python3-module-nbxmpp >= 4.0.1
BuildArch: noarch

%description
Gajim is a Jabber client written in PyGTK. The goal of Gajim's developers
is to provide a full featured and easy to use xmpp client for the GTK+
users. Gajim does not require GNOME to run, eventhough it exists with
it nicely.

%prep
%setup -n %name-%version
#patch1 -p1

%build
%python3_build

%install
%python3_install

%find_lang %name

%files -f %name.lang
#doc AUTHORS ChangeLog README THANKS
%_bindir/%name
%_bindir/%name-remote
#_bindir/%name-history-manager
%_man1dir/*
%_datadir/applications/%appid.desktop
%_datadir/metainfo/%appid.appdata.xml
%_datadir/icons/hicolor/scalable/apps/%appid.svg
%_datadir/icons/hicolor/scalable/apps/%appid-symbolic.svg
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%{version}*.egg-info

#_desktopdir/%name.desktop
#_desktopdir/%name-remote.desktop
#_iconsdir/hicolor/scalable/apps/%name.svg
#_iconsdir/hicolor/64x64/apps/%name.png
#_iconsdir/hicolor/128x128/apps/%name.png

%changelog
* Mon Jan 16 2023 Ilya Mashkin <oddity@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Jan 11 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.6.0-alt2
- Fixed minimal python3 version
- Removed needless dependency.

* Tue Jan 10 2023 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Tue Dec 06 2022 Ilya Mashkin <oddity@altlinux.ru> 1.5.4-alt1
- 1.5.4

* Tue Nov 01 2022 Ilya Mashkin <oddity@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Mon Oct 10 2022 Ilya Mashkin <oddity@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Thu Sep 22 2022 Ilya Mashkin <oddity@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Mon Jul 25 2022 Ilya Mashkin <oddity@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Fri Jul 08 2022 Ilya Mashkin <oddity@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Wed Jun 22 2022 Ilya Mashkin <oddity@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Sun Jun 18 2022 Ilya Mashkin <oddity@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Fri Jun 03 2022 Ilya Mashkin <oddity@altlinux.ru> 1.4.3-alt2
- Add BR libgtksourceview4-gir (Thanks to Vladimir D. Seleznev)

* Fri Jun 03 2022 Ilya Mashkin <oddity@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Wed Jun 01 2022 Ilya Mashkin <oddity@altlinux.ru> 1.4.2-alt2
- Add BR libsoup-gir (Closes: #42902)

* Fri May 27 2022 Ilya Mashkin <oddity@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Sun May 22 2022 Ilya Mashkin <oddity@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sat May 14 2022 Ilya Mashkin <oddity@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Oct 18 2021 Ilya Mashkin <oddity@altlinux.ru> 1.3.3-alt2
- BuildRequires python3-module-nbxmpp >= 2.0.4 (Closes: #41133)

* Mon Oct 11 2021 Ilya Mashkin <oddity@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue Apr 27 2021 Ilya Mashkin <oddity@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Wed Mar 10 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.1-alt1
- 1.3.1
- reduce amount of overabundant dependencies
- fix source url

* Mon Oct 19 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.2.2-alt1
- 1.2.2
- spec: fix license field

* Sat Aug 31 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.3-alt2
- update Requires

* Sun Aug 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.3-alt1
- 1.1.3

* Fri Oct 19 2018 Ilya Mashkin <oddity@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Oct 04 2018 Ilya Mashkin <oddity@altlinux.ru> 0.16.9-alt3
- rebuild

* Wed Dec 13 2017 Ilya Mashkin <oddity@altlinux.ru> 0.16.9-alt2
- add pyasn to requires

* Mon Dec 04 2017 Ilya Mashkin <oddity@altlinux.ru> 0.16.9-alt1
- 0.16.9
- Remove Requires: libgtk+2-gir-devel (Closes: #34276)

* Sat Jun 24 2017 Ilya Mashkin <oddity@altlinux.ru> 0.16.8-alt1
- 0.16.8

* Fri Mar 24 2017 Ilya Mashkin <oddity@altlinux.ru> 0.16.7-alt3
- spec cleanup, updated buildreqs (thanks to Yuri Sedunov)

* Tue Mar 14 2017 Ilya Mashkin <oddity@altlinux.ru> 0.16.7-alt2
- Much more requires added

* Sat Feb 11 2017 Ilya Mashkin <oddity@altlinux.ru> 0.16.7-alt1
- 0.16.7

* Wed Jan 13 2016 Ilya Mashkin <oddity@altlinux.ru> 0.16.5-alt1
- 0.16.5

* Tue Oct 06 2015 Ilya Mashkin <oddity@altlinux.ru> 0.16.4-alt1
- 0.16.4

* Wed Aug 05 2015 Ilya Mashkin <oddity@altlinux.ru> 0.16.3-alt1
- 0.16.3

* Mon Mar 02 2015 Ilya Mashkin <oddity@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Wed Oct 22 2014 Ilya Mashkin <oddity@altlinux.ru> 0.16-alt1
- 0.16 release

* Fri Jul 04 2014 Ilya Mashkin <oddity@altlinux.ru> 0.16-alt0.2
- 0.16 rc2

* Thu Apr 17 2014 Ilya Mashkin <oddity@altlinux.ru> 0.16-alt0.1
- 0.16 rc1
- drop patches

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.14-alt1.1.1
- Rebuild with Python-2.7

* Thu Jun 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- NMU: build w/o undefine _configure_target hack

* Wed Oct 06 2010 Slava Semushin <php-coder@altlinux.ru> 0.14-alt1
- NMU
- Updated to 0.14 (Closes: #24204)
- Made package noarch

* Sun Apr 04 2010 Alexander Myltsev <avm@altlinux.ru> 0.13.4-alt1
- new version.

* Sat Jan 02 2010 Alexander Myltsev <avm@altlinux.ru> 0.13.1-alt2
- socks5.py: catch EAFNOSUPPORT errors (closes #22667).

* Sun Dec 27 2009 Alexander Myltsev <avm@altlinux.ru> 0.13.1-alt1
- new version: BOSH, roster versioning, bug fixes.

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.5-alt2.qa1.1
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.12.5-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gajim
  * postclean-05-filetriggers for spec file

* Thu Aug 27 2009 Alexander Myltsev <avm@altlinux.ru> 0.12.5-alt2
- fix a TB in the sequential-dialogues patch.

* Tue Aug 18 2009 Alexander Myltsev <avm@altlinux.ru> 0.12.5-alt1
- new version: bug fixes (history manager, dependencies).
- fix detection of LaTeX support (closes #21090).

* Wed Aug 05 2009 Alexander Myltsev <avm@altlinux.ru> 0.12.3-alt1
- new version: bug fixes.

* Thu Jan 01 2009 Alexander Myltsev <avm@altlinux.ru> 0.12.1-alt1
- 0.12.1: critical fixes (incl. security), please update.

* Mon Sep 08 2008 Alexander Myltsev <avm@altlinux.ru> 0.12-alt1.alpha1
- Fix #17044 (gajim fails to start due to a misfeature in gzip.GzipFile)
- Add back some explicit library requirements

* Mon Aug 25 2008 Alex V. Myltsev <avm@altlinux.ru> 0.12-alt0.alpha1
- 0.12-alpha1: security improvements and many new features, see ChangeLog

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.11.4-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gajim

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.11.4-alt1.1
- Rebuilt with python-2.5.

* Mon Jan 07 2008 Alex V. Myltsev <avm@altlinux.ru> 0.11.4-alt1
- 0.11.4: better metacontacts sorting, bug fixes.
- Work around the incompatibility in pysqlite2-2.4.0 (#13873).

* Wed Oct 10 2007 Alex V. Myltsev <avm@altlinux.ru> 0.11.2-alt1
- 0.11.2: bug fixes.

* Sun Mar 04 2007 Alex V. Myltsev <avm@altlinux.ru> 0.11.1-alt1
- 0.11.1: bug fixes, support for Banshee, XEPs: 0202 (time), 0199 (ping)

* Wed Dec 20 2006 Alex V. Myltsev <avm@altlinux.ru> 0.11-alt1
- 0.11 release.

* Mon Nov 27 2006 Alex V. Myltsev <avm@altlinux.ru> 0.10.1-alt2.svn7651
- SVN:
- - privacy lists support
- - group operations, usability improvements
- - annotations, XHTML, rhythmbox link
- - metacontacts across accounts, IPv6, ad-hoc commands.

* Tue Jun 06 2006 Alex V. Myltsev <avm@altlinux.ru> 0.10.1-alt1
- 0.10.1: bug fixes (freezes, lost contacts in roster, etc).

* Wed May 03 2006 Alex V. Myltsev <avm@altlinux.ru> 0.10-alt1
- New version.

* Wed Apr 19 2006 Alex V. Myltsev <avm@altlinux.ru> 0.10-alt0.pre2
- 0.10-pre2: bug fixes (GPG, avatars, menus).

* Wed Apr 12 2006 Alex V. Myltsev <avm@altlinux.ru> 0.10-alt0.pre1
- New version (prerelease). Many added features.

* Sun Mar 19 2006 Alex V. Myltsev <avm@altlinux.ru> 0.9.1-alt3
- removed menu file.
- build-require python-devel explicitly.
- marked documentation as such.

* Tue Feb 07 2006 Alex V. Myltsev <avm@altlinux.ru> 0.9.1-alt2
- /usr/lib -> %%_libdir.
- link idle.so with libpython to avoid undefined symbols on x86_64.

* Mon Feb 06 2006 Alex V. Myltsev <avm@altlinux.ru> 0.9.1-alt1
- Version 0.9.1.
- Added BuildPreReq for xorg-x11-devel.

* Thu Dec 15 2005 Alex V. Myltsev <avm@altlinux.ru> 0.9-alt0.pre2
- Fixed dependency issues (#8660).
- 0.9. This version introduces sqlite-based logs; after the migration,
  downgrading to 0.8 is not recommended.

* Fri Nov 11 2005 Alex V. Myltsev <avm@altlinux.ru> 0.8.2-alt3.svn4344
- Current SVN version. Various bugfixes.

* Sat Oct 22 2005 Alex V. Myltsev <avm@altlinux.ru> 0.8.2-alt2
- Use libraries from pygnome-extras instead of building own versions

* Fri Oct 21 2005 Alex V. Myltsev <avm@altlinux.ru> 0.8.2-alt1
- Initial build for ALT Linux.

