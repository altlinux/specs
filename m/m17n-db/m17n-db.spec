%define indic_ver 0.4.25

Name: m17n-db
Version: 1.3.3
Release: alt0.1

Summary: Multilingualization datafiles for m17n-lib

Group: System/Libraries
License: LGPL
Url: http://www.m17n.org/m17n-lib-en/index.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.m17n.org/m17n-lib-download/%name-%version.tar.bz2
Source1: %name-indic-%indic_ver.tar.gz
BuildArch: noarch

Patch1: bn-itrans-t-182227.patch

# Automatically added by buildreq on Sun Nov 12 2006
BuildRequires: glibc-i18ndata

%description
This package contains multilingualization (m17n) datafiles for m17n-lib
which describe input maps, encoding maps, and OpenType font data
for many languages.

%package datafiles
Summary: Multilingualization datafiles for m17n-lib
Group: System/Libraries
Requires: %name = %version-%release

%description datafiles
m17n-db datafiles not needed for using the input maps.

%package common-cjk
Summary: m17n-db common files for CJK input
Group: System/Libraries
Requires: %name = %version-%release

%description common-cjk
m17n-db common files for Chinese, Japanese and Korean input maps.

%package amharic
Summary: m17n-db input table for Amharic
Group: System/Libraries
Requires: %name = %version-%release

%description amharic
m17n-db Amharic input table.

%package arabic
Summary: m17n-db input table for Arabic
Group: System/Libraries
Requires: %name = %version-%release

%description arabic
m17n-db Arabic input table.

%package armenian
Summary: m17n-db input table for Armenian
Group: System/Libraries
Requires: %name = %version-%release

%description armenian
m17n-db Armenian input table.

%package assamese
Summary: m17n-db input table for Assamese
Group: System/Libraries
Requires: %name = %version-%release

%description assamese
m17n-db Assamese input table.

%package bengali
Summary: m17n-db input table for Bengali
Group: System/Libraries
Requires: %name = %version-%release

%description bengali
m17n-db Bengali input table.

%package chinese
Summary: m17n-db input table for Chinese
Group: System/Libraries
Requires: %name-common-cjk
Obsoletes: %name-bopomofo < 1.3.3-13.fc6

%description chinese
m17n-db Chinese input map.

%package croatian
Summary: m17n-db input table for Croatian
Group: System/Libraries
Requires: %name = %version-%release

%description croatian
m17n-db Croatian input table.

%package dhivehi
Summary: m17n-db input table for Dhivehi
Group: System/Libraries
Requires: %name = %version-%release

%description dhivehi
m17n-db Dhivehi input table.

%package farsi
Summary: m17n-db input table for Farsi
Group: System/Libraries
Requires: %name = %version-%release

%description farsi
m17n-db Farsi input table.

%package generic
Summary: Generic m17n-db input tables
Group: System/Libraries
Requires: %name = %version-%release

%description generic
Generic m17n-db input table.

%package georgian
Summary: m17n-db input table for Georgian
Group: System/Libraries
Requires: %name = %version-%release

%description georgian
m17n-db Georgian input map.

%package greek
Summary: m17n-db input table for Greek
Group: System/Libraries
Requires: %name = %version-%release

%description greek
m17n-db Greek input table.

%package gujarati
Summary: m17n-db input table for Gujarati
Group: System/Libraries
Requires: %name = %version-%release

%description gujarati
m17n-db Gujarati input table.

%package hebrew
Summary: m17n-db input table for Hebrew
Group: System/Libraries
Requires: %name = %version-%release

%description hebrew
m17n-db Hebrew input table.

%package hindi
Summary: m17n-db input table for Hindi
Group: System/Libraries
Requires: %name = %version-%release

%description hindi
m17n-db Hindi input table.

%package japanese
Summary: m17n-db input table for Japanese
Group: System/Libraries
Requires: %name = %version-%release

%description japanese
m17n-db Japanese input map.

%package kazakh
Summary: m17n-db input table for Kazakh
Group: System/Libraries
Requires: %name = %version-%release

%description kazakh
m17n-db Kazakh input map.

%package khmer
Summary: m17n-db input table for Khmer
Group: System/Libraries
Requires: %name = %version-%release

%description khmer
m17n-db Khmer input map.

%package kannada
Summary: m17n-db input table for Kannada
Group: System/Libraries
Requires: %name = %version-%release

%description kannada
m17n-db Kannada input map.

%package korean
Summary: m17n-db input table for Korean
Group: System/Libraries
Requires: %name-common-cjk

%description korean
m17n-db Korean input map.

%package latin
Summary: m17n-db input table for Latin
Group: System/Libraries
Requires: %name = %version-%release

%description latin
m17n-db Latin input map.

%package lao
Summary: m17n-db input table for Lao
Group: System/Libraries
Requires: %name = %version-%release

%description lao
m17n-db Lao input map.

%package malayalam
Summary: m17n-db input table for Malayalam
Group: System/Libraries
Requires: %name = %version-%release

%description malayalam
m17n-db Malayalam input map.

%package marathi
Summary: m17n-db input table for Marathi
Group: System/Libraries
Requires: %name = %version-%release

%description marathi
m17n-db Marathi input map.

%package myanmar
Summary: m17n-db input table for Myanmar
Group: System/Libraries
Requires: %name = %version-%release

%description myanmar
m17n-db Myanmar input map.

%package nepali
Summary: m17n-db input tables for Nepali
Group: System/Libraries
Requires: %name = %version-%release

%description nepali
m17n-db Nepali input maps.

%package oriya
Summary: m17n-db input table for Oriya
Group: System/Libraries
Requires: %name = %version-%release

%description oriya
m17n-db Oriya input map.

%package punjabi
Summary: m17n-db input table for Punjabi
Group: System/Libraries
Requires: %name = %version-%release

%description punjabi
m17n-db Punjabi input map.

%package russian
Summary: m17n-db input table for Russian
Group: System/Libraries
Requires: %name = %version-%release

%description russian
m17n-db Russian input map.

%package serbian
Summary: m17n-db input table for Serbian
Group: System/Libraries
Requires: %name = %version-%release

%description serbian
m17n-db Serbian input map.

%package sinhala
Summary: m17n-db input table for Sinhala
Group: System/Libraries
Requires: %name = %version-%release

%description sinhala
m17n-db Sinhala input map.

%package slovak
Summary: m17n-db input table for Slovak
Group: System/Libraries
Requires: %name = %version-%release

%description slovak
m17n-db Slovak input map.

%package swedish
Summary: m17n-db input table for Swedish
Group: System/Libraries
Requires: %name = %version-%release

%description swedish
m17n-db Swedish input map.

%package syriac
Summary: m17n-db input table for Syriac
Group: System/Libraries
Requires: %name = %version-%release

%description syriac
m17n-db Syriac input map.

%package tamil
Summary: m17n-db input table for Tamil
Group: System/Libraries
Requires: %name = %version-%release

%description tamil
m17n-db Tamil input map.

%package telugu
Summary: m17n-db input table for Telugu
Group: System/Libraries
Requires: %name = %version-%release

%description telugu
m17n-db Telugu input map.

%package thai
Summary: m17n-db input table for Thai
Group: System/Libraries
Requires: %name = %version-%release

%description thai
m17n-db Thai input map.

%package tibetan
Summary: m17n-db input table for Tibetan
Group: System/Libraries
Requires: %name = %version-%release

%description tibetan
m17n-db Tibetan input table.

%package vietnamese
Summary: m17n-db input table for Vietnamese
Group: System/Libraries
Requires: %name = %version-%release

%description vietnamese
m17n-db Vietnamese input map.

%package urdu
Summary: m17n-db input table for Urdu
Group: System/Libraries
Requires: %name = %version-%release

%description urdu
m17n-db Urdu input map.

%prep
%setup -q -a1
%patch1 -p1 -b .1

%build
%configure
make

%install
%makeinstall

# add new Indic maps
cp -p %name-indic-%indic_ver/*.mim %buildroot%_datadir/m17n
cp -p %name-indic-%indic_ver/*.png %buildroot%_datadir/m17n/icons

# don't need ispell or anthy
rm %buildroot%_datadir/m17n/{ispell.mim,icons/en-ispell.png}
rm %buildroot%_datadir/m17n/{ja-anthy.mim,icons/ja-anthy.png}
# don't ship unijoy map for now
rm %buildroot%_datadir/m17n/{bn-unijoy.mim,icons/bn-unijoy.png}

# drop pkgconfig file for now
rm %buildroot%_pkgconfigdir/m17n-db.pc

%files
%doc AUTHORS COPYING README
%_bindir/*
%dir %_datadir/m17n
%dir %_datadir/m17n/icons
%_datadir/m17n/mdb.dir
%_datadir/m17n/*.tbl
%_datadir/m17n/command.mim

%files datafiles
%_datadir/m17n/*.flt
%_datadir/m17n/*.fst
%_datadir/m17n/*.map
%_datadir/m17n/*.tab
%_datadir/m17n/LOCALE.*

%files common-cjk
%_datadir/m17n/cjk-*.mim
%_datadir/m17n/variable.mim

%files amharic
%_datadir/m17n/am-*.mim
%_datadir/m17n/icons/am-*.png

%files arabic
%_datadir/m17n/ar-*.mim
%_datadir/m17n/icons/ar-*.png

%files armenian
%_datadir/m17n/hy-*.mim
%_datadir/m17n/icons/hy-*.png

%files assamese
%_datadir/m17n/as-*.mim
%_datadir/m17n/icons/as-*.png

%files bengali
%_datadir/m17n/bn-*.mim
%_datadir/m17n/icons/bn-*.png

%files chinese
%_datadir/m17n/zh-*.mim
%_datadir/m17n/icons/zh-*.png
%_datadir/m17n/bopo-*.mim
%_datadir/m17n/icons/bopo-*.png

%files croatian
%_datadir/m17n/hr-*.mim
%_datadir/m17n/icons/hr-*.png

%files dhivehi
%_datadir/m17n/dv-*.mim
%_datadir/m17n/icons/dv-*.png

%files farsi
%_datadir/m17n/fa-*.mim
%_datadir/m17n/icons/fa-*.png

%files generic
%_datadir/m17n/rfc1345.mim
%_datadir/m17n/icons/rfc1345.png
%_datadir/m17n/unicode.mim
%_datadir/m17n/icons/unicode.png

%files georgian
%_datadir/m17n/ka-*.mim
%_datadir/m17n/icons/ka-*.png

%files greek
%_datadir/m17n/el-*.mim
%_datadir/m17n/icons/el-*.png

%files gujarati
%_datadir/m17n/gu-*.mim
%_datadir/m17n/icons/gu-*.png

%files hebrew
%_datadir/m17n/he-*.mim
%_datadir/m17n/icons/he-*.png

%files hindi
%_datadir/m17n/hi-*.mim
%_datadir/m17n/icons/hi-*.png

%files japanese
%_datadir/m17n/ja-*.mim
%_datadir/m17n/icons/ja-*.png

%files kazakh
%_datadir/m17n/kk-*.mim
%_datadir/m17n/icons/kk-*.png

%files khmer
%_datadir/m17n/km-*.mim
%_datadir/m17n/icons/km-*.png

%files kannada
%_datadir/m17n/kn-*.mim
%_datadir/m17n/icons/kn-*.png

%files korean
%_datadir/m17n/ko-*.mim
%_datadir/m17n/icons/ko-*.png

%files lao
%_datadir/m17n/lo-*.mim
%_datadir/m17n/icons/lo-*.png

%files latin
%_datadir/m17n/latn-*.mim
%_datadir/m17n/icons/latn-*.png

%files malayalam
%_datadir/m17n/ml-*.mim
%_datadir/m17n/icons/ml-*.png

%files marathi
%_datadir/m17n/mr-*.mim
%_datadir/m17n/icons/mr-*.png

%files myanmar
%_datadir/m17n/my-*.mim
%_datadir/m17n/icons/my-*.png

%files nepali
%_datadir/m17n/ne-*.mim
%_datadir/m17n/icons/ne-*.png

%files oriya
%_datadir/m17n/or-*.mim
%_datadir/m17n/icons/or-*.png

%files punjabi
%_datadir/m17n/pa-*.mim
%_datadir/m17n/icons/pa-*.png

%files russian
%_datadir/m17n/ru-*.mim
%_datadir/m17n/icons/ru-*.png

%files serbian
%_datadir/m17n/sr-*.mim
%_datadir/m17n/icons/sr-*.png

%files sinhala
%_datadir/m17n/si-*.mim
%_datadir/m17n/icons/si-*.png

%files slovak
%_datadir/m17n/sk-*.mim
%_datadir/m17n/icons/sk-*.png

%files swedish
%_datadir/m17n/sv-*.mim
%_datadir/m17n/icons/sv-*.png

%files syriac
%_datadir/m17n/syrc-*.mim
%_datadir/m17n/icons/syrc-*.png

%files tamil
%_datadir/m17n/ta-*.mim
%_datadir/m17n/icons/ta-*.png

%files telugu
%_datadir/m17n/te-*.mim
%_datadir/m17n/icons/te-*.png

%files thai
%_datadir/m17n/th-*.mim
%_datadir/m17n/icons/th-*.png

%files tibetan
%_datadir/m17n/bo-*.mim
%_datadir/m17n/icons/bo-*.png

%files vietnamese
%_datadir/m17n/vi-*.mim
%_datadir/m17n/icons/vi-*.png

%files urdu
%_datadir/m17n/ur-*.mim
%_datadir/m17n/icons/ur-*.png

%changelog
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
