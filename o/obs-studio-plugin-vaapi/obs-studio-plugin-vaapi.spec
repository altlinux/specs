Name: obs-studio-plugin-vaapi
Version: 0.4.0
Release: alt1

Summary: OBS Studio VAAPI support via GStreamer

License: GPLv2
Group: Video
Url: https://github.com/fzwoch/obs-vaapi/

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(libobs)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(libpci)

Requires: obs-studio
Requires: gstreamer-vaapi
Requires: gst-plugins-base1.0
Requires: gst-plugins-good1.0
Requires: gst-plugins-bad1.0
Requires: gst-plugins-ugly1.0

ExclusiveArch: %ix86 x86_64

%description
GStreamer based VAAPI encoder implementation. Taken out of the GStreamer OBS plugin as a standalone plugin.
Simply because the FFMPEG VAAPI implementation shows performance bottlenecks on some AMD hardware.
Supports H.264 and H.265.
Note that not all options in the encoder properties may be working.
VAAPI is just an interface and it is up to the GPU hardware and driver what is actually supported.
Not all options make sense to change.

%prep
%setup

%build
%meson \
        --prefix=%_libdir/obs-plugins \
        --libdir=%_libdir/obs-plugins \
        --buildtype=release

%meson_build -v

%install
%meson_install

%files
%doc README.md LICENSE
%_libdir/obs-plugins/obs-vaapi.so

%changelog
* Tue Oct 24 2023 Mikhail Tergoev <fidel@altlinux.org> 0.4.0-alt1
- initial build for ALT Sisyphus

