%define _metainfodir %_datadir/metainfo
%set_verify_elf_method rpath=relaxed
Name: 86box
Version: 4.0
Release: alt1
Summary: 86Box is a low level x86 emulator that runs older operating systems and software designed for IBM PC systems
Group: Emulators
License: GPLv3
Url: https://86box.net/

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildPreReq: rpm-macros-cmake rpm-macros-qt5 qt5-declarative-devel libslirp-devel extra-cmake-modules
BuildRequires: gcc-c++ libevdev-devel ecm wayland-devel libwayland-client-devel libffi-devel libappstream-glib libjack-devel libxkbcommon-devel liblash-devel pkgconfig(systemd) libdbus-devel libinstpatch-devel
BuildRequires: cmake libpng-devel zlib-devel libopenal-devel librtmidi-devel libpcre-devel qt5-tools-devel libfluidsynth-devel libpcre2-devel bzlib-devel libbrotli-devel libpulseaudio-devel libsndfile-devel libXdmcp-devel
BuildRequires: fontconfig-devel git-core libxcb libSDL2_ttf-devel libXi-devel libalsa-devel python-modules-compiler python-modules-encodings python-modules-logging python-modules-xml qt5-base-devel libxkbcommon-x11-devel

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

%ifarch %e2k armh
%cmake -DRELEASE=on -DDYNAREC=off -DCMAKE_SKIP_RPATH:BOOL=yes
%else
    %ifarch aarch64
	%cmake -DRELEASE=on -DNEW_DYNAREC=on -DCMAKE_SKIP_RPATH:BOOL=yes
    %else
	%cmake -DRELEASE=on -DCMAKE_SKIP_RPATH:BOOL=yes
    %endif
%endif

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
