%define _romsdir %_datadir/roms

Name:           miniplanets
Version:        rev0.4
Release:        alt2
Summary:        Minimalistic platformer for Sega Megadrive/Genesis
Group: Games/Other

License:        Zlib
URL:            https://sik.itch.io/miniplanets
Vcs:		https://github.com/sikthehedgehog/miniplanets.git
Source0:        %name-%version.tar

BuildArch:      noarch
BuildRequires:  desktop-file-utils libappstream-glib

%description
Miniplanets - an unique platformer for Mega Drive, where you jump'n'run on small 3D planets
(the "miniplanets") in a quest to save Qisha's children and restore the Planelago System
back to normal.

%prep
%setup -q


%build
# Game data files.  Nothing to build!

%install

mkdir -p %buildroot%_romsdir/{genesis,megadrive}
install -p -m 0644 "Miniplanets REMIX Ver (REV04).bin" %buildroot%_romsdir/genesis/%name.gen
install -p -m 0644 "Miniplanets REMIX Ver (REV04).bin" %buildroot%_romsdir/megadrive/%name.smd

%files
%_romsdir/megadrive/%name.smd
%_romsdir/genesis/%name.gen

%changelog
* Tue Sep 30 2025 Artyom Bystrov <arbars@altlinux.org> rev0.4-alt2
- Change description and license
- Change paths for roms for compatibility with emulationstation-batocera

* Tue Feb  4 2025 Artyom Bystrov <arbars@altlinux.org> rev0.4-alt1
- Initial build for Sisyphus