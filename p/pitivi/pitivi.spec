%define ver_major 0.94
%define gst_api_ver 1.0
%define gst_ver 1.4.0

Name: pitivi
Version: %ver_major
Release: alt1

Summary: PiTiVi allows users to easily edit audio/video projects
License: LGPLv2.1+
Group: Video
Url: http://www.pitivi.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_compile_include %_libdir/%name/python

Requires: python3-module-gst%gst_api_ver  >= %gst_ver
Requires: gst-plugins-gnonlin%gst_api_ver
Requires: gst-libav >= %gst_ver
Requires: gst-plugins-base%gst_api_ver >= %gst_ver
Requires: gst-plugins-good%gst_api_ver >= %gst_ver
Requires: gst-plugins-bad%gst_api_ver >= %gst_ver
Requires: gst-plugins-ugly%gst_api_ver >= %gst_ver

BuildRequires: intltool yelp-tools rpm-build-gir libcairo-devel
BuildRequires: rpm-build-python3 python3-devel python3-module-pygobject3-devel
BuildRequires: python3-module-pycairo-devel

%description
Pitivi is a video editor built upon the GStreamer Editing Services.
It aims to be an intuitive and flexible application that can appeal to
newbies and professionals alike.

%prep
%setup

%build
#NOCONFIGURE=1 ./autogen.sh
#%autoreconf
%configure

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS NEWS RELEASE
%_bindir/*
%_libdir/%name/
%_datadir/%name/
%_datadir/mime/packages/%name.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_man1dir/%name.1*
%_datadir/appdata/%name.appdata.xml

%changelog
* Mon Nov 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.94-alt1
- 0.94

* Thu May 31 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15.0-alt1.1
- Rebuild with Python-2.7

* Mon Oct 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Thu Jun 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Sat Dec 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.13.5-alt2
- fixed requires (closes: #24825)

* Thu Sep 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.13.5-alt1
- 0.13.5

* Thu Mar 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.13.4-alt1
- 0.13.4

* Mon Sep 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.3-alt2
- updated some translation

* Sun Sep 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.3-alt1
- 0.13.3

* Wed Sep 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.2.4-alt1
- 0.13.2.4

* Fri Sep 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.2.3-alt1
- 0.13.2.3

* Sat Aug 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.2-alt1
- 0.13.2

* Thu May 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Mon Apr 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.11.3-alt2
- arch package

* Sun Apr 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.11.3-alt1
- 0.11.3

* Mon Jun 16 2008 Igor Zubkov <icesik@altlinux.org> 0.11.1-alt2
- fix requires (closes #12154 and #12138)

* Sun Dec 16 2007 Igor Zubkov <icesik@altlinux.org> 0.11.1-alt1
- 0.11.0 -> 0.11.1

* Sun Dec 16 2007 Igor Zubkov <icesik@altlinux.org> 0.11.0-alt1
- 0.10.3 -> 0.11.0
- update license to LGPLv2.1+

* Tue Jun 05 2007 Igor Zubkov <icesik@altlinux.org> 0.10.3-alt1
- 0.10.2 -> 0.10.3

* Mon May 07 2007 Igor Zubkov <icesik@altlinux.org> 0.10.2-alt1
- 0.10.0 -> 0.10.2
- change license to LGPL
- buildreq
- BuildArch -> noarch

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt0.3
- fix build

* Mon May 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt0.2
- new version

* Sat Dec 31 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.9.1-alt0.1
- initial build for ALT Linux Sisyphus

