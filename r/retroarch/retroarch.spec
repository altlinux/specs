Name:           retroarch
Version:        1.17.0
Release:        alt1
Summary:        Emulator frontend
License:        GPL-3.0-only
Group:          Emulators
URL:            http://www.retroarch.com
Source:         RetroArch-%{version}.tar.gz
Patch0:         retroarch-1.17.0-config.patch

BuildRequires:  libhid-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  p7zip
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  unzip
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(SDL2_gfx)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  vulkan-devel
BuildRequires:  libfribidi-devel
BuildRequires:  libdrm-devel
BuildRequires:  libfribidi-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  libfribidi-devel
BuildRequires:  wayland-devel
BuildRequires:  libwayland-egl-devel
BuildRequires:  wayland-protocols
BuildRequires:  libwayland-cursor-devel

Requires: retroarch-assets libretro libretro-core-info libretro-overlays 

ExcludeArch: ppc64le
%description
RetroArch is a modular multi-system emulator system that is designed to be
fast, lightweight, and portable. It has features few other emulators frontends
have, such as real-time rewinding and game-aware shading.

%prep
%setup -q -n RetroArch-%{version}

%autopatch -p1

# Change /usr/bin/env python to /usr/bin/python
sed -i s~%{_bindir}/env\ python~%{_bindir}/python~g tools/cg2glsl.py

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
./configure --prefix=%{_prefix} \
    --disable-sixel \
    --enable-hid \
    --enable-materialui \
    --enable-xmb \
    --enable-sdl2 \
    --enable-libusb \
    --enable-udev \
    --enable-threads \
    --enable-thread_storage \
    --enable-ffmpeg \
    --enable-ssa \
    --enable-dylib \
    --enable-networking \
    --enable-networkgamepad \
    --enable-opengl \
    --enable-x11 \
    --enable-xinerama\
    --enable-kms \
    --enable-egl \
    --enable-zlib \
    --enable-alsa \
    --enable-al \
    --enable-jack \
    --enable-pulse \
    --enable-freetype \
    --enable-xvideo \
    --enable-v4l2 \
    --enable-qt \
    --enable-dbus \
    --enable-wayland \
%ifarch x86
    --enable-sse \
%endif
    --enable-vulkan \
    --enable-7zip \
    --enable-mmap
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}
DESTDIR="%{buildroot}" make INSTALL="/bin/install -p" install

fdupes -rdN %{buildroot}

%files
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_bindir}/%{name}
%{_bindir}/%{name}-cg2glsl
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/com.libretro.*.xml
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man?/%{name}.?*
%{_mandir}/man?/%{name}-cg2glsl.?*
%{_datadir}/doc/%{name}

%changelog
* Mon Mar 18 2024 Artyom Bystrov <arbars@altlinux.org> 1.17.0-alt1
- Initial commit for Sisyphus (based on openmandriva srpm with fixes of saahriktu@)