%define _unpackaged_files_terminate_build 1

Name:     pacman4console
Version:  1.0.0
Release:  alt1

Summary:  Console based PacMan Game
License:  GPL-2.0-or-later
Group:    Games/Arcade

URL: https://github.com/YoctoForBeaglebone/pacman4console
VCS: https://github.com/YoctoForBeaglebone/pacman4console.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libncurses-devel

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%make_build prefix=%_prefix

%install
%makeinstall_std prefix=%_prefix

%files
%attr(0755,root,root) %_bindir/pacman
%attr(0755,root,root) %_bindir/pacmanedit
%_datadir/pacman/

%changelog
* Thu Jul 30 2026 Anton Osipov <radiolamp@altlinux.org> 1.0.0-alt1
- Initial build.
