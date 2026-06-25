Name:           lugaru
Version:        0.20260114
Release:        alt1
Source:         %name-master.tar.gz
License:        GPLv2+
Group:          Games/Arcade
Summary:        Third-person ninja rabbit action game
Requires:       %name-data = %EVR
URL:            https://osslugaru.gitlab.io/
VCS:            https://gitlab.com/osslugaru/lugaru

# Automatically added by buildreq on Thu Jun 25 2026
# optimized out: bash5 cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libImageMagick7-common libSDL2-devel libcrypt-devel libgcc15-devel libglvnd-devel libgpg-error libogg-devel libp11-kit libpng-devel libsasl2-3 libstdc++-devel pkg-config python3 python3-base sh5 zlib-devel
BuildRequires: ImageMagick-tools cmake flex gcc-c++ jsoncpp-devel libGLU-devel libSDL2-devel-static libSDL2_pango-devel libjpeg-devel libopenal-devel libvorbis-devel
BuildRequires(pre): rpm-build-cmake

%description
Lugaru (pronounced Loo-GAH-roo) is a cross-platform third-person action
game. The main character, Turner, is an anthropomorphic rebel bunny
rabbit with impressive combat skills. In his quest to find those
responsible for slaughtering his village, he uncovers a far-reaching
conspiracy involving the corrupt leaders of the rabbit republic and the
starving wolves from a nearby den. Turner takes it upon himself to fight
against their plot and save his fellow rabbits from slavery.

%package data
License: CC-BY-SA-3.0 AND CC-BY-SA-4.0
Summary:        Assets for Lugaru, a third-person ninja rabbit action game
Group:          Games/Arcade
BuildArch:      noarch

%description data
%summary

%prep
%setup -n %name-master

%build
%cmake  -DSYSTEM_INSTALL=ON \
        -DCMAKE_INSTALL_BINDIR=games \
        -DCMAKE_INSTALL_DATADIR=share/games

%cmake_build
for sz in 16 32 48 64; do
        magick Dist/Linux/lugaru.png Dist/Linux/lugaru-$sz.png
done
sed -i 's|^Exec=.*|Exec=%_gamesbindir/%name|' Dist/Linux/lugaru.desktop

%install
%cmake_install
for sz in 16 32 48 64; do
        install -D Dist/Linux/lugaru-$sz.png %buildroot%_iconsdir/hicolor/${sz}x${sz}/apps/lugaru.png
done
install -D Dist/Linux/lugaru.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc %_defaultdocdir/%name
%_gamesbindir/*
%_man6dir/%name.*
%_datadir/metainfo/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*

%files data
%_gamesdatadir/%name

%changelog
* Thu Jun 25 2026 Fr. Br. George <george@altlinux.ru> 0.20260114-alt1
- Resurrect from upstream still alive
- No versioning policy at upstream, so keep it 0

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.r262-alt2.2
- NMU: added URL

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.r262-alt2.1
- Rebuilt with libpng15

* Sun May 16 2010 Fr. Br. George <george@altlinux.ru> 0.0.r262-alt2
- Fix 'user do not saved' bug

* Sun May 16 2010 Fr. Br. George <george@altlinux.ru> 0.0.r262-alt1
- Initial build from scratch

