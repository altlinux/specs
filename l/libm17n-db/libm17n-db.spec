Name: libm17n-db
Version: 1.6.2
Release: alt1

Summary: Multilingualization datafiles for m17n-lib

Group: System/Libraries
License: LGPL
Url: http://www.m17n.org/m17n-lib-en/index.html

Packager: Alexey Gladkov <legion@altlinux.ru>

# http://www.m17n.org/m17n-lib-download/m17n-db-%version.tar.bz2
Source: m17n-db-%version.tar
BuildArch: noarch

# Automatically added by buildreq on Sun Nov 12 2006
BuildRequires: glibc-i18ndata

%description
This package contains multilingualization (m17n) datafiles for m17n-lib
which describe input maps, encoding maps, and OpenType font data
for many languages.

%prep
%setup -q -n m17n-db-%version

%build
%configure --disable-rpath
%make

%install
%makeinstall

%files
%doc AUTHORS COPYING README
%_bindir/*
%_datadir/m17n

%changelog
* Sat Dec 18 2010 Alexey Gladkov <legion@altlinux.ru> 1.6.2-alt1
- New version (1.6.2).

* Mon Dec 28 2009 Alexey Gladkov <legion@altlinux.ru> 1.5.5-alt1
- new version (1.5.5).

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt0.1
- initial build for ALT Linux Sisyphus

* Tue Sep 12 2006 Mayank Jain <majain@redhat.com>
- Added key summary to te-inscript keymap

* Thu Sep 7 2006 Mayank Jain <majain@redhat.com>
- Updated keymaps for typo errors, updated copyright header in all keymaps with "This file is part of the m17n contrib; a sub-part of the m17n library"
- Added key summary for ta-tamil99 keymap
- updated key summary for bn-itrans.mim

* Wed Sep 6 2006 Mayank Jain <majain@redhat.com>
- Updated or-inscript.mim for bug 204726

* Wed Sep 6 2006 Mayank Jain <majain@redhat.com>
- Updated bn-probhat & as-phonetic keymaps with *=>ৎ
- Corrected date type in changelog

* Tue Sep 5 2006 Mayank Jain <majain@redhat.com>
- Updated as-phonetic with key summary

* Mon Sep 4 2006 Mayank Jain <majain@redhat.com>
- Added key summaries to pa-inscript/jhelum
- Fixed 204755

* Tue Aug 31 2006 Mayank Jain <majain@redhat.com>
- Added ur-phonetic icon
- Updated spec file to incorporate the icon

* Tue Aug 31 2006 Mayank Jain <majain@redhat.com>
- Updated bn-{inscript,probhat,itrans} for RH bug #204275
- Added ur-phonetic.mim file for RH bug #177372
- Updated m17n-db.spec file to incorporate Urdu keymap.

* Tue Aug 8 2006 Mayank Jain <majain@redhat.com>
- Updated bn-probhat.mim for RH bz #200890 ...weird... that previous update didnt showed up!
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=200890#c4

* Tue Aug 1 2006 Mayank Jain <majain@redhat.com>
- Corrected bn-probhat.mim file, RH bz #200890, added U+09CE

* Tue Aug 1 2006 Mayank Jain <majain@redhat.com>
- Corrected ml-inscript.mim file, RH bz #200876

* Tue Jul 25 2006 Jens Petersen <petersen@redhat.com> - 1.3.3-14
- move bopomofo to chinese subpackage

* Mon Jul 17 2006 Mayank Jain <majain@redhat.com> - 1.3.3-13
- Removed ta-typewriter.mim keymap as its not working
- Added ml-inscript.png
- Added hi-inscript.png
- added hi-remington.png

* Thu Jul 13 2006 Mayank Jain <majain@redhat.com>
- Added ta-typewriter.mim keymap

* Thu Jul 6 2006 Mayank Jain <majain@redhat.com>
- Added key summaries in various keymaps

* Thu Jun 29 2006 Mayank Jain <majain@redhat.com>
- Added hi-remington keymap - <rranjan@redhat.com>
- Added hi-remington.png - <aalam@redhat.com>

* Thu Jun 8 2006 Mayank Jain <majain@redhat.com>
- Added hi-typewriter keymap.

* Wed Jun 7 2006 Mayank Jain <majain@redhat.com>
- Added or-*.png icons.

* Mon Jun 5 2006 Mayank Jain <majain@redhat.com>
- Added as-*.png icons.

* Fri Jun 2 2006 Mayank Jain <majain@redhat.com>
- Added or-inscript keymap to the tarball
- Commented out as-*.png and or-*.png from the directives as respective .png files are missing from tarball.

* Fri Jun 2 2006 Mayank Jain <majain@redhat.com>
- Added modified as-phonetic.mim keymap, modified by <runab@redhat.com> for RH bz #193849

* Mon May 29 2006 Mayank Jain <majain@redhat.com>
- Added icon for marathi inscript - thanks to <aalam@redhat.com>

* Wed May 17 2006 Mayank Jain <majain@redhat.com>
- Added following keymaps
	- as-inscript.mim
	- as-phonetic.mim
	- mr-inscript.mim
	- ta-tamil99.mim

* Wed Mar 22 2006 Jens Petersen <petersen@redhat.com>
- fix language names in Indic .mim file headers (Naoto Takahashi)
- add make-dist script to m17n-db-indic

* Thu Mar  9 2006 Jens Petersen <petersen@redhat.com> - 1.3.3-2
- Bengali input maps fixes (runab)
  - map Probhat '*' key to an alternate sequence since glyph missing (#179821)
  - more itrans cleanup (#182227)
- add icon for Tamil99 (aalam)

* Thu Mar  2 2006 Jens Petersen <petersen@redhat.com> - 1.3.3-1
- update to 1.3.3 bugfix release
- fixes to Bengali, Hindi, and Punjabi maps (runab, aalam)
- Tamil phonetic map now works
- new Tamil99 Government Standard map (I Felix)

* Tue Feb 14 2006 Jens Petersen <petersen@redhat.com> - 1.3.2-2
- add Indian input maps ported from scim-tables
- add Nepali subpackage

* Fri Feb 10 2006 Jens Petersen <petersen@redhat.com> - 1.3.2-1
- update to 1.3.2 bugfix release
- do not include ja-anthy.mim input map

* Thu Feb  2 2006 Jens Petersen <petersen@redhat.com> - 1.3.1-1
- update to 1.3.1 release
  - add new icons to language subpackages
  - new common-cjk subpackage for CJK common files
  - new Swedish subpackage
  - exclude new pkgconfig file

* Fri Dec 16 2005 Jens Petersen <petersen@redhat.com> - 1.2.0-2
- import to Fedora Core

* Wed Nov  9 2005 Jens Petersen <petersen@redhat.com> - 1.2.0-1
- separate output datafiles to datafiles subpackage.

* Wed Oct  5 2005 Jens Petersen <petersen@redhat.com>
- initial packaging for Fedora Extras

* Sat Sep 24 2005 Jens Petersen <petersen@redhat.com>
- split .mim input tables into separate subpackages per language

* Sat Jan 15 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp>
- modify spec for fedora
