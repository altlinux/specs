%define theme gertplastik
Name: design-icewm
Version: 1.0
Release: alt6
Summary: Default theme for IceWM
Group: Graphical desktop/Icewm
License: GPL
Url: http://www.whatis.mynetcologne.de/icewm/index.html
Packager: Dmitriy Khanzhin <jinn@altlinux.ru>
Source0: http://www.whatis.mynetcologne.de/icewm/20051225_gertplastik.tar.gz
BuildArch: noarch
%description
Default theme for IceWM

%prep
%setup -n %theme

%build
%install
mkdir -p %buildroot%_x11x11dir/icewm/themes
tar xzvf %SOURCE0 -C %buildroot%_x11x11dir/icewm/themes/
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
