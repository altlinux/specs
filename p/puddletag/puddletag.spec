Name: puddletag
Version: 1.2.0
Release: alt1

Summary: Feature rich, easy to use tag editor
License: GPLv2 and GPLv3+
Group: File tools

URL: http://puddletag.sourceforge.net/
Source: https://github.com/keithgg/%name/releases/download/v%version/%name-%version.tar.gz

Patch0: %name-1.0.1-translations_dir.diff

BuildArch: noarch

Requires: mutagen >= 1.20
# optional
#Requires: chromaprint >= 0.4

BuildRequires: python-devel python-modules-encodings
BuildRequires: desktop-file-utils libqt4-devel

%description
Puddletag is an audio tag editor. Unlike most taggers, it uses a
spreadsheet-like layout so that all the tags you want to edit by hand are
visible and easily editable.

The usual tag editor features are supported like extracting tag information
from filenames, renaming files based on their tags by using patterns (that you
define, not crappy, uneditable ones).

Then there're Functions, which can do things like replace text, trim, change
the case of tags, etc. Actions can automate repetitive tasks. You can import
your QuodLibet library, lookup tags using MusicBrainz, FreeDB or Amazon (though
it's only good for cover art) and more.

Supported formats: ID3v1, ID3v2 (mp3), MP4 (mp4, m4a, etc.), VorbisComments
(ogg, flac), Musepack (mpc), Monkey's Audio (.ape) and WavPack (wv).

%prep
%setup
%patch0 -p1

%build
%python_build
lrelease-qt4 ./translations/*.ts

%install
%python_install
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Audio \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/puddletag.desktop
mkdir -p %buildroot%_datadir/%name/translations
cp -a ./translations/*.qm %buildroot%_datadir/%name/translations/

%files
%_bindir/*
%python_sitelibdir/*
%_desktopdir/*
%_pixmapsdir/*
%_man1dir/*
%_datadir/%name/translations
%doc NEWS

%changelog
* Thu Jan 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0 (ALT #32991)

* Mon Jul 01 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Jan 06 2012 Victor Forsiuk <force@altlinux.org> 0.10.6.3-alt1
- 0.10.6.3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.6-alt1.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 0.10.6-alt1
- 0.10.6

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.10.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for puddletag

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 0.10.3-alt1
- 0.10.3

* Tue Mar 15 2011 Victor Forsiuk <force@altlinux.org> 0.10.0-alt1
- Initial build.
