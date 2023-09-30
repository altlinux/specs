%define optflags_lto %nil
Name:     denise
Version:  2.1
Release:  alt1

Summary:  Highly accurate C64/Amiga emulator
License:  GPL3
Group:    Emulators
Url:      https://sourceforge.net/projects/deniseemu/

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar
Source2:  LICENSE
BuildRequires: gcc-c++ libSDL2-devel libgtk+3-devel libpulseaudio-devel libopenal-devel libXrandr-devel libXfixes-devel bzlib-devel libpcre2-devel libbrotli-devel libudev-devel libfreetype-devel libpcre-devel


%description
Denise is a cycle accurate and platform independant c64 / amiga (not yet) emulator.
My motivation for this project is understanding how it works and write clean and easy readable code.
New in Denise are fast loaders such as ProfDOS, PrologicDOS, DolphinDOS, ProSpeed 1571, Turbo Trans and 1571 floppy emulation.

Denise supports REU, GeoRam, EasyFlash, EasyFlash^3, Gmod2, Retro Replay,
Action Replay, Final Cartridge, Light Guns/Pens, GunStick, Mouse 1351, Mouse Neos, Paddles.
I have added runAhead, PAL and CRT emulation, FreeSync/G-Sync support,
drag'n'drop and command line support.

Denise consists of 4 main modules.
"guikit", "driver", "emulation" could be used in any other project. "program" links these modules together.


%prep
%setup

%build
%make_install

%install
%makeinstall
install -D -m 0644 data/txt/licence.md %buildroot%_datadir
install -D -m 0644 %SOURCE2 %buildroot%_datadir

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/%name.png


%changelog
* Sat Sep 30 2023 Artyom Bystrov <arbars@altlinux.org> 2.1-alt1
- Update to new version

* Sat Jun 24 2023 Artyom Bystrov <arbars@altlinux.org> 2.0-alt2
- update sources
- fixed build on GCC13

* Tue Apr 25 2023 Artyom Bystrov <arbars@altlinux.org> 2.0-alt1
- update to new version
- added Commodore Amiga initial support

* Wed Dec 21 2022 Artyom Bystrov <arbars@altlinux.org> 1.1.3.1-alt1
- Initial build for Sisyphus
