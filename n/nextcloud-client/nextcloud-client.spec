%define rname owncloudclient
%define theme client_theming
Name: nextcloud-client
Version: 2.3.3
Release: alt4%ubt

Group: Networking/File transfer
Summary: Nextcloud Desktop Client
License: GPLv2
Url: https://github.com/nextcloud/client_theming

BuildRequires(pre): rpm-build-ubt

Provides: mirall = %version-%release
Obsoletes: mirall <= %version-%release

Source0: %theme-%version.tar
Source1: %rname-%version.tar
Source2: nextcloud-client.desktop
Patch1: alt-dont-check-updates.patch
Patch2: alt-confdir.patch
Patch3: alt-static-libs.patch
Patch4: %name-%version-alt-fix-help-url.patch
Patch5: alt-move-deleted-to-trash.patch

# Automatically added by buildreq on Mon Oct 24 2016 (-bi)
# optimized out: cmake cmake-modules desktop-file-utils elfutils gcc-c++ kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libgpg-error libgst-plugins1.0 libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libqtkeychain-qt5 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-module-google python-module-sphinx python-modules python3 python3-base qt5-base-devel qt5-tools rpm-build-gir rpm-build-python3 texlive-latex-base zlib-devel
#BuildRequires: doxygen extra-cmake-modules graphviz kf5-kio-devel libqtkeychain-qt5-devel libsqlite3-devel libssl-devel python3-dev qt5-tools-devel qt5-webkit-devel ruby ruby-stdlibs zlib-devel-static
BuildRequires: kde-common-devel rpm-build-kf5
BuildRequires: doxygen extra-cmake-modules graphviz kf5-kio-devel libqtkeychain-qt5-devel libsqlite3-devel libssl-devel python3-dev qt5-tools-devel qt5-webkit-devel zlib-devel

%description
The Nextcloud Desktop Client is a tool to synchronize files from Nextcloud Server with your computer.

%package kde5
Summary: KDE5 %name integration
Group: Graphical desktop/KDE
Requires: %name
%description kde5
KDE5 %name integration

%prep
%setup -qn %theme-%version
%patch4 -p1
%setup -T -D -a 1 -n %theme-%version
rm -Rf client
mv %rname-%version client
cd client
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch5 -p1

%build
%add_optflags %optflags_shared
%Kbuild \
    -DBUILD_WITH_QT4=OFF \
    -DDATA_INSTALL_DIR=%_datadir \
    -DCMAKE_INSTALL_SYSCONFDIR=/etc/%name \
    -DKDE_INSTALL_PLUGINDIR=%_K5plug \
    -DKDE_INSTALL_KSERVICES5DIR=%_K5srv \
    -DOEM_THEME_DIR=$(realpath nextcloudtheme) \
	../client \
    #

%install
%Kinstall
mkdir -p %buildroot/%_desktopdir
desktop-file-install \
    --dir=%buildroot/%_desktopdir %SOURCE2

%find_lang --with-qt --output=%name.lang client

%files -f %name.lang
%doc README.md
%dir %_datadir/nextcloud
%dir %_datadir/nextcloud/i18n
%dir %_sysconfdir/Nextcloud
%config(noreplace) %_sysconfdir/Nextcloud/sync-exclude.lst
%_bindir/nextcloud
%_bindir/nextcloudcmd
%_desktopdir/%name.desktop
%_datadir/nautilus-python/extensions/
%_datadir/caja-python/extensions/
%_iconsdir/hicolor/*/apps/Nextcloud.*
%_iconsdir/hicolor/*/apps/Nextcloud_*.*

%files kde5
%_K5lib/libnextclouddolphinpluginhelper.so
%_K5plug/kf5/overlayicon/
%_K5plug/*nextcloud*.so
%_K5srv/*nextcloud*.desktop

%changelog
* Wed Jan 17 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.3-alt4%ubt
- move remote-deleted files to trash (patch from owncloud-client 2.3.4-alt2)

* Wed Nov 22 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.3-alt3%ubt
- updated "client_theming" (beta1->release)

* Wed Oct 18 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.3-alt2%ubt
- fixed URL of docs

* Wed Oct 18 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.3-alt1%ubt
- new version (beta1)

* Fri Sep 22 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt3.M80P.1
- build for M80P

* Fri Sep 22 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt4
- fixed unowned files

* Fri Jul 14 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt2.M80P.1
- build for M80P

* Fri Jul 14 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt3
- updated "client_theming" (beta1->release)

* Fri Jun 16 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt1.M80P.1
- build for M80P

* Fri Jun 16 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt2
- build "nextcloud-client"

* Fri Jun 16 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt1
- new version

* Thu Nov 03 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt1.M80P.1
- build for M80P

* Thu Nov 03 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt2
- rebuild with new libqt5keychain

* Mon Oct 24 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt0.M80P.1
- build for M80P

* Mon Oct 24 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt1
- new version (ALT#32649)

* Mon Feb 08 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version

* Wed Oct 21 2015 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- new version

* Wed Oct 21 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.4-alt0.M70P.1
- build for M70P

* Mon Jul 13 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.4-alt1
- new version

* Wed Jul 08 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.3-alt1
- new version

* Mon Feb 02 2015 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt0.M70P.1
- build for M70P

* Mon Feb 02 2015 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt1
- new version

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt1.M70P.1
- built for M70P

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt2
- obsolete mirall

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt0.M70P.1
- built for M70P

* Fri Sep 19 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt1
- new version

* Fri Aug 24 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt1
- new version

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt3.M60P.2
- built for M60P

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt4
- don't conflict with mirall
- bump release

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1.M60P.1
- built for M60P

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt2
- fix menu item

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt0.M60P.1
- built for M60P

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- initial build
