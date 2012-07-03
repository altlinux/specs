Name: kasumi
Version: 2.5
Release: alt1

License: GPLv2+
Url: http://kasumi.sourceforge.jp/
Packager: Ilya Mashkin <oddity@altlinux.ru>
BuildRequires: libgtk+2-devel libanthy-devel gcc-c++
Source0: http://jaist.dl.sourceforge.jp/kasumi/41436/%name-%version.tar.gz

Summary: An anthy dictionary management tool
Group: Text tools
%description
Kasumi is a dictionary management tool for Anthy.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# remove .desktop file so that kasumi is accessible from scim panel/ibus panel and it's not necessary for other users.
rm -rf $RPM_BUILD_ROOT%_datadir/applications/*.desktop

%find_lang %name

%files -f %name.lang
%_bindir/kasumi
%_mandir/man1/kasumi.1*
%_datadir/pixmaps/kasumi.png
%doc AUTHORS COPYING ChangeLog NEWS README

%changelog
* Sun Dec 12 2010 Ilya Mashkin <oddity@altlinux.ru> 2.5-alt1
- Build for ALT Linux

* Tue Mar  9 2010 Akira TAGOH <tagoh@redhat.com> - 2.5-3
- Get rid of .desktop file again. (#546147)

* Mon Dec 21 2009 Akira TAGOH <tagoh@redhat.com> - 2.5-2
- improve the spec file (#546147)

* Mon Aug  3 2009 Akira TAGOH <tagoh@redhat.com> - 2.5-1
- New upstream release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Akira TAGOH <tagoh@redhat.com> - 2.4-1
- New upstream release.

* Tue Apr  8 2008 Akira TAGOH <tagoh@redhat.com> - 2.3-4
- Remove .desktop file since it's accessible from scim-panel and it's not
  necessarily used for every users, particularly on Live. (#439173)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3-3
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Akira TAGOH <tagoh@redhat.com> - 2.3-2
- kasumi-2.3-gcc43.patch: Fix build fails with gcc-4.3.

* Wed Oct 31 2007 Akira TAGOH <tagoh@redhat.com> - 2.3-1
- New upstream release.
- kasumi-2.2-fix-dict-breakage.patch: removed.

* Thu Aug 23 2007 Akira TAGOH <tagoh@redhat.com> - 2.2-6
- Rebuild

* Wed Aug  8 2007 Akira TAGOH <tagoh@redhat.com> - 2.2-4
- Update License tag.

* Thu Jun 14 2007 Akira TAGOH <tagoh@redhat.com> - 2.2-3
- kasumi-2.2-fix-dict-breakage.patch: patch from Debian to fix the dictionary
  breakage when adding words to the personal dictionary against the bugfix
  version of anthy that the version contains non-numeric characters.

* Wed Mar 28 2007 Akira TAGOH <tagoh@redhat.com> - 2.2-2
- Add X-GNOME-PersonalSettings to the category. (#234169)

* Fri Mar  2 2007 Akira TAGOH <tagoh@redhat.com> - 2.2-1
- Updated to 2.2
- Remove kasumi-2.0.1-errorcode.patch. no longer needed.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0.1-1.1
- rebuild

* Fri Jun 30 2006 Akira TAGOH <tagoh@redhat.com> - 2.0.1-1
- New upstream release.
- use dist tag.
- kasumi-2.0.1-errorcode.patch: fixed not working when the private dictionary is empty. (#197313)

* Wed Jun  7 2006 Akira TAGOH <tagoh@redhat.com> - 2.0-2
- added anthy-devel, automake and autoconf to BuildReq. (#194121)

* Tue May 30 2006 Akira TAGOH <tagoh@redhat.com> - 2.0-1
- New upstream release.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0-1.fc5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0-1.fc5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Dec 15 2005 Akira TAGOH <tagoh@redhat.com> - 1.0-1
- New upstream release.
- kasumi-1.0-gcc41.patch: build with -ffriend-injection to temporarily get it
  built with gcc-4.1.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Oct 13 2005 Akira TAGOH <tagoh@redhat.com> - 0.10-1
- New upstream release.

* Tue Aug 16 2005 Akira TAGOH <tagoh@redhat.com> - 0.9-3
- Rebuild

* Tue Aug  9 2005 Akira TAGOH <tagoh@redhat.com>
- added dist tag in Release.

* Fri Aug  5 2005 Akira TAGOH <tagoh@redhat.com> - 0.9-2
- Import into Core.
- clean up spec file.

* Wed Jun 29 2005 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.9-1
- Initial packaging for Fedora Extras

