Name: raw
Summary: game Another World (Out of this world) engine
Version: 0.3
Release: alt1
License: GPL2
Group: Games/Arcade
Url: https://github.com/fabiensanglard/Another-World-Bytecode-Interpreter
Packager: Ildar Mulyukov <ildar@altlinux.ru>

# GIT rev. 42641ea818d61f51363e5b3ae6c71d351e13bd59
Source: %name-%version.tar
Source1: %name.sh
Source2: %name.desktop
Source3: README_alt.md

# Automatically added by buildreq on Wed Sep 26 2012 (-bi)
# optimized out: elfutils libstdc++-devel python-base
BuildRequires: gcc-c++ libSDL-devel zlib-devel

%description
This is an Another World (Out Of This World in North America)
interpreter codebase. This work is based on:

- Piotr Padkowski's newRaw interpreter which was based on
- Gregory Montoir's reverse engineering of
- Eric Chahi's assembly code.

raw is a re-implementation of the engine used in the game Another World. This
game, released under the name Out Of This World in non-European countries, was
written by Eric Chahi at the beginning of the '90s. More information can be
found here : http://www.mobygames.com/game/sheet/p,2/gameId,564/.

Currently, only the english PC DOS version is supported ("Out of this World").

%prep
%setup
rm -rf %name
cp -a %SOURCE3 .

%build
make

%install
mv game %name
mkdir -p %buildroot{%_gamesbindir/,%_desktopdir/}
install -p -m 755 %SOURCE1 %name %buildroot%_gamesbindir/
install -p -m 644 %SOURCE2 %buildroot%_desktopdir/

%files
%_gamesbindir/*
%_desktopdir/*.desktop
%doc README*

%changelog
* Wed Sep 26 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus
