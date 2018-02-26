%define _disable_ld_no_undefined 1

Summary: An open source software for the creation of electronic schematic diagrams
Name: kicad
Version: 20110522
Release: alt2
Source0: %name-%version.tar.bz2
License: GPLv2+
Group: Sciences/Computer science
Url: http://kicad.sourceforge.net/
Packager: Alexey Shentzev <ashen@altlinux.ru>

# Automatically added by buildreq on Fri Feb 13 2009
BuildRequires: boost-devel ccmake cmake cmake-modules gcc-c++ libGL-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel
BuildRequires: libXext-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel
BuildRequires: libXxf86misc-devel libxkbfile-devel wxGTK-devel xorg-xf86vidmodeproto-devel zlib-devel
BuildRequires: fontconfig glibc-pthread libGLU-devel libICE-devel libSM-devel libX11-devel libXdamage-devel libXfixes-devel libXrender-devel
BuildRequires: libgtk+2-common libstdc++-devel wxGTK xorg-inputproto-devel xorg-kbproto-devel xorg-scrnsaverproto-devel xorg-xextproto-devel
BuildRequires: xorg-xf86miscproto-devel xorg-xineramaproto-devel xorg-xproto-devel

BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
Requires: %name-library %name-doc

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad is a set of four softwares and a project manager:

Eeschema :  Schematic entry.
Pcbnew :    Board editor.
Gerbview :  GERBER viewer (photoplotter documents).
Cvpcb :     footprint selector for components used in the circuit design.
Kicad:      project manager.

%prep
%setup -n %name

%build
export LC_ALL=C
cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DCMAKE_INSTALL_PREFIX=/usr -DKICAD_STABLE_VERSION=ON
%make

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/applications
install -p -m 644 resources/linux/mime/applications/* %buildroot%_datadir/applications

mkdir -p %buildroot%_datadir/icons/
cp -r resources/linux/mime/icons/hicolor %buildroot%_datadir/icons/
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Engineering \
	%buildroot%_desktopdir/eeschema.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Engineering \
	%buildroot%_desktopdir/kicad.desktop
#mv %{buildroot}usr/lib/kicad/plugins/netlist_form_pads-pcb.xsl %buildroot%_datadir/%name/


%files
%_bindir/*
%_datadir/%name
%_liconsdir/%name.png
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/*/*/*kicad*
%_datadir/mimelnk/application/*kicad*
%_datadir/mime/packages/kicad.xml
%doc %_datadir/doc/%name

%changelog
* Tue Jun 07 2011 Denis Klimov <zver@altlinux.org> 20110522-alt2
- fix inherit

* Mon Jun 06 2011 Denis Klimov <zver@altlinux.org> 20110522-alt1
- new version

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 20110421-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for kicad

* Fri Apr 22 2011 Denis Klimov <zver@altlinux.org> 20110421-alt1
- new version

* Tue Apr 12 2011 Denis Klimov <zver@altlinux.org> 20110409-alt2
- fix install netlist_form_pads-pcb.xsl for x86_64

* Mon Apr 11 2011 Denis Klimov <zver@altlinux.org> 20110409-alt1
- new version

* Fri Apr 08 2011 Denis Klimov <zver@altlinux.org> 20110401-alt1
- new version

* Mon Mar 28 2011 Denis Klimov <zver@altlinux.org> 20110325-alt1
- new version
- remove patches
- cleanup spec

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 20080825-alt0.2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for kicad
  * postclean-05-filetriggers for spec file

* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 20080825-alt0.2
- fix desktop files

* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 20080825-alt0.1
- first build for ALT Linux

