%define _romsdir %_datadir/roms

Name:           NovaTheSquirrel
Version:        1405
Release:        alt1
Summary:        Minimalistic platformer for Sega Megadrive/Genesis
Group: Games/Other

License:        GPLv3 and CC BY-NC-SA 4.0
URL:            https://novasquirrel.itch.io/nova-the-squirrel
Vcs:		https://github.com/NovaSquirrel/NovaTheSquirrel
Source0:        %name-%version.tar

BuildArch:      noarch
BuildRequires:  make cc65

%description
Nova the Squirrel is an NES game that stars Nova Storm, a green squirrel,
who finds herself in an unfamiliar world and is pushed into the position
of playing the hero, using a newly found ability to copy abilities from enemies.

%prep
%setup -q


%build

ca65 src/nova.s -o src/nova.o -l nova.lst -g
ld65 -C src/nova.x src/nova.o -o nova.nes -m map.txt --dbgfile debug.dbg

%install
mkdir -p %buildroot%_romsdir/nes
install -p -m 0644 nova.nes %buildroot%_romsdir/nes/%name.nes


%files
%_romsdir/nes/%name.nes

%changelog
* Thu Oct  2 2025 Artyom Bystrov <arbars@altlinux.org> 1405-alt1
- Initial build for Sisyphus