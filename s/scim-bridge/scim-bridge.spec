#%%define snapdate 20070223
%define snapshot 0%{?snapdate:1}

%define build_qt 1

Name: scim-bridge

Version: 0.4.16
Release: alt1
Summary: SCIM Bridge Gtk IM module
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: System/Libraries
License: GPLv2+ or LGPLv2+
Url: http://www.scim-im.org/projects/scim_bridge
Source0: http://dl.sourceforge.net/sourceforge/scim/%name-%version%{?snapdate:-%snapdate}.tar.gz

BuildRequires: autoconf gcc-c++
BuildRequires: scim-devel >= 1.4.6
%if %build_qt
BuildRequires: qt4-devel
BuildRequires: qt3-devel
%endif
%if %snapshot
BuildRequires: automake, libtool
%endif
Requires: scim >= 1.4.6
Patch0: scim-bridge-0.4.15-fix-gdm.patch
Patch1: scim-bridge-0.4.15-hotkey-help.patch
Patch2: scim-bridge-0.4.15-bz461373.patch
Patch3: scim-bridge-0.4.15-EOF.patch
Patch4: scim-bridge-0.4.16-fix-gtk-key-snooper.patch
Patch5: scim-bridge-0.4.16-fixes-null-imengine.patch
Patch6: scim-bridge-0.4.16-fixes-unistd-compile.patch

%description
SCIM Bridge is a C implementation of a Gtk IM module for SCIM.

%package gtk
Summary: SCIM Bridge Gtk IM module
Group: System/Libraries
# for update-gtk-immodules
Requires(post): gtk2 >= 2.9.1-2
Requires(postun): gtk2 >= 2.9.1-2
# need %_bindir/scim-bridge
Requires: %name = %version-%release
Obsoletes: scim-bridge-gtkimm < 0.4.2

%description gtk
This package provides the SCIM Bridge GTK input method module.

%if %build_qt
%package qt
Summary: SCIM Bridge Qt4 IM module
Group: System/Libraries
# need %_bindir/scim-bridge
Requires: %name = %version-%release

Obsoletes: scim-bridge-qtimm < 0.4.2
Obsoletes: scim-bridge-qt4 < 0.4.15-3

%description qt
This package provides the SCIM Bridge Qt4 input method module.

%package qt3
Summary: SCIM Bridge Qt3 IM module
Group: System/Libraries
Requires: %name = %version-%release

Obsoletes: scim-bridge-qtimm < 0.4.2
Obsoletes: scim-bridge-qt < 0.4.15-3
Provides: scim-qtimm
Obsoletes: scim-qtimm

%description qt3
This package provides the SCIM Bridge Qt3 input method module.

%endif

%prep
%setup
%patch0 -p1 -b .0-fix-gdm
%patch1 -p1 -b .1-hotkey-help
%patch2 -p1 -b .2-bz461373
%patch3 -p1 -b .3-EOF
pushd client-gtk
%patch4 -p0 -b .snooper
popd
%patch5 -p1 -b .null
%patch6 -p1 -b .unistd

%if %snapshot
mkdir m4
./bootstrap
%endif

%build
autoconf
%configure --disable-static --disable-documents \
%if !%build_qt
  --disable-qt3-immodule \
  --disable-qt4-immodule
%else
  --enable-qt3-immodule \
  --enable-qt4-immodule
%endif

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/%_libdir/gtk-2.0/immodules/im-scim-bridge.*a
%if %build_qt
rm $RPM_BUILD_ROOT/%_libdir/qt3/plugins/inputmethods/im-scim-bridge.*a
rm $RPM_BUILD_ROOT/%_libdir/qt4/plugins/inputmethods/im-scim-bridge.*a
%endif

# remove unnecessary doc files
rm doc/{Makefile.*,doxygen.conf}


%post gtk
%_bindir/gtk-query-immodules-2.0 > %_sysconfdir/gtk-2.0/gtk.immodules

%postun gtk
[ "$1" = 0 ] && \
%_bindir/gtk-query-immodules-2.0 > %_sysconfdir/gtk-2.0/gtk.immodules



%files
%doc AUTHORS COPYING doc
%_bindir/scim-bridge

%files gtk
%_libdir/gtk-2.0/immodules/im-scim-bridge.so

%if %build_qt
%files qt
%_libdir/qt4/plugins/inputmethods/*.so

%files qt3
%_libdir/qt3/plugins/inputmethods/*.so

%endif

%changelog
* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.4.16-alt1
- build for Sisyphus

* Mon Aug 26 2013 Jon Ciesla <limburgher@gmail.com> - 0.4.16-17
- libmng rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Peng Wu <pwu@redhat.com> - 0.4.16-15
- Fixes aarch64 build

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.4.16-13
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.4.16-12
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 02 2012  Peng Wu <pwu@redhat.com> - 0.4.16-10
- Add patch scim-bridge-0.4.16-fixes-unistd-compile.patch,
  to fix Fedora 17 compile

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-9
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.16-7
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 22 2010  Peng Wu <pwu@redhat.com> - 0.4.16-5
- Add a patch scim-bridge-0.4.16-fixes-null-imengine.patch,
  Resolves: bug 584462 - [abrt] crash in scim-bridge-0.4.16-4.fc13: Process /usr/bin/scim-bridge was killed by signal 11 (SIGSEGV).

* Fri Feb 12 2010 Peng Wu <pwu@redhat.com> - 0.4.16-4
- Add a patch scim-bridge-0.4.16-fix-gtk-key-snooper.patch,
  Resolves: bug 554025 (Text input in firefox becomes increasingly sluggish)

* Wed Feb 10 2010 Peng Wu <pwu@redhat.com> - 0.4.16-3
- Obsoletes scim-qtimm package.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May  2 2009 Jens Petersen <petersen@redhat.com> - 0.4.16-1
- update to 0.4.16
- recreate scim-bridge-0.4.15-hotkey-help.patch

* Tue Mar 03 2009 Caolán McNamara <caolanm@redhat.com> - 0.4.15.2-3
- use -1 instead of EOF for ret of getopt_long

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Jens Petersen <petersen@redhat.com> - 0.4.15.2-1
- update to 0.4.15.2 release
- update scim-bridge-0.4.15-bz461373.patch and
  scim-bridge-0.4.15-hotkey-help.patch

* Sun Sep 28 2008 Huang Peng <phuang@redhat.com> - 0.4.15-8
- Change release version to 8 for rebuilding rpms.

* Tue Sep 16 2008 Huang Peng <phuang@redhat.com> - 0.4.15-7
- Resolves: bug 461373 (Focus switch causes selected text to be deleted)

* Mon Apr 21 2008 Caius Chance <cchance@redhat.com> - 0.4.15-6
- Resolves: rhbz#199389 (Add global hotkey list in help window.)

* Thu Apr 03 2008 Huang Peng <phuang@redhat.com> -0.4.15-5
- Updated Obsoletes in spec file to fix some potential problems.

* Thu Apr 03 2008 Huang Peng <phuang@redhat.com> -0.4.15-4
- Add Obsoletes for resolving yum update problem.

* Wed Apr 02 2008 Huang Peng <phuang@redhat.com> -0.4.15-3
- Rename scim-bridge-qt to scim-bridge-qt3 and
  rename scim-bridge-qt4 to scim-bridge-qt to fix bug 440174.

* Fri Mar 07 2008 Caius Chance <cchance@redhat.com> - 0.4.15-2
- Resolves: rhbz#199389 (Add global hotkey list in help window.)

* Tue Mar 04 2008 Huang Peng <phuang@redhat.com> - 0.4.15-1
- Update to 0.4.15.
- Let scim-bridge gtkim context can work with gtkplug widget #251787.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.14-2
- Autorebuild for GCC 4.3

* Sun Dec 23 2007 Huang Peng <phuang@redhat.com> - 0.4.14-1
- Update to 0.4.14.

* Thu Dec 06 2007 Huang Peng <phuang@redhat.com> - 0.4.13-6
- Recreate scim-bridge-0.4.13-fix-undefined-symbol.patch.

* Thu Dec 06 2007 Huang Peng <phuang@redhat.com> - 0.4.13-5
- Backport upstream's patch to fix bug 412591

* Mon Aug 27 2007 Jens Petersen <petersen@redhat.com> - 0.4.13-4
- license is dual GPL and LGPL
- gtk-2.0/immodules is now owned by gtk2

* Wed Aug 22 2007 Huang Peng <phuang@redhat.com> - 0.4.13-3
- Update rpm License field to GPLv2+ and LGPLv2+

* Tue Aug  7 2007 Huang Peng <phuang@redhat.com> - 0.4.13-2
- setlocale in scim-agent to fix bug (#242864)

* Mon Jul  2 2007 Huang Peng <phuang@redhat.com> - 0.4.13-1
- Update to 0.4.13

* Wed Jun  6 2007 Huang Peng <phuang@redhat.com> - 0.4.12-3
- Do not fall back for some key events to fix a bug (#209626)

* Mon Jun  4 2007 Jens Petersen <petersen@redhat.com> - 0.4.12-2
- update scim requires and buildrequires to 1.4.6

* Mon May 21 2007 Jens Petersen <petersen@redhat.com> - 0.4.12-1
- update to 0.4.12

* Mon Feb 26 2007 Jens Petersen <petersen@redhat.com> - 0.4.10-1
- update to 0.4.10 (fixes #222633, #228947)

* Tue Feb 13 2007 Jens Petersen <petersen@redhat.com> - 0.4.9-2
- remove xinput files since scim xinput file now checks for scim-bridge

* Tue Jan  2 2007 Jens Petersen <petersen@redhat.com> - 0.4.9-1
- update to 0.4.9
  - fixes hanging agent processes (#210772)
  - fixes movement of preedit with clicking (#217329)
  - no longer need scim-bridge-0.4.8-qt-moc-path.patch and
    scim-bridge-0.4.8-tests-dir-missing.patch
- protect update-gtk-immodules in %%post and %%postun

* Thu Nov 23 2006 Jens Petersen <petersen@redhat.com> - 0.4.8-1
- update to 0.4.8
- add scim-bridge-0.4.8-qt-moc-path.patch to set full path to moc
  and  scim-bridge-0.4.8-tests-dir-missing.patch to allow rebootstrap

* Mon Oct 23 2006 Jens Petersen <petersen@redhat.com> - 0.4.7-1
- update to 0.4.7 release
  - fixes underline in preedit for Hangul (#208921)
  - fixes crash with long input with Chewing (#209573)
- build qtimm again

* Thu Oct 19 2006 Jens Petersen <petersen@redhat.com> - 0.4.6-1
- as of 0.4.6 now dual GPL/LGPL license
- update to latest cvs (fixes #208921, #209573)
- scim-bridge-0.4.5-key-event-order-206261.patch no longer needed

* Fri Sep 29 2006 Jens Petersen <petersen@redhat.com> - 0.4.5-3
- add scim-bridge-0.4.5-key-event-order-206261.patch from cvs to fix modifiers
  problem with scim-sinhala (Ryo Dairiki, #206261)
- make im module subpackages require scim-bridge = ver-rel instead of
  /usr/bin/scim-bridge (#207872)

* Tue Sep 19 2006 Jens Petersen <petersen@redhat.com> - 0.4.5-2
- turn off qtimm by default with build switch (#207076)

* Mon Sep 18 2006 Jens Petersen <petersen@redhat.com> - 0.4.5-1
- update to 0.4.5 bugfix release (#205098, #205699)
- remove dist tag from scim requires (#204154)

* Fri Sep  1 2006 Jens Petersen <petersen@redhat.com> - 0.4.2-1
- update to 0.4.2 release (fixes #204657, #204337)
- rename gtkimm and qtimm subpackages to gtk and qt respectively
- move gtkimm xinput.d script to gtk subpackage
- add qtimm xinput.d script to qt subpackage
- require scim >= 1.4.4-33.fc6

* Mon Aug 28 2006 Jens Petersen <petersen@redhat.com> - 0.4.1-1
- update to 0.4.1 stable release (fixes #204118)

* Wed Aug 23 2006 Jens Petersen <petersen@redhat.com> - 0.3.1-1
- update to 0.3.1 release
- buildrequire qt-devel
- disable building oxygen source documentation for now
- include html docs

* Fri Aug 18 2006 Jens Petersen <petersen@redhat.com> - 0.2.9-1
- 0.2.9 bugfix release

* Mon Jul 31 2006 Jens Petersen <petersen@redhat.com> - 0.2.7-1
- 0.2.7 bugfix release
- update url

* Mon Jul 24 2006 Jens Petersen <petersen@redhat.com> - 0.2.6-1
- 0.2.6 bugfix release
- require scim >= 1.4.4-25.fc6

* Mon Jul 24 2006 Jens Petersen <petersen@redhat.com> - 0.2.5-1
- 0.2.5 bugfix release
- define _xinputdir and move xinput file to aux subdir

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.2.4-1.1
- rebuild

* Fri Jul  7 2006 Jens Petersen <petersen@redhat.com> - 0.2.4-1
- 0.2.4, fixes activating with different IME from menu (#197658)

* Fri Jul  7 2006 Jens Petersen <petersen@redhat.com> - 0.2.3-2
- update with fixes from cvs (#197719)
- fix input state caching across desktop sessions (Ryo Dairiki, #197775)

* Sat Jul 01 2006 Warren Togami <wtogami@redhat.com> - 0.2.3-1
- 0.2.3

* Fri Jun 23 2006 Jens Petersen <petersen@redhat.com> - 0.2.2-1
- update to 0.2.2 (also fixes #194445)

* Wed Jun 21 2006 Jens Petersen <petersen@redhat.com> - 0.2.1-2
- update to cvs snapshot
- prereq gtk2 >= 2.9.1-2 for new gtk.immodules path on i386

* Mon Jun 19 2006 Jens Petersen <petersen@redhat.com> - 0.2.1-1
- 0.2.1 release
- scim-bridge-0.2.0-agent-fixes.patch no longer needed

* Fri Jun 16 2006 Jens Petersen <petersen@redhat.com> - 0.2.0-1.1
- update to 0.2.0
- add scim-bridge-0.2.0-agent-fixes.patch from cvs to fix trigger event
  handling and config reload problems (Ryo Dairiki)

* Thu Jun 15 2006 Jens Petersen <petersen@redhat.com> - 0.1.12-3
- use _host not _target_platform for update-gtk-immodules in scripts (#195343)

* Wed Jun  7 2006 Jens Petersen <petersen@redhat.com> - 0.1.12-2
- import into Core (#194202)

* Tue May 30 2006 Jens Petersen <petersen@redhat.com> - 0.1.12-1
- update to 0.1.12

* Tue May 16 2006 Jens Petersen <petersen@redhat.com> - 0.1.8-1
- update to 0.1.8

* Thu May 11 2006 Jens Petersen <petersen@redhat.com> - 0.1.7-1
- update to 0.1.7 release

* Sat Apr 29 2006 Jens Petersen <petersen@redhat.com>
- package for Fedora Extras (#190243)

* Wed Mar 15 2006 Jens Petersen <petersen@redhat.com>
- cvs snapshot
