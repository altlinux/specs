%def_enable Werror

Name: 	  pacman
Version:  0.9.0.19.git7cf259d
Release:  alt1

Summary:  Yet another pacman clone in C/C++ and SDL
License:  GPLv2, fonts of unknown license
Group:    Games/Arcade

Url:	  https://github.com/ebuc99/pacman

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar
Patch:	  pacman-0.9-alt1-fix_path.patch

BuildRequires: gcc-c++ libSDL2-devel libSDL2_image-devel libSDL2_ttf-devel libSDL2_mixer-devel

%description
This is a clone of the original pacman by Namco.
One of the main goals of this implementation is an SDL application
with a very low CPU usage.

%prep
%setup
%patch -p2

%build
%configure
%make_build

%install
%makeinstall_std
rm -r %buildroot/%_defaultdocdir/%name

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%_bindir/*
%_datadir/%name
%_datadir/applications/pacman.desktop

%changelog
* Tue Oct 31 2017 Grigory Ustinov <grenka@altlinux.org> 0.9.0.19.git7cf259d-alt1
- Initial build for Sisyphus.
