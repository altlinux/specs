%define _unpackaged_files_terminate_build 1
%define _name org.aegisub.Aegisub

Name: aegisub
Version: 3.5.0
Release: alt1

Summary:  Cross-platform advanced subtitle editor
License: ISC and BSD-3-Clause and MIT
Group: Editors

Url: http://www.aegisub.org
Vcs: https://github.com/TypesettingTools/Aegisub

Source: %name-%version.tar
Source1: LuaJIT-04dca7911ea255f37be799c18d74c305b921c1a6.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: fontconfig-devel
BuildRequires: libass-devel
BuildRequires: git
BuildRequires: boost-devel
BuildRequires: boost-locale-devel
BuildRequires: libwxGTK3.2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libalsa-devel
BuildRequires: libportaudio2-devel
BuildRequires: libopenal-devel
BuildRequires: libffms2-devel
BuildRequires: libfftw3-devel
BuildRequires: libhunspell-devel
BuildRequires: libuchardet-devel
BuildRequires: libcurl-devel
BuildRequires: pkgconfig(luajit)
BuildRequires: libgtest-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-devel-headers
BuildRequires: libglvnd-devel
BuildRequires: boost-interprocess-devel
BuildRequires: boost-flyweight-devel
BuildRequires: boost-asio-devel
BuildRequires: pkgconfig(libportal-gtk3)

%description
%summary.

%prep
%setup
git config --global user.email "user at altlinux.org"
git config --global user.name "user"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version
tar -xf %SOURCE1 -C subprojects/

%build
%meson -Denable_update_checker=false
%meson_build

%install
%meson_install
rm -vr %buildroot%_libdir
rm -vr %buildroot%_includedir
rm -vr %buildroot%_datadir/luajit-2.1
rm -vr %buildroot%_datadir/licenses
rm -vr %buildroot%_datadir/man
%find_lang %name --all-name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_datadir/applications/%_name.desktop
%_iconsdir/hicolor/*/apps/%_name.*
%_datadir/metainfo/%_name.metainfo.xml
%doc *.md LICENCE

%changelog
* Mon Oct 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 3.5.0-alt1
- 3.4.2 -> 3.5.0

* Wed Oct 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.4.2-alt2
- Rebuild from upstream tarbol.
- Spec cleanup.

* Fri Sep 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.4.2-alt1
- Initial build for ALT Linux (git.e600e4780).
