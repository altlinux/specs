%define _unpackaged_files_terminate_build 1

Name: gpu-screen-recorder
Version: 5.12.3
Release: alt1
Summary: This is a screen recorder that has minimal impact on system performance

Url: https://git.dec05eba.com/gpu-screen-recorder/about/
VCS: https://repo.dec05eba.com/gpu-screen-recorder

Group: Video
License: GPL-3.0-only
Source0: %name-%version.tar
Source1: %name-%version-gpu-screen-recorder-gtk.tar
Source2: %name-%version-gpu-screen-recorder-notification-depends-mglpp-depends-mgl.tar
Source3: %name-%version-gpu-screen-recorder-notification-depends-mglpp.tar
Source4: %name-%version-gpu-screen-recorder-notification.tar
Source5: %name-%version-gpu-screen-recorder-ui.tar



BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ libglvnd-devel libdrm-devel libXcomposite-devel 
BuildRequires: libXrandr-devel libavfilter-devel libwayland-egl-devel 
BuildRequires: libcap-devel libavcodec-devel libavformat-devel
BuildRequires: libpulseaudio-devel libswresample-devel libgtk+3-devel
BuildRequires: vulkan-headers libavutil-devel libX11-devel libXfixes-devel
BuildRequires: libXdamage-devel libva-devel meson 
BuildRequires: ninja-build cmake libdbus-devel pipewire-libs-devel
BuildRequires: libayatana-appindicator3-devel libXi-devel libXcursor-devel
Requires: kmod

%package cli
Summary: The cli applitation for %name
Group: Video

%package devel
Summary: Plugin support
Requires: %name-cli = %EVR
Group: Video

%package gtk
Summary: The gui app for %name
Group: Video
Requires: %name-cli = %EVR

%package notification
Summary: Notification in the style of ShadowPlay
Group: Video
Requires: %name-cli = %EVR

%package ui
Summary: A fullscreen overlay UI for GPU Screen Recorder
Group: Video
Requires: %name-notification = %EVR

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
    AV1

%description cli
This package contains cli app for screen recorder

%description gtk
This package contains gui app for screen recorder

%description devel
GPU Screen Recorder supports plugins for rendering 
additional graphics on top of the monitor/window capture.

%description notification
On X11 the notification shows on the monitor that the cursor is on.
On Wayland the notification shows on the monitor the Wayland compositor considers focused.

%description ui
A fullscreen overlay UI for GPU Screen Recorder in the style of ShadowPlay.
The application is currently primarly designed for X11 but it can run on Wayland as well through XWayland, with some caveats because of Wayland limitations.

%prep
%setup -a1 -a2 -a3 -a4 -a5
cp -r gpu-screen-recorder-notification/depends/mglpp gpu-screen-recorder-ui/depends/

# build the main CLI
%build
%add_optflags %optflags_shared
%meson -Dnvidia_suspend_fix=false -Dplugin_examples=false
%meson_build

# build the GTK part
cd gpu-screen-recorder-gtk
%meson
%meson_build
cd ..

# build the notifications module
cd gpu-screen-recorder-notification
%meson
%meson_build
cd ..

# build the ui module
cd gpu-screen-recorder-ui
%meson
%meson_build
cd ..


%install
%meson_install
cd gpu-screen-recorder-gtk
%meson_install
cd ..
cd gpu-screen-recorder-notification
%meson_install
cd ..
cd gpu-screen-recorder-ui
%meson_install
cd ..


%files cli
%_bindir/gsr-kms-server
%_bindir/gpu-screen-recorder
%_userunitdir/gpu-screen-recorder.service
%_datadir/gpu-screen-recorder/scripts/*.sh
%_mandir/man1/gpu-screen-recorder.1.xz
%_mandir/man1/gsr-kms-server.1.xz

%files devel
%_includedir/gsr/plugin.h


%files gtk
%_bindir/gpu-screen-recorder-gtk
%_desktopdir/com.dec05eba.gpu_screen_recorder.desktop
%_datadir/icons/hicolor/*/status/*.png
%_datadir/icons/hicolor/*/apps/*.png

%files notification
%_bindir/gsr-notify
%_datadir/gsr-notify/* 

%files ui
%_bindir/gsr-global-hotkeys
%_bindir/gsr-kwin-helper
%_bindir/gsr-ui
%_bindir/gsr-ui-cli
%_bindir/gsr-hyprland-helper

%_userunitdir/gpu-screen-recorder-ui.service
%_desktopdir/gpu-screen-recorder.desktop
%_datadir/gsr-ui/* 

%changelog
* Mon Feb 02 2026 Oleg Proskurin <proskur@altlinux.org> 5.12.3-alt1
- New version

* Tue Jun 17 2025 Oleg Proskurin <proskur@altlinux.org> 5.5.9-alt1
- New version

* Thu Jan 09 2025 Oleg Proskurin <proskur@altlinux.org> 5.0.0-alt1
- New version (Closes: #51382)

* Tue Jan 09 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build
