Name: xtrlock
Version: 2.0
Release: alt1.qa1

Summary: Minimal X display lock program

License: GPL
Group: Graphical desktop/Other
Url: http://packages.debian.org/stable/x11/xtrlock.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

# http://ftp.debian.org/debian/dists/potato/main/source/x11/xtrlock_2.0-6.tar.gz
Source: http://debian.nctu.edu.tw/debian/pool/main/x/xtrlock/%{name}_%version-10.tar.bz2
Source1: %name-icons.tar.bz2
# TODO: make use TCB
Patch: %name.patch

# Automatically added by buildreq on Tue Feb 08 2011
BuildRequires: imake libX11-devel xorg-cf-files
BuildRequires: desktop-file-utils

%description
xtrlock is a very minimal X display lock program, which uses nothing
except the Xlib library.  It doesn't obscure the screen, it is
completely idle while the display is locked and you don't type at it,
and it doesn't do funny things to the X access control lists.

Default password: 123

%prep
%setup
%setup -T -D -a1 # unpack icons
%patch -p0

%build
xmkmf
%make CFLAGS="%optflags -DSHADOW_PWD" xtrlock

%install
install -m 755 -d  %buildroot/%_bindir/
install -m 755 -d  %buildroot/%_man1dir/
install -m 755 xtrlock %buildroot/%_bindir/
install -m 644 xtrlock.man %buildroot/%_man1dir/

# icon
install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
install -D -m 644 %{name}32.png %buildroot/%_niconsdir/%name.png
install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

mkdir -p %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Name=Xtrlock
Comment=X terminal lock
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=System;
EOF
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=System \
	--add-category=Utility \
	--add-category=X-Desktop \
	%buildroot%_desktopdir/xtrlock.desktop

%files
%doc debian/README.Debian
%_bindir/%name
%_desktopdir/%name.desktop
%_man1dir/*

%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for xtrlock

* Tue Feb 08 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- fix build, cleanup spec, update buildreqs
- add desktop file instead menu file

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.0-alt0.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for xtrlock
  * pixmap-in-deprecated-location for xtrlock
  * postclean-05-filetriggers for spec file

* Tue Feb 15 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1
- first build for ALT Linux Sisyphus (from debian 2.0-10)
- works with password 123 only

* Tue Apr 29 2003 David Abilleira <david1@abilleira.com> 2.0-1mdk
- First mdk version
