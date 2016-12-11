Name: 7kaa
Version: 2.14.6
Release: alt1
Summary: Seven Kingdoms: Ancient Adversaries

License: GPLv3+ and GPLv2+
Group: Games/Strategy
Url: http://7kfans.com/
# Source-url: https://github.com/the3dfxdude/7kaa/releases/download/v%version/7kaa-%version.tar.xz
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source1: %name.autodlrc
Source2: %name-data-installer

BuildRequires: gcc-c++ libSDL2-devel libSDL2_net-devel libenet-devel libopenal-devel desktop-file-utils ImageMagick-tools
Requires: %name-data = %version-%release

%description
Seven Kingdoms is a real-time strategy (RTS) computer game developed
by Trevor Chan of Enlight Software. The game enables players to
compete against up to six other kingdoms allowing players to conquer
opponents by defeating them in war (with troops or machines),
capturing their buildings with spies, or offering opponents money
for their kingdom.

Seven Kingdoms: Ancient Adversaries is a free patch provided by
Interactive Magic and added three new cultures, the Egyptians, the
Mughals and the Zulus, and a new war machine, Unicorn.

%package data
Summary: In-Game data Seven Kingdoms: Ancient Adversaries
Group: Games/Strategy
BuildArch: noarch

%description data
In-Game music data Seven Kingdoms: Ancient Adversaries

%package music
License: Redistributable, no modification permitted
Group: Games/Strategy
BuildArch: noarch
Summary: In-Game music for Seven Kingdoms: Ancient Adversaries
Requires: %name-data = %version-%release

%description music
In-Game music for Seven Kingdoms: Ancient Adversaries
Due to license issue, you need to run 7kaa-data-installer install the music.

%prep
%setup

%build
export CXXFLAGS="%optflags -fsigned-char"
%configure
%make_build

%install
%makeinstall_std

for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
        convert data/image/7k_icon.bmp -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/7kaa_icon.png
done

### == desktop file
cat>%name.desktop<<END
[Desktop Entry]
Name=%name
GenericName=Seven Kingdoms: Ancient Adversaries
Comment=A real-time strategy (RTS) computer game
Exec=%_bindir/%name
Icon=7kaa_icon
Terminal=false
Type=Application
Categories=Game;StrategyGame
END

desktop-file-install --dir=%buildroot%_desktopdir %name.desktop

### == music autodownload
%global music_installer %name-music-installer
%global data_installer %name-data-installer
%global prj_music_dir %_datadir/%name/music
mkdir -p %buildroot%prj_music_dir
mkdir -p %buildroot%_docdir/%name-music

### === Downloader Music
cat >%music_installer<<END
#!/bin/bash
echo "This program will download necessary data files."
if [ -r %prj_music_dir/win.wav ];then
   echo "music already downloaded" > /dev/stderr
   exit 2
fi
if ! %_datadir/autodl/AutoDL.py %prj_music_dir/%name.autodlrc; then
    echo "Error on music download" > /dev/stderr
    exit 3
fi
cd /tmp/%name-music
tar xjvf /tmp/%name-music/%name-music.tar.bz2
echo "Input password root: "
su -c install -v -m 644 /tmp/%name-music/%name-music/music/* %_datadir/%name/music
echo "Done"
END

install -m 755 %SOURCE2 %buildroot%_bindir
install -m 755 %music_installer %buildroot%_bindir
install -m 644 %SOURCE1 %buildroot%prj_music_dir

%postun music
if [ $1 -eq 0 ] ; then
## When Uninstall
    rm -fr %prj_music_dir
fi

%files
%doc %_docdir/%name
%_bindir/%name
%_bindir/%data_installer
%_desktopdir/%name.desktop

%files data
%dir %_datadir/%name
%_datadir/%name/[^m]*
%_liconsdir/*
%_niconsdir/*
%_miconsdir/*

%files music
%_bindir/%music_installer
%dir %prj_music_dir
%prj_music_dir/%name.autodlrc

%changelog
* Sun Dec 11 2016 Anton Midyukov <antohami@altlinux.org> 2.14.6-alt1
- new version (2.14.6) with rpmgs script

* Tue Jul 26 2016 Anton Midyukov <antohami@altlinux.org> 2.14.5-alt1
- Initial build for ALT Linux Sisyphus (Thanks Fedora Team).
