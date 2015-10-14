Name: skomoroh
Version: 1.0
Release: alt1.1
Summary: Skomoroh is GUI for Speech Systems
Summary(ru_RU.UTF-8): Графическая программа для озвучки текстов
License: GPL
Group: Sound
Url: http://menestrel.sourceforge.net/

Packager: Anton Midyukov <antohami@altlinux.org>

Source: skomoroh-1.0.tar.gz
Source1: %name.desktop
Source2: %name.png
Source3: FB2_2_txt.xsl
Patch0: alt.patch

# Automatically added by buildreq on Tue Oct 13 2015
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libstdc++-devel phonon-devel zlib-devel
BuildRequires: gcc-c++ libqt4-devel libstdc++-devel zlib-devel
Requires: antiword xsltproc lynx xmlstarlet unzip sox RHVoice ru_tts espeak

%description
Skomoroh is GUI for Speech Systems
 
%description -l ru_RU.UTF-8
Skomoroh - универсальная программа для озвучки текстов, которая может
использовать в качестве tts-движка:
- ru_tts;
- eSpeak;
- RHVoice;
- или любой другой, который может работать из командной строки и, преобразование
в речь из которого, можно сохранить в виде wav файла.

%prep
%setup -n %name-%version
%patch0 -p1

%build
qmake-qt4 Skomoroh.pro PREFIX=%buildroot/usr
%make_build

%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_desktopdir
mkdir -p %buildroot/%_iconsdir
mkdir -p %buildroot%_datadir/%name
cp build/target/Skomoroh %buildroot/%_bindir/%name

install -Dp -m0644 %SOURCE1 %buildroot/%_desktopdir
install -Dp -m0644 %SOURCE2 %buildroot/%_iconsdir
install -Dp -m0755 %SOURCE3 %buildroot/%_datadir/%name

%files
%_bindir/*
%_desktopdir/*
%_iconsdir/*
%_datadir/%name/*

%changelog
* Wed Oct 14 2015 Anton Midyukov <antohami@altlinux.org> 1.0-alt1.1
- Small fix in spec file.

* Tue Oct 13 2015 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build for ALT Linux Sisyphus.
