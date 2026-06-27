%define git_commit_short 6a7d096
%define _unpackaged_files_terminate_build 1

Name: lact
Version: 0.9.1
Release: alt1

Summary: Linux GPU Control Application
License: MIT
Group: Monitoring

Url: https://github.com/ilya-zlobintsev/LACT
Vcs: https://github.com/ilya-zlobintsev/LACT
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64 ppc64le loongarch64

# Source-url: https://github.com/ilya-zlobintsev/LACT/archive/v%version/LACT-%version.tar.gz
Source0: LACT-%version.tar
# cargo vendor
Source1: crates.tar

Source2: config.toml

Patch1: lact-0.7.3-alt-loongarch-define.patch

BuildRequires(pre): clang-devel

BuildRequires: alt-os-release
BuildRequires: libadwaita-devel
BuildRequires: libdisplay-info-devel
BuildRequires: llvm-devel
BuildRequires: rust-cargo

%description
This application allows you to control your AMD, Nvidia or Intel GPU on a Linux system.

Current features:

   - Viewing information about the GPU
   - Power and thermals monitoring, power limit configuration
   - Fan curve control (AMD and Nvidia)
   - Overclocking (GPU/VRAM clockspeed and voltage)
   - Power states configuration (AMD only)

All of the functionality works regardless of the desktop session (there is no dependency on X11 extensions).

%prep
%setup -n LACT-%version
tar xf %SOURCE1
%__mkdir_p cargo
%__cp %SOURCE2 cargo

# allow patching vendored rust code
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
     ./vendor/libc/.cargo-checksum.json

%autopatch -p1

%build
export VERGEN_GIT_SHA=%git_commit_short
export CARGO_HOME=${PWD}/cargo
cargo build --release --offline

%install
DESTDIR=%buildroot PREFIX=%prefix make install

%post
%post_systemd %{name}d.service

%preun
%preun_systemd %{name}d.service

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/io.github.ilya_zlobintsev.LACT.desktop
%_iconsdir/hicolor/512x512/apps/io.github.ilya_zlobintsev.LACT.png
%_iconsdir/hicolor/scalable/apps/io.github.ilya_zlobintsev.LACT.svg
%_datadir/metainfo/io.github.ilya_zlobintsev.LACT.metainfo.xml
%_unitdir/%{name}d.service

%changelog
* Sat Jun 27 2026 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt1
- New version 0.9.1.

* Sun May 10 2026 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt1
- New version 0.9.0.

* Sun Jan 25 2026 Nazarov Denis <nenderus@altlinux.org> 0.8.4-alt1
- New version 0.8.4.

* Sat Nov 22 2025 Nazarov Denis <nenderus@altlinux.org> 0.8.3-alt1
- New version 0.8.3.

* Sat Oct 18 2025 Nazarov Denis <nenderus@altlinux.org> 0.8.2-alt1
- New version 0.8.2.

* Thu Aug 07 2025 Nazarov Denis <nenderus@altlinux.org> 0.8.1-alt1
- New version 0.8.1.

* Tue Jul 01 2025 Nazarov Denis <nenderus@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Mon May 12 2025 Nazarov Denis <nenderus@altlinux.org> 0.7.4-alt1
- New version 0.7.4.

* Tue Apr 29 2025 Andrew Guschin <guschin@altlinux.org> 0.7.3-alt2
- NMU: fix FTBFS on loongarch64

* Sun Apr 06 2025 Nazarov Denis <nenderus@altlinux.org> 0.7.3-alt1
- New version 0.7.3.

* Sun Mar 23 2025 Nazarov Denis <nenderus@altlinux.org> 0.7.2-alt1
- New version 0.7.2.

* Fri Feb 28 2025 Nazarov Denis <nenderus@altlinux.org> 0.7.1-alt1
- New version 0.7.1.

* Wed Jan 15 2025 Nazarov Denis <nenderus@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Sat Nov 16 2024 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt1
- New version 0.6.0.

* Wed Sep 25 2024 Nazarov Denis <nenderus@altlinux.org> 0.5.6-alt1
- New version 0.5.6.

* Sat Aug 03 2024 Nazarov Denis <nenderus@altlinux.org> 0.5.5-alt1
- New version 0.5.5.

* Sun Jun 23 2024 Nazarov Denis <nenderus@altlinux.org> 0.5.4-alt2
- Fix FTBFS

* Wed Apr 24 2024 Nazarov Denis <nenderus@altlinux.org> 0.5.4-alt1
- New version 0.5.4.

* Wed Mar 20 2024 Ivan A. Melnikov <iv@altlinux.org> 0.5.3-alt1.1
- NMU: fix FTBFS on loongarch64
  + backport upstream patch on vendored libc crate
    that adds more ioctl constants.

* Sat Mar 09 2024 Nazarov Denis <nenderus@altlinux.org> 0.5.3-alt1
- New version 0.5.3.

* Wed Feb 14 2024 Nazarov Denis <nenderus@altlinux.org> 0.5.2-alt1
- New version 0.5.2.

* Mon Nov 27 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.5.0-alt1.1
- NMU: build for LoongArch too

* Sat Nov 25 2023 Nazarov Denis <nenderus@altlinux.org> 0.5.0-alt1
- Initial build for ALT Linux

