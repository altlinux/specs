%define _name org.aegisub.Aegisub

Name: aegisub
Version: 3.4.2
Release: alt1

Summary:  Cross-platform advanced subtitle editor
License: ISC and BSD-3-Clause and MIT
Group: Editors

Url: http://www.aegisub.org
Vcs: https://github.com/TypesettingTools/Aegisub

Source: %name-%version.tar
Source1: LuaJIT-04dca7911ea255f37be799c18d74c305b921c1a6.tar

Patch: luajitwrap-3.4.2-alt-build.patch

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
git config --global user.email "user at altlinux.org"
git config --global user.name "user"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

#Add submodule luajit, for new luajit run
#meson subprojects download luajit
tar -xf %SOURCE1 -C subprojects/
%patch -p0

%build
meson subprojects packagefiles --apply luajit
export CXXFLAGS+=" -fpermissive"
%meson \
    -Dluajit:default_library=static \
    -Db_lto=false \
    -Dtests=false \
    -Dopenal=disabled \
    -Dportaudio=disabled \
    -Denable_update_checker=false
%meson_build

%install
mkdir -p %buildroot
meson install -C %_arch-alt-linux --destdir "%buildroot" --skip-subprojects luajit

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_datadir/applications/%_name.desktop
%_iconsdir/hicolor/*/apps/%_name.*
%_datadir/metainfo/%_name.metainfo.xml
%doc *.md LICENCE

%changelog
* Fri Sep 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.4.2-alt1
- Initial build for ALT Linux (git.e600e4780).

