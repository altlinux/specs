%define _metainfodir %_datadir/metainfo
%set_verify_elf_method rpath=relaxed
Name: 86box
Version: 4.2
Release: alt2
Summary: 86Box is a low level x86 emulator that runs older operating systems and software designed for IBM PC systems
Group: Emulators
License: GPLv3
Url: https://86box.net/

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildPreReq: rpm-macros-cmake rpm-macros-qt5 qt5-declarative-devel libslirp-devel extra-cmake-modules
BuildRequires: gcc-c++ libevdev-devel ecm wayland-devel libwayland-client-devel libffi-devel libappstream-glib libjack-devel libxkbcommon-devel liblash-devel pkgconfig(systemd) libdbus-devel libinstpatch-devel
BuildRequires: cmake libpng-devel zlib-devel libopenal-devel librtmidi-devel libpcre-devel qt5-tools-devel libfluidsynth-devel libpcre2-devel bzlib-devel libbrotli-devel libpulseaudio-devel libsndfile-devel libXdmcp-devel
BuildRequires: fontconfig-devel libxcb libSDL2_ttf-devel libXi-devel libalsa-devel qt5-base-devel libxkbcommon-x11-devel

ExcludeArch: ppc64le

%description
86Box is a low level x86 emulator that runs older operating systems
and software designed for IBM PC systems and compatibles from 1981
through fairly recent system designs based on the PCI bus.

Important note.
For correct work you need BIOS files: https://github.com/86Box/roms/
Download release with the release number of emulator, and unzip in
~/.local/share/86Box/

%prep
%setup -n %name-%version

%build

%cmake \
	-DRELEASE=on \
	-DCMAKE_SKIP_RPATH:BOOL=yes \
%ifarch aarch64
	-DNEW_DYNAREC=on \
%endif
%ifarch %e2k armh loongarch64
	-DDYNAREC=off \
%endif
	%nil

%cmake_build

%install

%cmakeinstall_std

# install -D -m0755 ./%_cmake__builddir/src/86Box %buildroot%_bindir/%name

# install icons
for i in 48 64 72 96 128 192 256 512; do
  mkdir -p %buildroot%_iconsdir/hicolor/${i}x${i}/apps
  cp src/unix/assets/${i}x${i}/net.86box.86Box.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps
done

# install desktop file
install -Dpm0644 src/unix/assets/net.86box.86Box.desktop %buildroot%_desktopdir/net.86box.86Box.desktop

# install metadata
mkdir -p %buildroot%_metainfodir
cp src/unix/assets/net.86box.86Box.metainfo.xml %buildroot%_metainfodir
appstream-util validate-relax --nonet %buildroot%_metainfodir/net.86box.86Box.metainfo.xml

%files
%doc README.md COPYING
%_bindir/86Box
%_desktopdir/net.86box.86Box.desktop
%_metainfodir/net.86box.86Box.metainfo.xml
%_iconsdir/hicolor/*/apps/net.86box.86Box.png

%changelog
* Mon Aug 26 2024 Artyom Bystrov <arbars@altlinux.org> 4.2-alt2
- fix version (wrong update method)

* Mon Aug 26 2024 Artyom Bystrov <arbars@altlinux.org> 4.2-alt1
- update to new version

* Wed Feb 28 2024 Artyom Bystrov <arbars@altlinux.org> 4.1-alt1
- update to new version

* Thu Feb 08 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.0.1-alt2
- NMU: build for LoongArch (no DYNAREC here). While at it trimmed build
  dependencies (python2 stuff is not required, etc).

* Thu Feb  1 2024 Artyom Bystrov <arbars@altlinux.org> 4.0.1-alt1
- update to new version

* Wed Aug 30 2023 Artyom Bystrov <arbars@altlinux.org> 4.0-alt1
- update to new version

* Sat May 20 2023 Artyom Bystrov <arbars@altlinux.org> 3.11-alt2
- update sources
- add build on e2k (tnx @entityfx)

* Sat Dec 03 2022 Artyom Bystrov <arbars@altlinux.org> 3.11-alt1
- update to new version

* Fri Aug 5 2022 Artyom Bystrov <arbars@altlinux.org> 3.7-alt1
 - update to new version

* Mon Jul 26 2022 Artyom Bystrov <arbars@altlinux.org> 3.6-alt1
 - initial release
