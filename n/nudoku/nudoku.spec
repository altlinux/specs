%def_enable Werror

Name:     nudoku
Version:  0.2.5
Release:  alt1

Summary:  ncurses based sudoku game
License:  GPLv3
Group:    Games/Puzzles

Url:      https://github.com/jubalh/nudoku

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar
Patch0:   nudoku-0.2.5-use_libncursesw.patch

BuildRequires: libncursesw-devel

%description
%summary.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man6dir/*
%doc AUTHORS LICENSE README.md

%changelog
* Mon Oct 30 2017 Grigory Ustinov <grenka@altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus.
