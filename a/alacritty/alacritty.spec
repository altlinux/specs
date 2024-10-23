Name: alacritty
Version: 0.14.0
Release: alt1

Summary: A fast, cross-platform, OpenGL terminal emulator
License: Apache-2.0
Group: Terminals
Url: https://github.com/alacritty/alacritty

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: scdoc
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
mkdir -p %buildroot%_man1dir %buildroot%_man5dir
scdoc < extra/man/alacritty.1.scd > %buildroot%_man1dir/alacritty.1
scdoc < extra/man/alacritty-msg.1.scd > %buildroot%_man1dir/alacritty-msg.1
scdoc < extra/man/alacritty.5.scd > %buildroot%_man5dir/alacritty.5
scdoc < extra/man/alacritty-bindings.5.scd > %buildroot%_man5dir/alacritty-bindings.5
install -pm0755 -D target/release/alacritty %buildroot%_bindir/alacritty
install -pm0644 -D extra/linux/Alacritty.desktop %buildroot%_desktopdir/Alacritty.desktop
install -pm0644 -D extra/logo/alacritty-term.svg %buildroot%_iconsdir/hicolor/scalable/apps/Alacritty.svg
install -pm0644 -D extra/completions/_alacritty %buildroot%_datadir/zsh/site-functions/_alacritty
install -pm0644 -D extra/completions/alacritty.bash %buildroot%_datadir/bash-completion/completions/alacritty
install -pm0644 -D /dev/null %buildroot%_sysconfdir/alacritty/alacritty.toml

%files
%doc README* LICENSE* docs/*

%dir %_sysconfdir/alacritty
%ghost %config(noreplace) %_sysconfdir/alacritty/alacritty.toml

%_bindir/alacritty

%_datadir/zsh/site-functions/_alacritty
%_datadir/bash-completion/completions/alacritty

%_desktopdir/Alacritty.desktop
%_iconsdir/hicolor/scalable/apps/Alacritty.svg

%_man1dir/alacritty*.1*
%_man5dir/alacritty*.5*

%changelog
* Wed Oct 23 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.14.0-alt1
- 0.14.0 released

* Mon Mar 25 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.13.2-alt1
- 0.13.2 released

* Mon Jan 22 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.1-alt2
- placed properly app icon (closes: 49143)

* Tue Jan 09 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.1-alt1
- 0.13.1 released

* Thu Dec 28 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.0-alt1
- 0.13.0 released

* Tue Oct  3 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.3-alt1
- 0.12.3 released

* Tue Jul 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.2-alt1
- 0.12.2 released

* Tue May 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.1-alt1
- 0.12.1 released

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
