Name: gadmin-dhcpd
Version: 0.4.2
Release: alt2

Summary: Gadmin-dhcpd is a fast and easy to use GTK+ administration tool for the ISC DHCPD server
Group: Development/C
Source: %name-%version.tar.gz
Source1: %name.pam
License: GPL
Packager: Eugene Ostapets <eostapets@altlinux.org>

# Automatically added by buildreq on Mon Apr 30 2007
BuildRequires: libgtk+2-devel  ImageMagick
Obsoletes: gdhcpd < 0.4
Provides: gdhcpd
Patch: alt-gadmin-dhcpd-desktop.patch
%description
GDHCPD is a fast and easy to use GTK+ administration tool for the ISC DHCPD server.

%prep
%setup

%build
%configure \
	--sysconfdir=%_sysconfdir/dhcp \
	--localstatedir=/var/lib/dhcp \
	--sbindir=/usr/sbin \
	SYSINIT_START_CMD="chkconfig dhcpd on" \
	SYSINIT_STOP_CMD="chkconfig dhcpd off" \
	LEASE_FILE="/var/lib/dhcpd/dhcpd.leases"

%make_build

%install
%make DESTDIR=%buildroot install
rm -r %buildroot%_docdir/%name

# pam auth
install -d %buildroot%_bindir
install -d %buildroot%_sysconfdir/pam.d/
install -d %buildroot%_sysconfdir/security/console.apps
install -m 644 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -m 644 etc/security/console.apps/%name %buildroot%_sysconfdir/security/console.apps/%name

ln -s consolehelper %buildroot%_bindir/%name

# desktop entry
install -d %buildroot%_desktopdir
install -m 644 desktop/net-gadmin-dhcpd.desktop %buildroot%_desktopdir/%name.desktop
for size in 16x16 32x32 48x48 ; do
    mkdir -p %buildroot%_iconsdir/hicolor/$size/apps
    convert %buildroot%_pixmapsdir/%name.png -size $size %buildroot%_iconsdir/hicolor/$size/apps/%name.png
done

%find_lang %name

%files -f %name.lang
%doc README AUTHORS ChangeLog COPYING
%_bindir/%name

%config %_sysconfdir/pam.d/*
%config(noreplace) %_sysconfdir/security/console.apps/*

%_desktopdir/*.desktop
%_sbindir/%name
%_pixmapsdir/%name.png
%dir %_pixmapsdir/%name
%_pixmapsdir/%name/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Wed Mar 12 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.2-alt2
- fix desktop file (tnx repocop)
- fix icons (tnx repocop)

* Thu Mar 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.2-alt1
- new version
- rename with upstream

* Mon Apr 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3.1-alt0.1
- first build

