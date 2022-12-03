Name: hypnotix
Version: 3.1
Release: alt2
Summary: An M3U IPTV Player
License: GPL-2.0-or-later
Group: Video
Url: https://github.com/linuxmint/hypnotix
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
BuildRequires: glib2-devel python3-dev
Requires: libmpv1
Requires: python3-module-cinemagoer
Requires: python3-module-pygobject3
Requires: python3-module-pycairo
Requires: python3-module-setproctitle
Requires: python3-module-xapp
Requires: libxapps-gir
BuildArch: noarch

%description
Hypnotix is an IPTV streaming application with support for live TV, movies and series.

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot/usr
cp -r usr %buildroot

%find_lang %name

%files
%doc README.md
%_bindir/%name
%_prefix/lib/%name/
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/org.x.%name.gschema.xml
%_datadir/%name/*
%_datadir/locale/*/LC_MESSAGES/*.mo
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Sat Dec 03 2022 Artyom Bystrov <arbars@altlinux.org> 3.1-alt2
- back localizations in package

* Sat Dec 03 2022 Artyom Bystrov <arbars@altlinux.org> 3.1-alt1
- update to new version

* Fri Nov 25 2022 Artyom Bystrov <arbars@altlinux.org> 1.4-alt1
- initial build for ALT Sisyphus
