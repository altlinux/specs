%define _unpackaged_files_terminate_build 1

Name: chess-tui
Version: 2.9.0
Release: alt1

Summary: A rusty chess game in your terminal
License: MIT
Group: Games/Boards
URL: https://github.com/thomas-mauran/chess-tui
VCS: https://github.com/thomas-mauran/chess-tui.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(alsa)

%description
Chess-tui is a simple chess game you can play from your terminal. It supports
local 2 players mode, online multiplayer and playing against any UCI compatible
chess engine.

Features:
- Local 2 player mode
- Online multiplayer
- Play against any UCI compatible chess engine as black or white
- Helper menu
- Draws (stalemate, 50 moves rule, 3 time repetition)
- Piece promotion

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc README.md
%_bindir/%name

%changelog
* Mon Nov 23 2026 Aleksandr A. Voyt <sobue@altlinux.org> 2.9.0-alt1
- 2.8.1 -> 2.9.0

* Thu Nov 19 2026 Aleksandr A. Voyt <sobue@altlinux.org> 2.8.1-alt1
- 2.7.1 -> 2.8.1

* Wed Jul 29 2026 Aleksandr A. Voyt <sobue@altlinux.org> 2.7.1-alt1
- Initial build.
