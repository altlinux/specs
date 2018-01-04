%define git d243325

Name: piper
Version: 0.2.900
Release: alt0.2.git%git
Summary: GTK+ application to configure gaming mice using ratbagd
Group: System/Configuration/Hardware
License: GPL2
Url: https://github.com/libratbag/%name
Source0: https://github.com/libratbag/%name/archive/v%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: python3-module-pygobject3-devel python3-dev

BuildArch: noarch

Requires: ratbagd

%description
Piper is a GTK+ application to configure gaming mice, using libratbag via
ratbagd.  In order to run Piper, ratbagd has to be running (without it, you'll
get to see a pretty mouse trap).

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README* COPYING
%_bindir/*
%dir %python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name
%dir %_datadir/%name
%_datadir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg

%changelog
* Thu Jan 04 2018 L.A. Kostis <lakostis@altlinux.ru> 0.2.900-alt0.2.gitd243325
- GIT d243325.

* Wed Oct 25 2017 L.A. Kostis <lakostis@altlinux.ru> 0.2.900-alt0.1.git39ddd05
- GIT 39ddd05.
- initial build for ALTLinux.
