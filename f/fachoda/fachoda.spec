Name: fachoda
Version: 2.1
Release: alt2

Summary: Flight simulator/arcade game
License: GPLv3
Group: Games/Arcade
Url: http://rixed.github.io/fachoda-complex/

Packager: Alexey Appolonov <alexey@altlinux.org>

# https://github.com/rixed/fachoda-complex/archive/release/2.1.zip
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
%makeinstall_std -C src

%files
%_gamesbindir/%name
%_libexecdir/games/%name
%_defaultdocdir/%name

%changelog
* Mon Oct 2 2017 Alexey Appolonov <alexey@altlinux.org> 2.1-alt2
- Second ALT Linux release.
