Name: vlc-plugin-pause-click
Version: 2.2.0
Release: alt2

Summary: Pause Click plugin for VLC
License: LGPLv2.1+
Group: Video

Url: https://github.com/nurupo/vlc-pause-click-plugin
Source: %name-%version.tar

BuildRequires: libvlc-devel

%description
VLC plugin that allows you to pause/play a video by clicking
on the video image.
Can be configured to work nicely with double-click-to-fullscreen by
enabling "Prevent pause/play from triggering on double click" option
in the settings. By default it pauses on every click instead.

%prep
%setup

%build
%make

%install
%makeinstall_std

%files
%_libdir/vlc/plugins/video_filter/libpause_click_plugin.so

%changelog
* Tue Oct 03 2023 Kirill Izmestev <felixz@altlinux.org> 2.2.0-alt2
- Spec moved to .gear directory
- Removed dependency on vlc package
- Removed extra lines from the spec

* Mon May 02 2022 Kirill Izmestev <felixz@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
