Name: xvattr
Version: 1.3
Release: alt6

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Getting and setting Xv attributes
License: GPLv2+
Group: Video

URL: http://www.dtek.chalmers.se/groups/dvd/downloads.shtml
Source0: http://www.dtek.chalmers.se/groups/dvd/dist/xvattr-1.3.tar.gz

# Automatically added by buildreq on Fri Nov 26 2010 (-bi)
BuildRequires: imake libXt-devel libXv-devel perl-Pod-Parser xorg-cf-files

%description
This program is used for getting and setting Xv attributes such as
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY.

%prep
%setup

%build
%configure --disable-gtktest
%make_build xvattr

%install
%make_install DESTDIR=%buildroot install-man1
# Too lazy to write patch for removing gxvattr from Makefile. Instead I will
# just install only xvattr by hand. :)
install -pD -m755 xvattr %buildroot%_bindir/xvattr

%files
%_bindir/xvattr
%_man1dir/*

%changelog
* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 1.3-alt6
- Add to BuildRequires perl package needed to generate man page.

* Tue Dec 02 2008 Victor Forsyuk <force@altlinux.org> 1.3-alt5
- Renew build requirements to fix FTBFS.

* Tue Dec 11 2007 Victor Forsyuk <force@altlinux.org> 1.3-alt4
- Do not package gxvattr thus eliminating package requirement of gtk1.

* Wed Nov 07 2007 Victor Forsyuk <force@altlinux.org> 1.3-alt3
- Refresh buildrequires for Xorg.
- Cleanup spec.

* Mon Mar 17 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.3-alt2
- new buidrequires

* Thu Jul 25 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.3-alt1
- 1.3
- specfile cleanup
