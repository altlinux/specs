%define _unpackaged_files_terminate_build 1

Name: command-not-found
Version: 0.3
Release: alt1

Summary: Console assistant for ALT Linux
License: GPL-3.0-or-later
Group: Terminals

URL: https://altlinux.space/alt-gnome/command-not-found.git
VCS: https://altlinux.space/alt-gnome/command-not-found.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_sysconfdir/bashrc.d/%name.sh
%_sysconfdir/fish/conf.d/%name.fish
%_sysconfdir/zshrc.d/%name.zsh
%config(noreplace) %_sysconfdir/command-not-found/config

%changelog
* Thu Nov 20 2025 Anton Osipov <radiolamp@altlinux.org> 0.3-alt1
- New version: 0.3.

* Tue Oct 21 2025 Anton Osipov <radiolamp@altlinux.org> 0.2-alt1
- Initial build.
