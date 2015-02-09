%define theme AltClearlooks
Name: design-icewm
Version: 1.0
Release: alt9
Summary: Default theme for IceWM
Group: Graphical desktop/Icewm
License: GPL
Url: http://www.whatis.mynetcologne.de/icewm/index.html
Packager: Dmitriy Khanzhin <jinn@altlinux.ru>
Source0: AltClearlooks.tar
Source1: http://www.whatis.mynetcologne.de/icewm/20051225_gertplastik.tar
BuildArch: noarch
%description
Default theme for IceWM

%prep
%build
%install
mkdir -p %buildroot%_x11x11dir/icewm/themes
tar xf %SOURCE0 -C %buildroot%_x11x11dir/icewm/themes/
tar xf %SOURCE1 -C %buildroot%_x11x11dir/icewm/themes/
find %buildroot%_x11x11dir/icewm/themes -type f -print0 |
	xargs -r0 chmod 0444
find %buildroot%_x11x11dir/icewm/themes -type d -print0 |
	xargs -r0 chmod 0755
pushd %buildroot%_x11x11dir/icewm/themes
ln -s %theme default
popd

%files
%dir %_x11x11dir/icewm
%dir %_x11x11dir/icewm/themes
%_x11x11dir/icewm/themes/*

%changelog
* Mon Feb 09 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.0-alt9
- added AltClearlooks theme and set as default

* Wed Jun 05 2013 Dmitriy Khanzhin <jinn@altlinux.org> 1.0-alt8
- don't gzip content

* Sat Jan 05 2013 Dmitriy Khanzhin <jinn@altlinux.org> 1.0-alt7
- updated some .xpm's for fix breaks themes with xorg 1.12.3.902 and later
  (bfo#54168)

* Sun Mar 20 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0-alt6
- removed circular dependencies
- fixed Url
- changed packager

* Sat Nov  3 2007 Terechkov Evgenii <evg@altlinux.ru> 1.0-alt5
- Russian summary and description removed (Specspo)
- Packager tag added to spec
- Package separation fixes
- Spec cleanupd (un__.sh)

* Wed Dec 27 2006 Terechkov Evgenii <evg@altlinux.ru> 1.0-alt4
- Default theme changed to "gertplastik"
- Minimum icewm version set to 1.2.28 (cause /usr/share/X11/icewm)
- Spec cleanups

* Sun Jan 29 2006 Anton Farygin <rider@altlinux.ru> 1.0-alt3
- use %_datadir

* Mon Oct 21 2002 Rider <rider@altlinux.ru> 1.0-alt2
- permissions fix

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 1.0-alt1
- first build
