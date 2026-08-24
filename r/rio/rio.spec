%global _unpackaged_files_terminate_build 1
%def_with check

Name: rio
Version: 0.5.25
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

%build
%rust_build -p rioterm
scdoc < extra/man/rio.1.scd > rio.1
scdoc < extra/man/rio.5.scd > rio.5
scdoc < extra/man/rio-bindings.5.scd > rio-bindings.5

%install
%rust_install
install -Dm0644 misc/rio.desktop \
    %buildroot%_desktopdir/com.rioterm.Rio.desktop
install -Dm0644 misc/com.rioterm.Rio.metainfo.xml \
    %buildroot%_datadir/metainfo/com.rioterm.Rio.metainfo.xml
install -Dm0644 misc/logo-2024.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/rio.svg
install -dm0755 %buildroot%_datadir/terminfo
tic -x -e xterm-rio,rio,rio-direct \
    -o %buildroot%_datadir/terminfo misc/rio.terminfo
install -Dm0644 rio.1 %buildroot%_man1dir/rio.1
install -Dm0644 rio.5 %buildroot%_man5dir/rio.5
install -Dm0644 rio-bindings.5 %buildroot%_man5dir/rio-bindings.5

%check
%rust_test -p rioterm

%files
%_bindir/%name
%_desktopdir/com.rioterm.Rio.desktop
%_datadir/metainfo/com.rioterm.Rio.metainfo.xml
%_iconsdir/hicolor/scalable/apps/rio.svg
%_datadir/terminfo/*/*
%_man1dir/rio.1*
%_man5dir/rio.5*
%_man5dir/rio-bindings.5*

%changelog
* Sun Aug 23 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.25-alt1
- Initial build for ALT.
