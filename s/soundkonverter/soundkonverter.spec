%define qtdir %_qt3dir
%define kdedir %_K3prefix

%def_without mp4v2
# TODO:
# - enable mp4 support (configure fails to find headers)

Name: soundkonverter
Version: 0.3.9
Release: alt8

%define Name soundKonverter

Summary: A frontend to various audio converters
License: %gpl2only
Group: Sound

Url: http://www.kde-apps.org/content/show.php/%Name?content=29024
Source: http://hessijames.googlepages.com/%name-%version.tar
Patch: %name-%version-%release.patch
Patch1: tde-3.5.13-build-defdir-autotool.patch
Patch2: cvs-auto_version_check.patch
Packager: Roman Savochenko <rom_as@altlinux.ru>

Requires: vorbis-tools vorbisgain wavpack speex flac cdparanoia mppenc
Requires: faad

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Fri May 16 2008
BuildRequires: gcc-c++ imake kdelibs-devel libXt-devel
BuildRequires: libcdparanoia-devel libdnet-devel libjpeg-devel
BuildRequires: libtag-devel xml-utils xorg-cf-files

%description
%Name project is a frontend to various audio converters.
Currently supported backends are oggenc, oggdec, flac, lame, ffmpeg
(partly), mplayer (partly).
With %Name you can convert between various audio file formats.
Supported formats are: (encode/decode)
    ogg (e/d)
    flac (e/d)
    mp3 (e/d)
    wav (e/d)
    wma (d)

%prep
%setup
%patch -p1
%patch1
%patch2

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common

# for i in acinclude.m4 admin/acinclude.m4.in configure
# do
# 	sed -i 's|mcopidl|mcopidl-tqt|g' $i
# done

%build
# add_optflags -I%_includedir/tqtinterface
# make_build -f Makefile.cvs
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%kdedir

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

%configure \
    --disable-rpath \
    --enable-nmcheck \
    --enable-final \
    --enable-new-ldflags \
    --enable-pch \
    --with-pic \
		--without-arts \
    %{subst_with mp4v2} \
    --with-qt-libraries=%_libdir/qt3/lib 

%make_build
bzip2 --keep --force --best ChangeLog

%install
%make_install DESTDIR=%buildroot install
mv %buildroot%_datadir/apps/%name/amarokscript/README{,.html}
%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS ChangeLog.* README
%_bindir/%name
%_desktopdir/kde/*
%_docdir/HTML/en/%name
%_iconsdir/hicolor/*/*/*
%_datadir/apps/%name
%attr(755,root,root) %_datadir/apps/%name/amarokscript/*.rb
%_datadir/apps/konqueror/servicemenus/*
%_datadir/mimelnk/*/*

%changelog
* Thu Apr 26 2012 Roman Savochenko <rom_as@altlinux.ru> 0.3.9-alt8
- Automake version check for 1.11.5 fixed.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.3.9-alt7
- Build for TDE 3.5.13 release

* Fri Apr 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt6.1
- Fixed build

* Tue Sep 29 2009 Michael Shigorin <mike@altlinux.org> 0.3.9-alt6
- dropped Requires: faac (closes: #21723)

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 0.3.9-alt5
- appled patch by prividen@ to close drive tray (Closes: #20001)
- spec cleanup

* Mon May 25 2009 Michael Shigorin <mike@altlinux.org> 0.3.9-alt4.1
- rebuilt for Sisyphus, thanks led@ for fixups

* Thu May 21 2009 Led <led@altlinux.ru> 0.3.9-alt4
- support automake 1.11

* Sat May 16 2009 Led <led@altlinux.ru> 0.3.9-alt3
- fixed build with g++ 4.4

* Mon Feb 16 2009 Led <led@altlinux.ru> 0.3.9-alt2
- cleaned up spec

* Mon Nov 10 2008 Led <led@altlinux.ru> 0.3.9-alt1
- 0.3.9
- updated %name.desktop

* Fri Aug 08 2008 Led <led@altlinux.ru> 0.3.8-alt2
- fixed %name.desktop

* Wed Jun 18 2008 Led <led@altlinux.ru> 0.3.8-alt1
- 0.3.8
- fixed URL
- cleaned up spec

* Fri May 16 2008 Led <led@altlinux.ru> 0.3.7-alt0.1
- 0.3.7:
  + sox plugin for aiff
  + toolame and twolame plugins for mp2 encoding
  + amr decoding with ffmpeg
  + flake plugin
  + wavpack encoding
- cleaned up BuildRequires

* Sun Feb 24 2008 Michael Shigorin <mike@altlinux.org> 0.3.6-alt3
- rebuild
  + hardwire autocrap versions
  + disable autoreconf
  + updated buildrequires
  + thx gorev@ for figuring things out

* Wed Dec 26 2007 Michael Shigorin <mike@altlinux.org> 0.3.6-alt2
- fix build with current autotools, nothing more
  (there seem to be no more versions)

* Mon Sep 17 2007 Michael Shigorin <mike@altlinux.org> 0.3.6-alt1
- 0.3.6
- official site seems down, had to locate source by hand

* Mon Jan 29 2007 Michael Shigorin <mike@altlinux.org> 0.3.1-alt1
- built for ALT Linux (spec from Mandriva cooker)
- heavy spec cleanup
