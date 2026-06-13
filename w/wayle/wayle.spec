%global _unpackaged_files_terminate_build 1
%global desktop_file com.wayle.settings.desktop
%def_with check

Name: wayle
Version: 0.6.0
Release: alt1
Summary: A compositor agnostic shell with extensive customization
License: MIT
Group: Graphical desktop/Other
URL: https://wayle.app
VCS: https://github.com/wayle-rs/wayle

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: clang-devel
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: libgtksourceview5-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(graphene-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(xkbcommon)

%if_with check
BuildRequires: desktop-file-utils
%endif

%description
A Wayland desktop shell with the bar, notifications, OSD, wallpaper,
and device controls built in. Written in Rust with GTK4 and Relm4.

%prep
%setup -a 1
%rust_prep

%build
%rust_build
target/release/wayle completions bash > wayle.bash
target/release/wayle completions zsh > wayle.zsh
target/release/wayle completions fish > wayle.fish

%install
%rust_install wayle wayle-settings
install -Dm 0644 wayle.bash %buildroot%_datadir/bash-completion/completions/wayle
install -Dm 0644 wayle.zsh %buildroot%_datadir/zsh/site-functions/_wayle
install -Dm 0644 wayle.fish %buildroot%_datadir/fish/vendor_completions.d/wayle.fish
install -Dm 0644 resources/%desktop_file %buildroot%_desktopdir/%desktop_file
install -Dm 0644 resources/wayle.service %buildroot%_userunitdir/wayle.service
install -Dm 0644 resources/wayle-settings.svg \
                %buildroot%_iconsdir/hicolor/scalable/apps/wayle-settings.svg
cp -r resources/icons/hicolor/scalable/actions %buildroot%_iconsdir/hicolor/scalable/

%check
%rust_test
desktop-file-validate %buildroot%_desktopdir/%desktop_file

%files
%_bindir/wayle
%_bindir/wayle-settings
%_userunitdir/wayle.service
%_datadir/applications/%desktop_file
%_iconsdir/hicolor/scalable/apps/wayle-settings.svg
%_iconsdir/hicolor/scalable/actions/*.svg
%_datadir/bash-completion/completions/wayle
%_datadir/zsh/site-functions/_wayle
%_datadir/fish/vendor_completions.d/wayle.fish

%changelog
* Sat Jun 13 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.0-alt1
- Updated to version 0.6.0.

* Sat May 30 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.0-alt1
- Initial build for ALT.
