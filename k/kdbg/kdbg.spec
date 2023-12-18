
Name: kdbg
Version: 3.1.0
Release: alt1
%K5init no_altplace

Group: Development/Other
Summary: A Graphical Debugger Interface
License: GPL
URL: http://www.kdbg.org/

Requires: gdb

Source: %name-%version.tar

Patch1: alt-parse-gdb-output.patch

# Automatically added by buildreq on Mon Mar 11 2019 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ gem-power-assert gem-setup glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kwidgetsaddons-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 rpm-build-ruby ruby ruby-bundler ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
#BuildRequires: appstream asciidoctor extra-cmake-modules gem-did-you-mean kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel libssl-devel python3-dev ruby-minitest ruby-net-telnet ruby-rubygems-update ruby-test-unit ruby-xmlrpc
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
#libssl-devel

%description
KDbg is a graphical user interface to gdb, the GNU debugger.

It provides an intuitive interface for setting breakpoints,
inspecting variables, and stepping through code.

%prep
%setup -q
%patch1 -p1


%build
%K5build

%install
%K5install

%find_lang --with-kde %name


%files -f %name.lang
%doc BUGS TODO README ReleaseNotes*
%config(noreplace) %_K5xdgconf/kdbgrc
%_K5bin/*
%_datadir/kdbg
%_K5xmlgui/kdbg/
#
%_K5xdgapp/kdbg.desktop
%_iconsdir/*/*/apps/kdbg.*

%changelog
* Mon Dec 18 2023 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1
- new version

* Tue Sep 12 2023 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt1
- new version

* Mon Mar 11 2019 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt1
- new version

* Fri Jul 29 2016 Sergey V Turchin <zerg@altlinux.org> 2.5.5-alt2
- fix for new cmake

* Fri Jul 03 2015 Sergey V Turchin <zerg@altlinux.org> 2.5.5-alt1
- new version

* Fri Jan 24 2014 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt0.M70P.1
- built for M70P

* Fri Jan 24 2014 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt1
- new version

* Wed Jun 26 2013 Sergey V Turchin <zerg@altlinux.org> 2.5.3-alt1
- new version

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.1-alt1
- new version

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt1
- new version

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.92-alt0.1
- build kde4 version

* Wed Aug 26 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt2
- fix to build with new automake

* Fri May 08 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version
- remove deprecated macroses from specfile
- fix to build with gcc4.4

* Wed Dec 26 2007 Sergey V Turchin <zerg at altlinux dot org> 2.1.0-alt1
- new version
- fixed build with new automake

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.5-alt1
- new version
- add patches from Alexey Morozov

* Tue Jul 04 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.4-alt2
- fix build on x86_64

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.4-alt1
- new version

* Fri Jan 20 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.2-alt1
- new version

* Thu Dec 16 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.10-alt1
- new version
- fix "Using libthread ..."

* Mon Mar 22 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.9-alt2
- fix translation encoding
- rebuild with new KDE

* Mon Sep 08 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.9-alt1
- new version

* Tue Jun 24 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.8-alt1
- new version

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.7-alt1
- new version

* Mon Jan 20 2003 Sergey V Turchin <zerg@altlinux.ru> 1.2.6-alt2
- fix .po files

* Tue Nov 05 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.6-alt1
- new version

* Thu Sep 12 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.5-alt2
- rebuild with gcc3.2

* Fri Apr 26 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.5-alt1
- new version
- build with KDE3

* Fri Jan 18 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.3-alt2
- rebuild without fam

* Thu Dec 20 2001 Sergey V Turchin <zerg@altlinux.ru> 1.2.3-alt1
- new version

* Tue Oct 30 2001 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt3
- fix BuildRequires

* Fri Oct 12 2001 Sergey V Turchin <zerg@altlinux.ru> 1.2.2-alt2
- rebuild with new libpng

* Fri Aug 24 2001 Rider <rider@altlinux.ru> 1.2.2-alt1
- Build for ALT

* Tue Aug 21 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.2-0.1mdk
- Update code (1.2.2)

* Sat Jun 02 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.1-0.2mdk
- Rebuild with kde2.2alpha2

* Wed May 2 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.1-0.1mdk
- Update code

* Tue Apr 10 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.0-0.6mdk
- Move KDE menu entry in %%_datadir/applnk
- Rebuild against latest GCC

* Sat Mar 31 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.0-0.5mdk
- Fix BuildRequires for non %%ix86 architectures

* Thu Mar 29 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.0-0.4mdk
- Add build requires

* Wed Mar 14 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.0-0.3mdk
- Rebuild against Qt 2.3.0

* Mon Feb 26 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.0-0.2mdk
- rebuild

* Fri Dec 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-0.1mdk
- new in contribs
