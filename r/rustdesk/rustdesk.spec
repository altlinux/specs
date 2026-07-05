Name: rustdesk
Version: 1.4.8
Release: alt1

Summary: An open-source remote desktop, and alternative to TeamViewer
License: AGPL-3.0
Group: Networking/Remote access
Url: https://rustdesk.com/
Vcs: https://github.com/rustdesk/rustdesk.git

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: hbb_common.tar
Source2: vendor.tar
Source3: vcpkg-env.tar
Source4: %name.sh
Source5: libsciter-install.sh
Patch: %name-%version-alt-no-cacao-deps.patch
Patch1: %name-%version-alt-vendoring-config.patch
Patch2: %name-%version-alt-cargolock-fix.patch
Patch3: %name-%version-alt-fix-main-page-ru.patch
Patch4: %name-%version-alt-change-ffmpeg-opts.patch
Patch5: %name-%version-alt-libsciter-path-fix.patch
Patch6: %name-%version-alt-disable-update-notify.patch
Patch7: %name-%version-alt-fix-build-with-gcc15.patch

BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: libXi-devel
BuildRequires: libXtst-devel
BuildRequires: clang-devel
BuildRequires: glib2-devel
BuildRequires: perl-IPC-Cmd
BuildRequires: perl-Time-Piece
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: libpulseaudio-devel
BuildRequires: xdotool-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libgtk+3-devel
BuildRequires: libdbus-devel
BuildRequires: libfuse3-devel
BuildRequires: libpam0-devel
BuildRequires: libssl-devel
BuildRequires: libalsa-devel
BuildRequires: libva-devel
BuildRequires: libvdpau-devel
BuildRequires: nv-codec-headers
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: vcpkg
BuildRequires: nasm
BuildRequires: yasm
BuildRequires: ninja-build
BuildRequires: patchelf
BuildRequires: zip
BuildRequires: git-core
BuildRequires: cargo-vendor-checksum
#for tray to work
Requires: libayatana-appindicator3-1

%description
Yet another remote desktop software, written in Rust. Works out of the box, no
configuration required. You have full control of your data, with no concerns
about security. You can use our rendezvous/relay server, set up your own, or
write your own rendezvous/relay server.

NOTE: To use this program, you need to get a third-party shared library -
libsciter-gtk.so.

%prep
%setup -a1 -a2
%autopatch -p1
#move hbb_common files to libs
mv -v hbb_common/* libs/hbb_common
#prepare vcpkg environment
tar -xvf %SOURCE3 -C $HOME/
#not use default parameters
rm -v vcpkg.json

%build
cargo-vendor-checksum --all --ignore-missing
#build static libs and headers via vcpkg
export VCPKG_ROOT=$HOME/vcpkg-env
export VCPKG_FORCE_SYSTEM_BINARIES=1
vcpkg install --no-downloads --overlay-ports=res/vcpkg libvpx libyuv opus aom ffmpeg
#build binary
python3 res/inline-sciter.py
cargo build %_smp_mflags --offline --release --bin %name --features inline,hwcodec,unix-file-copy-paste

%install
install -D %SOURCE4 %buildroot%_bindir/%name
install -D %SOURCE5 %buildroot%_bindir/libsciter-install
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
* Sun Jul 05 2026 Anton Kurachenko <srebrov@altlinux.org> 1.4.8-alt1
- New version 1.4.8.

* Sun May 10 2026 Anton Kurachenko <srebrov@altlinux.org> 1.4.6-alt1
- New version 1.4.6.

* Sun Apr 12 2026 Anton Kurachenko <srebrov@altlinux.org> 1.4.4-alt2
- Added yasm to BuildReq(Fix FTBFS).

* Wed Nov 19 2025 Anton Kurachenko <srebrov@altlinux.org> 1.4.4-alt1
- New version 1.4.4.

* Tue Sep 23 2025 Anton Kurachenko <srebrov@altlinux.org> 1.4.2-alt1
- New version 1.4.2.

* Mon Aug 18 2025 Anton Kurachenko <srebrov@altlinux.org> 1.4.1-alt1
- New version 1.4.1.

* Mon May 12 2025 Anton Kurachenko <srebrov@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Thu May 8 2025 Anton Kurachenko <srebrov@altlinux.org> 1.3.9-alt2
- Improved additional scripts and switched that to using pkexec for install/remove libsciter-gtk.so.
- Changed package description.

* Wed Apr 02 2025 Anton Kurachenko <srebrov@altlinux.org> 1.3.9-alt1
- New version 1.3.9.

* Sun Feb 23 2025 Anton Kurachenko <srebrov@altlinux.org> 1.3.8-alt1
- New version 1.3.8.
- Disabled notification of the availability updates.
- Enabled unix-file-copy-paste feature.

* Tue Feb 11 2025 Anton Kurachenko <srebrov@altlinux.org> 1.3.7-alt3
- Added info about the option to use epm play to install libsciter-gtk.

* Mon Jan 27 2025 Anton Kurachenko <srebrov@altlinux.org> 1.3.7-alt2
- Updated the vcpkg-env to ensure compatibility with vcpkg 2025.01.11(Fix FTBFS).

* Sat Jan 25 2025 Anton Kurachenko <srebrov@altlinux.org> 1.3.7-alt1
- New version 1.3.7.

* Fri Dec 27 2024 Anton Kurachenko <srebrov@altlinux.org> 1.3.6-alt1
- New version 1.3.6.

* Tue Dec 10 2024 Anton Kurachenko <srebrov@altlinux.org> 1.3.5-alt1
- Initial build for Sisyphus.
