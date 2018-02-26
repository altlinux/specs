Name:    specspo
Version: 10.07
Release: alt2

Summary: ALT Linux package descriptions, summaries, and groups.

Group:   System/Internationalization
License: GPL
BuildArch: noarch

BuildRequires: gettext
Conflicts: packages-info-i18n-common
Conflicts: packages-info-i18n-be
Conflicts: packages-info-i18n-ru
Conflicts: packages-info-i18n-uk

Source:  specspo-%{version}.tar.bz2

%description
The specspo package contains the portable object catalogues used to
internationalize ALT Linux packages.

%prep
%setup -q

%build
make

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/rpm
echo '%%_i18ndomains	altlinux-dist' > %{buildroot}%{_sysconfdir}/rpm/macros.specspo
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/specspo

%find_lang altlinux-dist

%files -f altlinux-dist.lang
%config(noreplace) %{_sysconfdir}/rpm/macros.specspo
%_sysconfdir/buildreqs/packages/ignore.d/specspo

%changelog
* Mon Aug 23 2010 Andrey Cherepanov <cas@altlinux.org> 10.07-alt2
- ignore specspo package for buildreq

* Fri Jul 16 2010 Andrey Cherepanov <cas@altlinux.org> 10.07-alt1
- backport from Fedora project, all packages-info-i18n* are deprecated
- fix package summary and description translation (closes: #23399)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 Stepan Kasal <skasal@redhat.com> - 16-1
- fix typo s/fromating/formatting/
- restore en_GB.po, which was replaced by es.po by mistake

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 15-2
- fix license tag

* Thu Oct  4 2007 Stepan Kasal <skasal@redhat.com> - 15-1
- Updated translations
- Fixed make_dist_pot, so that backslashes in the descriptions do not get
  mangled.
- Removed C.po, they do not contain any information; removed the code to handle
  them in the Makefile.
- Removed Makefile.rules, it is not used.

* Thu May 24 2007 Martin Bacovsky <mbacovsk@redhat.com> - 14-1
- Updated translations

* Thu Nov 30 2006 Martin Bacovsky <mbacovsk@redhat.com> 13-1
- Updated translations
- Resolves: #217856

* Tue Oct  3 2006 Martin Bacovsky <mbacovsky@redhat.com> 12-1
- New version of catalogues
- New translations
- Catalogue generator is now configurable

* Fri Jul 21 2006 Martin Bacovsky <mbacovsk@redhat.com> 11-1
- New version of catalogues

* Tue Jun 06 2006 Jesse Keating <jkeating@redhat.com> 10-2
- Added missing BR of gettext

* Thu Mar 02 2006 Bill Nottingham <notting@redhat.com> 10-1
- update

* Thu Jul 03 2003 Paul Gampe <pgampe@redhat.com> 9.0.92
- Update translations

* Tue Feb 25 2003 Paul Gampe <pgampe@redhat.com> 9.0-1
- Update translations

* Mon Feb 24 2003 Bill Nottingham <notting@redhat.com> 8.0.95-1
- bump

* Wed Feb 12 2003 Paul Gampe <pgampe@redhat.com> 8.0.94-2
- group spec and distribution list corrections

* Mon Feb 10 2003 Paul Gampe <pgampe@redhat.com> 8.0.94-1
- Bump

* Tue Dec 17 2002 Paul Gampe <pgampe@redhat.com> 8.0.92-1
- Bump

* Thu Sep  5 2002 Trond Eivind Glomsrød <teg@redhat.com> 8.0-3
- Bump

* Tue Sep  3 2002 Trond Eivind Glomsrød <teg@redhat.com> 8.0-2
- Bump

* Mon Sep  2 2002 Trond Eivind Glomsrød <teg@redhat.com> 8.0-1
- Update translations

* Wed Aug 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3.94-2
- Add new locales (#72106)

* Thu Aug  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3.93-3
- Update

* Thu Jul 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3.93-2
- Update - most po files are now UTF-8

* Wed Jul 24 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3.93-1
- Update

* Thu Jul 18 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3.92-3
- Update

* Fri Jul 12 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3.92-2
- Update

* Thu Jun 27 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3.92-1
- Update

* Wed Jun 12 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3.91-1
- Update

* Wed May 29 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3.90-1
- Update

* Thu Apr 18 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3-4
- Update translations

* Wed Apr 17 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3-3
- Update translations

* Tue Apr 16 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3-2
- Update translations

* Mon Apr 15 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.3-1
- Update translations

* Wed Apr 10 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.2.94-1
- Update translations, add jfsutils

* Wed Apr  3 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.2.93-3
- Update translations

* Thu Mar 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.2.93-2
- Update translations

* Wed Mar 27 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.2.93-1
- Update translations

* Tue Mar 19 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.2.92-3
- Updated translations

* Sat Mar 16 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.2.92-2
- Various fixes, corrections from docs

* Fri Mar 15 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.2.92-1
- Rebuild

* Thu Feb 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.2.91-1
- bump

* Fri Jan 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.2.90-1
- Rebuild

* Fri Jan 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 7.2-3
- Updated translations

* Wed Dec  5 2001 Trond Eivind Glomsrød <teg@redhat.com> 7.2-2
- Updated translations

* Wed Sep  5 2001 Trond Eivind Glomsrød <teg@redhat.com> 7.2-1
- Updated translations

* Mon Aug 27 2001 Trond Eivind Glomsrød <teg@redhat.com> 7.1.95-1
- Updated translations

* Fri Aug 24 2001 Trond Eivind Glomsrød <teg@redhat.com> 7.1.95-0.1
- Updated translations
- Include Danish

* Sat Aug 18 2001 Trond Eivind Glomsrød <teg@redhat.com> 7.1.94-2
- updated translations

* Sun Aug 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 7.1.94-1
- updated translations

* Fri Aug 10 2001 Trond Eivind Glomsrød <teg@redhat.com> 7.1.94-0.4
- Updated translations

* Thu Aug  9 2001 Trond Eivind Glomsrød <teg@redhat.com> 7.1.94-0.3
- s/X11R6-contrib/XFree86-tools/ (#51330)

* Wed Aug  8 2001 Trond Eivind Glomsrød <teg@redhat.com> 7.1.94-0.2
- add cyrus-sasl-md5

* Wed Aug  8 2001 Trond Eivind Glomsrød <teg@redhat.com> 7.1.94-0.1
- refresh-po

* Tue Jul 31 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new drop, new refresh-po

* Sun Jul 29 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Updated translations

* Fri Jul 27 2001 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild, safe iconv

* Thu Jul 26 2001 Trond Eivind Glomsrød <teg@redhat.com>
- add some missing applications

* Wed Jul 25 2001 Trond Eivind Glomsrød <teg@redhat.com>
- add some missing applications

* Tue Jul 24 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 7.1.93

* Fri Jul 20 2001 Trond Eivind Glomsrød <teg@redhat.com>
- update from CVS
- exclude powertools

* Mon May 21 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add some IA64-specific packages (#40710)

* Wed May  9 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add more languages

* Sat Apr  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Updated translations

* Mon Mar 26 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Updated translations

* Thu Mar 15 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Fixes to the Spanish translation (#30289)

* Tue Mar  6 2001 Nalin Dahyabhai <nalin@redhat.com>
- add msgid strings for openssl095a

* Fri Mar 02 2001 Trond Eivind Glomsrød <teg@redhat.com>
- fix some redundancies in the Spanish po file

* Wed Feb 28 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Added ddskk and ddskk-el
- Added tux and kdebindings-*

* Wed Feb 14 2001 Preston Brown <pbrown@redhat.com>
- merged translations for European languages.

* Thu Feb  8 2001 Matt Wilson <msw@redhat.com>
- updated from CVS

* Thu Jan 25 2001 Matt Wilson <msw@redhat.com>
- updated ja

* Tue Jan 23 2001 Matt Wilson <msw@redhat.com>
- updated de es it fr, updated C.po to current package set
- ran make update-po

* Mon Jan 22 2001 Preston Brown <pbrown@redhat.com>
- build for 7.1 Public Beta
- langify everything

* Thu Jan 11 2001 Jeff Johnson <jbj@redhat.com>
- build for 7.1
