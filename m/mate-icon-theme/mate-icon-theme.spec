Name: mate-icon-theme
Version: 1.20.0
Release: alt1
Epoch: 1
Summary: Icon theme for MATE Desktop
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: mate-common icon-naming-utils intltool

%description
Icon theme for MATE Desktop

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
%doc AUTHORS COPYING README
%_iconsdir/mate
%_iconsdir/menta

%changelog
* Tue Mar 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
