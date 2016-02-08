%define rname owncloudclient
Name: owncloud-client
Version: 2.0.2
Release: alt1

Group: Networking/File transfer
Summary: Applet for owncloud files syncronization
License: GPLv2

Provides: mirall = %version-%release
Obsoletes: mirall <= %version-%release

Source: %rname-%version.tar
Source1: owncloud-client.desktop
Patch1: alt-dont-check-updates.patch
Patch2: alt-confdir.patch
Patch3: alt-static-libs.patch

# Automatically added by buildreq on Fri Sep 19 2014 (-bi)
# optimized out: cmake-modules elfutils fontconfig libcloog-isl4 libgst-plugins libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-webkit libqt4-xml libqt4-xmlpatterns libstdc++-devel pkg-config python-base texlive-latex-base
#BuildRequires: cmake desktop-file-utils gcc-c++ libneon-devel libqt3-devel libqtkeychain-devel libsqlite3-devel phonon-devel python-module-sphinx qt4-designer ruby ruby-stdlibs
BuildRequires: cmake desktop-file-utils gcc-c++ libneon-devel libqt4-devel libqtkeychain-devel libsqlite3-devel kde-common-devel

%description
Applet for file syncronization via owncloud.

%prep
%setup -qn %rname-%version
%patch1 -p1
#%patch2 -p1
%patch3 -p1

%build
%add_optflags %optflags_shared
%Kbuild \
    -DBUILD_WITH_QT4=ON \
    -DDATA_INSTALL_DIR=%_datadir \
    -DCMAKE_INSTALL_SYSCONFDIR=/etc/owncloud-client \
    #

%install
%Kinstall
mkdir -p %buildroot/%_desktopdir
desktop-file-install \
    --dir=%buildroot/%_desktopdir \
    %{SOURCE1}

%find_lang --with-qt --output=%name.lang client

%files -f %name.lang
%doc ChangeLog README.md
%config(noreplace) %_sysconfdir/ownCloud/sync-exclude.lst
%_bindir/owncloud
%_bindir/owncloudcmd
%_desktopdir/%name.desktop
#%_datadir/owncloud-client
%_datadir/nautilus-python/extensions/
%_iconsdir/hicolor/*/apps/owncloud.*
%_iconsdir/hicolor/*/apps/ownCloud_*.*

%changelog
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
