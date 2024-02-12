Name:    zxtune
Version: r5056
Release: alt1

Summary: Crossplatform chiptune player
License: GPL
Group:   Sound
Url:     https://github.com/vitamin-caig/zxtune

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-qt5
BuildRequires: qt5-base-devel qt5-tools qt5-wayland-devel make gcc-c++ boost-devel boost-interprocess-devel boost-program_options-devel boost-locale-devel zlib-devel libalsa-devel libpulseaudio-devel zip unzip

%description
%summary

%prep
%setup

%build
%make_build qt.includes=/usr/include/qt5 tools.uic=uic-qt5 tools.moc=moc-qt5 tools.rcc=rcc-qt5 system.zlib=1 release=1 -C ./apps platform=linux

%install
mkdir -p %buildroot{%_bindir,%_datadir/%name,%_desktopdir,%_iconsdir}

for bin in benchmark xtractor zxtune123 zxtune-qt; do
install -Dm0755 ./bin/linux/release/$bin %buildroot%_bindir
done
install -Dpm0644 ./apps/zxtune-qt/dist/linux/zxTune.desktop %buildroot%_desktopdir
install -Dpm0644 ./apps/zxtune123/dist/zxtune.conf %buildroot%_datadir/%name
install -Dpm0644 ./apps/zxtune123/dist/dingux/zxtune.png %buildroot%_iconsdir/%name.png

%files
%doc README.md
%_bindir/benchmark
%_bindir/zxtune-qt
%_bindir/zxtune123
%_bindir/xtractor
%_datadir/%name/zxtune.conf
%_desktopdir/zxTune.desktop
%_iconsdir/%name.png

%changelog
* Mon Feb 12 2024 Artyom Bystrov <arbars@altlinux.org> r5056-alt1
- Initial build for Sisyphus
