Name: rustdesk
Version: 1.3.5
Release: alt1

Summary: An open-source remote desktop, and alternative to TeamViewer
License: AGPL-3.0
Group: Networking/Remote access
Url: https://rustdesk.com/
Vcs: https://github.com/rustdesk/rustdesk.git

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: vendor.tar
Source2: vcpkg-env.tar
Source3: %name.sh
Source4: libsciter-install.sh
Patch: %name-%version-alt-no-cacao-deps.patch
Patch1: %name-%version-alt-vendoring-config.patch
Patch2: %name-%version-alt-cargolock-fix.patch
Patch3: %name-%version-alt-fix-main-page-ru.patch
Patch4: %name-%version-alt-change-ffmpeg-opts.patch

BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: libXi-devel
BuildRequires: libXtst-devel
BuildRequires: clang-devel
BuildRequires: glib2-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: libpulseaudio-devel
BuildRequires: xdotool-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libgtk+3-devel
BuildRequires: libdbus-devel
BuildRequires: libpam0-devel
BuildRequires: libalsa-devel
BuildRequires: libva-devel
BuildRequires: libvdpau-devel
BuildRequires: nv-codec-headers
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: vcpkg
BuildRequires: nasm
BuildRequires: ninja-build
BuildRequires: patchelf
BuildRequires: zip
BuildRequires: git-core
#for tray to work
Requires: libayatana-appindicator3-1

%description
Yet another remote desktop software, written in Rust. Works out of the box, no
configuration required. You have full control of your data, with no concerns
about security. You can use our rendezvous/relay server, set up your own, or
write your own rendezvous/relay server.

NOTE: To use this program, you need to get a third-party shared library -
libsciter-gtk.so. Run the "libsciter-install" command as root after package
installing to download and install this library.

%prep
%setup -a1
%autopatch -p1
#prepare vcpkg environment
tar -xvf %SOURCE2 -C $HOME/
#not use default parameters
rm -v vcpkg.json

%build
#build static libs and headers via vcpkg
export VCPKG_ROOT=$HOME/vcpkg-env
export VCPKG_FORCE_SYSTEM_BINARIES=1
vcpkg install --no-downloads --overlay-ports=res/vcpkg libvpx libyuv opus aom ffmpeg
#build binary
python3 res/inline-sciter.py
cargo build %_smp_mflags --offline --release --bin %name --features inline,hwcodec

%install
install -D %SOURCE3 %buildroot%_bindir/%name
install -D %SOURCE4 %buildroot%_bindir/libsciter-install
install -D target/release/%name -t %buildroot%_libexecdir/%name/
install -D res/%name.service -t %buildroot%_unitdir/
install -D res/%name.desktop -t %buildroot%_datadir/applications/
install -D res/%name-link.desktop -t %buildroot%_datadir/applications/
install -D res/128x128.png %buildroot%_datadir/pixmaps/%name.png

%check
#has no tests

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.* LICENCE
%_bindir/%name
%_bindir/libsciter-install
%_libexecdir/%name
%_unitdir/%name.service
%_datadir/applications/*.desktop
%_datadir/pixmaps/*.png

%changelog
* Tue Dec 10 2024 Anton Kurachenko <srebrov@altlinux.org> 1.3.5-alt1
- Initial build for Sisyphus.
