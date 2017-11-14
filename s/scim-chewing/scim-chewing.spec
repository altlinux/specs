# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           scim-chewing
Version:        0.3.5
Release:        alt1.qa1_11
Summary:        Chewing Chinese input method for SCIM

License:        GPLv2+
Url:            http://chewing.csie.net/
Group:          System/Libraries
Source:         http://chewing.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0:         scim-chewing-0.3.5-libchewing04.patch

BuildRequires:  scim-devel, libchewing-devel >= 0.3.4 gettext gettext-tools, intltool >= 0.34
BuildRequires:  libtool
Requires:       scim
Source44: import.info

%description
This package provides Chewing Chinese input method for SCIM. 


%prep
%setup -q
%patch0 -p1

%build
autoreconf -ivf
intltoolize --force
autoreconf

%configure --disable-static
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS COPYING
%{_libdir}/scim-1.0/*/SetupUI/chewing-imengine-setup.so
%{_libdir}/scim-1.0/*/IMEngine/chewing.so
%{_datadir}/scim/icons/scim-chewing.png
%{_datadir}/scim/icons/scim-chewing-swap-colors.png


%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1.qa1_11
- NMU (for oddity@): new version by fcimport

* Sat Oct 17 2015 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.3.5-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.


* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Dec 19 2010 Ilya Mashkin <oddity@altlinux.ru> 0.3.3-alt1
- Build for ALT Linux

* Thu Dec 11 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.3-0
- Upstream update.

* Tue Nov 11 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-1
- Upstream update.

* Wed Sep 17 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.1.901-0
- Upstream update.

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.1-16
- fix license tag

* Wed Apr 09 2008 Caius Chance <cchance@redhat.com> 0.3.1-15.fc10
- Resolves: rhbz#195416 (Initial input mode configuration.)
- Modified patch naming in .spec file.

* Tue Apr 08 2008 Caius Chance <cchance@redhat.com> 0.3.1-14.fc9
- Resolves: rhbz#228428 (Ctrl-v during preedit appears in buffer on Qt XIM.)

* Wed Jan 13 2008 Caius Chance <cchance@redhat.com> 0.3.1-13.fc9
- Rebuild for F9.

* Tue Jan 08 2008 Caius Chance <cchance@redhat.com> 0.3.1-12.fc9
- Updated buildrequires version of libchewing-devel to 0.3.0-9.

* Tue Jan 08 2008 Caius Chance <cchance@redhat.com> 0.3.1-11.fc9
- Resolves: rhbz#200694 (Moving "Han-Yin" <-> Zhu-Yin" option to AUX UI.)

* Wed Dec 20 2007 Caius Chance <cchance@redhat.com> 0.3.1-10.fc9
- Resolves: rhbz#237924 (Last candidate on lookup table is not a valid
                         candidate.)
  <<< Refit lookup table page size for last lookup page.

* Wed Jul  4 2007 Jens Petersen <petersen@redhat.com>
- remove with_libstdc_preview macro

* Tue Nov 21 2006 Caius Chance <cchance@redhat.com> - 0.3.1-9.fc7
- Fixed bz#216851 : ported following bugfix to rawhide:
  (bz#216377: PageUp/PageDown doesn't work when Chewing is activated.)

* Wed Nov 08 2006 Caius Chance <cchance@redhat.com> - 0.3.1-8.fc7
- Fixed bz#206120 : gedit crashes when select-all with preedit exists.

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 0.3.1-7
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Caius Chance <cchance@redhat.com> - 0.3.1-6.fc6
- Fixed bz#206112 : Esc key to clean all buffer could't be disabled.

* Fri Sep 15 2006 Caius Chance <cchance@redhat.com> - 0.3.1-5_fc6
- Fixed bz#206125 : scim-chewing: Trigger keys setting isn't correct

* Mon Sep 04 2006 Caius Chance <cchance@redhat.com> - 0.3.1-4_fc6
- Fixed bz#197556 : pre-edit buffer for chewing is not reset after
  deactivation.

* Thu Aug 17 2006 Caius Chance <cchance@redhat.com> - 0.3.1-3
- remove patch of 0.3.1-2 as bug# 191957 is not reproduceable

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3.1-2.1
- rebuild

* Mon Jun 26 2006 Darshan Santani <dsantani@redhat.com> - 0.3.1-2
- Add scim-chewing-LTC23919-191957.patch (Shoji Sugiyama [IBM Japan], #191957)

* Fri Jun 16 2006 Darshan Santani <dsantani@redhat.com>
- Update to 0.3.1
- Changed BuildRequires to include intltool

* Tue Jun 06 2006 Darshan Santani <dsantani@redhat.com>
- Changed the BuildRequires to include gettext
- Rebuild

* Tue May 23 2006 Darshan Santani <dsantani@redhat.com>
- Revised the version number
- Rebuild

* Mon May 22 2006 Darshan Santani <dsantani@redhat.com>
- New source tarball added.
- Rebuild.

* Fri Mar 31 2006 Jens Petersen <petersen@redhat.com> - 0.2.1-6
- rebuild without libstdc++so7

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.2.1-5.1
- bump again for double-long bug on ppc(64)

* Thu Feb  9 2006 Jens Petersen <petersen@redhat.com> - 0.2.1-5
- build conditionally with libstdc++so7 preview library (#166041)
- add with_libstdc_preview switch and tweak libtool to link against newer lib
- update filelist since module dir is now api-versioned

* Fri Dec 16 2005 Jens Petersen <petersen@redhat.com> - 0.2.1-4
- rebuild with gcc-4.1

* Mon Nov 14 2005 Jens Petersen <petersen@redhat.com> - 0.2.1-3
- obsoletes iiimf-le-xcin for upgrades (#173071)

* Thu Oct  6 2005 Jens Petersen <petersen@redhat.com> - 0.2.1-2
- require scim explicitly

* Tue Aug 16 2005 Jens Petersen <petersen@redhat.com> - 0.2.1-1
- initial build for Fedora Core
- version 0.2.1 buildrequires libchewing 0.2.7 or later
- spec file cleanup

* Mon Jun 20 2005 Jens Petersen <petersen@redhat.com> - 0.2.0-2
- rebuild against scim-1.3.1

* Tue Jun 14 2005 Jens Petersen <petersen@redhat.com> - 0.2.0-1
- initial build
