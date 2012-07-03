Name: nvidia-xconfig
Version: 295.20
Release: alt1

Group: System/Configuration/Hardware
Summary: Command line tool for setup X11 for the NVIDIA driver
Url: ftp://download.nvidia.com/XFree86/nvidia-xconfig/
License: GPLv2

Source: %name-%version.tar.gz
Patch1: nvidia-xconfig-1.0-alt-fix-linking.patch
Patch2: flags.patch

BuildRequires: glibc-devel-static

%description
Command line tool for setup X11 for the NVIDIA driver

%prep
%setup -q
#%patch1 -p1
%patch2 -p1

%build
%add_optflags -I XF86Config-parser
%make_build CC=gcc LOCAL_CFLAGS="%optflags" LOCAL_LDFLAGS="-L/usr/lib -L/usr/lib64"

%install
make install bindir=%buildroot/%_bindir mandir=%buildroot/%_man1dir
#mkdir -p %buildroot/%_bindir
#install -m 0755 nvidia-xconfig %buildroot/%_bindir

%files
%_bindir/%name
%_man1dir/%name.*


%changelog
* Wed Feb 15 2012 Sergey V Turchin <zerg@altlinux.org> 295.20-alt1
- new version

* Thu Jan 19 2012 Sergey V Turchin <zerg@altlinux.org> 290.10-alt0.M60P.1
- built for M60P

* Thu Jan 19 2012 Sergey V Turchin <zerg@altlinux.org> 290.10-alt1
- new version

* Mon Jun 20 2011 Sergey V Turchin <zerg@altlinux.org> 275.09.07-alt1
- new version

* Wed Apr 13 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.03-alt1
- new version

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 260.19.29-alt1
- new version

* Mon Sep 13 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt0.M51.1
- built for M51

* Mon Sep 13 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt1
- new version

* Thu Jul 15 2010 Sergey V Turchin <zerg@altlinux.org> 256.35-alt0.M51.1
- built for M51

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 256.35-alt1
- new version

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.15-alt0.M51.1
- build for M51

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.15-alt1
- new version

* Thu Feb 04 2010 Sergey V Turchin <zerg@altlinux.org> 190.53-alt0.M51.1
- built for M51

* Thu Feb 04 2010 Sergey V Turchin <zerg@altlinux.org> 190.53-alt1
- new version

* Mon Aug 17 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.31-alt1
- new version

* Fri Jun 26 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.14-alt1
- new version

* Fri Mar 20 2009 Sergey V Turchin <zerg@altlinux.org> 180.29-alt1
- new version
- don't use deprecated macroses

* Mon Sep 01 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt12
- update tarball

* Wed Feb 27 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt11
- update tarball 

* Fri Jan 25 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt10
- update tarball

* Fri Dec 21 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt9
- update tarball

* Tue Oct 23 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt8
- update tarball

* Fri Jun 22 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt7
- update tarball

* Sat Jun 09 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt6
- update tarball

* Wed Oct 11 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt5
- update tarball

* Fri Apr 14 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt4
- fix linking

* Tue Apr 11 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt3
- update tarball

* Mon Mar 27 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt2
- fix linking

* Mon Dec 26 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- initial spec

