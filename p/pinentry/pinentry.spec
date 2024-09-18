%def_disable libcap
%def_enable qt5
%def_enable qt6
%def_disable fltk

Name: pinentry
Version: 1.3.1
Release: alt1

Summary: Simple PIN or passphrase entry dialog
License: GPLv2+
Group: File tools
Url: http://gnupg.org/related_software/pinentry/

Requires: %name-common
Requires: %name-qt5

# ftp://ftp.gnupg.org/gcrypt/pinentry/%name-%version.tar.gz
Source: %name-%version.tar
Source1: pinentry-wrapper
# FC
Patch1: pinentry-1.1.1-coverity.patch

%if_enabled qt5
BuildRequires: qt5-base-devel kf5-kwayland-devel rpm-build-kf5
%endif
%if_enabled libfltk-devel
BuildRequires: libfltk-devel
%endif
%if_enabled qt6
BuildRequires: qt6-base-devel kf6-kwindowsystem-devel kf6-kguiaddons-devel rpm-build-kf6
%endif
%if_enabled libcap
BuildRequires: libcap-devel
%endif
BuildRequires: gcc-c++ libgtk+2-devel libncursesw-devel
BuildRequires: libsecret-devel gcr-libs-devel libassuan-devel
BuildRequires: texinfo

%description
This is simple PIN or passphrase entry dialog which utilize
the Assuan protocol as described by the aegypten project.

%package common
Group: %group
Summary: %summary
Provides: %name = %version-%release
Provides: %name-terminal = %version-%release
Provides: %name-console = %version-%release
Provides: %name-tty = %EVR
Provides: %name-curses = %EVR
Obsoletes: %name-curses < %EVR
Conflicts: pinentry < 0.7.2 pinentry-curses < 0.7.2
Conflicts: pinentry-qt < 0.7.2 pinentry-gtk < 0.7.2

%package gtk2
Group: %group
Summary: %summary
Requires: %name-common = %EVR
Requires: xprop
Provides: %name = %version-%release
Provides: %name-x11 = %version-%release
Provides: pinentry-gtk = %EVR
Obsoletes: pinentry-gtk < %EVR

%package gnome3
Group: %group
Summary: %summary
Requires: %name-common = %EVR
Requires: xprop
Provides: %name = %version-%release
Provides: %name-x11 = %version-%release

%package qt5
Group: %group
Summary: %summary
Requires: xprop
Requires: %name-common = %EVR
Provides: %name = %version-%release
Provides: %name-x11 = %version-%release
Provides: pinentry-qt = %EVR
Obsoletes: pinentry-qt < %EVR

%package qt6
Group: %group
Summary: %summary
Requires: xprop
Requires: %name-common = %EVR
Provides: %name = %version-%release
Provides: %name-x11 = %version-%release

%description gtk2
This is simple PIN or passphrase entry dialog which utilize
the Assuan protocol as described by the aegypten project.
%description gnome3
This is simple PIN or passphrase entry dialog which utilize
the Assuan protocol as described by the aegypten project.
%description qt5
This is simple PIN or passphrase entry dialog which utilize
the Assuan protocol as described by the aegypten project.
%description qt6
This is simple PIN or passphrase entry dialog which utilize
the Assuan protocol as described by the aegypten project.
%description common
This package contains common files and documentation for %name.

%prep
%setup -T -c
tar xf %SOURCE0
mv %name-%version gui
pushd gui
%patch1 -p1
popd

%{?_enable_qt6:cp -a gui gui-qt6}
%{?_enable_qt5:cp -a gui gui-qt5}
cp -a gui tui

install -pm644 %SOURCE1 pinentry-wrapper

for d in tui gui \
             %{?_enable_qt6:gui-qt6} \
             %{?_enable_qt5:gui-qt5} ; do
    pushd $d
    %autoreconf
    popd
done

%build
%add_optflags -std=gnu++17

pushd tui
%configure \
    --disable-rpath \
    --enable-pinentry-curses \
    --enable-pinentry-tty \
    --disable-pinentry-gtk2 \
    --disable-pinentry-fltk \
    --disable-pinentry-gnome3 \
    --disable-pinentry-qt \
    --disable-pinentry-qt5 \
    --disable-libsecret \
    %{?_enable_libcap:--with-libcap}%{!?_enable_libcap:--without-libcap} \
    #
%make_build
popd

pushd gui
%configure \
    --disable-rpath \
    --disable-pinentry-curses \
    --disable-pinentry-tty \
    --enable-pinentry-gtk2 \
    %{?_enable_fltk:--enable-pinentry-fltk} \
    --enable-pinentry-gnome3 \
    --disable-pinentry-qt \
    --disable-pinentry-qt5 \
    --disable-pinentry-qt-clipboard \
    --enable-libsecret \
    %{?_enable_libcap:--with-libcap}%{!?_enable_libcap:--without-libcap} \
    #
%make_build
popd

%if_enabled qt6
pushd gui-qt6
export KF6GUIADDONS_LIBS='-lKF6GuiAddons -lQt6Gui -lQt6Core -L%_K6link'
%configure \
    --disable-rpath \
    --disable-pinentry-curses \
    --disable-pinentry-tty \
    --disable-pinentry-gtk2 \
    --disable-pinentry-fltk \
    --disable-pinentry-gnome3 \
    --enable-pinentry-qt \
    --disable-pinentry-qt5 \
    --enable-pinentry-qt-clipboard \
    --enable-libsecret \
    %{?_enable_libcap:--with-libcap}%{!?_enable_libcap:--without-libcap} \
    #
%make_build
popd
%endif

%if_enabled qt5
pushd gui-qt5
export KF5WAYLANDCLIENT_LIBS="`pkg-config  --libs KF5WaylandClient` -L%_K5link"
%configure \
    --disable-rpath \
    --disable-pinentry-curses \
    --disable-pinentry-tty \
    --disable-pinentry-gtk2 \
    --disable-pinentry-fltk \
    --disable-pinentry-gnome3 \
    --disable-pinentry-qt \
    --enable-pinentry-qt5 \
    --enable-pinentry-qt-clipboard \
    --enable-libsecret \
    %{?_enable_libcap:--with-libcap}%{!?_enable_libcap:--without-libcap} \
    #
%make_build
popd
%endif

%install
pushd tui
%makeinstall_std
popd
rm %buildroot%_bindir/%name

pushd gui
%makeinstall_std
popd
rm %buildroot%_bindir/%name

%if_enabled qt6
pushd gui-qt6
%makeinstall_std
popd
[ -e %buildroot/%_bindir/%name-qt ] && \
    mv %buildroot/%_bindir/%name-qt %buildroot/%_bindir/%name-qt6 ||:
if [ -e %buildroot/%_desktopdir/org.gnupg.pinentry-qt.desktop ]; then
    mv %buildroot/%_desktopdir/org.gnupg.pinentry-qt{,6}.desktop
    sed -i '/^Exec=/s|pinentry-qt$|pinentry-qt6|' %buildroot/%_desktopdir/org.gnupg.pinentry-qt6.desktop
fi
%endif

%if_enabled qt5
pushd gui-qt5
%makeinstall_std
popd
[ -e %buildroot/%_bindir/%name-qt ] && \
    mv %buildroot/%_bindir/%name-qt %buildroot/%_bindir/%name-qt5 ||:
%endif

ln -s %name-gtk-2 %buildroot/%_bindir/%name-gtk

install -pDm755 pinentry-wrapper %buildroot/%_bindir/pinentry

%files gtk2
%_bindir/%name-gtk
%_bindir/%name-gtk-2

%if_enabled qt6
%files qt6
%_bindir/%name-qt6
%_desktopdir/org.gnupg.pinentry-qt6.desktop
%endif

%if_enabled qt5
%files qt5
%_bindir/%name-qt5
%_desktopdir/org.gnupg.pinentry-qt5.desktop
%endif

%files gnome3
%_bindir/%name-gnome3

%files common
%doc gui/AUTHORS gui/NEWS gui/README gui/THANKS
%_bindir/%name
%_bindir/%name-curses
%_bindir/%name-tty
%_datadir/pixmaps/pinentry.png
%_infodir/*.info*

%changelog
* Tue Sep 17 2024 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt1
- new version
- build Qt6 version

* Mon May 15 2023 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1
- new version

* Mon Oct 17 2022 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt7
- drop ubt macro

* Mon Jun 28 2021 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt6
- disable qt4 UI

* Mon Jul 29 2019 Nikita Ermakov <arei@altlinux.org> 1.1.0-alt5
- NMU: Clean up spec file.
  + Make qt4 optional and disable it for riscv64 architecture.
  + Make qt5 option actually work.
  + Remove obsolete libtqt3-devel (trinity-tqt3 package was removed).

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt4
- NMU: remove rpm-build-ubt from BR:

* Mon Apr 01 2019 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt3
- fix spec cleanup

* Sat Mar 30 2019 Michael Shigorin <mike@altlinux.org> 1.1.0-alt2
- minor spec cleanup
  + dropped unused macros
  + dropped %%ubt

* Thu Apr 19 2018 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Thu Dec 07 2017 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt2
- fix detect pinentry-qt5 (ALT#34290)

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- new version

* Fri Apr 29 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt2
- build pinentry-qt5

* Tue Dec 08 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt1
- new version

* Tue Dec 08 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt2
- fix build requires

* Mon Oct 26 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt1
- new version

* Tue Jun 23 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.4-alt1
- new version

* Tue Dec 02 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt2
- don't require xprop for console subpackage

* Tue Nov 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version
- using wrapper script instead of alternatives

* Fri Jun 20 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.3-alt2
- rename pinentry-qt to pinentry-qt4

* Thu Oct 31 2013 Sergey V Turchin <zerg@altlinux.org> 0.8.3-alt0.M70P.1
- built for M70P

* Fri Oct 25 2013 Sergey V Turchin <zerg@altlinux.org> 0.8.3-alt1
- new version

* Thu Dec 20 2012 Alexander Plehanov <tonik@altlinux.org> 0.8.2-alt2
- fix text encoding

* Tue Dec 04 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.2-alt1
- new version

* Mon Jul 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version

* Mon Jun 07 2010 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt2
- add fixes from FC

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Sun Feb 07 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt3
- Rebuilt with libassuan0.so.0.
- Cleaned up specfile.

* Wed Feb 03 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.6-alt2
- rebuilt with static assuan

* Mon Jul 06 2009 Sergey V Turchin <zerg@altlinux.org> 0.7.6-alt1
- new version

* Tue Dec 02 2008 Sergey V Turchin <zerg at altlinux dot org> 0.7.5-alt3
- built with libcap
- remove deprecated macroses from specfile

* Tue Sep 16 2008 Sergey V Turchin <zerg at altlinux dot org> 0.7.5-alt2
- built without libcap

* Tue May 13 2008 Sergey V Turchin <zerg at altlinux dot org> 0.7.5-alt1
- new version
- update build requires
- don't use internal g_malloc if defined

* Mon Dec 24 2007 Sergey V Turchin <zerg at altlinux dot org> 0.7.4-alt2
- fix requires

* Wed Dec 19 2007 Sergey V Turchin <zerg at altlinux dot org> 0.7.4-alt1
- new version

* Tue Jul 10 2007 Sergey V Turchin <zerg at altlinux dot org> 0.7.3-alt1
- new version

* Tue May 23 2006 Sergey V Turchin <zerg at altlinux dot org> 0.7.2-alt2
- rebuilt with new gcc

* Thu Jun 23 2005 Sergey V Turchin <zerg at altlinux dot org> 0.7.2-alt1
- new version; built with gtk-2

* Thu Jan 20 2005 Sergey V Turchin <zerg at altlinux dot org> 0.7.1-alt2
- rebuild with gcc3.4

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 0.7.1-alt1
- new version

* Tue Apr 06 2004 Sergey V Turchin <zerg at altlinux dot org> 0.7.0-alt2
- build all qt/gtk/curses
- update BuildRequires
- patch from PLD for build with system libassuan

* Thu Feb 12 2004 Sergey V Turchin <zerg at altlinux dot org> 0.7.0-alt1
- new version

* Fri Sep 05 2003 Sergey V Turchin <zerg at altlinux dot org> 0.6.9-alt3
- rebuild with Qt and with --enable-fallback-curses

* Wed May 07 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.6.9-alt2
- fix requires
- fix update of alternatives

* Wed May 07 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.6.9-alt1
- new version

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.6-alt3.1
- new alternatives config format

* Fri Mar 14 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.6-alt3
- PreReq fixes

* Thu Mar 13 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.6-alt2
- move to new alternatives scheme
- texinfo fix, added missing script to install info pages into info dir
- added trigger 'cause pervious scripts was proken

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 0.6.6-alt1
- build for ALT

* Wed Dec 11 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.6-1mdk
- update spec file from Fabrice MARIE <fabrice-marie-sec@ifrance.com>

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.5-1mdk
- Initial package
