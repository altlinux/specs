#%%def_enable Werror

Name:     pacman
Version:  0.9.0.19.git7cf259d
Release:  alt4

Summary:  Yet another pacman clone in C/C++ and SDL
License:  GPLv2, fonts of unknown license
Group:    Games/Arcade

Url:      https://github.com/ebuc99/pacman

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar
Patch:    pacman-0.9-alt1-fix_path.patch

BuildRequires: gcc-c++ libSDL2_image-devel libSDL2_mixer-devel libSDL2_ttf-devel

%description
This is a clone of the original pacman by Namco.
One of the main goals of this implementation is an SDL application
with a very low CPU usage.

%prep
%setup
%patch -p2

%build
%configure
%make_build pacman_CXXFLAGS='%optflags -std=gnu++11'

%install
%makeinstall_std
rm -r %buildroot/%_defaultdocdir/%name

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%_bindir/*
%_datadir/%name
%_datadir/applications/pacman.desktop

%changelog
* Thu Oct 11 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.0.19.git7cf259d-alt4
- Fix menu icon.

* Thu Sep 20 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.0.19.git7cf259d-alt3
- Cleanup Build Requires.
- Rebuild for aarch64.

* Wed May 23 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.0.19.git7cf259d-alt2
- Force building with optflags and c++11 standart for e2k.
- Disable Werror flag.

* Tue Oct 31 2017 Grigory Ustinov <grenka@altlinux.org> 0.9.0.19.git7cf259d-alt1
- Initial build for Sisyphus.
