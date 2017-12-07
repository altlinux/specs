%def_disable libcap
%def_enable qt5

Name: pinentry
Version: 1.0.0
Release: alt2%ubt

Group: File tools
Summary: Simple PIN or passphrase entry dialog
Url: http://gnupg.org/related_software/pinentry/
License: GPLv2+

Requires: %name-common = %version-%release

Requires: %name-qt4 = %version-%release
Requires: %name-gtk2 = %version-%release

# ftp://ftp.gnupg.org/gcrypt/pinentry/%name-%version.tar.gz
Source: %name-%version.tar
Source1: pinentry-wrapper
# ALT
Patch10: alt-mask-xprop.patch


BuildRequires(pre): rpm-build-ubt
# due to qt macros
%if_enabled qt5
BuildRequires(pre): qt5-base-devel
%endif
BuildRequires(pre): libqt4-devel
%if_enabled libcap
BuildRequires: libcap-devel
%endif
BuildRequires: gcc-c++ libgtk+2-devel libncursesw-devel
BuildRequires: libsecret-devel gcr-libs-devel libassuan-devel
BuildRequires: texinfo

%description
This is simple PIN or passphrase entry dialog which
utilize the Assuan protocol as described by the aegypten project.

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

%package qt4
Group: %group
Summary: %summary
Requires: xprop
Requires: %name-common = %EVR
Provides: %name = %version-%release
Provides: %name-x11 = %version-%release

%description gtk2
This is simple PIN or passphrase entry dialog which
utilize the Assuan protocol as described by the aegypten project.
%description gnome3
This is simple PIN or passphrase entry dialog which
utilize the Assuan protocol as described by the aegypten project.
%description qt5
This is simple PIN or passphrase entry dialog which
utilize the Assuan protocol as described by the aegypten project.
%description qt4
This is simple PIN or passphrase entry dialog which
utilize the Assuan protocol as described by the aegypten project.
%description common
This package contains common files and documentation for %name.

%prep
%setup -T -c
tar xf %SOURCE0
mv %name-%version gui

cp -ar gui gui-qt5
cp -ar gui tui
mv gui gui-qt4

install -m0644 %SOURCE1 pinentry-wrapper
%patch10 -p0

for d in gui-qt5 gui-qt4 tui ; do
    pushd $d
    %autoreconf
    popd
done

%build
%add_optflags -std=gnu++11

pushd gui-qt5
%configure \
    --disable-rpath \
    --disable-pinentry-curses \
    --disable-pinentry-tty \
    --disable-pinentry-gtk2 \
    --enable-pinentry-qt \
    --enable-pinentry-qt5 \
    --enable-pinentry-qt-clipboard \
    --disable-pinentry-gnome3 \
    --enable-libsecret \
    %{?_enable_libcap:--with-libcap}%{!?_enable_libcap:--without-libcap} \
    #
%make_build
popd

pushd gui-qt4
%configure \
    --disable-rpath \
    --disable-pinentry-curses \
    --disable-pinentry-tty \
    --enable-pinentry-gtk2 \
    --enable-pinentry-qt \
    --disable-pinentry-qt5 \
    --enable-pinentry-qt-clipboard \
    --enable-pinentry-gnome3 \
    --enable-libsecret \
    %{?_enable_libcap:--with-libcap}%{!?_enable_libcap:--without-libcap} \
    #
%make_build
popd

pushd tui
%configure \
    --disable-rpath \
    --enable-pinentry-curses \
    --enable-pinentry-tty \
    --disable-pinentry-gtk2 \
    --disable-pinentry-qt \
    --disable-pinentry-gnome3 \
    --disable-libsecret \
    %{?_enable_libcap:--with-libcap}%{!?_enable_libcap:--without-libcap} \
    #
%make_build
popd

%install
pushd gui-qt5
%makeinstall_std
popd
mv %buildroot/%_bindir/%name-qt %buildroot/%_bindir/%name-qt5
pushd gui-qt4
%makeinstall_std
popd
mv %buildroot/%_bindir/%name-qt %buildroot/%_bindir/%name-qt4
pushd tui
%makeinstall_std
popd
rm %buildroot%_bindir/%name

ln -s %name-gtk-2 %buildroot/%_bindir/%name-gtk
ln -s %name-qt5 %buildroot/%_bindir/%name-qt

install -p -m0755 -D pinentry-wrapper %buildroot/%_bindir/pinentry

%files gtk2
%_bindir/%name-gtk
%_bindir/%name-gtk-2

%files qt4
%_bindir/%name-qt4

%files qt5
%_bindir/%name-qt5
%_bindir/%name-qt

%files gnome3
%_bindir/%name-gnome3

%files common
%doc gui-qt5/AUTHORS gui-qt5/NEWS gui-qt5/README gui-qt5/THANKS
%_bindir/%name
%_bindir/%name-curses
%_bindir/%name-tty
%_infodir/*.info*

%changelog
* Thu Dec 07 2017 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt2%ubt
- fix detect pinentry-qt5 (ALT#34290)

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1%ubt
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
