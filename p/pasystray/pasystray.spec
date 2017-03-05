Name:		pasystray
Version:	0.6.0
Release:	alt1

Summary:	a replacement for the deprecated padevchooser
License:	GPLv2.1
Group:		Sound

# packaged sources from upstream git repo tag
Source:		%name-%version.tar
# http://git.altlinux.org/gears/p/pasystray.git
Patch1:		%name-%version-%release.patch

# Automatically added by buildreq on Sun Mar 05 2017
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libavahi-devel libavahi-glib libcairo-devel libdbusmenu-devel libdbusmenu-gtk2 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgtk+2-devel libpango-devel libwayland-client libwayland-server perl pkg-config python-base python-modules xorg-xproto-devel
BuildRequires: libappindicator-devel libavahi-glib-devel libnotify-devel libpulseaudio-devel
Requires: pulseaudio-daemon >= 1.0

%description
A replacement for the deprecated padevchooser.

pasystray allows setting the default PulseAudio source/sink and moving
streams on the fly between sources/sinks without restarting the client
applications.


%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
	--enable-avahi \
	--enable-notify \
	--enable-x11 \
	--enable-statusicon \
	--enable-appindicator \
	--with-gtk=2 \
	#
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS
%doc LICENSE
%doc README.md
%_xdgconfigdir/autostart/*
%_bindir/*
%_desktopdir/*
%_man1dir/*
%dir %_datadir/%name
%_datadir/%name/*
%_pixmapsdir/*
%_iconsdir/hicolor/scalable/*

%changelog
* Thu Mar 02 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.

