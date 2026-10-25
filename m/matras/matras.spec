Name: matras
Version: 1.0.1
Release: alt1
Summary: Native Mattermost client for GNOME
License: GPL-3.0-only
Group: Networking/Instant messaging
Url: https://altlinux.space/toxblh/matras

ExcludeArch: %ix86

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(alsa)
BuildRequires: glib2-devel

%description
Matras is a native Mattermost client for GNOME, built with GTK4 and
libadwaita. It supports chat, threads, notifications, single sign-on,
and calls.

%prep
%setup -a1
%rust_prep
%autopatch -p 1

%build
# libopus workaround
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%rust_build -p matras

%install
%rust_install
install -Dpm644 data/ru.toxblh.Matras.desktop \
    %buildroot%_datadir/applications/ru.toxblh.Matras.desktop
install -Dpm644 data/ru.toxblh.Matras.metainfo.xml \
    %buildroot%_datadir/metainfo/ru.toxblh.Matras.metainfo.xml
install -Dpm644 data/icons/hicolor/scalable/apps/ru.toxblh.Matras.svg \
    %buildroot%_datadir/icons/hicolor/scalable/apps/ru.toxblh.Matras.svg

%files
%_bindir/matras
%_datadir/applications/ru.toxblh.Matras.desktop
%_datadir/metainfo/ru.toxblh.Matras.metainfo.xml
%_datadir/icons/hicolor/scalable/apps/ru.toxblh.Matras.svg
%doc README.md LICENSE

%changelog
* Fri Oct 23 2026 Vasiliy Doylov <neko@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
