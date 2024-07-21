Name:           retroarch
Version:        1.19.1
Release:        alt2.2
Summary:        Emulator frontend
License:        GPL-3.0-only
Group:          Emulators
URL:            http://www.retroarch.com
Source:         RetroArch-%{version}.tar.gz
Source1:        retroarch-mobile.cfg
Source2:        retroarch-mobile.desktop
Source3:        retroarch-mobile.sh

Patch0:         retroarch-1.18.0-config.patch

Patch2000: 0001-Fix-E2K-build.patch
Patch2001: 0002-Add-E2K-init.patch


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

Requires: retroarch-assets libretro-core-info libretro-overlays retroarch-assets

ExcludeArch: ppc64le
%description
RetroArch is a modular multi-system emulator system that is designed to be
fast, lightweight, and portable. It has features few other emulators frontends
have, such as real-time rewinding and game-aware shading.

%package mobile
Summary:  Setup for mobile devices
Group:    Emulators
Requires: retroarch

%description mobile
Config file and desktop file for mobile devices like Pinephone Pro

%prep
%setup -q -n RetroArch-%{version}

%patch0 -p1

%ifarch %e2k
%patch2000 -p1
%patch2001 -p1
%endif

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
    --enable-debug \
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

install -Dpm0644 %SOURCE2 %buildroot%_desktopdir/%name-mobile.desktop
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/%name-mobile.cfg
install -Dm0755 %SOURCE3 %buildroot%_bindir/%name-mobile


fdupes -rdN %{buildroot}

%files
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_bindir}/%{name}
%{_bindir}/%{name}-cg2glsl
%{_datadir}/applications/org.libretro.RetroArch.desktop
%{_datadir}/metainfo/com.libretro.*.xml
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man?/%{name}.?*
%{_mandir}/man?/%{name}-cg2glsl.?*
%{_datadir}/doc/%{name}

%files mobile
%_bindir/%name-mobile
%_desktopdir/%name-mobile.desktop
%config %{_sysconfdir}/%{name}-mobile.cfg


%changelog
* Sun Jul 21 2024 Artyom Bystrov <arbars@altlinux.org> 1.19.1-alt2.2
- Fix path to assets and cores (ALTBUG#50786)
- disable download cores from the internet (all cores are in repo)

* Wed Jul  3 2024 Artyom Bystrov <arbars@altlinux.org> 1.19.1-alt2.1
- Fix path to assets and cores (ALTBUG#50786)

* Mon Jul  1 2024 Artyom Bystrov <arbars@altlinux.org> 1.19.1-alt2
- Fix config for Retroarch
- Add retroarch-assets on Requires (ALTBUG#50786)

* Thu Jun 27 2024 Artyom Bystrov <arbars@altlinux.org> 1.19.1-alt1
- Update to new version
- Added initial E2K support (thnks to ilyakurdyukov@)

* Tue Jun 25 2024 Artyom Bystrov <arbars@altlinux.org> 1.19.0-alt1.1
- Fix retroarch-mobile.sh
- Update retroarch-mobile.cfg

* Sat Jun 22 2024 Artyom Bystrov <arbars@altlinux.org> 1.19.0-alt1
- Update to new version
- Making possible to rewrite config file on mobile devices (smartphones, portable game consoles, etc.)
- Minor spec cleanup

* Wed May  1 2024 Artyom Bystrov <arbars@altlinux.org> 1.18.0-alt1.2
- getting back libretro core path to default

* Sun Mar 24 2024 Artyom Bystrov <arbars@altlinux.org> 1.18.0-alt1.1
- update to new version
- added cfg file for mobile devices

* Mon Mar 18 2024 Artyom Bystrov <arbars@altlinux.org> 1.17.0-alt1
- Initial commit for Sisyphus (based on openmandriva srpm with fixes of saahriktu@)