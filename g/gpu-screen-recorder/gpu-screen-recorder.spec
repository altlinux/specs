Name: gpu-screen-recorder
Version: 5.0.0
Release: alt1
Summary: This is a screen recorder that has minimal impact on system performance.
Url: https://git.dec05eba.com/gpu-screen-recorder/about/
Group: Video
License: GPL-3.0-only
Source: %name-%version.tar
Source1:%name-%version-gpu-screen-recorder-gtk.tar

BuildRequires: gcc-c++ libglvnd-devel libdrm-devel libXcomposite-devel libXrandr-devel libavfilter-devel 
BuildRequires: libwayland-egl-devel libcap-devel libavcodec-devel libavformat-devel libpulseaudio-devel
BuildRequires: libswresample-devel libgtk+3-devel vulkan-headers libavutil-devel libX11-devel libXfixes-devel
BuildRequires: libXdamage-devel libva-devel meson rpm-macros-meson ninja-build cmake libdbus-devel pipewire-libs-devel
BuildRequires: libayatana-appindicator3-devel
Requires: kmod

%package cli
Summary: The cli applitation for %name
Group: Video

%package gtk
Summary: The gui app for %name
Group: Video
Requires: %name-cli

%description
This is a screen recorder that has minimal impact on system performance 
by recording your monitor using the GPU only, similar to shadowplay on windows. 
This is the fastest screen recording tool for Linux.
This screen recorder can be used for recording your desktop offline, 
for live streaming and for nvidia shadowplay-like instant replay,
where only the last few minutes are saved.
Supported video codecs:

    H264 (default on Intel)
    HEVC (default on AMD and NVIDIA)
    AV1 (not currently supported on NVIDIA if you use GPU Screen Recorder flatpak)

%description cli
This package contains cli app for screen recorder

%description gtk
This package contains gui app for screen recorder

%prep
%setup -a1

%build
%add_optflags %optflags_shared
%meson
%meson_build
cd gpu-screen-recorder-gtk
%meson
%meson_build
cd ..

%install
%meson_install
cd gpu-screen-recorder-gtk
%meson_install
cd ..

%files cli
%_bindir/gsr-kms-server
%_bindir/gpu-screen-recorder
%_userunitdir/gpu-screen-recorder.service

%files gtk
%_bindir/gpu-screen-recorder-gtk
%_desktopdir/com.dec05eba.gpu_screen_recorder.desktop
%_datadir/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml
%_datadir/icons/hicolor/*/status/*.png
%_datadir/icons/hicolor/*/apps/*.png


%changelog
* Thu Jan 09 2025 Oleg Proskurin <proskur@altlinux.org> 5.0.0-alt1
- New version (Closes: #51382)

* Tue Jan 09 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build
