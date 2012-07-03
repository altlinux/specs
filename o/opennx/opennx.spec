# Enable USBIP support
%define with_usbip %{?_with_usbip: 1} %{?!_with_usbip: 0}

Summary: An OpenSource NX client
Name: opennx
Version: 0.16
Release: alt17.svn708
License: LGPL/GPL
Group: Networking/Remote access
Url: http://sourceforge.net/projects/opennx
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version.tar

Patch: %name-0.16-disable-opensc.patch

%if %with_usbip
Requires: usbip2-nxclient
%endif

# Automatically added by buildreq on Sat Sep 19 2009
BuildRequires: gcc-c++ imake libSM-devel libXmu-devel nx ImageMagick-tools
BuildRequires: libopensc-devel libsmbclient-devel
BuildRequires: libwxGTK-devel xorg-cf-files zip libcups-devel
BuildRequires: libXau-devel

%description
opennx is an OSS replacement for Nomachine's NX client.

%prep
%setup

#patch0 -p1

test -d conf || mkdir conf
#Convince gettextize not to modify EXTRA_DIST
test -f conf/config.rpath || touch conf/config.rpath
#Convince gettextize not to modify AC_CONFIG_FILES
test -f po/Makefile.in.in || touch po/Makefile.in.in
#Tweak gettextize
#Stupid gettextize uses /dev/tty for interactively getting a
#confirm of it's "oh so incredibly important notes".
#YES, i've read them at least a dozen times and now, i REALLY
#don't want to hit RETURN anymore!
GETTEXTIZE=`which gettextize`
test -n "$GETTEXTIZE" && \
    sed -e 's@/dev/tty@/dev/null@' "$GETTEXTIZE" > gettextize.local
test -f gettextize.local && sh gettextize.local -f --no-changelog
rm -f gettextize.local
test -e conf/mkinstalldirs || touch conf/mkinstalldirs
%autoreconf

%build
%configure \
    --bindir=%_libdir/%name/bin \
    --datadir=%_datadir/%name \
    --localedir=%_datadir/locale \
%if %with_usbip
    --enable-usbip \
%endif
    --with-nxproto=3.3.0

%make_build

%install
%makeinstall_std

mkdir -p %buildroot{%_bindir,%_desktopdir}

ln -s ../..%_libdir/%name/bin/%name %buildroot%_bindir/%name
ln -s ../../share/%name %buildroot%_libdir/%name/share
for f in nxesd nxssh nxservice nxproxy ; do
    ln -s  ../../../bin/$f %buildroot%_libdir/%name/bin/$f
done

mkdir -p %buildroot%_libdir/%name/%_lib

for lib in libsmbclient.so libcups.so ; do
    ln -s %_libdir/`readlink %_libdir/$lib` %buildroot%_libdir/%name/%_lib/$lib
done

cp %buildroot%_datadir/%name/applnk/xdg/*.desktop %buildroot%_desktopdir
rm -rf %buildroot%_datadir/%name/applnk
rm -rf %buildroot%_datadir/%name/icons
subst "s|/usr/NX/bin|%_bindir|g" %buildroot%_desktopdir/*

install -d %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
for f in nx opennx-admin opennx-wizard ; do
    convert -size 16x16 ./extres/scalable/apps/$f.svg %buildroot%_miconsdir/$f.png
    convert -size 32x32 ./extres/scalable/apps/$f.svg %buildroot%_niconsdir/$f.png
    convert -size 48x48 ./extres/scalable/apps/$f.svg %buildroot%_liconsdir/$f.png
done

install -d %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48}/mimetypes/
convert -background none -size 16x16 ./extres/scalable/mimetypes/nx-desktop.svg %buildroot%_iconsdir/hicolor/16x16/mimetypes/nx-desktop.png
convert -background none -size 32x32 ./extres/scalable/mimetypes/nx-desktop.svg %buildroot%_iconsdir/hicolor/32x32/mimetypes/nx-desktop.png
convert -background none -size 48x48 ./extres/scalable/mimetypes/nx-desktop.svg %buildroot%_iconsdir/hicolor/48x48/mimetypes/nx-desktop.png

%if %with_usbip
install -d -m 755 %buildroot%_sysconfdir/udev/rules.d
install -m 644 etc/*.rules %buildroot%_sysconfdir/udev/rules.d
%endif

%find_lang %name

%if %with_usbip
%pre
%_sbindir/groupadd -r opennx || :
%endif

%files -f %name.lang
%doc COPYING INSTALL
%_bindir/%name
%_libdir/%name
%_datadir/%name
%_desktopdir/*.desktop
%_liconsdir/*.png
%_niconsdir/*.png
%_miconsdir/*.png
%_iconsdir/hicolor/*/mimetypes/nx-desktop.png
%if %with_usbip
%_sysconfdir/udev
%endif

%changelog
* Wed Mar 28 2012 Boris Savelev <boris@altlinux.org> 0.16-alt17.svn708
- update from trunk

* Fri Jun 17 2011 Boris Savelev <boris@altlinux.org> 0.16-alt16.svn634
- update from trunk

* Wed Mar 02 2011 Boris Savelev <boris@altlinux.org> 0.16-alt15.svn611
- update from trunk

* Mon Feb 28 2011 Lenar Shakirov <snejok@altlinux.ru> 0.16-alt14.svn595
- build fixed: disable opensc support by default

* Tue Feb 15 2011 Lenar Shakirov <snejok@altlinux.ru> 0.16-alt13.svn595
- lib{smbclient,cups}.so symlinks packaging fixed for x86_64

* Thu Nov 18 2010 Boris Savelev <boris@altlinux.org> 0.16-alt12.svn595
- update from trunk

* Sat Nov 13 2010 Lenar Shakirov <snejok@altlinux.ru> 0.16-alt11.svn567
- package nx-desktop.png (closes: #24467)

* Thu Sep 09 2010 Boris Savelev <boris@altlinux.org> 0.16-alt10.svn567
- update from trunk

* Tue Aug 31 2010 Boris Savelev <boris@altlinux.org> 0.16-alt9.svn555
- update from trunk

* Mon Aug 02 2010 Boris Savelev <boris@altlinux.org> 0.16-alt8.svn547
- update from trunk
- fix build

* Sat Feb 13 2010 Boris Savelev <boris@altlinux.org> 0.16-alt7.svn481
- update from trunk

* Mon Jan 25 2010 Boris Savelev <boris@altlinux.org> 0.16-alt6.svn450
- update from trunk (work with proxy with authorization)

* Sat Jan 16 2010 Boris Savelev <boris@altlinux.org> 0.16-alt5.svn446
- update from trunk
- add russian localization

* Thu Nov 12 2009 Boris Savelev <boris@altlinux.org> 0.16-alt4.svn444
- update from trunk
- add symlink for nxproxy

* Sun Oct 11 2009 Boris Savelev <boris@altlinux.org> 0.16-alt3.svn442
- update from trunk
- add symlinks for cups and samba

* Thu Sep 24 2009 Boris Savelev <boris@altlinux.org> 0.16-alt2.svn427
- update buildreq
- fix repocop warning

* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 0.16-alt1.svn418
- intial build for Sisyphus

* Sun Apr 19 2009 Fritz Elfert <fritz@fritz-elfert.de>
- Set prefix to /opt/lsb/%name for FHS compliance
* Wed Apr 15 2009 Michael Kromer <michael.kromer@millenux.com>
- Fixes for SuSE Plattform (openSuSE/SLES)
* Sun Jan  7 2007 Fritz Elfert <fritz@fritz-elfert.de>
- Initial package
