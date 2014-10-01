Name: libmediainfo
Version: 0.7.70
Release: alt1

Group: System/Libraries
Summary: %name - Shared library for mediainfo
License: LGPL
Url: http://mediainfo.sourceforge.net
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Source0: %{name}_%{version}.tar.bz2

# Automatically added by buildreq on Sat Dec 03 2005
BuildRequires: gcc-c++ automake autoconf libtool
BuildRequires: dos2unix
BuildRequires: doxygen
BuildRequires: zlib-devel
BuildRequires: libmms-devel
BuildRequires: id3lib-devel
BuildRequires: pkg-config
BuildRequires: libflac-devel
BuildRequires: libmatroska-devel
BuildRequires: libfaad-devel
BuildRequires: libzen-devel >= 0.4.29
BuildRequires: libcurl-devel
#Can't compile using g++ because of "this" vars in definitions
#BuildRequires: libmms-devel

%package devel
Group: System/Libraries
Summary: Devel package for %name
Requires: %name = %version
Provides: %name.so

%description
MediaInfo supplies technical and tag information about a video or audio file.
What information can I get from MediaInfo?
General: title, author, director, album, track number, date, duration...
Video: codec, aspect, fps, bitrate...
Audio: codec, sample rate, channels, language, bitrate...
Text: language of subtitle
Chapters: number of chapters, list of chapters

What format (container) does MediaInfo support?
Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
       MPEG-4, DVD (VOB)...
(Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF...
Subtitles: SRT, SSA, ASS, SAMI...

This package includes the shared library

%description devel
This package includes the development support files of the libmediainfo

%prep
%setup -q -T -b 0 -n MediaInfoLib

%build
#dos2unix      *.txt Source/Doc/*.txt
#chmod 644    *.txt Source/Doc/*.txt
pushd Source/Doc
doxygen Doxyfile
popd
#cp Source/Doc/*.txt ./
pushd Project/GNU/Library
%autoreconf
%configure --enable-shared=yes --enable-static=no --with-libcurl=system --with-libmms=system
%make
popd

%install
pushd Project/GNU/Library
%makeinstall
popd
# Add here commands to install the package
install -dm 755 %buildroot%_includedir/MediaInfo/{Duplicate,Multiple,Tag}/
install -m 644 Source/MediaInfo/*.h %buildroot%_includedir/MediaInfo
install -m 644 Source/MediaInfo/Duplicate/*.h %buildroot%_includedir/MediaInfo/Duplicate
install -m 644 Source/MediaInfo/Multiple/*.h %buildroot%_includedir/MediaInfo/Multiple
install -m 644 Source/MediaInfo/Tag/*.h %buildroot%_includedir/MediaInfo/Tag
install -m 644 Source/ThirdParty/tinyxml2/tinyxml2.h %buildroot%_includedir/MediaInfo/
install -m 644 Source/ThirdParty/aes-gladman/*.h %buildroot%_includedir/MediaInfo/
install -m 644 Source/ThirdParty/md5/*.h %buildroot%_includedir/MediaInfo/

install -dm 755 %buildroot%_includedir/MediaInfoDLL
install -m 644 Source/MediaInfoDLL/*.h %buildroot%_includedir/MediaInfoDLL
install -m 644 Source/MediaInfoDLL/MediaInfoDLL.cs %buildroot%_includedir/MediaInfoDLL
install -m 644 Source/MediaInfoDLL/MediaInfoDLL.*.java %buildroot%_includedir/MediaInfoDLL
install -m 644 Source/MediaInfoDLL/MediaInfoDLL*.py %buildroot%_includedir/MediaInfoDLL

sed -i -e 's|Version: |Version: %{version}|g' Project/GNU/Library/libmediainfo.pc
install -dm 755 %buildroot%_pkgconfigdir
install -m 644 Project/GNU/Library/libmediainfo.pc %buildroot%_pkgconfigdir

%files
%doc ReadMe.txt
%_libdir/*.so.*

%files devel
%_includedir/MediaInfo
%_includedir/MediaInfoDLL
%_pkgconfigdir/libmediainfo.pc
%_libdir/*.so

%changelog
* Wed Oct 01 2014 Motsyo Gennadi <drool@altlinux.ru> 0.7.70-alt1
- 0.7.70

* Sat Feb 18 2012 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.53-alt1
- New version
- Add libmms test build support

* Sat Dec 03 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.51-alt1
- New version

* Thu Jul 21 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.47-alt1
- New version

* Sun Mar 06 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.42-alt1
- New version

* Mon Feb 28 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.41-alt1
- New version

* Mon Oct 18 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.35-alt1
- New version

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt4
- Rebuild

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt3
- Remove libmms support due to continious error in libmms

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt2
- Add libmms support

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt1
- New version

* Mon Nov 23 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.25-alt1
- New version

* Thu Nov 12 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.24-alt1
- initial build
