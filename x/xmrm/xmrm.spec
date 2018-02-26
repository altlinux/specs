Name: xmrm
Version: 2.0
%define lversion 20
Release: alt6

Summary: Multi Resolution Morphing for X
License: GPL
Group: Graphics

Packager: Fr. Br. George <george@altlinux.ru>

#BuildRequires: libgimp2-devel
Url: http://www.cg.tuwien.ac.at/~xmrm
Source0: %name%{lversion}_sources.tgz
Source1: %name.png
Patch0: xmrm.Makefile.patch
Patch1: xmrm.const.h.patch
Patch2: xmrm.io.cc.patch
Patch3: xmrm.io.h.patch
Patch4: xmrm.morphvec.cc.patch
Patch5: xmrm.xmrm.cc.patch
Patch6: xmrm.xmrm_main.cc.patch
Patch7: xmrm.xmrm_mpeg_main.cc.patch
Patch8: xmrm.gcc44.patch

%def_disable static

# Automatically added by buildreq on Sat May 23 2009
BuildRequires: gcc-c++ libX11-devel libtiff-devel libxforms-devel

%description
XMRM (stands for Multi Resolution Morphing for X) is an image morphing program written for XWindow. A special feature of this program is the ability to control the morphing speed of details in relation to the morphing speed of big features. Basic morphing ahs simple vector-driven interface.

%prep
%setup -cq
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%make_build

%install
install -D %name $RPM_BUILD_ROOT/%_x11bindir/%name

install -m755 -d %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=MR Morphing for X
Comment=an image morphing program written for XWindow
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Graphics;2DGraphics;RasterGraphics;
EOF

install -Dm644 %{SOURCE1} %buildroot%_liconsdir/%{name}.xpm

%files
%_x11bindir/%name
%doc README.TXT 
%_desktopdir/%{name}.desktop
%_liconsdir/%{name}.xpm

%changelog
* Thu Apr 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt6
- rebuild with new libxforms
- added .desktop file
- added menu pixmap

* Sat May 23 2009 Fr. Br. George <george@altlinux.ru> 2.0-alt5
- GCC4.4 build fixup

* Sat Oct 07 2006 Fr. Br. George <george@altlinux.ru> 2.0-alt4
- GEAR adapted

* Mon Feb 20 2006 Fr. Br. George <george@altlinux.ru> 2.0-alt3
- XOrg7 adaptation

* Wed Dec 21 2005 Fr. Br. George <george@altlinux.ru> 2.0-alt2
- Some code cleansing, vectors are drawn properly

* Tue Dec 20 2005 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Initial build with pile of patches 

