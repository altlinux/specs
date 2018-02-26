%define content design-graphics
%define theme children
%define pkgtheme children
%define priority 10

Name: design-graphics-children
Version: 4.0.0
Release: alt4.qa1

Summary: design for ALT
License: Different licenses
Group: Graphics

Packager: Alexandra Panyukova <mex3@altlinux.ru>

BuildArch: noarch

PreReq(post,preun): alternatives >= 0.2
Provides: gnome-session-splash = %version-%release
Obsoletes: gnome-session-splash
#
Provides: design-graphics = %version-%release
Obsoletes: design-graphics
%if "%theme" != "%pkgtheme"
Provides: design-graphics-%theme = %version-%release
Obsoletes: design-graphics-%theme < %version-%release
%endif

Source: %content-%theme-%version.tar

BuildRequires: libalternatives-devel

%description
This package contains some graphics for ALT design.

%prep
%setup -q -n %content-%theme-%version

%build
%install
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
cp -ar %_builddir/%content-%theme-%version/* %buildroot/%_datadir/design/%theme

pushd %buildroot/%_datadir/design/%theme
    pushd backgrounds
	ln -sf ../../../wallpapers more
    popd
popd

install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat >%buildroot%_sysconfdir/alternatives/packages.d/%content-%theme <<__EOF__
%_datadir/artworks	%_datadir/design/%theme	%priority
%_datadir/design-current	%_datadir/design/%theme	%priority
__EOF__

%files
%config %_sysconfdir/alternatives/packages.d/%content-%theme
%_datadir/design

%changelog
* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 4.0.0-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-alternatives-0.3 for design-graphics-children
  * postclean-05-filetriggers for spec file

* Tue Jun 17 2008 Alexandra Panyukova <mex3@altlinux.ru> 4.0.0-alt4
- build for children project

* Fri Dec 28 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0-alt1.M40.2
- backport to branch

* Wed Oct 17 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0-alt1
- orange barckground added

* Thu May 31 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0-alt0.1
- build from design-graphics-compact

* Mon Jul 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.1
- build from design-graphics-sisyphus.spec

* Wed Jun 29 2005 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- fix to alterantives-0.2
- change default background

* Mon Jul 19 2004 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt2
- remove unneeded link to wallpapers
- change default wallpaper

* Wed May 19 2004 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt1
- new version
- update faces
- change default wallpaper

* Sat Mar 20 2004 Sergey V Turchin <zerg at altlinux dot org> 3.1.1-alt1
- add alternative from %%_datadir/design/%%theme to %%_datadir/design-current
- add .rc file for KDE-3.2 splash
- change default wallpaper

* Fri Oct 17 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt5
- fix requires, provides
- include alternatives file into spec

* Wed Oct 15 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt4
- change default background

* Wed Oct 15 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt3
- change default background

* Tue Oct 14 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt2
- change default background
- add new user icons
  by Rafael Matito Matito<finrod2k@lycos.es>

* Thu Jul 31 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt1
- URL to design files is %_datadir/artworks
- add altarnatives support
- new placement of files
- don't conflict with any old design-graphics* package versions
- compatibile with backgrounds packages placed in %_datadir/design/backgrounds

* Tue Jul 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.0.4-alt2
- fix Conflicts

* Mon Jul 21 2003 Sergey V Turchin <zerg at altlinux dot org> 3.0.4-alt1
- rename to design-graphics-sisyphus

* Thu Jun 26 2003 Sergey V Turchin <zerg at altlinux dot org> 3.0.3-alt1
- add windowmaker catalog for WindowMaker

* Thu Jan 23 2003 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- add new faces
- change default background
- add new xdm logo (change default)

* Tue Nov 12 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- fixed same pics been non symbolic links
- change default background

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.0-alt4
- add missing file

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.0-alt3
- fix kdm-logo

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.0-alt2
- fix paths

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.0-alt1
- add images for KDE
- increase %%version to sync with distro version

* Tue Oct 08 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt3
- added temporary background

* Mon Oct 07 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt2
- fix summary and description

* Fri Oct 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt1
- initial release
- added light modified gnome splash from art.gnome.org
