Name: puddletag
Version: 2.2.0
Release: alt1.1

Summary: Feature rich, easy to use tag editor
License: GPLv2 and GPLv3+
Group: File tools
Url: https://github.com/puddletag/puddletag
BuildArch: noarch

Source0: %name-%version.tar.gz

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: ImageMagick

%add_python3_req_skip quodlibet.parse tags puddlestuff.libraries.mysqllib

%description
puddletag is an audio tag editor for GNU/Linux similar to Windows program
Mp3tag (http://www.mp3tag.de). Unlike most taggers for GNU/Linux, it uses a
spreadsheet-like layout so that all the tags you want to edit by hand are
visible and easily editable.

The usual tag editor features are supported like extracting tag information
from filenames, renaming files based on their tags by using patterns (that you
define, not crappy, uneditable ones).

Then there're functions, which can do things like replace text, trim, change
the case of tags, etc. Actions can automate repetitive tasks. You can import
your QuodLibet library, lookup tags using MusicBrainz, FreeDB or Amazon
(though it's only good for cover art) and more, but I've reached my comma
quota.

Supported formats: ID3v1, ID3v2 (mp3), MP4 (mp4, m4a, etc.), VorbisComments
(ogg, flac), Musepack (mpc), Monkey's Audio (.ape) and WavPack (wv).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,64x64,96x96,128x128,256x256}/apps
install -m 0644 %name.png %buildroot%_iconsdir/hicolor/256x256/apps/

for i in 16x16 32x32 64x64 96x96 128x128; do
  convert -resize "$i" %name.png %buildroot%_iconsdir/hicolor/"$i"/apps/%name.png
done

%files
%doc NEWS TODO THANKS
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%exclude %_datadir/pixmaps/%name.*
%python3_sitelibdir/puddlestuff/
%python3_sitelibdir/%name-%version.dist-info/
%_man1dir/%name.*

%changelog
* Thu Aug 17 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 2.2.0-alt1.1
- NMU: ignored unmet dependency.

* Sun Jul 16 2023 Anton Kurachenko <srebrov@altlinux.org> 2.2.0-alt1
- Update to new version 2.2.0.

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
