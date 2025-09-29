%define _romsdir %_datadir/roms

Name:           miniplanets
Version:        rev0.4
Release:        alt1
Summary:        Doom styled first person shooter game
Group: Games/Other

License:        BSD
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

mkdir -p %buildroot%_romsdir/smd
install -p -m 0644 "Miniplanets REMIX Ver (REV04).bin" %buildroot%_romsdir/smd/%name.md

%files
%_romsdir/smd/%name.md

%changelog
* Tue Feb  4 2025 Artyom Bystrov <arbars@altlinux.org> rev0.4-alt1
- Initial build for Sisyphus