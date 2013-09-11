%define _kde_alternate_placement 1
%define x11confdir %_sysconfdir/X11

%define rname startactive
Name: kde4-startactive
Version: 0.4
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE mobile environment startup
License: GPLv2+
Url: http://kde.org/

Source: %rname-%version.tar
Patch1: startactive-0.4-env.patch
Patch2: startactive-0.4-startactive.patch
Patch3: startactive-0.2-config.patch
Patch4: alt-startactive-modules.patch

# Automatically added by buildreq on Tue Jan 31 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-xml libqt4-xmlpatterns libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel
BuildRequires: kde-common-devel

%description
KDE mobile environment startup


%prep
%setup -qn %rname-%version
%patch1 -p1
%patch2 -p1 -b .start
%patch3 -p1
%patch4 -p1
#sed -i \
#    's|\(^cmake_minimum_required.*\)$|\1\n\nset(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules )|' \
#    CMakeLists.txt
%if_enabled desktop
sed -i 's|^exec=.*|exec=kwrapper4 ksmserver --windowmanager kwin|' modules/ksmserver.module
%else
sed -i 's|^exec=.*|exec=kwrapper4 ksmserver --windowmanager kwinactive|' modules/ksmserver.module
sed -i 's|^exec=.*|exec=true|' modules/kstartupconfig.module
%endif
sed -i 's|^exec=.*|exec=true|' modules/setup-kde-skel.module

%build
%K4build \
    -DKDE_DEFAULT_HOME=".kde4"

%install
%K4install
mkdir -p %buildroot/%_bindir
ln -s `relative %buildroot/%_kde4_bindir/startactive %buildroot/%_bindir/startactive` %buildroot/%_bindir/startactive

# Add chksession support
mkdir -p %buildroot/%x11confdir/wmsession.d/
cat <<__EOF__ > %buildroot/%x11confdir/wmsession.d/02KDE4mobile
NAME=MobileKDE4
DESC=Mobile K Desktop Environment
ICON=%_K4iconsdir/oxygen/64x64/apps/kde.png
EXEC=%_bindir/startactive
SCRIPT:
exec %_bindir/startactive
__EOF__

%K4find_lang --with-kde %rname


%files -f %rname.lang
%config(noreplace) %x11confdir/wmsession.d/*KDE*mobile
%_bindir/startactive
%_kde4_bindir/startactive
%_kde4_bindir/startactive.bin
%_K4apps/ksplash/Themes/qmldefault/
%_K4apps/startactive/

%changelog
* Wed Sep 11 2013 Sergey V Turchin <zerg@altlinux.org> 0.4-alt1
- new version

* Tue Jun 25 2013 Sergey V Turchin <zerg@altlinux.org> 0.3-alt4
- allow to start custom modules

* Tue Nov 20 2012 Sergey V Turchin <zerg@altlinux.org> 0.3-alt3
- fix startup

* Tue Nov 20 2012 Sergey V Turchin <zerg@altlinux.org> 0.3-alt2
- update startactive script

* Wed Oct 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- new version

* Fri May 11 2012 Sergey V Turchin <zerg@altlinux.org> 0.2-alt3
- fix modules

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 0.2-alt2
- update from Active/Two branch

* Tue Jan 31 2012 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- initial specfile
