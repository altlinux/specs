%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# LTO causes errors on armh, disable it
%global optflags_lto %nil

%def_disable debug
%def_disable profiling

%def_enable qt
%def_with flac
%def_with dvdread

%undefine _configure_gettext

Name: mkvtoolnix
Version: 75.0.0
Release: alt1
Summary: Tools to create, alter and inspect Matroska files
License: GPL-2
Group: Video
Url: https://mkvtoolnix.download/

# https://gitlab.com/mbunkus/mkvtoolnix.git
Source: %name-%version.tar

Provides: mkvmerge = %EVR

BuildRequires(pre): rpm-build-xdg
BuildRequires: gcc-c++ boost-devel boost-filesystem-devel zlib-devel libmagic-devel
BuildRequires: libgmp-devel
BuildRequires: libvorbis-devel libogg-devel
BuildRequires: ruby ruby-stdlibs ruby-tools
BuildRequires: libebml-devel >= 1.4.4 libmatroska-devel >= 1.7.1 libfmt-devel >= 6.1.0
BuildRequires: docbook-style-xsl xsltproc
BuildRequires: libpugixml-devel
BuildRequires: po4a
BuildRequires: libgtest-devel
BuildRequires: libpcre2-devel
BuildRequires: libutfcpp-devel
BuildRequires: nlohmann-json-devel

%{?_enable_qt:BuildRequires: qt5-base-devel qt5-tools qt5-multimedia-devel qt5-svg-devel cmark-devel}
%{?_with_flac:BuildRequires: libflac-devel}
%{?_with_dvdread:BuildRequires: libdvdread-devel}

%description
Matroska is a new multimedia file format aiming to become the new
container format for the future.
With these tools one can extract tracks/data from (mkvextract) Matroska
files and create (mkvmerge) Matroska files from other media files.

%if_enabled qt
%package gui
Summary: GUI for mkvmerge including a chapter editor
Group: Video
Provides: mmg = %EVR
Provides: mkvmerge-gui = %EVR
Obsoletes: mkvmerge-gui < %EVR
Requires: %name = %EVR
Requires: mkvinfo = %EVR

%description gui
Matroska is a new multimedia file format aiming to become the new
container format for the future.
mkvmerge GUI is a Qt based GUI for mkvmerge. It offers easy
access to all of mkvmerge's options. All settings (e.g. source files,
track options etc) can be saved and restored. Included is a chapter
editor that can read OGM style and XML style chapter files, write XML
style chapter files and even read chapters from Matroska files and
write chapters directly to Matroska files.
%endif

%package -n mkvinfo
Summary: Tool for print information about tracks in Matroska files
Group: Video

%description -n mkvinfo
Matroska is a new multimedia file format aiming to become the new
container format for the future.
With mkvinfo you can get information about Matroska files. This program
lists all tracks contained in a Matroska file including information
about the codecs used.

%prep
%setup

# remove some bundled libraries
rm -rf lib/nlohmann-json lib/pugixml lib/utf8-cpp

%ifarch %e2k riscv64
sed -i 's,aarch64,&|riscv64|e2k,' ac/ax_boost_base.m4
%endif

%build
./autogen.sh
%configure \
    --disable-update-check \
    --disable-optimization \
    %{subst_enable debug} \
    %{subst_enable profiling} \
    %{subst_enable qt} \
%if_enabled qt
    ac_cv_path_LCONVERT=%_bindir/lconvert-qt5 \
%endif
    %{subst_with flac} \
    %{subst_with dvdread} \
    %nil

rake V=1

%install
rake DESTDIR=%buildroot install

%find_lang --with-man %name
%find_lang --with-man %name-gui
%find_lang --with-man mkvextract
%find_lang --with-man mkvmerge
%find_lang --with-man mkvpropedit
%find_lang --with-man mkvinfo

cat mkvextract.lang mkvmerge.lang mkvpropedit.lang >> %name.lang

%check
rake V=1 tests:unit
rake V=1 tests:run_unit

%files -f %name.lang
%doc COPYING
%doc AUTHORS NEWS.md README.md CODE_OF_CONDUCT.md
%doc examples
%_bindir/mkvextract
%_bindir/mkvmerge
%_bindir/mkvpropedit
%_man1dir/mkvextract.*
%_man1dir/mkvmerge.*
%_man1dir/mkvpropedit.*
%_iconsdir/hicolor/*/apps/mkvextract.*
%_iconsdir/hicolor/*/apps/mkvmerge.*
%_iconsdir/hicolor/*/apps/mkvpropedit.*

%files -n mkvinfo -f mkvinfo.lang
%doc COPYING
%doc AUTHORS NEWS.md README.md CODE_OF_CONDUCT.md
%_bindir/mkvinfo
%_man1dir/mkvinfo.*
%_iconsdir/hicolor/*/apps/mkvinfo.*

%if_enabled qt
%files gui -f %name-gui.lang
%doc COPYING
%doc AUTHORS NEWS.md README.md CODE_OF_CONDUCT.md
%_bindir/%name-gui
%_man1dir/%name-gui.*
%_iconsdir/hicolor/*/apps/%name-gui.*
%_desktopdir/org.bunkus.%name-gui.desktop
%_xdgmimedir/packages/org.bunkus.%name-gui.xml
%_datadir/mkvtoolnix/sounds/*.webm
%_datadir/metainfo/org.bunkus.%name-gui.appdata.xml
%endif

%changelog
* Wed Mar 29 2023 L.A. Kostis <lakostis@altlinux.ru> 75.0.0-alt1
- 75.0.0.

* Mon Feb 20 2023 L.A. Kostis <lakostis@altlinux.ru> 74.0.0-alt1
- 74.0.0.

* Thu Jan 19 2023 L.A. Kostis <lakostis@altlinux.ru> 73.0.0-alt1
- 73.0.0.

* Thu Dec 29 2022 L.A. Kostis <lakostis@altlinux.ru> 72.0.0-alt1
- NMU update:
  + 71.0.0 -> 72.0.0.
  + disable optimization (use RPM cflags instead).

* Sun Nov 13 2022 L.A. Kostis <lakostis@altlinux.ru> 71.0.0-alt1
- NMU update:
  + 65.0.0 -> 71.0.0 (fixes FTBFS).

* Wed Feb 16 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 65.0.0-alt2
- Updated interpackage dependencies (Closes: #41966).

* Thu Feb 10 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 65.0.0-alt1
- Updated to upstream version 65.0.0.

* Thu Jan 13 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 64.0.0-alt1
- Updated to upstream version 64.0.0.

* Tue Dec 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 63.0.0-alt1
- Updated to upstream version 63.0.0.

* Fri Sep 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 61.0.0-alt1
- Updated to upstream version 61.0.0.

* Thu Aug 05 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 60.0.0-alt1
- Updated to upstream version 60.0.0.

* Fri Jul 23 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 59.0.0-alt1
- Updated to upstream version 59.0.0.

* Wed Jun 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 58.0.0-alt1
- Updated to upstream version 58.0.0.

* Fri Jun 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 57.0.0-alt1
- Updated to upstream version 57.0.0.
- Unbundled libraries.

* Mon Mar 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 55.0.0-alt1
- Updated to upstream version 55.0.0.

* Wed Feb 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 53.0.0-alt1
- Updated to upstream version 53.0.0.

* Fri Jan 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 52.0.0-alt1
- Updated to upstream version 52.0.0.

* Fri Oct 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 51.0.0-alt1
- Updated to upstream version 51.0.0.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 50.0.0-alt1
- Updated to upstream version 50.0.0.

* Wed Aug 19 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 49.0.0-alt1
- Updated to upstream version 49.0.0.
- Enabled dvdread support.
- Enabled tests.

* Wed Jul 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 48.0.0-alt1
- Updated to upstream version 48.0.0.

* Fri Jul 10 2020 Michael Shigorin <mike@altlinux.org> 47.0.0-alt2
- e2k, riscv64: fix broken boost.m4

* Fri Jun 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 47.0.0-alt1
- Updated to upstream version 47.0.0.

* Fri Apr 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 45.0.0-alt1
- Updated to upstream version 45.0.0.

* Tue Feb 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 43.0.0-alt1
- Updated to upstream version 43.0.0.

* Mon Sep 02 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 37.0.0-alt1
- Updated to upstream version 37.0.0.

* Thu Jul 25 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 35.0.0-alt1
- Updated to upstream version 35.0.0 (Closes: #36879).

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 23.0.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 23.0.0-alt2
- NMU: remove %%ubt from release

* Tue May 29 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 23.0.0-alt1
- Updated to upstream version 23.0.0.

* Thu Jun 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 12.0.0-alt1
- Update to 12.0.0

* Fri Sep 02 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.4.0-alt1
- 9.4.0 released

* Thu Jul 23 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.2.0-alt1
- 8.2.0 released

* Wed Jul 15 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.1.0-alt1
- 8.1.0 released

* Sat Mar 14 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.7.0-alt2
- rebuilt with wxGTK 3.1

* Wed Mar 11 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.7.0-alt1
- 7.7.0 released

* Fri Jan 16 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.5.0-alt1
- 7.5.0 released

* Sun Nov 02 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.3.0-alt1
- 7.3.0 released

* Sun Sep 14 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.2.0-alt1
- 7.2.0 released

* Sun Apr 14 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.0-alt1
- 6.1.0 released

* Mon Dec 10 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.9.0-alt1
- 5.9.0 released

* Tue Sep 11 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.7.0-alt1
- 5.7.0 released

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
- Fixed Requires/Provides for %%gname package

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
