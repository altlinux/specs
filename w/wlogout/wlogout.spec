Name: wlogout
Version: 1.1.1
Release: alt1

Summary: A logout menu for wayland environments
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/ArtsyMacaw/wlogout

Source: %name-%version.tar

BuildRequires(pre):  rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gtk+-wayland-3.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: scdoc

%description
%summary

%prep
%setup
subst "s|/fish/completions|/fish/vendor_completions.d|" meson.build

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/layout
%config(noreplace) %_sysconfdir/%name/style.css
%_datadir/%name/
%_man1dir/%name.1.*
%_man5dir/%name.5.*

%_datadir/bash-completion/completions/wlogout*
%_datadir/fish/vendor_completions.d/wlogout*.fish
%_datadir/zsh/site-functions/_wlogout*

%changelog
* Sun Jun 04 2023 Roman Alifanov <ximper@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

