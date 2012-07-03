Name: gajim
Version: 0.14
Release: alt1.1.1

Summary: a Jabber client written in PyGTK
License: GPL v3
Group: Networking/Instant messaging
Url: http://gajim.org
Packager: Alexander Myltsev <avm@altlinux.ru>

AutoReqProv: yes, noshell

Source: %url/downloads/%name-%version.tar.bz2

Patch1: gajim-alt-dont_install_docdata.patch
Patch2: gajim-alt-package-names.patch
Patch3: gajim-alt-ru-po.patch
Patch5: gajim-alt-tmpfile.patch

Patch10: gajim-alt-PassphraseDialog-cancel.patch
Patch11: gajim-alt-sequential-dialogues.patch

%add_python_compile_include %_datadir/%name/src

%py_requires dbus sqlite3 libglade OpenSSL libasyncns

# Automatically added by buildreq on Sat Apr 03 2010 (-bi)
BuildRequires: imake intltool libgtk+2-devel python-module-pygtk-devel python-modules-encodings xorg-cf-files

BuildArch: noarch

%description
Gajim is a Jabber client written in PyGTK. The goal of Gajim's developers
is to provide a full featured and easy to use xmpp client for the GTK+
users. Gajim does not require GNOME to run, eventhough it exists with
it nicely.

%prep
%setup
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch5 -p2

%patch10 -p2
%patch11 -p2

%build
%configure --enable-remote

%install
%make PREFIX=%prefix LIBDIR=/%_lib DESTDIR=%buildroot install
%find_lang %name

rm %buildroot%_datadir/%name/scripts/dev -rf


%files -f %name.lang
%doc AUTHORS ChangeLog README THANKS
%_bindir/%name
%_bindir/%name-remote
%_bindir/%name-history-manager
%_man1dir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/64x64/apps/%name.png

%changelog
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

