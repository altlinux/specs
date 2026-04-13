%define _unpackaged_files_terminate_build 1
Name: goldendict-ng
Version: 26.3.0
Release: alt1
Summary: The Next Generation GoldenDict. A feature-rich open-source dictionary lookup program, supporting multiple dictionary formats and online dictionaries.
License: GPL-3.0
ExclusiveArch: %qt6_qtwebengine_arches
Group: Text tools
URL: https://github.com/xiaoyifang/goldendict-ng

Source: %name-%version.tar
Patch0: rename_user_config_file.patch
Patch1: disable_default_online_resources.patch


BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: cmake gcc-c++ qt6-webengine-devel qt6-webchannel-devel qt6-speech-devel qt6-speech-devel
BuildRequires: qt6-5compat-devel qt6-tools-devel qt6-svg-devel qt6-declarative-devel qt6-multimedia-devel
BuildRequires: bzip2-devel libxapian-devel libXtst-devel liblzo2-devel libXdmcp-devel opencc-devel liblzma-devel
BuildRequires: libzim-devel libfmt-devel libtomlplusplus-devel libavcodec-devel  libavformat-devel libavutil-devel
BuildRequires: libswresample-devel git zlib-devel libhunspell-devel libvorbis-devel 

Requires: qt6-webengine  qt6-webchannel  qt6-speech qt6-declarative 
Requires: qt6-5compat qt6-tools qt6-svg qt6-multimedia  
Conflicts: goldendict
Provides: stardict = 3

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
%patch1 -p1


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
* Mon Apr 13 2026 Oleg Proskurin <proskur@altlinux.org> 26.3.0-alt1
- New version

* Mon Jun 30 2025 Oleg Proskurin <proskur@altlinux.org> 25.07.0-alt1
- New version (Closes: #54942)

* Wed Feb 19 2025 Oleg Proskurin <proskur@altlinux.org> 25.04.0-alt1
- New version

* Fri Dec 13 2024 Oleg Proskurin <proskur@altlinux.org> 24.09.01-alt1
- New version

* Tue May 14 2024 Oleg Proskurin <proskur@altlinux.org> 24.05.05-alt1
- New version

* Thu Dec 21 2023 Oleg Proskurin <proskur@altlinux.org> 23.12.07-alt1
- New version

* Mon Dec 11 2023 Oleg Proskurin <proskur@altlinux.org> 0.1.0-alt1
- New version

* Mon Nov 20 2023 Oleg Proskurin <proskur@altlinux.org> 0.1.0-alt1
- Initial build 



