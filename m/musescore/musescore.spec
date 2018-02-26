%define rname mscore

Name: musescore
Version: 1.2
Release: alt1

Summary: A free WYSIWYG music score typesetter

License: GPL2
Group: Sound
Url: http://mscore.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%rname/%rname-%version.tar
Source1: mscore.desktop
Patch1: mscore-dso-linking.patch

BuildPreReq: chrpath

# Automatically added by buildreq on Thu Jan 06 2011
BuildRequires: ccmake doxygen gcc-c++ ghostscript-utils graphviz latex2html libalsa-devel libjack-devel libportaudio2-devel libsndfile-devel qt4-designer

# needed for qt.core and so on in JavaScript plugins
Requires: qtscriptbindings

%description
MuseScore is a graphical music typesetter. It allows for fast
and easy note entry on a virtual note sheet. It has an
integrated sequencer to allow for immediate play of the score.
MuseScore can import and export MusicXml and standard Midi files.

Run
"modprobe snd-seq" as root
if you get ALSA lib seq_hw.c:457:(snd_seq_hw_open) open /dev/snd/seq failed: No such file or directory

%prep
%setup -n %rname-%version
sed -i "s| -m32||g" mscore/CMakeLists.txt
%patch1 -p1 -b .dso

%build
export PATH=$PATH:%_qt4dir/bin
mkdir build && cd build
cmake \
	-DCMAKE_BUILD_TYPE=RELEASE \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
        -DBUILD_SCRIPTGEN=FALSE \
	../mscore
# compile translations
make lrelease
# run build
%make_build
make doxy
cp %SOURCE1 .

%install
cd build
%makeinstall_std

chrpath -d %buildroot%_bindir/mscore

%files
%_bindir/mscore
%_desktopdir/mscore.desktop
%_datadir/mscore-1.2/
%_qt4dir/plugins/designer/libawlplugin.so
%_pixmapsdir/mscore.*

%changelog
* Sat Jun  2 2012 Terechkov Evgenii <evg@altlinux.org> 1.2-alt1
- 1.2

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.3-alt1.1
- Removed bad RPATH

* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.6.3-alt1
- new version (ALT bug 23626), update buildreqs
- fix dependencies (ALT bug #21884)

* Tue Apr 21 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- new version 0.9.4 (with rpmrb script), fix bug #19710
- update buildreqs

* Mon Jun 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux Sisyphus

* Sun Feb 10 2008 - Carlos Goncalves <cgoncalves@opensuse.org>
- updated to version 0.9.1

* Tue Jul 31 2007 - Carlos Goncalves <cgoncalves@opensuse.org>
- updated to version 0.6.1
 * This is a bugfix release fixing the midi import crash and adding some small usability enhancements.

* Sun Jul 29 2007 - Carlos Goncalves <cgoncalves@opensuse.org>
- initial package
