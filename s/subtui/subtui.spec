%global _unpackaged_files_terminate_build 1
%global commit_hash e5702ad

Name: subtui
Version: 2.14.3
Release: alt1
Summary: A lightweight Subsonic TUI music player
License: MIT
Group: Sound
Url: https://github.com/MattiaPun/SubTUI
VCS: https://github.com/MattiaPun/SubTUI

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
Requires: mpv

%description
SubTUI is your next favorite lightweight, terminal-based music player
for Subsonic-compatible servers like Navidrome, Gonic, and Airsonic.
Built with Go and the Bubble Tea framework, it provides a clean terminal
interface to listen to your favorite high-quality audio.

%prep
%setup -a 1

%build
go build -ldflags "\
         -X main.version=%version \
         -X main.commit=%commit_hash" \
         -o %name

%install
install -Dm 0755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Sat May 23 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.14.3-alt1
- Updated to version 2.14.3.

* Thu May 14 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.14.2-alt1
- Updated to version 2.14.2.

* Sat May 02 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.14.1-alt1
- Initial build for ALT.
