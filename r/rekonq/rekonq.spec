Name:         rekonq
Version:      0.9.2
Release:      alt1

Group:        Networking/WWW
Summary:      Web browser easy for use
License:      GPLv3
Url: http://rekonq.sourceforge.net/

PreReq(post,preun): alternatives >= 0.2
Provides: webclient

Source:      %name-%version.tar

# Automatically added by buildreq on Wed Mar 23 2011 (-bi)
#BuildRequires: cvs gcc-c++ git-core glib2-devel kde4libs-devel libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libqt3-devel libxkbfile-devel mercurial openssh-common qt4-designer subversion valgrind zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt4-devel zlib-devel
BuildRequires: libalternatives-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel
BuildRequires: libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libxkbfile-devel desktop-file-utils

%description
Web browser easy for use.

%prep
%setup -q

%build
%K4cmake
%K4make


%install
%K4install

# install alternative
mkdir -p %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/xbrowser       %_K4bindir/rekonq      101
%_bindir/x-www-browser       %_K4bindir/rekonq      101
__EOF__

# add mime types categories
desktop-file-install --dir %buildroot/%_K4xdg_apps --add-mime-type=x-scheme-handler/http --add-mime-type=x-scheme-handler/https --add-mime-type=x-scheme-handler/ftp %buildroot/%_K4xdg_apps/rekonq.desktop

%K4find_lang --with-kde %name
%K4find_lang --with-kde --append --output=%name.lang kwebapp


%files -f %name.lang
%doc AUTHORS ChangeLog TODO
%config %_sysconfdir/alternatives/packages.d/%name
%_K4bindir/%name
#%_K4bindir/kwebapp
%_K4libdir/libkdeinit4_rekonq.so
%_K4xdg_apps/%name.desktop
%_K4apps/%name/
%_K4iconsdir/hicolor/*/apps/%name.*
%_K4cfg/%name.kcfg

%changelog
* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt1
- new version

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt0.M60P.1
- built for M60P

* Mon Apr 02 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1
- new version

* Thu Mar 22 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt0.M60P.1
- built for M60P

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version

* Sat Jan 21 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt0.M60P.1
- built for M60P

* Fri Jan 20 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version
- add x-www-browser alternative

* Mon Oct 17 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Thu Sep 22 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.92-alt1
- new version

* Tue May 03 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt2
- add x-scheme-handler mimetypes

* Mon Apr 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- 0.7.0

* Wed Mar 23 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.95-alt1
- 0.7 RC

* Wed Oct 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- initial build
