%define gname mkvmerge-gui

%def_disable debug
%def_disable profiling

%def_enable gui
%def_enable bz2
%def_enable lzo
%def_enable wxwidgets
%def_disable qt
%def_with flac
%def_with tools

%undefine _configure_gettext

Name: mkvtoolnix
Version: 5.0.1
Release: alt3

Summary: Tools to create, alter and inspect Matroska files
License: GPL
Group: Video
URL: http://www.bunkus.org/videotools/%name/
Source: %{url}sources/%name-%version.tar

Provides: mkvmerge = %version-%release

BuildRequires(pre): rpm-build-xdg
BuildRequires: gcc-c++ boost-devel boost-filesystem-devel zlib-devel libmagic-devel
BuildRequires: libexpat-devel libvorbis-devel ImageMagick ruby ruby-stdlibs symlinks
BuildRequires: libebml-devel >= 1.2.2 libmatroska-devel >= 1.3.0

%{?_enable_gui:BuildRequires: libpango-devel libwxGTK-devel}
%{?_enable_bz2:BuildRequires: bzlib-devel}
%{?_enable_lzo:BuildRequires: liblzo2-devel}
%{?_enable_qt:BuildRequires: libSM-devel libXcursor-devel libXi-devel libXinerama-devel libXrandr-devel libqt4-devel}
%{?_with_flac:BuildRequires: libflac-devel}

%description
Matroska is a new multimedia file format aiming to become the new
container format for the future.
With these tools one can extract tracks/data from (mkvextract) Matroska
files and create (mkvmerge) Matroska files from other media files.

%if_enabled gui
%package -n %gname
Summary: GUI for mkvmerge including a chapter editor
License: GPL
Group: Video
Provides: mmg = %version-%release

%description -n %gname
Matroska is a new multimedia file format aiming to become the new
container format for the future.
mkvmerge GUI is a wxWindows based GUI for mkvmerge. It offers easy
access to all of mkvmerge's options. All settings (e.g. source files,
track options etc) can be saved and restored. Included is a chapter
editor that can read OGM style and XML style chapter files, write XML
style chapter files and even read chapters from Matroska files and
write chapters directly to Matroska files.
%endif

%package -n mkvinfo
Summary: Tool for print information about tracks in Matroska files
License: GPL
Group: Video

%description -n mkvinfo
Matroska is a new multimedia file format aiming to become the new
container format for the future.
With mkvinfo you can get information about Matroska files. This program
lists all tracks contained in a Matroska file including information
about the codecs used.

%if_with tools
%package tools
Summary: %name additional tools
Group: Video
Conflicts: %name < 2.4.0-alt1

%description tools
Matroska is a new multimedia file format aiming to become the new
container format for the future.
This package contains some additional tools.
%endif

%prep
%setup

%build
%add_optflags -DBOOST_FILESYSTEM_VERSION=2
./autogen.sh
export LINGUAS="en ru uk"
%configure \
    --disable-option-checking \
    %{subst_enable debug} \
    %{subst_enable profiling} \
    %{subst_enable gui} \
    %{subst_enable bz2} \
    %{subst_enable lzo} \
    %{subst_enable wxwidgets} \
    %{subst_enable qt} \
    %{subst_with flac}

./drake %{?_with_tools:TOOLS=1} V=1

bzip2 --best --force --keep ChangeLog

%install
./drake DESTDIR=%buildroot install

mkdir -p %buildroot%_defaultdocdir/%name-%version
install -m0644 AUTHORS ChangeLog.* README %buildroot%_defaultdocdir/%name-%version
cp -ar examples %buildroot%_defaultdocdir/%name-%version
mv %buildroot%_datadir/doc/%name/guide %buildroot%_defaultdocdir/%name-%version

%if_with tools
install -m0755 -D src/tools/{base64tool,diracparser,ebml_validator,vc1parser} %buildroot%_bindir
%endif

%if_enabled gui
mv %buildroot%_bindir/mmg %buildroot%_bindir/%gname
ln -s %gname %buildroot%_bindir/mmg
mv %buildroot%_man1dir/mmg.1 %buildroot%_man1dir/%gname.1
ln -s %gname.1 %buildroot%_man1dir/mmg.1
sed -i 's/mkvmergeGUI/%gname/' %buildroot%_desktopdir/mkvmergeGUI.desktop 
find %buildroot%_datadir -name 'mkvmergeGUI.*' -exec rename mkvmergeGUI %gname "{}" +
%endif

%find_lang %name

%files -f %name.lang
%_bindir/mkvextract
%_bindir/mkvmerge
%_bindir/mkvpropedit
%_man1dir/mkvextract.*
%_man1dir/mkvmerge.*
%_man1dir/mkvpropedit.*
%_defaultdocdir/%name-%version

%files -n mkvinfo
%_bindir/mkvinfo
%_man1dir/mkvinfo.*
%_iconsdir/hicolor/*/apps/mkvinfo.*
%_datadir/applications/mkvinfo.desktop
%_desktopdir/mkvinfo.desktop

%if_enabled gui
%files -n %gname
%_bindir/%gname
%_bindir/mmg
%_man1dir/%gname.*
%_man1dir/mmg.*
%_iconsdir/hicolor/*/apps/%{gname}.*
%_desktopdir/%gname.desktop
%_xdgmimedir/packages/%name.xml
%endif

%if_with tools
%files tools
%_bindir/base64tool
%_bindir/*parser
%_bindir/ebml_validator
%endif

%changelog
* Wed Apr 18 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.1-alt3
- rebuilt with recent boost, again

* Thu Dec 08 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.1-alt2
- rebuilt with recent boost

* Thu Oct 13 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.1-alt1
- 5.0.1 released

* Mon Aug 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.8.0-alt1
- 4.8.0 released

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.1
- Rebuilt with Boost 1.46.1

* Fri Jan 21 2011 Afanasov Dmitry <ender@altlinux.org> 4.4.0-alt1
- 4.4.0 release
- closes #24121

* Fri Dec 17 2010 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Wed Aug 18 2010 Afanasov Dmitry <ender@altlinux.org> 4.2.0-alt1
- 4.2.0 release

* Fri Feb 26 2010 Afanasov Dmitry <ender@altlinux.org> 3.2.0-alt1
- 3.2.0 release

* Wed Feb 17 2010 Afanasov Dmitry <ender@altlinux.org> 3.1.0-alt2
- build with libwxGTK-2.8

* Mon Jan 25 2010 Afanasov Dmitry <ender@altlinux.org> 3.1.0-alt1
- 3.1.0 release

* Sat Dec 19 2009 Afanasov Dmitry <ender@altlinux.org> 3.0.0-alt1
- 3.0.0 release
  + add mkvpropedit
- alt-changes patch: add deleted manpage for base64tool

* Wed Jul 08 2009 Afanasov Dmitry <ender@altlinux.org> 2.9.7-alt1
- 2.9.7 release

* Fri Jun 05 2009 Afanasov Dmitry <ender@altlinux.org> 2.9.0-alt2
- change packager

* Sun May 24 2009 Led <led@altlinux.ru> 2.9.0-alt1
- 2.9.0 with postrelease upstream's fixes

* Sat Apr 18 2009 Led <led@altlinux.ru> 2.7.0-alt1
- 2.7.0 with postrelease upstream's fixes

* Fri Apr 03 2009 Led <led@altlinux.ru> 2.6.0-alt1
- 2.6.0 with postrelease upstream's fixes

* Sun Mar 15 2009 Led <led@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Sun Feb 15 2009 Led <led@altlinux.ru> 2.4.2-alt1
- 2.4.2:
  + added support for reading the pixel aspect ratio from Theora video
    tracks

* Sun Dec 14 2008 Led <led@altlinux.ru> 2.4.1-alt1
- 2.4.1 (SVN revision 4028)

* Tue Dec 02 2008 Led <led@altlinux.ru> 2.4.0-alt3
- SVN revision 4022:
  + Sync with the official ISO 639-2 standard
- cleaned up spec

* Mon Nov 10 2008 Led <led@altlinux.ru> 2.4.0-alt2
- SVN revision 4019

* Mon Nov 10 2008 Led <led@altlinux.ru> 2.4.0-alt1
- 2.4.0:
  + mkvextract:
    added support for handling SimpleBlocks for timecode extraction;
    added support for extracting Theora video tracks into Ogg files.
  + Added the extensions "evo", "evob" and "vob" to mmg's "add file"
    dialog.
  + mkvmerge: Added support for Dirac video tracks.
- added %name-tools subpackage

* Sun Sep 14 2008 Led <led@altlinux.ru> 2.3.0-alt1
- 2.3.0
- removed %name-1.7.0-configure.patch
- updated BuildRequires

* Sun Aug 10 2008 Led <led@altlinux.ru> 2.2.0-alt2
- fixed *.desktop

* Thu Mar 06 2008 Led <led@altlinux.ru> 2.2.0-alt1
- 2.2.0:
  + support for handling AC3 in WAV in ACM mode
  + support for reading AC3 from QuickTime/MP4 files
  + support for handling AC3 in WAV in IEC 61937 compatible streams
    (aka SPDIF mode)
  + support for WAV files with multiple data chunks
  + support for AAC-in-AVI with CodecID 0x706d as created by mencoder
  + SRT files that contain coordinates in the timecode line are
    supported

* Tue Mar 04 2008 Led <led@altlinux.ru> 2.1.0-alt3
- fixed *.desktop

* Sat Mar 01 2008 Led <led@altlinux.ru> 2.1.0-alt2
- added icons
- fixed mkvinfo.desktop

* Wed Aug 22 2007 Led <led@altlinux.ru> 2.1.0-alt1
- 2.1.0:
  + Added support for EAC3/DD+ (Dolby Digital Plus) files and tracks
    (raw EAC3 files or inside Matroska with CodecID A_EAC3)
  + Added support for EAC3 tracks in MPEG program streams
  + Added support for handling AVC/h.264 tracks in MPEG program streams
  + Disabled the support for DTS tracks in MPEG program streams
  + Added support for RealAudio v3 in RealMedia files
  + Added support for extracting Dolby Digital Plus (EAC3) tracks
  + Added support for reading MP2 audio tracks from OGM files

* Tue Apr 17 2007 Led <led@altlinux.ru> 2.0.2-alt2
- fixed typing errors in summaries, descriptions, menu file.

* Tue Feb 27 2007 Led <led@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Tue Jan 16 2007 Led <led@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Mon Jan 15 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.1-alt1.0
- Rebuilt with libpcrecpp.so.1.

* Mon Nov 27 2006 Led <led@altlinux.ru> 1.8.1-alt1
- 1.8.1
- Fixed Requires/Provides for %gname package

* Tue Nov 14 2006 Led <led@altlinux.ru> 1.8.0-alt1
- 1.8.0
- fixed BuildRequires

* Wed May 03 2006 Led <led@altlinux.ru> 1.7.0-alt1
- 1.7.0
- added %name-1.7.0-configure.patch
- fixed spec

* Tue Feb 14 2006 Led <led@altlinux.ru> 1.6.5-alt4
- removed redundant sources

* Thu Jan 26 2006 Led <led@altlinux.ru> 1.6.5-alt3
- added examples to docs
- uk and ru Summary and description
- fix menu files
- fix spec

* Tue Dec 27 2005 Led <led@altlinux.ru> 1.6.5-alt2
- mkvinfo moved into sepatate package

* Mon Dec 26 2005 Led <led@altlinux.ru> 1.6.5-alt1
- initial build
