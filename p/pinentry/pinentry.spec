Name: pinentry
Version: 0.8.1
Release: alt1

Group: File tools
Summary: Simple PIN or passphrase entry dialog
Url: http://gnupg.org/related_software/pinentry/
License: GPLv2+

Requires: %name-common = %version-%release

Requires: %name-qt = %version-%release
Requires: %name-gtk = %version-%release
Requires: %name-curses = %version-%release

# ftp://ftp.gnupg.org/gcrypt/pinentry/%name-%version.tar.gz
Source: %name-%version.tar
Patch4: 0004-Fix-qt4-pinentry-window-created-in-the-background.patch
# ALT
Patch100: pinentry-0.7.6-alt-system-assuan.patch

%define qtdir %_qt3dir
%def_with libcap

# due to qt macros
BuildRequires(pre): libqt3-devel libqt4-devel

%if_with libcap
BuildRequires: libcap-devel
%endif

# Automatically added by buildreq on Sun Feb 07 2010
BuildRequires: gcc-c++ libassuan0-devel libgtk+2-devel libncurses-devel

%description
This is simple PIN or passphrase entry dialog which
utilize the Assuan protocol as described by the aegypten project.

%package common
Group: %group
Summary: %summary
Conflicts: pinentry < 0.7.2 pinentry-curses < 0.7.2
Conflicts: pinentry-qt < 0.7.2 pinentry-gtk < 0.7.2

%package curses
Group: %group
Summary: %summary
Provides: %name-terminal = %version-%release
Provides: %name = %version-%release
Provides: %_bindir/%name
Requires: %name-common = %version-%release

%package gtk
Group: %group
Summary: %summary
Provides: %name = %version-%release
Provides: %name-x11 = %version-%release
Provides: %_bindir/%name
Requires: %name-common = %version-%release

%package qt
Group: %group
Summary: %summary
Provides: %name = %version-%release
Provides: %_bindir/%name
Provides: %name-x11 = %version-%release
Requires: libqt4-core >= %{get_version libqt4-core}
Requires: %name-common = %version-%release

%package qt3
Group: %group
Summary: %summary
Provides: %name = %version-%release
Provides: %_bindir/%name
Provides: %name-x11 = %version-%release
Requires: libqt3 >= %{get_version libqt3}
Requires: %name-common = %version-%release

%description curses
This is simple PIN or passphrase entry dialog which
utilize the Assuan protocol as described by the aegypten project.

%description gtk
This is simple PIN or passphrase entry dialog which
utilize the Assuan protocol as described by the aegypten project.

%description qt
This is simple PIN or passphrase entry dialog which
utilize the Assuan protocol as described by the aegypten project.

%description qt3
This is simple PIN or passphrase entry dialog which
utilize the Assuan protocol as described by the aegypten project.

%description common
This package contains common files and documentation for %name.

%prep
%setup
%patch4 -p1
%patch100 -p1

rm doc/*.info

pushd qt4
for h in pinentrydialog.h qsecurelineedit.h; do
    m="${h%%.h}.moc"
    rm $m
    moc-qt4 $h -o $m
done
popd

%build
%autoreconf
export QTDIR=%qtdir

%configure \
    --disable-rpath \
    --disable-pinentry-gtk \
    --enable-pinentry-gtk2 \
    --enable-pinentry-qt \
    --enable-pinentry-qt4 \
    --enable-pinentry-curses \
    %{subst_with libcap} \
    --enable-fallback-curses

%make_build

%install
%makeinstall_std
rm %buildroot%_bindir/%name
mv %buildroot%_bindir/%name-gtk{-2,}
mv %buildroot%_bindir/%name-qt{,3}
mv %buildroot%_bindir/%name-qt{4,}

mkdir -p %buildroot%_altdir
WEIGHT=10
for i in curses qt3 gtk qt; do
cat >%buildroot%_altdir/%name-$i<<EOF
%_bindir/%name	%_bindir/%name-$i	$WEIGHT
EOF
((WEIGHT+=10))
done

%files curses
%_altdir/%name-curses
%_bindir/%name-curses

%files gtk
%_altdir/%name-gtk
%_bindir/%name-gtk

%files qt
%_altdir/%name-qt
%_bindir/%name-qt

%files qt3
%_altdir/%name-qt3
%_bindir/%name-qt3

%files common
%doc AUTHORS NEWS README THANKS
%_infodir/*.info*

%changelog
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
