%define _unpackaged_files_terminate_build 1

Name: command-not-found
Version: 0.7
Release: alt1

Summary: Console assistant for ALT Linux
License: GPL-3.0-or-later
Group: Terminals

URL: https://altlinux.space/alt-gnome/command-not-found.git
VCS: https://altlinux.space/alt-gnome/command-not-found.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: apt-repo-tools

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

%post
echo "Please exit from all shells and restart them."

%postun
echo "After package removal, it is recommended to exit from all shells and restart them."

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_sysconfdir/bashrc.d/%name.sh
%_sysconfdir/fish/conf.d/%name.fish
%_sysconfdir/zshrc.d/%name.zsh
%config(noreplace) %_sysconfdir/command-not-found/config
%dir %_datadir/%name
%dir %_datadir/%name/modules
%_datadir/%name/modules/00-example

%changelog
* Mon May 16 2026 Anton Osipov <radiolamp@altlinux.org> 0.7-alt1
- Added tests, improved functionality, refactored code.

* Mon Mar 16 2026 Anton Osipov <radiolamp@altlinux.org> 0.6-alt1
- Improved package sorting (Closes: 58094).
- Added post and postun recommendation to restart $SHELL (Closes: 57241).
- Added warning that command not found if program is disabled (Closes: 57241).
- Complete removal of apt-cache.

* Tue Dec 16 2025 Anton Osipov <radiolamp@altlinux.org> 0.5-alt2
- Add runtime dependency on apt-repo-tools (Closes: 57242).

* Mon Dec 08 2025 Anton Osipov <radiolamp@altlinux.org> 0.5-alt1
- New version: 0.5.

* Thu Nov 27 2025 Anton Osipov <radiolamp@altlinux.org> 0.4-alt1
- Initial build.
