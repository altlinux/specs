Name: gpu-screen-recorder
Version: 0.1
Release: alt1
Summary: This is a screen recorder that has minimal impact on system performance.
Url: https://git.dec05eba.com/gpu-screen-recorder/about/
Group: Video
License: GPL-3.0-only
Source: %name-%version.tar
Source1:%name-%version-gpu-screen-recorder-gtk.tar

Patch: add_debug_symbols.patch

BuildRequires: gcc-c++ libglvnd-devel libdrm-devel libXcomposite-devel libXrandr-devel libavfilter-devel 
BuildRequires: libwayland-egl-devel libcap-devel libavcodec-devel libavformat-devel libpulseaudio-devel
BuildRequires: libswresample-devel libgtk+3-devel

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
%patch0

%build
%add_optflags %optflags_shared
./build.sh
./gpu-screen-recorder-gtk/build.sh

%install
install -Dm755 "gsr-kms-server" %buildroot%_bindir/gsr-kms-server
install -Dm755 "gpu-screen-recorder" %buildroot%_bindir/gpu-screen-recorder
install -Dm644 "extra/gpu-screen-recorder.service" %buildroot/%_unitdir/gpu-screen-recorder.service

cd gpu-screen-recorder-gtk
install -Dm755 "gpu-screen-recorder-gtk" %buildroot%_bindir/gpu-screen-recorder-gtk
install -Dm644 "gpu-screen-recorder-gtk.desktop" %buildroot%_desktopdir/com.dec05eba.gpu_screen_recorder.desktop
install -Dm644 com.dec05eba.gpu_screen_recorder.appdata.xml %buildroot%_datadir/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml
install -Dm644 icons/hicolor/64x64/apps/com.dec05eba.gpu_screen_recorder.png %buildroot%_datadir/icons/hicolor/64x64/apps/com.dec05eba.gpu_screen_recorder.png
install -Dm644 icons/hicolor/128x128/apps/com.dec05eba.gpu_screen_recorder.png %buildroot%_datadir/icons/hicolor/128x128/apps/com.dec05eba.gpu_screen_recorder.png

%files cli
%_bindir/gsr-kms-server
%_bindir/gpu-screen-recorder
%_unitdir/gpu-screen-recorder.service

%files gtk
%_bindir/gpu-screen-recorder-gtk
%_desktopdir/com.dec05eba.gpu_screen_recorder.desktop
%_datadir/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml
%_datadir/icons/hicolor/64x64/apps/com.dec05eba.gpu_screen_recorder.png
%_datadir/icons/hicolor/128x128/apps/com.dec05eba.gpu_screen_recorder.png

%changelog
* Tue Jan 09 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build