Name: xorg-drv-openchrome
Version: 0.2.999
Release: alt1
Epoch: 1
Summary: VIA openchrome graphics driver
License: MIT/X11
Group: System/X11
Url: http://www.openchrome.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

BuildRequires(Pre): xorg-sdk xorg-util-macros
BuildRequires: libX11-devel libXext-devel libXvMC-devel xorg-fontsproto-devel
BuildRequires: xorg-randrproto-devel xorg-renderproto-devel libdrm-devel

%description
openchrome  is an Xorg driver for VIA chipsets that have  an integrated
Unichrome graphics engine.

The  openchrome  driver  supports  the  following   chipsets:   CLE266,
KM400/KN400,   CN400,  CN700,  K8M800/K8N800,  PM800/PN800,  P4M800Pro,
VN800, PM880, K8M890/K8N890, CN896,  VN896,  and  P4M900.   The  driver
includes  2D acceleration and Xv video overlay extensions.  Flat panel,
TV, and VGA outputs are supported, depending on the hardware configura-
tion.

Direct rendering 3D is available using experimental  drivers  in  Mesa,
www.mesa3d.org.   Also  there  is  an  XvMC client library for hardware
MPEG1 /  MPEG2  decoding  acceleration  available  on  the  CLE266  and
K8M/N800  chipsets  that uses the Direct Rendering Infrastructure, DRI.
The XvMC client library implements a nonstandard "VLD" extension to the
XvMC standard. The current Direct Rendering Manager Linux kernel module
is available at dri.sourceforge.net.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-dri \
	--disable-static

echo "#undef XF86DRI" >> config.h
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc NEWS README
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.999-alt1
- requires XORG_ABI_VIDEODRV = 12.0

* Mon Feb 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.905-alt1
- 0.3.0 RC5
- disabled dri

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.904-alt9
- requires XORG_ABI_VIDEODRV = 11.0
- SVN revision 933

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.904-alt8
- requires XORG_ABI_VIDEODRV = 10.0

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.904-alt7
- updated build dependencies
- SVN revision 919

* Wed Dec 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.904-alt6
- fixed requires

* Fri Dec 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.904-alt5
- SVN revision 890
- added VX900 support

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.904-alt4
- requires XORG_ABI_VIDEODRV = 8.0

* Thu Mar 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.904-alt3
- SVN revision 841

* Sun Jan 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.904-alt2.svn830
- SVN revision 830

* Fri Oct 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.904-alt1
- 0.3.0 RC4

* Fri Sep 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt18
- SVN revision 787

* Sat Sep 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt17
- SVN revision 782

* Thu Aug 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt16
- SVN revision 773:
  + RandR initial support

* Thu Jul 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt15
- SVN revision 760

* Fri Jul 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt14
- SVN revision 758:
  + added VX855 support

* Tue Jul 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt13
- SVN revision 755:
  + Sharp PC-AE30J

* Fri Jun 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt12
- SVN revision 753

* Wed Mar 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt11
- SVN revision 740:
  + fixed 2D engine initialization
  + added support for CX700 integrated TMDS encoder

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt10
- SVN revision 735
- requires XORG_ABI_VIDEODRV = 5.0

* Mon Feb 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt9
- SVN revision 726:
  + small bug fixes for XAA and EXA

* Wed Jan 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt8
- SVN revision 712:
  + initial XVideo support for VX800

* Sun Dec 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt7
- SVN revision 695:
  + Axper XP-M8VM800
  + VIA Epia M700

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt6
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Nov 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt5
- SVN revision 685:
  + initial VX800 support

* Thu Oct 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt4
- SVN revision 595:
  + native mode setting for P4M890, P4M900, K8M890 and CX700
  + LVDS power functions for P4M900 and CX700
  + ARGB hardware cursor support

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt3
- requires XORG_ABI_VIDEODRV = 4.1

* Sun Aug 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt2
- added Gigabyte M704 / RoverPC A700GQ

* Thu Aug 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.903-alt1
- 0.3.0 RC3

* Tue Jul 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.902-alt4
- SVN revision 581:
  + ECS CLE266
  + MSI VR321

* Fri Jun 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.902-alt3
- rewrite spec for gear

* Tue Jun 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.902-alt2
- SVN revision 572
- renamed xorg-x11-drv-openchrome to xorg-drv-openchrome
- added requires XORG_ABI_VIDEODRV = 2.0
- convert xinf to fdi

* Sat Mar 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.902-alt1
- 0.3.0 RC2

* Tue Mar 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.901-alt4
- SVN revision 554:
  + Mitac 8624 aka Benq Joybook R42
  + Mitac 8515
  + Clevo M660SR
- obsoletes xorg-x11-drv-via
  
* Wed Feb 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.901-alt3
- SVN revision 532:
  + Asustek P5VD2-VM SE
  + Biostar P4M800 Pro-M7
  + Medion Notebook MD96483
  + VIA Epia SN
  + Apollo BMOVE SR

* Thu Jan 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.901-alt2
- update xinf file

* Fri Jan 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.901-alt1
- 0.3.0 RC1

* Wed Nov 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.900-alt0.svn447
- SVN revision 447

* Sun Oct 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.900-alt0.svn420
- 0.3.0 RC

* Thu Oct 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt2.svn406
- SVN revision 406:
  + fix memory detection for P4M900 and CX700

* Mon Oct 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt2.svn401
- new pci ids

* Wed Sep 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt2.svn395
- SVN revision 395

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt2.svn393
- SVN revision 393

* Mon Jul 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt2.svn371
- added ASRock P4VM890

* Thu Jun 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt2.svn363
- added Everex NC1501/NC1503

* Wed Jun 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt2.svn357
- fixed xf86DrvMsg (ViaXvMC -> OpenChromeXvMC)

* Tue Jun 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt1.svn357
- SVN revision 357
- rename to openchrome_drv
- remove Conflicts: xorg-x11-drv-via
- added openchrome.xinf

* Tue Feb 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt1.svn295
- SVN revision 295

* Sat Dec 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt1.svn280
- SVN revision 280

* Thu Dec 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt1.svn256
- SVN revision 256

* Sun Sep 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt1.svn216
- SVN revision 216

* Fri Sep 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt1.svn213
- SVN revision 213

* Thu Aug 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt1.svn208
- SVN revision 208

* Thu Aug 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt1.svn202
- SVN revision 202

* Mon May 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.1-alt1
- 0.2.1

* Sun Mar 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.33.1-alt2
- Obsoletes xorg-x11-drv-via

* Fri Mar 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.33.1-alt1
- 0.1.33.1

* Tue Jan 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.32-alt3
- SVN snapshot 20060112

* Sun Jan 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.32-alt2
- SVN snapshot 20060108

* Fri Dec 30 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.32-alt1
- SVN snapshot 20051229
