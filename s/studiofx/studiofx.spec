%define _unpackaged_files_terminate_build 1

Name: studiofx
Version: 0.4.3
Release: alt1

Summary: Audio and video enhancer app implementing RNN for noise cancellation.
License: MIT
Group: Sound
Url: https://altlinux.space/alt-gnome/StudioFX
Vcs: https://altlinux.space/alt-gnome/StudioFX

Source: %name-%version.tar

Requires: ladspa_sdk
Requires: ladspa-swh-plugins
Requires: ladspa-noise-suppression-for-voice

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: gobject-introspection-devel
BuildRequires: pipewire-libs-devel
BuildRequires: libcamera-devel
BuildRequires: libopencv-devel

%description
StudioFX is an audio and video enhancer app designed to work
with various meeting apps and solutions to provide
 noiseless microphone audio via RNN filtering and other
various audio enhancements.

%package video
Summary: File to autoload a kernel module required for video pipeline.
Group: Video
Requires: %name = %EVR

%description video
StudioFX itself and a file to automatically load v4l2-loopback
on session start.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/studiofx
%_datadir/dbus-1/services/org.altlinux.StudioFX.service
%_datadir/polkit-1/rules.d/studiofx.rules
%_datadir/studiofx/presets
%_unitdir/studiofx-v4l2loopback.service
%_libexecdir/studiofx-setup
%_datadir/studiofx/selfie_segmenter.tflite
%_userunitdir/studiofx.service

%files video
%_modules_loaddir/v4l2loopback.conf

%changelog
* Wed Nov 25 2026 Pavel Mitrofanov <cobalt@altlinux.org> 0.4.3-alt1
- Initial commit.
