%define _unpackaged_files_terminate_build 1

Name: goldendict
Version: 1.5.0
Release: alt2

Summary: Feature-rich dictionary lookup program
License: GPL-3.0
Group: Education
URL: http://www.goldendict.org
VCS: https://github.com/goldendict/goldendict

Source0: %name-%version.tar
Patch0: goldendict-ru-desktop.patch
Patch1: goldendict-remove-git-version.patch

BuildRequires(pre): qt5-base-devel
BuildRequires: bzlib-devel
BuildRequires: eb-devel
BuildRequires: gcc-c++
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: libao-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libhunspell-devel
BuildRequires: liblzo2-devel
BuildRequires: libtiff-devel
BuildRequires: libvorbis-devel
BuildRequires: libzip-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-phonon-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools
BuildRequires: qt5-tools-devel
BuildRequires: qt5-webkit-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libswresample-devel

%description
GoldenDict is feature-rich dictionary lookup program. Features:
* Use of WebKit for an accurate articles' representation, complete with
  all formatting, colors, images and links.
* Support of multiple dictionary file formats, namely:
  - Babylon .BGL files, complete with images and resources
  - StarDict .ifo/.dict./.idx/.syn dictionaries
  - Dictd .index/.dict(.dz) dictionary files
  - ABBYY Lingvo .dsl source files, together with abbreviations. The
    files can be optionally compressed with dictzip. Dictionary
    resources can be packed together into a .zip file.
  - ABBYY Lingvo .lsa/.dat audio archives. Those can be indexed
    separately, or be referred to from .dsl files.
* Support for Wikipedia, Wiktionary, or any other MediaWiki-based sites
  to perform lookups in.
* Ability to use arbitrary websites as dictionaries via templated Url
  patterns.
* Support for looking up and listening to pronunciations from forvo.com
* Hunspell-based morphology system, used for word stemming and spelling
  suggestions.
* Ability to index arbitrary directories with audio files for
  pronunciation lookups.
* Full Unicode case, diacritics, punctuation and whitespace folding.
  This means the ability to type in words without any accents, correct
  case, punctuation or spaces.
* Scan popup functionality. A small window pops up with the translation
  of a word chosen from another application.
* Support for global hotkeys. You can spawn the program window at any
  point, or directly translate a word from the clipboard.
* Tabbed browsing in a modern Qt 4 interface.

%prep
%setup -q
%autopatch -p1

%build
export PREFIX=%_prefix
%qmake_qt5 DISABLE_INTERNAL_PLAYER=1 CONFIG+=no_epwing_support %name.pro
%make_build

%install
%installqt5

# our find-lang.sh doesn't recognize .qm translation files
%find_lang --with-qt goldendict
echo "%_datadir/%name/locale/ie_001.qm" >> goldendict.lang
rm -rf %buildroot%_datadir/app-install

%files -f goldendict.lang
%_bindir/*
%attr(0644, root, root) %_datadir/applications/*.desktop
%_pixmapsdir/*
%dir %_datadir/%name
%dir %_datadir/%name/locale
%_datadir/%name/help
%_datadir/metainfo/*.xml

%changelog
* Tue Nov 14 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt2
- Release 1.5.0.

* Thu Nov 22 2018 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1.git36a1881
- 1.5.0-rc2 with fixes from git (closes: #32750, #30973, #29268, #27218, #20887)

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.0.1-alt7.git.qa1
- Rebuilt for gcc5 C++11 ABI.

* Sun Apr 15 2012 Alexey Morozov <morozov@altlinux.org> 1.0.1-alt7.git
- post-1.0.1 git snapshot 296d6d5203d5dab9915ac52e6fcb8271c2ef739d
- rebuilt against newer kde4libs

* Fri Feb 24 2012 Alexey Morozov <morozov@altlinux.org> 1.0.1-alt6.git
- post-1.0.1 git snapshot 0c38bb851974f85319d901ba0f5a42ebf37af914
- slightly updated Russian translations

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.1-alt5.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for goldendict

* Tue Apr 26 2011 Alexey Morozov <morozov@altlinux.org> 1.0.1-alt5
- post-1.0.1 git snapshot 28fd948b999be1f2475d7c51e2667a35b015e93e
- build requirements updated

* Fri Apr 08 2011 Alexey Morozov <morozov@altlinux.org> 1.0.1-alt4
- post-1.0.1 git snapshot 359805ecca07e7e0530b166d752ada611dfd2cff:
  * few Hunspell and l10n fixes
  * translations updates for several languages (in the order of
    appearance):
    * Polish
    * Japanese
    * Chinese Traditional
    * Albanian
    * Italian
    * Brasilian Portuguese
    * Ukranian

* Sat Dec 18 2010 Alexey Morozov <morozov@altlinux.org> 1.0.1-alt3
- a new git snapshot (7ec3b9852154)
- added proper default path for Hunspell dictionaries

* Mon Dec  6 2010 Alexey Morozov <morozov@altlinux.org> 1.0.1-alt2
- store application data files in %_datadir/%name not in %_datadir/apps/%name
- explicitly mention package-specific directories in the spec
- dropped git SHA1 id from release, it's too scary for ordinary users

* Mon Dec  6 2010 Alexey Morozov <morozov@altlinux.org> 1.0.1-alt1.0.f71c0ac7a7c3
- build a new git snapshot (post-1.0.1)
- updated Russian translation

* Tue Jul  6 2010 Alexey Morozov <morozov@altlinux.org> 0.9-alt1.8.621d842394cf
- build a new git snapshot
- updated Russian translation

* Sat Jun 12 2010 Alexey Morozov <morozov@altlinux.org> 0.9-alt1.7.c33fa2c9ccce
- fixed few mistakes in the Russian translation

* Fri Jun 04 2010 Alexey Morozov <morozov@altlinux.org> 0.9-alt1.6.c33fa2c9ccce
- build a new git snapshot upon rider@'s request. Closes #23518
- updated Russian translation

* Fri Mar 12 2010 Alexey Morozov <morozov@altlinux.org> 0.9-alt1.5.83115adf6e42
- a new version from git (translations updates)
- desktop-file permissions fixed (executable bit removed)

* Wed Jan 20 2010 Alexey Morozov <morozov@altlinux.org> 0.9-alt1.4.199deb89850b
- build a new version from git
- small fixes to build process and package dependencies

* Thu Nov 12 2009 Alexey Morozov <morozov@altlinux.org> 0.9-alt1.3.c83b6cd5da04
- build a new version from git (c83b6cd5da0470492697d948e2ffec9007678812)
- updated Russian translation

* Wed Nov 11 2009 Alexey Morozov <morozov@altlinux.org> 0.9-alt1.2.g416b231587a
- build a new version from git (416b231587a801b2a27cb76d86a50ca8cf44d231)

* Wed Nov 11 2009 Alexey Morozov <morozov@altlinux.org> 0.9-alt1.1
- re-organize the repository structure to follow upstream moved to git.

* Mon May 25 2009 Anton Farygin <rider@altlinux.ru> 0.9-alt1
- new version

* Tue May 12 2009 Anton Farygin <rider@altlinux.ru> 0.8-alt1.r279
- fixed build in new environment
- new snapshot

* Fri Apr 24 2009 Anton Farygin <rider@altlinux.ru> 0.8-alt1
- 0.8

* Thu Apr 23 2009 Anton Farygin <rider@altlinux.ru> 0.8-alt0.r179
- new snapshot

* Mon Apr 20 2009 Anton Farygin <rider@altlinux.ru> 0.8-alt0.r159
- new snapshot

* Thu Apr 16 2009 Anton Farygin <rider@altlinux.ru> 0.8-alt0.r132
- new snapshot

* Tue Apr 14 2009 Anton Farygin <rider@altlinux.ru> 0.8-alt0.r129
- new snapshot
- enabled russian translation
- fixed myspell dictionary search path
- added ALT Linux Wiki to mediawiki lists
- enabled by default russian Wikipedia

* Fri Apr 03 2009 Anton Farygin <rider@altlinux.ru> 0.7-alt1.r76
- first build for Sisyphus
