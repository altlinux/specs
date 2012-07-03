Name: libchewing
Version: 0.3.2
Release: alt1.1
Summary: Intelligent phonetic input method library for Traditional Chinese

Group: System/Libraries
License: LGPLv2+
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://chewing.csie.net/
Source: http://chewing.csie.net/download/libchewing/%name-%version.tar.bz2
#Patch0: libchewing-0.3.0-3.bz199353.patch
#Patch1: libchewing-0.3.0-4.bz206232.patch
#Patch2: libchewing-0.3.0-5.bz216581a.patch
#Patch3: libchewing-0.3.0-5.bz216581b.patch
#Patch4: libchewing-0.3.0-6.bz231568.patch
#Patch5: libchewing-0.3.0-7.bz237233.patch
#Patch6: libchewing-0.3.0-8.bz237916.patch
#Patch7: libchewing-0.3.0-9.bz200694.patch
#Patch8: libchewing-0.3.0-11.bz195416.patch
Patch9: libchewing-0.3.2.bz477690.patch
Patch10: libchewing-0.3.2.phraseChoiceRearward.2.patch
Patch11: libchewing-0.3.2.chewing_zuin.patch
Patch12: libchewing-0.3.2.hsu.patch
Patch13: libchewing-0.3.2.hsu.2.patch
# Rhbz#625980
Patch14: libchewing-0.3.2.align.patch

%{!?python_sitearch: %define python_sitearch %(%__python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define libchewing_python_dir %python_sitearch/%name

BuildRequires: autoconf automake libtool pkgconfig

%description
libchewing is an intelligent phonetic input method library for Chinese.

It provides the core algorithm and logic that can be used by various
input methods.  The Chewing input method is a smart bopomofo phonetics
input method that is useful for inputting Mandarin Chinese.


%package -n %name-devel
Summary: Development files for libchewing
Group: Development/Other
Requires: %name = %version-%release, pkgconfig

%description -n %name-devel
Headers and other files needed to develop applications using the %name
library.


%package -n  python-module-chewing
Summary: libchewing python binding
Group: Development/Other
BuildRequires: python-devel
Requires: %name = %version-%release
Requires: python

%description -n  python-module-chewing
Python binding of libchewing.


%prep
%setup -q
#%patch0 -p1 -b .1-bz199353
#%patch1 -p1 -b .2-bz206232
#%patch2 -p1 -b .3-bz216581a
#%patch3 -p1 -b .4-bz216581b
#%patch4 -p1 -b .5-bz231568
#%patch5 -p1 -b .6-bz237233
#%patch6 -p1 -b .7-bz237916
#%patch7 -p1 -b .8-bz200694
#%patch8 -p1 -b .9-bz195416
%patch9 -p0 -b .bz477690
%patch10 -p0 -b .phraseChoiceRearward
%patch11 -p0 -b .chewing_zuin
%patch12 -p0 -b .hsu
%patch13 -p0 -b .hsu.2
%patch14 -p0 -b .align

%build
export CFLAGS=-DLIBINSTDIR='\"%_libdir\" -g'
autoreconf -ivf
%configure --disable-static
%__make RPM_CFLAGS="%optflags" %_smp_mflags

%install

%__make DESTDIR=%buildroot install
%__rm $RPM_BUILD_ROOT%_libdir/libchewing.la
%__mkdir -p $RPM_BUILD_ROOT%libchewing_python_dir
%__cp python/chewing.py $RPM_BUILD_ROOT%libchewing_python_dir
%__mkdir -p $RPM_BUILD_ROOT%_libdir/chewing
%__cp data/fonetree.dat $RPM_BUILD_ROOT%_libdir/chewing
touch $RPM_BUILD_ROOT%libchewing_python_dir/__init__.py


%files
%doc README AUTHORS COPYING
%dir %_datadir/chewing
%_datadir/chewing/*
%_libdir/*.so.*
%_libdir/chewing

%files devel
%dir %_includedir/chewing
%_includedir/chewing/*
%_libdir/pkgconfig/chewing.pc
%_libdir/*.so

%files -n python-module-chewing
%libchewing_python_dir

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt1.1
- Rebuild with Python-2.7

* Sun Dec 19 2010 Ilya Mashkin <oddity@altlinux.ru> 0.3.2-alt1
- Build for ALT Linux

* Thu Sep 02 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-28
- Resolves: #625980
  Add padding to wch_t to ensure it's word aligned.

* Wed Mar 04 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-27
- Fix Dvorak Hsu 4th tone key (ibus google issue 755 comment 12,
  chewing google issue 10)
- Resolves: #555192

* Mon Feb 15 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-24
- Fix Hsu and Dvorak Hsu input (ibus google issue 755,
  chewing google issue 10)
- Resolves: #555192

* Mon Feb 15 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-23
- Fix Hsu and Dvorak Hsu input (ibus google issue 755,
  chewing google issue 10)
- Resolves: #555192

* Wed Feb 10 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-22
- Fix Hsu and Dvorak Hsu input (ibus google issue 755)
- Resolves: #555192

* Tue Feb 02 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-21
- Revised phrase choice from rear logic.
  Thus update phraseChoiceRearward.patch as phraseChoiceRearward.2.patch
- Resolves: #555192

* Fri Jan 21 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-20
- Resolves: #555192
- Fix for package wrangler.

* Tue Jan 19 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-18
- Resolves: #555192
- Fix for package wrangler.

* Tue Jan 05 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-17
- Add zh_TW summary and description
- Split out python binding into a subpackage.
- Fix for package wrangler.

* Wed Sep 30 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-16
- Fix chewing Google issue 352:
  zuin_count in chewing_zuin_String( ChewingContext *ctx, int *zuin_count )
  does not count correctly.

* Mon Aug 03 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-15
- Fix [Bug 512108:issue 11] ibus-chewing crash the application
  by move cursor_orig to chewingio.c global.

* Thu Jul 30 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-14
- Fix [Bug 512108] ibus-chewing crash the application

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-12
- Rebuild to correct tags.

* Fri Jun 26 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-11
- Revise phraseChoiceRearward.patch so the cursor won't move to left
  when repeatly press down key.

* Wed May 20 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-10
- Need autoreconf and BuildRequires: pkgconfig to make changes in
  Makefile.am effective, thus actually fix [Bug 477960] libchewing multilib conflict.

* Mon May 18 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-9
- Possible Fix of Bug 501220 - RFE: edit last preedit character from end of line
  Chewing upstream does not handle if phrase choice rearward is enabled.

* Wed Apr 22 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-8
- Fix [Bug 496968] - libchewing-debuginfo does not contain sources.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-6
- Fix [Bug 486409] - Wrong python binding installed path
  Add BuildRequires:  python-devel

* Wed Feb 18 2009 Adam Jackson <ajax@redhat.com> 0.3.2-5
- Rerun autotools so changes to Makefile.am actually take effect.

* Fri Jan 23 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-4
- touch python-<ver>/site-packages/libchewing/__init__.py,
  So python thinks libchewing is a library.

* Thu Jan 14 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-3
- Add python binding by copy python/chewing.py to
  <python_dir>/site_packages/libchewing

* Tue Dec 23 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-2
- [Bug 477690] libchewing multilib conflict
  Move /usr/share/chewing/fonetree.dat to corresponding libdir.

* Wed Dec 03 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-0
- Upstream update to 0.3.2.

* Wed Oct 08 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.1-0
- Upstream update.

* Wed Sep 17 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.0.901-0
- Upstream update.

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.0-12
- fix license tag

* Tue Apr 22 2008 Caius Chance <cchance@redhat.com> - 0.3.0-11.fc10
- Resolves: rhbz195416 (Initial input mode between Chinese and English.)

* Wed Feb 13 2008 Caius Chance <cchance@redhat.com> - 0.3.0-10.fc9
- Rebuild for F9.

* Tue Jan 08 2008 Caius Chance <cchance@redhat.com> - 0.3.0-9.devel
- Resolves: rhbz#200694 (Moving "Han-Yin" <-> Zhu-Yin" option to AUX UI.)

* Fri Jun 01 2007 Caius Chance <cchance@redhat.com> - 0.3.0-8.devel
- Fixed bz#237916: [chewing] Candidate list (symbol) page change inaccracy.

* Fri Apr 20 2007 Caius Chance <cchance@redhat.com> - 0.3.0-7.fc7
- Fixed bz#237233: Up arrow on candidate list doesn't work.

* Fri Mar 09 2007 Caius Chance <cchance@redhat.com> - 0.3.0-6.devel
- Fixed bz231568: [chewing] Look up table is showing candidates of previous
  look-up.

* Tue Nov 21 2006 Caius Chance <cchance@redhat.com> - 0.3.0-5.fc7
- Fixed bz#216581: Ported the following bugfix:
- (bz#216337: Page Up / Page Down key doesn't when Chewing is activated.)
- (bz#209575: preedit buffer is not cleared when framework calls for
  instance reset.)

* Fri Sep 15 2006 Caius Chance <cchance@redhat.com> - 0.3.0-4.fc6
- Fixed bz#206232 - Shift_L + space doesn't work correctly

* Mon Sep 04 2006 Caius Chance <cchance@redhat.com> - 0.3.0-3.fc6
- Fixed bz#199353 - scim-chewing hangs for commit > 6 characters

* Wed Jul 19 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-2
- fix release

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-1.2.1.1
- rebuild

* Mon May 22 2006 Darshan Santani <dsantani@redhat.com>
- New source tarball added.
- Rebuild.

* Thu May 18 2006 Jens Petersen <petersen@redhat.com>
- configure with --disable-static
- exclude INSTALL from docs

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.2.7-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.2.7-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Aug 16 2005 Jens Petersen <petersen@redhat.com> - 0.2.7-1
- Initial build for Fedora Core
- cleanup spec file according to Fedora standard

* Fri Dec 31 2004 rabit <rabit@ipserv.org> 0.2.5-fc3
- update for 0.2.5. and fedora core 3

* Thu Oct 8 2004 rabit <rabit@ipserv.org> 0.2.4-fc2
- update for 0.2.4.

* Thu Oct 7 2004 rabit <rabit@ipserv.org> 0.2.3-fc2
- Initial build.
