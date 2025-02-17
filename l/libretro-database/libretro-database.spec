Name: libretro-database
Version: 1.20.0
Release: alt1

Summary: Databases for RetroArch
License: GPL2
Group: Emulators

Url: https://github.com/libretro/mame
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: make

%description
RetroArch incoporates a ROM scanning system to automatically produce playlists.
Each ROM that is scanned by the playlist generator is checked against a database of ROMs
that are known to be good copies

%prep
%setup -n %name-%version

%build
%make_build

%install
%makeinstall_std

%files
%_datadir/libretro/database/*

%changelog
* Thu Feb  6 2025 Artyom Bystrov <arbars@altlinux.org> 1.20.0-alt1
- Update to new version

* Wed Mar 27 2024 Artyom Bystrov <arbars@altlinux.org> 1.18.0-alt1
- Initial commit for Sisyphus