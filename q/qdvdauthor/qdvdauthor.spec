%define rel %nil
Name: qdvdauthor
Version: 1.5.0
Release: alt2.qa3

Summary: The GUI frontend for dvdauthor and other related tools

License: GPL
Group: Video
Url: http://sourceforge.net/projects/qdvdauthor/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version%rel.tar.bz2
# remove make from configure :)
Patch: %name.patch
Patch1: %name-1.5.0-alt-DSO.patch

# manually removed: nvidia_glx_169.12 qt3-designer
# Automatically added by buildreq on Wed Nov 12 2008
BuildRequires: dvdauthor gcc-c++ kdepim-devel mjpegtools mplayer

Requires: mplayer dvdauthor >= 0.6.10 bzip2 ImageMagick lame
Requires: mjpegtools sox netpbm vorbis-tools
BuildRequires: desktop-file-utils

%description
qdvdauthor is a gui frontend for using dvdauthor and dvd-slideshow
scripts to easily build DVD menus and assemble the DVD VOB files.
Build with MPlayer for playing.

%prep
%setup -q
# remove make from configure :)
sed -i "s|cd qdvdauthor|exit 0|g" configure
#%patch
%patch1 -p2

%build
unset QTDIR || : ; . %_sysconfdir/profile.d/qt3dir.sh
export PATH=$QTDIR/bin:$PATH
./configure --qt-dir=%_qt3dir \
	--with-mplayer-support

# move from configure here
export WITH_MPLAYER_SUPPORT=1
export QT_LIB=qt-mt
cd qdvdauthor
$QTDIR/bin/qmake qdvdauthor.pro CONFIG+=no_fixpath
%make_build

cd qslideshow
$QTDIR/bin/qmake qslideshow.pro CONFIG+=no_fixpath
%make_build
cd ..

cd qplayer;
$QTDIR/bin/qmake qplayer.pro CONFIG+=no_fixpath
%make_build
cd ..

#cd qrender;
#$QTDIR/bin/qmake qrender.pro CONFIG+=no_fixpath
#make_build

%install
unset QTDIR || : ; . %_sysconfdir/profile.d/qt3dir.sh
export PATH=$QTDIR/bin:$PATH
make install INSTALL_ROOT=%buildroot

# due strange mainstream install 
#mkdir -p %buildroot%_bindir
mkdir -p %buildroot{%_pixmapsdir,%_desktopdir,%_datadir/%name}
#install -s -m 0755 bin/qdvdauthor %buildroot%_bindir
#install -s -m 0755 bin/qslideshow %buildroot%_bindir
#install -s -m 0755 bin/qplayer %buildroot%_bindir
install -m 0644 silence.mp2 %buildroot%_datadir/%name

install -m 0644 qdvdauthor.png %buildroot%_pixmapsdir
install -m 0644 qdvdauthor.desktop %buildroot%_desktopdir
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=DiscBurning \
	%buildroot%_desktopdir/qdvdauthor.desktop

#%find_lang %name

%files
%doc README TODO CHANGELOG
%_bindir/qdvdauthor
%_bindir/qplayer
%_bindir/qslideshow
#%_bindir/qrender
%_datadir/%name/
%_pixmapsdir/qdvdauthor.png
%_desktopdir/qdvdauthor.desktop

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.qa3
- Fixed build

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.5.0-alt2.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qdvdauthor
  * postclean-03-private-rpm-macros for the spec file

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.5.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for qdvdauthor
  * postclean-05-filetriggers for spec file

* Sat Feb 21 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- remove strage build requires

* Wed Nov 12 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)
- update buildreq
- drop qrender (Qt4 app)

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Tue Apr 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (fix bug #14299)

* Thu Jan 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- release 1.0.0
- clean spec, rewrote build process, enable SMP-build

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1beta3
- new version
- cleanup spec, update buildreqs
- strip binary files

* Sat Dec 30 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt0.1beta
- new version, cleanup spec, remove COPYING
- change packager
- update buildreq, fix requires
- build with mplayer

* Wed Dec 22 2004 Alex Yustasov <yust@altlinux.ru> 0.0.9-alt1
- initial release
