%global _unpackaged_files_terminate_build 1
%def_with check

Name: cli-games
Version: 0.2.2
Release: alt1
Summary: A collection of terminal mini-games
License: MIT
Group: Games/Other
URL: https://github.com/furybee/cli-games
VCS: https://github.com/furybee/cli-games

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
A collection of polished terminal mini-games, in one binary.
35 games - Snake, Tetris, 2048, Minesweeper, Pong, Wordle, Chess, Sokoban,
Breakout, Solitaire and many more, all in your terminal, built on ratatui.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name

%changelog
* Sun Oct 04 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.2-alt1
- Initial build for ALT.
