Name: ly
Version: 0.6.0
Release: alt0.g2ca870c

Summary: TUI display manager
License: WTFPL
Group: Graphical desktop/Other

Url: https://github.com/fairyglade/ly
# Source-url: https://github.com/fairyglade/ly.git
Source: %name-%version.tar

%filter_from_requires /^\/etc\/xprofile/d

BuildRequires: gcc-c++
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(pam)

%description
Ly is a lightweight TUI (ncurses-like) display manager for Linux and BSD. 
Should work with any X desktop environment, and provides basic wayland support.

%prep
%setup
subst "s|/usr/lib/systemd/system|%_unitdir|" makefile

%build
%make_build

%install
%makeinstall_std
%make installsystemd DESTDIR=%buildroot

%files
%_bindir/%name
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/lang
%config(noreplace) %_sysconfdir/%name/config.ini
%_sysconfdir/%name/lang/*.ini
%_sysconfdir/%name/*setup.sh

%_sysconfdir/pam.d/%name
%_unitdir/%name.service

%changelog
* Mon Jun 26 2023 Roman Alifanov <ximper@altlinux.org> 0.6.0-alt0.g2ca870c
- Initial build for Sisyphus
