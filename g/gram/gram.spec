Name: gram
Version: 3.0.1
Release: alt1

Summary: A high-performance, multiplayer code editor
License: GPL-3.0
Group: Editors
URL: https://gram.liten.app/
VCS: https://codeberg.org/GramEditor/gram

ExclusiveArch: aarch64 x86_64

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: gcc-c++ clang cmake
BuildRequires: rust-cargo cargo-about /proc
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)

%description
%summary

%prep
%setup -a1
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
%endif

%build
export OPENSSL_NO_VENDOR=1
export ALLOW_MISSING_LICENSES=1
sed -ri "/^CARGO_ABOUT_VERSION/ s,=.+\$,=\"$(rpmquery --qf %%{version} cargo-about)\"," \
	script/generate-licenses
./script/generate-licenses
cargo build --release --offline --package gram --package cli

%define _libexecdir /usr/libexec

%install
install -pm0755 -D target/release/gram %buildroot%_libexecdir/gram-editor
install -pm0755 -D target/release/cli %buildroot%_bindir/gram
install -pm0644 -D crates/gram/resources/app-icon.png \
    %buildroot%_iconsdir/hicolor/512x512/apps/gram.png
sed -e 's,$DO_STARTUP_NOTIFY,true,' -e 's,$APP_NAME,Gram,' \
    -e 's,$APP_CLI,gram,' -e 's,$APP_ICON,gram,' -e 's,$APP_ARGS,%%U,' \
    < crates/gram/resources/gram.desktop.in > gram.desktop
install -pm0644 -D gram.desktop %buildroot%_desktopdir/gram.desktop

%files
%doc README* LICENSE* docs
%_bindir/gram
%_libexecdir/gram-editor
%_desktopdir/gram.desktop
%_iconsdir/*/*/*/*.png

%changelog
* Mon Jul 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.1-alt1
- 3.0.1 released

* Wed Jun 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.0-alt1
- 2.2.0 released

* Mon May 25 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.2-alt1
- 2.1.2 released

* Fri May 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.1-alt1
- 2.1.1 released

* Tue May 19 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.0-alt1
- 2.1.0 released

* Tue May 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.0-alt1
- 2.0.0 released

* Wed Mar 25 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.0-alt1
- 1.2.0 released

* Mon Mar 23 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.0-alt1
- 1.1.0 released

* Wed Mar 04 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt2
- fixed dependency licenses generation

* Tue Mar 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt1
- 1.0.0 released
