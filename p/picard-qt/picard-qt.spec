Name: picard-qt
Version: 0.15.1
Release: alt1.1.1

Summary: MusicBrainz tagger (Qt GUI)
License: GPLv2+
Group: Sound
Url: http://musicbrainz.org/doc/PicardQt

Source: picard-%version.tar

Conflicts: picard

BuildPreReq: gcc-c++ libavformat-devel libofa-devel python-devel python-modules-encodings

%description
The project code-named Picard is the next generation MusicBrainz tagging
application. This new tagging concept is Release oriented, as opposed to
track oriented like the ClassicTagger was. Picard is written in Python,
which is a cross-platform language - this allows the same code to run
both on Windows and on Linux.

PicardQt is a new version of PicardTagger, written using Qt as the
GUI toolkit. It also includes implementations of a few new ideas, such
as IntuitivePicardInterface or TaggerScript.

%prep
%setup -n picard-%version

%build
rm -Rf installer
python setup.py config
%python_build

%install
%python_install
%find_lang picard

%files -f picard.lang
%doc AUTHORS.txt NEWS.txt INSTALL.txt
%_bindir/*
%python_sitelibdir/picard/
%python_sitelibdir/*.egg-info
%_iconsdir/*/*/*/*.png
%_desktopdir/picard.desktop

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15.1-alt1.1
- Rebuild with Python-2.7

* Tue Aug 16 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.15.1-alt1
- 0.15.1

* Thu Feb 11 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.12.1-alt1
- 0.12.1
- spec fixes/cleanup

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2.1
- Rebuilt with python 2.6

* Fri Sep 04 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.11-alt2
- Rebuild with libavcodec.so.52

* Tue Dec 09 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.11-alt1
- 0.11
- Remove obsolete %%clean_menus/%%update_menus calls

* Sun Aug 31 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.10-alt1
- 0.10
- Enable locales installation

* Sun Mar 18 2007 Mikhail Yakshin <greycat@altlinux.org> 0.9.0alpha4-alt2
- Added acoustic fingerprinting support (libofa, ffmpeg)
- Added CD DiscID support (libdiscid)

* Sun Mar 18 2007 Mikhail Yakshin <greycat@altlinux.org> 0.9.0alpha4-alt1
- Initial build for ALT Linux
