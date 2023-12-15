Name: goldendict-ng
Version: 0.1.0
Release: alt1
Summary: The Next Generation GoldenDict. A feature-rich open-source dictionary lookup program, supporting multiple dictionary formats and online dictionaries.
License: GPL-3.0
ExclusiveArch: %qt6_qtwebengine_arches
Group: Text tools
URL: https://github.com/xiaoyifang/simple-eb/

Source: %name-%version.tar
Patch0: path_media_format_to_player.patch
Patch1: add_method_to_player_interface.patch
Patch2: rename_user_config_file.patch
Patch3: epwing_include_path_cpp.patch
Patch4: epwing_include_path_header.patch
Patch5: add_play_implementation_to_player.patch
Patch6: add_play_definition_to_player_header.patch

BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: cmake gcc-c++ qt6-webengine-devel qt6-webchannel-devel qt6-speech-devel qt6-speech-devel
BuildRequires: qt6-5compat-devel qt6-tools-devel qt6-svg-devel qt6-declarative-devel qt6-multimedia-devel
BuildRequires: bzip2-devel libxapian-devel libXtst-devel liblzo2-devel libXdmcp-devel opencc-devel liblzma-devel
BuildRequires: libzim-devel libfmt-devel libtomlplusplus-devel libavcodec-devel  libavformat-devel libavutil-devel
BuildRequires: libswresample-devel git zlib-devel libhunspell-devel libvorbis-devel 

Requires: qt6-webengine  qt6-webchannel  qt6-speech qt6-declarative 
Requires: qt6-5compat qt6-tools qt6-svg qt6-multimedia  
Conflicts: goldendict

%description
The Next Generation GoldenDict. A feature-rich open-source dictionary lookup program, supporting multiple dictionary formats and online dictionaries.
 - webengine with latest html/css feature support
 - support >4GB dictionary
 - support highdpi screen resolution
 - built with xapian as fulltext engine
 - support Qt5.15.2 and higher ,include latest Qt6
 - performance optimization(eg. >10000000 headwords support)
 - anki integration
 - dark theme
 - daily auto release support
 - lots of bug fixes and improvements

%prep
%setup
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6

%build
%cmake -DUSE_SYSTEM_FMT=ON -DUSE_SYSTEM_TOML=ON -DUSE_ALTERNATIVE_NAME=ON -DWITH_FFMPEG_PLAYER=OFF -DWITH_EPWING_SUPPORT=OFF
%cmake_build

%install
%cmake_install

%files 
%_bindir/goldendict-ng
%_datadir/applications/io.github.xiaoyifang.goldendict_ng.desktop
%_datadir/%name/
%_datadir/metainfo/*.xml
%_datadir/pixmaps/goldendict-ng.png

%changelog
* Mon Dec 11 2023 Oleg Proskurin <proskur@altlinux.org> 0.1.0-alt1
- New version

* Mon Nov 20 2023 Oleg Proskurin <proskur@altlinux.org> 0.1.0-alt1
- Initial build 



