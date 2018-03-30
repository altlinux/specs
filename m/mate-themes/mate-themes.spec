Name: mate-themes
Version: 3.22.16
Release: alt1
Epoch: 1
Summary: MATE Desktop themes
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: mate-icon-theme libgtk-engines-default libgtk-engine-murrine

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: mate-common glib2-devel intltool pkgconfig(gtk+-2.0) pkgconfig(gdk-pixbuf-2.0)

%description
MATE Desktop themes

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-icon-mapping

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING README ChangeLog
%_datadir/themes/*
%_iconsdir/*

%changelog
* Fri Mar 30 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.16-alt1
- 3.22.16

* Fri Mar 16 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:3.22.15-alt1
- initial build from git.mate-desktop.org

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.22.14-alt1_2
- new fc release

