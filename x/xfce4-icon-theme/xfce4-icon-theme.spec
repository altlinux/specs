Name: xfce4-icon-theme
Version: 4.4.3
Release: alt1.qa1

Summary: Rodent vector icon theme for XFce 4
License: GPL
Url: http://www.xfce.org/
Group: Graphical desktop/XFce
Packager: Eugene Ostapets <eostapets@altlinux.ru>

Source: ftp://ftp.berlios.de/pub/xfce-goodies/%version/%name-%version.tar.bz2
BuildArch: noarch

Requires: xfce4-panel, libgtk+2-common
BuildPreReq: xfce4-panel-devel >= %version, xfce4-dev-tools >= 4.4.0

# Automatically added by buildreq on Sun Nov 09 2008
BuildRequires: intltool

%description
Rodent icon theme for the XFce 4.

%prep
%setup

%build
%configure --build=%_arch-alt-linux --host=%_arch-alt-linux
%make_build

%install
%make install DESTDIR=%buildroot

%files
%doc README TODO ChangeLog NEWS INSTALL COPYING AUTHORS
%_datadir/icons/Rodent
%_datadir/xfce4/mime/*
%exclude %_pkgconfigdir/*.pc

%changelog
* Sat Nov 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 4.4.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for xfce4-icon-theme
  * postclean-05-filetriggers for spec file

* Sun Nov 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 4.4.3-alt1
- Xfce 4.4.3 release

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Sun Oct 01 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- 4.4rc1

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- First version of RPM package for Sisyphus.
