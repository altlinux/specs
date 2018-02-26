%define content design-graphics
%define theme Sisyphus2
%define pkgtheme sisyphus2
%define priority 5

Name: %content-%pkgtheme
Version: 1.0
Release: alt1.qa1

Summary: Design for ALT Linux, revisited
License: Different licenses
Group: Graphics

BuildArch: noarch

PreReq(post,preun): alternatives >= 0.2
Provides: gnome-session-splash = %version-%release
Obsoletes: gnome-session-splash
#
Provides: design-graphics = %version-%release
Obsoletes: design-graphics
%if "%theme" != "%pkgtheme"
Provides: design-graphics-%theme = %version-%release
Obsoletes: design-graphics-%theme
%endif

Url: http://wiki.sisyphus.ru/beta/design
# Gnome splash screen from art.gnome.org
# Name: GNOME2-Mountains
# Author: Roman "star" Beigelbeck <roman_n0spam@gnome.org>
# Release Date: 08/06/2002
Source0: %content-%theme-%version.tar.gz
# photo: http://paq.osdn.org.ua/~adiel/alt-back/hpim4099.jpg
# (c) 2005, Michael Shigorin
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libalternatives-devel

%description
This package contains a little better graphical design for ALT Linux

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

install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%content-%theme <<__EOF__
%_datadir/artworks	%_datadir/design/%theme	%priority
%_datadir/design-current	%_datadir/design/%theme	%priority
__EOF__

%files
%config /etc/alternatives/packages.d/%content-%theme
%_datadir/design

# TODO
# - review the rest of the package, update if better styled
#   alternatives arise

%changelog
* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-alternatives-0.3 for design-graphics-sisyphus2
  * postclean-05-filetriggers for spec file

* Thu Feb 15 2007 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- cloned off design-graphics-sisyphus-3.1.4-alt2
- replaced default background with nice nature photo
  (added 1600x1200 default.jpg for higher-quality displays)

* Wed Oct 05 2005 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt2
- add symlink for kdm logo

* Thu Sep 29 2005 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- add default color-scheme for KDM

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
- URL to design files is /usr/share/artworks
- add altarnatives support
- new placement of files
- don't conflict with any old design-graphics* package versions
- compatibile with backgrounds packages placed in /usr/share/design/backgrounds

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
