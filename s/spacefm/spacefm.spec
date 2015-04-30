Name: spacefm
Version: 1.0.0
Release: alt1
Summary: Multi-panel tabbed file and desktop manager
License: GPLv3+ and LGPLv3+
Group: File tools
Url: http://ignorantguru.github.io/spacefm
Source0: https://github.com/IgnorantGuru/%name/archive/%version.tar.gz#/%name-%version.tar.gz
Source1: %name.conf

# Automatically added by buildreq on Thu Apr 30 2015 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libopencore-amrnb0 libopencore-amrwb0 libpango-devel libwayland-client libwayland-server perl-Encode perl-XML-Parser pkg-config python-base xorg-xproto-devel
BuildRequires: intltool libffmpegthumbnailer-devel libgtk+2-devel libudev-devel

# Mount without root requirement.
Requires: udisks2

%description
SpaceFM is a multi-panel tabbed file and desktop manager for GNU/Linux
with built-in VFS, udev-based device manager, customizable menu system
and bash integration. SpaceFM is popular among novice and power users
alike for its stability, speed, convenience and flexibility.

%prep
%setup

%build
%autoreconf
%configure \
  --with-preferable-sudo=%_bindir/xdg-su \
  --htmldir=%_docdir/%name-%version
%make_build

%install
make DESTDIR=%buildroot install
install -Dp -m 0644 %SOURCE1 %buildroot/%_sysconfdir/%name/%name.conf

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING COPYING-LGPL ChangeLog README
%dir %_sysconfdir/%name
%_bindir/*
%config(noreplace) %_sysconfdir/%name/%name.conf
%_datadir/%name/
%_desktopdir/*.desktop
%_datadir/icons/hicolor/*/apps/%{name}*.png
%_datadir/icons/Faenza/
%_datadir/mime/packages/%name-mime.xml

%changelog
* Thu Apr 30 2015 Motsyo Gennadi <drool@altlinux.ru> 1.0.0-alt1
- build for ALT Linux
