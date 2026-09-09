%define soname 0

Name: hrmp
Version: 0.15.0
Release: alt1
Summary: High-Resolution Music Player
License: GPL-3.0-or-later
Group: Sound
Url: https://highresmusicplayer.github.io
Vcs: https://github.com/HighResMusicPlayer/hrmp.git
Source0: %name-%version.tar
Patch: %name-alt-sndfile.patch

# %%ix86 fails with
# src/libhrmp/mkv.c:74:34: error: expected declaration specifiers or '...' before '__int128'
ExclusiveArch: x86_64 aarch64

BuildRequires(pre): cmake
BuildRequires: python3-module-docutils libalsa-devel libsndfile-devel libopus-devel libfaad-devel libgtk+3-devel libncurses-devel libcdio-devel

%description
hrmp is a high resolution music player.

%package -n lib%{name}%{soname}
Summary: %name library
Group: System/Libraries
Provides: lib%name = %EVR

%description -n lib%{name}%{soname}
%name library.

%prep
%setup
%autopatch -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_SKIP_RPATH=true
%cmake_build

%install
%cmake_install

%files
%doc {README,CODE_OF_CONDUCT}.md
%doc doc/images
%doc doc/{CLI,GETTING_STARTED,CONFIGURATION}.md
%doc LICENSE
%_man1dir/*.1*
%_man5dir/hrmp.conf.5*
%_bindir/%name
%_bindir/%name-ui
%_datadir/applications/hrmp-ui.desktop
%_datadir/icons/hicolor/*/apps/hrmp-ui.png

%files -n lib%{name}%{soname}
%_libdir/lib%{name}.so.%{soname}
%_libdir/lib%{name}.so.%version

%changelog
* Wed Sep 09 2026 L.A. Kostis <lakostis@altlinux.ru> 0.15.0-alt1
- Initial build for ALTLinux.
