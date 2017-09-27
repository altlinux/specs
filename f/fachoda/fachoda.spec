Name: fachoda
Version: 2.1
Release: alt1

Summary: Flight simulator/arcade game
License: GPLv3
Group: Games/Arcade
Url: https://github.com/rixed/fachoda-complex/archive/release/2.1.zip

Packager: Alexey Appolonov <alexey@altlinux.org>

Source: %name-%version.tar

BuildRequires: libSDL-devel
BuildRequires: libopenal-devel
BuildRequires: libjpeg-devel

%description
Fachoda-complex is a flight simulator/arcade game for Linux,
tailored for small hardware configs.

%prep
%setup

%build
%make_build -C src

%install
%make_install -C src install DESTDIR=%buildroot

%files
%_gamesbindir/%name
/usr/lib/games/%name
%_defaultdocdir/%name

%changelog
* Tue Sep 27 2017 Alexey Appolonov <alexey@altlinux.org> 2.1-alt1
- Initial ALT Linux release.
