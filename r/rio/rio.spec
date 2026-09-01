%global _unpackaged_files_terminate_build 1
%global bin_name rioterm
%def_with check

Name: rio
Version: 0.5.27
Release: alt1
Summary: A hardware-accelerated GPU terminal emulator
License: MIT
Group: Terminals
URL: https://rioterm.com
VCS: https://github.com/raphamorim/rio

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: gcc-c++
BuildRequires: glslc
BuildRequires: scdoc
BuildRequires: termutils-devel
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)

Provides: xvt
Provides: x-terminal-emulator

%description
Rio is a modern, hardware-accelerated GPU terminal emulator written in Rust.
It supports tabs and split panes, configurable themes, images in the terminal,
and both the Wayland and X11 display protocols.

%prep
%setup -a1
# Upstream config has no trailing newline, while %%rust_prep appends to it.
sed -i -e '$a\' .cargo/config.toml
%rust_prep

# ALT already ships /usr/bin/rio with Rasterio. Keep the application and
# its manual pages available under the unambiguous rioterm name.
sed -i \
    -e '1s/^RIO(1)$/RIOTERM(1)/' \
    -e 's/\*rio\*(5)/\*rioterm\*(5)/g' \
    extra/man/rio.1.scd
sed -i \
    -e '1s/^RIO(5)$/RIOTERM(5)/' \
    -e 's/\*rio\*(1)/\*rioterm\*(1)/g' \
    extra/man/rio.5.scd
sed -i \
    -e '1s/^RIO-BINDINGS(5)$/RIOTERM-BINDINGS(5)/' \
    -e 's/\*rio\*(1)/\*rioterm\*(1)/g' \
    -e 's/\*rio\*(5)/\*rioterm\*(5)/g' \
    extra/man/rio-bindings.5.scd

%build
%rust_build -p %bin_name
scdoc < extra/man/rio.1.scd > %bin_name.1
scdoc < extra/man/rio.5.scd > %bin_name.5
scdoc < extra/man/rio-bindings.5.scd > %bin_name-bindings.5

%install
install -Dm0755 target/release/rio %buildroot%_bindir/%bin_name
install -Dm0644 misc/rio.desktop \
    %buildroot%_desktopdir/com.rioterm.Rio.desktop
sed -i \
    -e 's/^TryExec=rio$/TryExec=%bin_name/' \
    -e 's/^Exec=rio$/Exec=%bin_name/' \
    %buildroot%_desktopdir/com.rioterm.Rio.desktop
install -Dm0644 misc/com.rioterm.Rio.metainfo.xml \
    %buildroot%_datadir/metainfo/com.rioterm.Rio.metainfo.xml
install -Dm0644 misc/logo-2024.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/rio.svg
install -dm0755 %buildroot%_datadir/terminfo
tic -x -e xterm-rio,rio-direct \
    -o %buildroot%_datadir/terminfo misc/rio.terminfo
install -Dm0644 %bin_name.1 %buildroot%_man1dir/%bin_name.1
install -Dm0644 %bin_name.5 %buildroot%_man5dir/%bin_name.5
install -Dm0644 %bin_name-bindings.5 %buildroot%_man5dir/%bin_name-bindings.5

%check
%rust_test -p %bin_name

%files
%_bindir/%bin_name
%_desktopdir/com.rioterm.Rio.desktop
%_datadir/metainfo/com.rioterm.Rio.metainfo.xml
%_iconsdir/hicolor/scalable/apps/rio.svg
%_datadir/terminfo/*/*
%_man1dir/%bin_name.1*
%_man5dir/%bin_name.5*
%_man5dir/%bin_name-bindings.5*

%changelog
* Tue Sep 01 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.27-alt1
- Updated to version 0.5.27.

* Wed Aug 26 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.26-alt2
- Renamed the executable to rioterm to avoid a conflict with Rasterio.
- Dropped the rio terminfo entry already provided by terminfo-extra.

* Tue Aug 25 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.26-alt1
- Updated to version 0.5.26.

* Sun Aug 23 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.25-alt1
- Initial build for ALT.
