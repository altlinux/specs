Name: tuxguitar
Version: 1.2
Release: alt3

Summary: A multitrack guitar tablature editor and player
License: LGPL
Group: Sound

Url: http://www.tuxguitar.com.ar/

Source: http://prdownloads.sf.net/tuxguitar/tuxguitar-src-%version.tar
Source3: TuxGuitar.png

# Fedora specific build script. Accepted by upstream:
# http://tuxguitar.svn.sourceforge.net/viewvc/tuxguitar/trunk/TuxGuitar/xml/build-fedora.xml
Source11: %name-build-altlinux.xml
# From upstream trunk, to disable certain plugins by default
# http://tuxguitar.svn.sourceforge.net/viewvc/tuxguitar/trunk/TuxGuitar/src/org/herac/tuxguitar/gui/system/plugins/TGPluginProperties.java?r1=99&r2=770
Patch: %name-plugin-properties.patch

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Automatically added by buildreq on Thu Jan 06 2011
BuildRequires: ant-antlr ant-bcel ant-commons-logging ant-commons-net ant-jai ant-jakarta-oro ant-jakarta-regexp ant-javamail ant-jdepend ant-jmf ant-jsch ant-junit ant-log4j ant-nodeps ant-stylebook ant-swing ant-trax ant-xml-resolver checkstyle4 eclipse-swt itext jtidy libfluidsynth-devel libgcj-devel tzdata

BuildRequires: rpm-build-java
#BuildRequires: xml-commons-apis

Requires: eclipse-swt
Requires: itext
Requires: java
BuildRequires: desktop-file-utils

%description
TuxGuitar is a guitar tablature editor with player support through midi.
It can display scores and multitrack tabs. It can open GP3, GP3 and GP5
files.

With TuxGuitar, you will be able to compose music using the following features:
* Tablature editor
* Score Viewer
* Multitrack display
* Autoscroll while playing
* Note duration management
* Various effects (bend, slide, vibrato, hammer-on/pull-off)
* Support for triplets (5,6,7,9,10,11,12)
* Repeat open and close
* Time signature management
* Tempo management
* Imports and exports gp3,gp4 and gp5 files

%prep
%setup -n tuxguitar-src-%version
%patch0 -p1
cp %SOURCE11 TuxGuitar/xml/build-altlinux.xml

%build
test -f %_libdir/java/swt.jar
test -f %_javadir/itext.jar

# disabled plugins: gervill
# Plugins to build:
PLUGINS="alsa ascii browser-ftp community compat converter fluidsynth \
         gtp jack jsa lilypond midi musicxml pdf ptb tef tray"

# JNI's to build
JNIS="alsa fluidsynth jack"

LIBSUFFIX=$(echo %_lib|sed 's|lib||')

# to pass to ant:
ANT_FLAGS=" \
   -Dpath.tuxguitar=$PWD/TuxGuitar/%name.jar \
   -Dpath.itext=%_javadir/itext.jar \
   -Dpath.swt=%_libdir/java/swt.jar \
   -Dlib.swt.jar=%_libdir/java/swt.jar \
   -Ddist.lib.path=%_libdir/%name/ \
   -Ddist.file=xml/build-altlinux.xml \
   -Ddist.jar.path=%_datadir/%name/ \
   -Ddist.share.path=%_datadir/%name/ \
   -Dos.lib.suffix=$LIBSUFFIX \
   -Dos.data.dir=%_datadir/ \
   -Ddist.default.style=Lavender \
   -Ddist.default.song=%_datadir/%name/%name.tg"

# build jars
ant -f TuxGuitar/build.xml -v -d $ANT_FLAGS all
for jarname in $PLUGINS; do
   ant -f TuxGuitar-$jarname/build.xml -v -d $ANT_FLAGS \
      -Dbuild.jar=../TuxGuitar/share/plugins/tuxguitar-$jarname.jar all
done

# build jnis
for jni in $JNIS; do
%make_build -C TuxGuitar-$jni/jni CFLAGS="${RPM_OPT_FLAGS} \
              -I%_jvmdir/java-openjdk/include \
              -I%_jvmdir/java-openjdk/include/linux \
              -fPIC"
done

%install
LIBSUFFIX=$(echo %_lib|sed 's|lib||')

# to pass to ant:
ANT_FLAGS=" \
   -Dpath.tuxguitar=$PWD/TuxGuitar/%name.jar \
   -Dos.bin.dir=%_bindir \
   -Ddist.file=xml/build-altlinux.xml \
   -Ddist.jar.path=%_datadir/%name/ \
   -Ddist.share.path=%_datadir/%name/ \
   -Dos.lib.suffix=$LIBSUFFIX \
   -Dos.data.dir=%_datadir/ \
   -Ddist.default.style=Lavender \
   -Ddist.doc.path=%_docdir/%name-%version/ \
   -Ddist.default.song=%_datadir/%name/%name.tg \
   -Ddist.dst.path=%buildroot"

ant -f TuxGuitar/build.xml -v -d $ANT_FLAGS install

# install jnis we built
mkdir -p %buildroot%_libdir/%name/
cp -a TuxGuitar-*/jni/*.so %buildroot%_libdir/%name/

# icon
install -dm 755 %buildroot%_pixmapsdir/
install -m 644 %SOURCE3 \
	%buildroot%_pixmapsdir/

install -dm 755 %buildroot%_man1dir/
cp -f misc/%name.1 %buildroot%_man1dir/
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Music \
	%buildroot%_desktopdir/tuxguitar.desktop

#%post
#pushd %_javadir/%name/share > /dev/null
#	ln -s %_datadir/%name/* .
#popd  > /dev/null

#%postun
#rm -r %_javadir/%name/share

%files
#doc AUTHORS ChangeLog COPYING LICENSE README
%_docdir/%name-%version/
%_bindir/tuxguitar
#%_libdir/*.so
%_libdir/%name/

%dir %_datadir/%name
%_datadir/%name/*.jar
%_datadir/%name/tuxguitar.tg
%_datadir/%name/plugins/
%_datadir/%name/help/
%_datadir/%name/scales/
%_datadir/%name/lang/
%_datadir/%name/skins/

%_xdgmimedir/packages/%name.xml
%_man1dir/*
%_desktopdir/*.desktop
%_pixmapsdir/*.png

%changelog
* Mon Mar 19 2012 Michael Shigorin <mike@altlinux.org> 1.2-alt3
- rebuilt in current environment (closes: #21801)
- minor spec cleanup

* Tue Oct 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- fix CVE-2010-3385: insecure library loading (ALT bug #24333)

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for tuxguitar

* Thu Jan 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- new version 1.2 (with rpmrb script)
- add requires to eclipse-swt (ALT #24865)
- use Fedora's spec

* Thu Oct 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- subst /usr/lib with %_libdir (fix #21799)
- remove jpackage utils (fix #21521)

* Fri Sep 11 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version 1.1 (with rpmrb script)

* Sat Jun 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version (1.0)
- rewrote spec, use external itext

* Sat May 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0rc4-alt1
- initial build for ALT Linux Sisyphus (thanks to SUSE for spec)

* Fri Apr 04 2008 Toni Graffy <toni@links2linux.de> - 1.0rc3-0.pm.1
- update to 1.0rc3
- changed BuildArch as this package contains two shared libs
- TuxGuitar-alsa is obsoleted now
* Mon Oct 29 2007 Toni Graffy <toni@links2linux.de> - 0.9.1-0.pm.2
- rebuild with new eclipse-swt-gtk2 package
* Wed Jan 31 2007 Toni Graffy <toni@links2linux.de> - 0.9.1-0.pm.1
- update to 0.9.1
* Tue Jan 30 2007 Toni Graffy <toni@links2linux.de> - 0.9-0.pm.1
- update to 0.9
* Wed Sep 27 2006 Toni Graffy <toni@links2linux.de> - 0.8-0.pm.1
- build for packman
- added itext.jar as internal lib
* Sat Sep 02 2006 oc2pus <oc2pus@arcor.de> - 0.8-0.oc2pus.2
- rebuild, change in start-script for alsa-plugin
* Thu Aug 24 2006 oc2pus <oc2pus@arcor.de> - 0.8-0.oc2pus.1
- update to 0.8
* Mon Jul 17 2006 oc2pus <oc2pus@arcor.de> - 0.7-0.oc2pus.1
- update to 0.7
- switched to ant-build
- repacked without lib/* as tar.gz2
* Sun Jun 10 2006 oc2pus <oc2pus@arcor.de> - 0.6-0.oc2pus.2
- corrected desktop-entry
* Sun May 28 2006 oc2pus <oc2pus@arcor.de> - 0.6-0.oc2pus.1
- update to 0.6
- added itext to dependencies
* Sat Apr 08 2006 oc2pus <oc2pus@arcor.de> - 0.5-0.oc2pus.1
- First packaged release 0.5
- repacked without swt.jar and native libs (jameica-swt3-gtk)
