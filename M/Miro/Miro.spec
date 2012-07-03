Name:           Miro
Version:        3.5.0
Release:        alt3.1
Summary:        Miro - Internet TV Player

Group:          Video
License:        GPLv2+
URL:            http://www.getmiro.com/
Packager:       Evgeny Sinelnikov <sin@altlinux.ru>
Source0:        http://ftp.osuosl.org/pub/pculture.org/miro/src/%name-%version.tar.gz

Provides:  miro = %version-%release

BuildRequires:  gcc-c++
BuildRequires:  python-devel xulrunner-devel
BuildRequires:  gettext libgtk+2-devel libssl-devel
BuildRequires:  xorg-xextproto-devel libXv-devel
BuildRequires:  boost-devel boost-python-devel boost-filesystem-devel boost-asio-devel
BuildRequires:  python-module-Pyrex 
BuildRequires:  python-module-pygtk-devel
BuildRequires:  python-module-libtorrent-rasterbar
#BuildRequires:  python-module-pygnome-gtkmozembed
BuildRequires:  python-module-pygnome-gconf
BuildRequires:  python-module-dbus
BuildRequires:  libwebkit-devel

Requires:  python-module-libtorrent-rasterbar
Requires: python-module-pysqlite2

%description
Miro is a free application that turns your computer into an
internet TV video player. This release is still a beta version, which means 
that there are some bugs, but we're moving quickly to fix them and will be 
releasing bug fixes on a regular basis.

%prep
%setup -q -n %name-%version
# Intentionally not using -b .<descr> :
# Otherwise, the unpatched files get re-added into Miro
# (and '.' breaks Python imports)

%build
cd linux && CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
#mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}
# fix EOL
sed -ie 's|\r$||g' CREDITS
# remove shebangs from scripts
cd linux && \
  find ../lib -name '*.py' -exec sed -i "1{/^#!/d}" {} \; && \
  python setup.py install -O1 --skip-build --root "%buildroot"
%find_lang miro

%files -f linux/miro.lang
%doc README license.txt CREDITS 
%_bindir/*
%exclude %_datadir/miro/resources/testdata
%_datadir/miro
%_datadir/pixmaps/*
%_datadir/applications/*.desktop
%_mandir/man1/*
%_datadir/mime/packages/*.xml
%_iconsdir/hicolor/*/apps/miro.png
%python_sitelibdir/*egg-info
%python_sitelibdir/miro/

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt3.1
- Rebuild with Python-2.7

* Tue Apr 12 2011 Paul Wolneykien <manowar@altlinux.ru> 3.5.0-alt3
- Depend on Python module "pysqlite2".

* Wed Mar 23 2011 Paul Wolneykien <manowar@altlinux.ru> 3.5.0-alt2
- Updating translations from Launchpad. (thx Will Kahn-Greene).
- Update copyright and serial. (thx Geoffrey Lee).
- #16056 - default to False on startup on login prompt. (thx Geoffrey Lee).
- Updating version numbers in dev docs. (thx Will Kahn-Greene).
- Get rid of Check Version from file Menu - not very Mac-like. (thx Geoffrey Lee).
- Bye bye unused code. (thx Geoffrey Lee).
- Hide Check Version if app store edition. (thx Geoffrey Lee).
- Fix about dialog - config system changed post 3.5.x. (thx Geoffrey Lee).
- Getting ready for release, bump app serial. (thx Geoffrey Lee).
- Workaround a circular import. (thx Geoffrey Lee).
- Tweaking platform to handle Windows 7 release issues in Python 2.6. (thx Will Kahn-Greene).
- Updating binary kit url. (thx Will Kahn-Greene).
- Fix #15749. (thx Geoffrey Lee).
- Fix #15736. (thx Geoffrey Lee).
- Moving clean to clean.sh like other platforms. (thx Will Kahn-Greene).
- Updating Miro User Manual urls. (thx Will Kahn-Greene).
- Fix #15671.  Don't put the git commit id into the CFBundleVersion
  property. (thx Geoffrey Lee).
- Fix #15776: add LSApplicatinCategoryType for Mac App Store. (thx Geoffrey Lee).
- Moving version number back to -git (thx Ben Dean-Kawamura).
- Bumping version for 3.5.1 release (thx Ben Dean-Kawamura).
- Replay 0c564f1bf0652c12e05d08e192146a2011f910e1 from master. (thx Geoffrey Lee).
- Fix for #15352 (thx Ben Dean-Kawamura).
- Moving version back to 3.5-git (thx Ben Dean-Kawamura).
- Bumping version number to 3.5.1-rc2 (thx Ben Dean-Kawamura).
- Revert "Revert 49c62c8cea8f2fc504b9186cd04040eebe04679f" (thx Ben Dean-Kawamura).
- Hack for 15341 (thx Ben Dean-Kawamura).
- Revert 49c62c8cea8f2fc504b9186cd04040eebe04679f (thx Ben Dean-Kawamura).
- Another fix for #15150 (thx Ben Dean-Kawamura).
- Switching version back to -git (thx Ben Dean-Kawamura).
- Fix for #15312 (thx Ben Dean-Kawamura).
- Fix for #15309 (thx Ben Dean-Kawamura).
- Updatating version number for 3.5.1-rc1 (thx Ben Dean-Kawamura).
- Made mp4 conversions work on OS X. (thx Ben Dean-Kawamura).
- Added code to set up ffmpeg presets on windows (thx Ben Dean-Kawamura).
- More #14984 work. (thx Ben Dean-Kawamura).
- Replay 1fc43b34df0d2e88f43a0e0424c4b3d0e3990c65 from master. (thx Geoffrey Lee).
- Implemented #14894 (thx Ben Dean-Kawamura).
- Added some logging info to try to help diagnose #15071 (thx Ben Dean-Kawamura).
- Fix for #15233 (thx Ben Dean-Kawamura).
- Fix for #15227 (thx Ben Dean-Kawamura).
- Cherry pick 226f0c5ad13142c3dbe1ccfad1d35b5bfe3b2813 from master. (thx Geoffrey Lee).
- Updating translations. (thx Will Kahn-Greene).
- Re-adding presets to Windows nsis. (thx Will Kahn-Greene).
- Moved ffmpeg stuff. (thx Will Kahn-Greene).
- Updating binary kit to 20101119-3.5 for osx. (thx Will Kahn-Greene).
- Adding -strict experimental args to ffmpeg. (thx Will Kahn-Greene).
- Updating to 20101120 binary kit. (thx Will Kahn-Greene).
- Adding kw strings. (thx Will Kahn-Greene).
- Fix for #14994 (thx Ben Dean-Kawamura).
- Only setup sys.excepthook on GTK. (thx Ben Dean-Kawamura).
- Syncing translations. (thx Will Kahn-Greene).
- Fixed OS X so that we don't crash on frontend exceptions. (thx Ben Dean-Kawamura).
- Fix for #14804 (thx Ben Dean-Kawamura).
- Implemented #15152 (thx Ben Dean-Kawamura).
- Fix for #15217 (thx Ben Dean-Kawamura).
- Bug #15185.  Fixes hardcoded fonts folder. (thx Will Kahn-Greene).
- Bug #15168.  Show everything from getwindowsversion. (thx Will Kahn-Greene).
- Replay patches from the master branch into Miro-3.5 branch. (thx Geoffrey Lee).
- Fix for #14924 (thx Ben Dean-Kawamura).
- Improved code form 0b97f68 (thx Ben Dean-Kawamura).
- Fix for #15198. (thx Ben Dean-Kawamura).
- Fix for #15079 (thx Ben Dean-Kawamura).
- Possible fix for #12538 (thx Ben Dean-Kawamura).
- Changing branch version back to 3.5-git. (thx Will Kahn-Greene).
- Fixes 15119.  When Miro is focused, re-take mediakeys. (thx Will Kahn-Greene).
- Fix for #14973 (thx Ben Dean-Kawamura).
- Bug #15168.  Log Windows versions better. (thx Will Kahn-Greene).
- Fix for #15156 (thx Ben Dean-Kawamura).
- Fix for #15151 (thx Ben Dean-Kawamura).
- Fix for #15150 (thx Ben Dean-Kawamura).
- Another fix for #14490. (thx Ben Dean-Kawamura).
- Bug #14490.  Fixes playing externally when something is downloaded. (thx Will Kahn-Greene).
- Bug #15137.  Fixes DeprecationWarning from conversions. (thx Will Kahn-Greene).
- Bug #15119.  Fixes MediaKeys support. (thx Will Kahn-Greene).
- Bug #15144.  Updates wiki urls in codebase. (thx Will Kahn-Greene).
- change search toolbar name per Zugo's request (thx Paul Swartz).
- Fix to remember list/normal view for the library tabs. (thx Ben Dean-Kawamura).
- Blind fix for a database bug (thx Ben Dean-Kawamura).
- changes to the installer for Zugo (thx Paul Swartz).

* Wed Nov 24 2010 Paul Wolneykien <manowar@altlinux.ru> 3.5.0-alt1
- Build fresh v3.5.0 from the upstream git.
- Remove unnecessary `Video' path correction patch.

* Tue Jun 01 2010 Motsyo Gennadi <drool@altlinux.ru> 3.0.2-alt0.M51.1
- build for M51

* Sun May 30 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.2-alt1
- Update to new release

* Sun Apr 18 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.1-alt1
- Update to new release

* Mon Jan 04 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.5.4-alt1
- Update to new release
- The following repocop fixes applied:
 * desktop-mime-entry for Miro

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.1
- Rebuilt with python 2.6

* Sun Aug 30 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.5.2-alt1
- Update to new release

* Sun Jun 28 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.0.5-alt1
- Update to new release
- Add manual require for python-module-libtorrent-rasterbar

* Sat Jun 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.0.4-alt1
- Initial build for Sisyphus

* Sat Jun 13 2009 Alex Lancaster <alexlan[AT}fedoraproject org> - 2.0.4-1
- Update to upstream 2.0.4

* Sat Jun 13 2009 Alex Lancaster <alexlan[AT}fedoraproject org> - 2.0.3-3
- Rebuild against newer Python boost

* Mon Apr 27 2009 Christopher Aillon <caillon@redhat.com> - 2.0.3-2
- Rebuild against newer gecko

* Mon Mar 16 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.0.3-1
- Update to upstream 2.0.3
- Add patch to disable xine-hack, hopefully fixes #480527
- Use internal 0.14 version of rb_libtorrent for < F-11 (#489755)

* Mon Mar  9 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.0.2-1
- Update to upstream 2.0.2
- Add Requires: gstreamer-python (#489134)
- Drop patch for libtorrent 0.13, applied upstream

* Fri Feb 27 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.0-5
- Combine the fhs patches into one, and fix the path to
  /usr/libexec/xine_extractor (#487442)

* Fri Feb 27 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.0-4
- Add another upstream patch to fix patch on x86_64 (#487442)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Michel Salim <salimma@fedoraproject.org> - 2.0-2
- Use system libtorrent >= 0.13
- Do not ship testdata
- Switch default download directory to ~/Videos/Miro

* Tue Feb 10 2009 Michel Salim <salimma@fedoraproject.org> - 2.0-1
- Update to 2.0

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.8-5
- rebuild with new openssl

* Tue Dec 23 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.8-4
- Rebuild against newer gecko 1.9.1

* Thu Dec 18 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.8-3
- Enable patch for new boost 1.37 for F-11+

* Thu Dec 18 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.8-2
- Rebuild against new boost

* Wed Dec  3 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.8-1
- Update to latest upstream (1.2.8)
- Rebuild for Python 2.6

* Wed Nov 12 2008 Christopher Aillon <caillon@redhat.com> - 1.2.7-2
- Rebuild against newer gecko 1.9.0.4

* Sun Sep 28 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.7-1
- Update to 1.2.7
- Rebuild against gecko-libs 1.9.0.2 (#464205)

* Fri Aug 22 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.6-3
- Do not create backup files when patching; the backup files get re-added during the build process

* Fri Aug 22 2008 Michel Salim <salimma@fedoraproject.org> - 1.2.6-2
- Unapply boost patch; boost-1.36 has been backed out for F10

* Fri Aug 22 2008 Michel Salim <salimma@fedoraproject.org> - 1.2.6-1
- Update to 1.2.6
- Patch for boost API change

* Tue Aug 12 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.4-4
- Rebuild for new boost (fixes broken deps).

* Sat Jul 19 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.4-3
- Rebuild for xulrunner-1.9.0.1
- Unfortunately we probably need to make this an exact match because
  Miro uses the unstable API, so a rebuild may need to be done on every
  package update to be sure that it will work with new xulrunner updates

* Wed Jun 18 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.4-2
- Rebuild for xulrunner-1.9 final.

* Sun Jun 15 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.4-1
- Update to latest upstream (1.2.4)

* Mon Apr 28 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.3-2
- Update and re-enable xulrunner patch from Martin Stransky (#393521)

* Mon Apr 28 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.3-1
- Update to official 1.2.3 upstream release (includes the previous
  xulrunner fixes in test release).

* Sat Mar 29 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.2-0.1.test
- Update to test snapshot which is supposed to fix xulrunner 1.9 support
  (http://bugzilla.pculture.org/show_bug.cgi?id=9692)
- Drop xulrunner patch.

* Fri Mar 28 2008 Christopher Aillon <caillon@redhat.com> - 1.2-2
- Prune spurious (Build)Requires

* Mon Mar 24 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2-1
- Update to latest upstream (1.2)
- Remove much of xulrunner patch, keep modifications to setup.py to look
  for libxul rather than xulrunner-xpcom

* Tue Mar 11 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.1.2-4
- Update GCC 4.3 patch by Christopher Aillon (#434480)

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.2-3
- Autorebuild for GCC 4.3

* Fri Feb 15 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.1.2-2
- Patch to build against GCC 4.3.0

* Fri Feb 15 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.1.2-1
- Update to 1.1.2

* Sat Feb  9 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.1-3
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Fri Jan 25 2008 Michel Salim <michel.sylvan@gmail.com> - 1.1-2
- Fix charset mismatch in download window
- Remove shebangs from scripts
- Sanitize end-of-line markers

* Thu Jan 17 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.1-1
- Update to upstream 1.1 release
- BuildRequires: gecko-devel-unstable, openssl-devel

* Tue Jan  8 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.0-5
- Update xulrunner patch to use upstream .pc files

* Sun Dec 23 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 1.0-4
- Add support for python eggs for F9+

* Sun Dec 23 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 1.0-3
- Re-enable gecko-libs 1.9, as 1.8.1.10 has now gone away as a BR.
- Add first-cut patch from Martin Stransky from #393521 that attempts to
  patch Miro to work against xulrunner. Likely incomplete. 

* Tue Dec  4 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 1.0-2
- Back to building against 1.8.1.10 (firefox) until #393521 is fixed.

* Fri Nov 16 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 1.0-1
- Update to latest upstream (1.0).

* Wed Nov 14 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.9.9.9-2
- Build against gecko-libs 1.9 (new xulrunner)

* Fri Nov 09 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.9.9.9-1
- Update to latest upstream (0.9.9.9)
- Build against gecko-libs 1.8.1.9 (firefox 2.0.0.9)
- Include xine_extractor in package (thanks to Jason Farrell)
- Drop Miro-setup.py.patch

* Thu Nov 01 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.9.9.1-6
- Update patch with workaround suggested on:
  http://bugzilla.pculture.org/show_bug.cgi?id=8579

* Wed Oct 31 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.9.9.1-5
- Add setup.py patch to ignore call to svn.

* Tue Oct 30 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.9.9.1-3
- Add BuildRequires: libXv-devel
- Drop dbus patch

* Sun Oct 28 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.9.9.1-1
- Update to latest upstream (0.9.9.1)

* Fri Oct 26 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.9.8.1-8
- Replace Requires and BuildRequires for firefox with gecko to 
  smooth eventual xulrunner transition 

* Thu Oct 25 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.9.8.1-7
- Rebuild for new Firefox (2.0.0.8)
- License: GPLv2+ to conform with Fedora licensing guidelines

* Thu Sep 20 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.8.1-3
- new Firefox dep

* Wed Aug 15 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.8.1-2
- made Democracy obsolte with this release

* Tue Aug 14 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.8.1-1
- new upstream version and new naming
- fix to solve the python/dbus problem

* Fri Jun 22 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.6-2
- new upstream version

* Fri Jun 22 2007 Thorsten Scherf <tscherf@redhat.com> 0.9.6-1
- new upstream version

