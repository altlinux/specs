Name: scim-hangul
Version: 0.3.2
Release: alt1

License: GPLv3
Url: http://www.scim-im.org/
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: scim-devel >= 1.2.0 libhangul-devel gcc-c++
Source0: http://downloads.sourceforge.net/scim/%name-%version.tar.gz
Patch0: scim-hangul-0.3.2.gcc43.patch

Summary: Hangul Input Method Engine for SCIM
Group: System/Libraries
Requires: scim
Obsoletes: iiimf-le-hangul <= 1:12.2
%description
Scim-hangul is a SCIM IMEngine module for Korean (Hangul) input support.

%prep
%setup -q -n %name-%version
%patch0 -p1 -b .gcc43

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm $RPM_BUILD_ROOT%_libdir/scim-1.0/*/{IMEngine,SetupUI}/hangul*.la

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING README ChangeLog
%_libdir/scim-1.0/*/IMEngine/hangul.so
%_libdir/scim-1.0/*/SetupUI/hangul-imengine-setup.so
%_datadir/scim/icons/scim-hangul.png
%_datadir/scim/hangul

%changelog
* Sun Jan 02 2011 Ilya Mashkin <oddity@altlinux.ru> 0.3.2-alt1
- Build for ALT Linux

* Tue Dec  2 2008 Jens Petersen <petersen@redhat.com> - 0.3.2-5
- own datadir/scim/hangul (#473663)

* Mon Mar 03 2008 Hu Zheng <zhu@redhat.com> - 0.3.2-4
- ppc64 build fix.

* Mon Feb 25 2008 Hu Zheng <zhu@redhat.com> - 0.3.2-3
- Gcc4.3 compile fix.

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.2-2
- Autorebuild for GCC 4.3

* Tue Jan 8 2008 Hu Zheng <zhu@redhat.com> - 0.3.2-1
- New upstream release.

* Wed Mar 22 2007 Akira TAGOH <tagoh@redhat.com> - 0.3.1-1
- New upstream release.
  - remove the unnecessary patches:
    - scim-hangul-0.2.2-help.patch
    - scim-hangul-0.2.2-ascii-mode.patch
    - scim-hangul-0.2.2-swap-keybinding.patch
    - scim-hangul-update-caret.patch

* Tue Feb  6 2007 Akira TAGOH <tagoh@redhat.com> - 0.2.2-8
- cleanups for mass package review. (#226393)

* Tue Aug 29 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-7
- scim-hangul-update-caret.patch: backported from CVS to update the caret.
  (#198721)

* Tue Jul 25 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-6
- scim-hangul-0.2.2-swap-keybinding.patch: swap the keybindings to move
  the cursor on the candidate window according to the candidate window's
  orientation.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.2.2-5.1
- rebuild

* Wed Jul  5 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-5
- add a keybindings documentation into the online help. (#186884)
- use dist tag.

* Fri Jun  9 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-4
- gettextized the input layout string on panel. (#194444)

* Wed May 17 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-3
- scim-hangul-0.2.2-ascii-mode.patch: applied to support the ASCII input mode
  in scim-hangul. (#185506)

* Fri Mar 31 2006 Jens Petersen <petersen@redhat.com> - 0.2.2-2.fc6
- rebuild without libstdc++so7

* Thu Mar 30 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-1
- New upstream release.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.2.1-3.fc5.1
- bump again for double-long bug on ppc(64)

* Thu Feb  9 2006 Jens Petersen <petersen@redhat.com> - 0.2.1-3
- build conditionally with libstdc++so7 preview library (#166041)
  - add with_libstdc_preview switch and tweak libtool to link against newer lib
- update filelist since moduledir is now api-versioned

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 14 2005 Akira TAGOH <tagoh@redhat.com> - 0.2.1-2
- added Obsoletes: iiimf-le-hangul <= 12.2 to ensure the upgrade path.

* Mon Oct 31 2005 Akira TAGOH <tagoh@redhat.com> - 0.2.1-1
- New upstream release.
- scim-hangul-0.2.0-ignore-invisible-char.patch: removed.

* Thu Oct  6 2005 Jens Petersen <petersen@redhat.com> - 0.2.0-6
- require scim

* Thu Aug 25 2005 Akira TAGOH <tagoh@redhat.com> - 0.2.0-5
- fixed the description of this package. (Ryo Dairiki)
- scim-hangul-0.2.0-ignore-invisible-char.patch: applied to not commit any
  Hangul characters with the keys unrelated to Yetgeul. (#166138)

* Tue Aug 16 2005 Akira TAGOH <tagoh@redhat.com> - 0.2.0-4
- Rebuild.

* Fri Aug  5 2005 Warren Togami <wtogami@redhat.com> - 0.2.0-3
- minor spec cleanup

* Thu Aug  4 2005 Akira TAGOH <tagoh@redhat.com> - 0.2.0-2
- Import into Core.
- clean up the spec.

* Sun Jun 13 2004 James Su <suzhe@tsinghua.org.cn>
- first release of scim-uim.

