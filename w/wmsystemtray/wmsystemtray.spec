# vim: set ft=spec: -*- rpm-spec -*-

Name: wmsystemtray
Version: 1.2
Release: alt1.qa1

Summary: A freedesktop.org system tray as a Window Maker dock app
Group: Graphical desktop/Window Maker
License: GPLv2+
Url: http://wmsystemtray.sourceforge.net/

# Automatically added by buildreq on Fri May 07 2010
BuildRequires: libXext-devel libXfixes-devel libXmu-devel libXpm-devel

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
wmsystemtray is a system tray using the freedesktop.org system tray
protocol designed as a Window Maker dock app. It has the ability to
display more than one dock window to make room for more tray icons,
and the ability to scroll through the icons if more are present than
will fit.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/wmsystemtray
%_man1dir/wmsystemtray.1*

%changelog
* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1.qa1
- Disclosure xorg-devel build requirement

* Fri May 07 2010 Alexey I. Froloff <raorn@altlinux.org> 1.2-alt1
- Built for Sisyphus

