Name: gtkevemon
Version: 1.8
Release: alt2.qa1
Summary: GtkEveMon is a skill monitoring application for EVE Online 

Packager: Alexey Borovskoy <alb@altlinux.ru>

License: GPL-3
Group: Games/Other
URL: http://gtkevemon.battleclinic.com

Source: %name-%version.tar

BuildPreReq: gcc-c++ libgtk+2-devel libgtkmm2-devel libxml2-devel zlib-devel
BuildRequires: desktop-file-utils

%description
GtkEveMon is a skill monitoring application for EVE Online.
With GtkEveMon you can monitor your current skills and your
skill training process without starting EVE Online.

%prep
%setup -q

%build

%make_build

%install

%make_install install DESTDIR=%buildroot

mkdir -p %buildroot%_docdir/%name-%version
cp {COPYING,README,TODO,CHANGES} %buildroot%_docdir/%name-%version
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=RolePlaying \
	%buildroot%_desktopdir/gtkevemon.desktop

%files
%_bindir/*
%_docdir/%name-%version
%_desktopdir/*
%_pixmapsdir/*

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.8-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gtkevemon

* Tue Apr 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt2
- fix build

* Fri May 28 2010 Alexey Borovskoy <alb@altlinux.ru> 1.8-alt1
- Version 1.8.
- SVN revision: 117.

* Sun May 09 2010 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt11
- SVN revision: r114.

* Wed Apr 07 2010 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt10
- SVN revision: r111.

* Thu Feb 04 2010 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt9
- SVN revision: r110.

* Sun Jan 03 2010 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt8
- SVN revision: r108.

* Fri Sep 04 2009 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt7
- SVN revision: r107.

* Wed Sep 02 2009 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt6
- SVN revision: r106.

* Wed Aug 12 2009 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt5
- SVN revision: r105.

* Sat Jul 18 2009 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt4
- SVN revision: r104.

* Thu Jul 09 2009 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt3
- SVN revision: r103.

* Tue May 26 2009 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt2
- SVN revision: r101.
- Fix typo in changelog.
- Update description and summary.

* Tue May 12 2009 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt1
- Build for Sisyphus.

* Tue May 12 2009 Alexey Borovskoy <alb@altlinux.ru> 1.7-alt0.M50.1
- SVN revision: r100.

* Tue Apr 21 2009 Alexey Borovskoy <alb@altlinux.ru> 0.0.1-alt0.M50.1
- SVN revision: r99.

* Sun Feb 22 2009 Alexey Borovskoy <alb@altlinux.ru> 0.0.1-alt0.M40.1
- Fisrt build.
- SVN revision: r85.
