Name: yuki-iptv
Version: 0.0.5
Release: alt1

Summary: IPTV player with EPG support (Astroncia IPTV fork)

License: GPLv3
Group: Video
Url: https://github.com/yuki-iptv/yuki-iptv

# Source-url: https://github.com/yuki-iptv/yuki-iptv/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: rpm-build-python3

Requires: libmpv2 ffmpeg

Requires: python3-module-PyQt5

# recommends
Requires: yt-dlp

%add_python3_path /usr/lib/%name

# by some uknown reason there are no packages provide that
%add_python3_req_skip gi.repository.GLib

%description
IPTV player with EPG support (Astroncia IPTV fork).

Disclaimer: yuki-iptv doesn't provide any playlists or other digital content.
The channels and pictures in the screenshots are for demonstration purposes only.

%prep
%setup
sed -i "s/__DEB_VERSION__/${pkgver//+*/}/g" usr/lib/yuki-iptv/yuki-iptv.py

%build
make

%install
mkdir -p %buildroot/
cp -r usr/ %buildroot/

%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/%name
/usr/lib/%name/
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/yuki-iptv.svg
%_datadir/metainfo/*

%changelog
* Thu May 11 2023 Vitaly Lipatov <lav@altlinux.ru> 0.0.5-alt1
- initial build for ALT Sisyphus
