%define _name org.aegisub.Aegisub

Name: aegisub
Version: 3.4.2
Release: alt2

Summary:  Cross-platform advanced subtitle editor
License: ISC and BSD-3-Clause and MIT
Group: Editors

Url: http://www.aegisub.org
Vcs: https://github.com/TypesettingTools/Aegisub

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ fontconfig-devel libass-devel git
BuildRequires: boost-devel boost-locale-devel libwxGTK3.2-devel
BuildRequires: libpulseaudio-devel libalsa-devel libportaudio2-devel
BuildRequires: libopenal-devel libffms2-devel libfftw3-devel libhunspell-devel
BuildRequires: libuchardet-devel libcurl-devel pkgconfig(luajit) libgtest-devel
BuildRequires: boost-filesystem-devel boost-devel-headers libglvnd-devel
BuildRequires: boost-interprocess-devel boost-flyweight-devel
BuildRequires: boost-asio-devel

%description
%summary.

%prep
%setup

%build
%meson -Denable_update_checker=false
%meson_build

%install
%meson_install

%find_lang %name --all-name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_datadir/applications/%_name.desktop
%_iconsdir/hicolor/*/apps/%_name.*
%_datadir/metainfo/%_name.metainfo.xml
%doc *.md LICENCE

%changelog
* Wed Oct 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.4.2-alt2
- Rebuild from upstream tarbol.
- Spec cleanup.

* Fri Sep 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.4.2-alt1
- Initial build for ALT Linux (git.e600e4780).
