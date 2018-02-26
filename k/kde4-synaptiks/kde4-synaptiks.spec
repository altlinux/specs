%define _kde_alternate_placement 1

%define rname synaptiks
Name: kde4-synaptiks
Version: 0.8.1
Release: alt3

Group: Graphical desktop/KDE
Summary: A touchpad management tool for KDE
Url: http://synaptiks.lunaryorn.de/
#Url: http://kde-apps.org/content/show.php/?content=114270
License: BSD

Requires: kde4base-workspace-core

Source: %rname-%version.tar.bz2
Patch:  %rname-ru-l10n.patch

# Automatically added by buildreq on Wed Feb 15 2012 (-bi)
# optimized out: libqt4-core libqt4-dbus libqt4-network libqt4-xml python-base python-devel python-module-4Suite-XML python-module-BeautifulSoup python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-beaker python-module-cups python-module-dateutil python-module-distribute python-module-docutils python-module-genshi python-module-html5lib python-module-imaging python-module-jinja2 python-module-lxml python-module-mako python-module-mpmath python-module-nose python-module-numpy python-module-protobuf python-module-pyExcelerator python-module-pyglet python-module-pylib python-module-pytz python-module-simplejson python-module-sympy python-module-whoosh python-module-xlwt python-modules python-modules-compiler python-modules-email python-modules-encodings
#BuildRequires: dblatex java-1.5.0-gcj-aot-compile kde-common-devel kde4libs libicu mercurial python-module-Reportlab python-module-cupshelpers python-module-matplotlib python-module-scipy python-module-sphinx rpm-build-gir
BuildRequires: kde4libs kde-common-devel python-module-distribute python-devel

%description
synaptiks is a touchpad management tool for KDE. It provides a simple
configuration interface and can automatically switch off your touchpad
on keyboard activity or if mouse devices are plugged.

Author:
--------
    Sebastian Wiesner

%prep
%setup -qn %rname-%version
%patch -p1

%build
%python_build 

%install
%python_install --prefix=%_kde4_prefix

mv %buildroot/%_kde4_prefix/share/* %buildroot/%_kde4_prefix/
rm -rf %buildroot/%_kde4_prefix/share
#
mkdir -p %buildroot/%_libdir/
mv %buildroot/%_kde4_prefix/lib*/* %buildroot/%_libdir/
rm -rf %buildroot/%_kde4_prefix/lib*
#
mkdir -p %buildroot/%_kde4_bindir
mv %buildroot/%_kde4_prefix/bin/* %buildroot/%_kde4_bindir/
rm -rf %buildroot/%_kde4_prefix/bin
#
mkdir -p %buildroot/%_K4start
mv %buildroot/%_sysconfdir/xdg/autostart/* %buildroot/%_K4start/
#
#mkdir -p %buildroot/%_K4start
#mv %buildroot/%_datadir/autostart/* %buildroot/%_K4start/
#

%K4find_lang --with-kde %rname

%files -f %rname.lang
%_kde4_bindir/*
%_K4apps/synaptiks
%_K4start/*.desktop
%_kde4_xdg_apps/*.desktop
%_K4srv/*.desktop
%_kde4_iconsdir/hicolor/*/apps/synaptiks.*
%python_sitelibdir/*/*

%changelog
* Mon May 14 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt3
- fix to build

* Wed Feb 15 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt2
- build for Sisyphus

* Wed Feb 15 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt0.M60P.2
- Complete Russian translation in desktop files

* Wed Feb 15 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt0.M60P.1
- Backport to p6 branch (new version)

* Mon Feb 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version

* Wed Sep 21 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt2
- Add Russian translation

* Fri Jun 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- initial build (ALT#25799)
