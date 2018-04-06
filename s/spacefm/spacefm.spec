%define gtkver 2

Name: spacefm
Version: 1.0.6
Release: alt1%ubt
Summary: Multi-panel tabbed file and desktop manager
License: GPLv3+ and LGPLv3+
Group: File tools
Url: http://ignorantguru.github.io/spacefm
Source0: %name-%version.tar
Source1: %name.conf
Source2: session

BuildRequires(pre): rpm-build-ubt
BuildRequires: intltool libgtk+%gtkver-devel libudev-devel

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
  --htmldir=%_docdir/%name-%version \
  --disable-video-thumbnails \
  --with-%gtkver
%make_build

%install
make DESTDIR=%buildroot install
install -Dp -m 0644 %SOURCE1 %buildroot/%_sysconfdir/%name/%name.conf
install -Dp -m 0644 %SOURCE2 %buildroot/%_sysconfdir/xdg/%name/session

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING COPYING-LGPL ChangeLog README
%_sysconfdir/%name/
%_sysconfdir/xdg/%name/
%_bindir/*
%exclude %_bindir/%name-installer
%config(noreplace) %_sysconfdir/%name/%name.conf
%_datadir/%name/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%{name}*.png
%_iconsdir/Faenza/
%_datadir/mime/packages/%name-mime.xml

%changelog
* Fri Apr 06 2018 Anton Midyukov <antohami@altlinux.org> 1.0.6-alt1%ubt
- New version 1.0.6 (Closes: 34754)

* Thu Apr 30 2015 Motsyo Gennadi <drool@altlinux.ru> 1.0.0-alt1
- build for ALT Linux
