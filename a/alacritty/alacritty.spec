Name: alacritty
Version: 0.12.0
Release: alt1

Summary: A fast, cross-platform, OpenGL terminal emulator
License: Apache-2.0
Group: Terminals
Url: https://github.com/alacritty/alacritty

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-shape)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: pkgconfig(xkbcommon)

%description
Alacritty is a modern terminal emulator that comes with sensible defaults, but
allows for extensive configuration. By integrating with other applications,
rather than reimplementing their functionality, it manages to provide a flexible
set of features with high performance. The supported platforms currently consist
of BSD, Linux, macOS and Windows.

%prep
%setup
%ifdef bootstrap
cargo vendor crates
tar cf %SOURCE1 crates
%else
tar xf %SOURCE1
%endif

%build
export CARGO_HOME=${PWD}/cargo
cargo build --release

%install
install -pm0755 -D target/release/alacritty %buildroot%_bindir/alacritty
install -pm0644 -D extra/alacritty.man %buildroot%_man1dir/alacritty.1
install -pm0644 -D extra/linux/Alacritty.desktop %buildroot%_desktopdir/Alacritty.desktop
install -pm0644 -D extra/logo/alacritty-term.svg %buildroot%_iconsdir/hicolor/scalable/Alacritty.svg
install -pm0644 -D alacritty.yml %buildroot%_sysconfdir/alacritty/alacritty.yml

%files
%doc README* LICENSE* docs/*

%dir %_sysconfdir/alacritty
%config(noreplace) %_sysconfdir/alacritty/alacritty.yml

%_bindir/alacritty

%_desktopdir/Alacritty.desktop
%_iconsdir/hicolor/scalable/Alacritty.svg

%_man1dir/alacritty.1*

%changelog
* Mon Apr 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- 0.12.0 released

* Thu Oct 13 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt1
- 0.11.0 released

* Mon Feb 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt1
- 0.10.1 released

* Mon Jan 31 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt1
- 0.10.0 released

* Wed Aug 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt2
- lower required OpenGL version to 3.1

* Tue Aug 03 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt1
- initial
