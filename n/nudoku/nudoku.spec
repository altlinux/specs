Name:     nudoku
Version:  2.1.0
Release:  alt1

Summary:  ncurses based sudoku game
License:  GPLv3
Group:    Games/Puzzles

Url:      https://github.com/jubalh/nudoku

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires: libncursesw-devel
BuildRequires: libcairo-devel

%description
%summary.

%prep
%setup

%build
%autoreconf
%configure --enable-cairo
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/*
%_man6dir/*
%doc AUTHORS LICENSE README.md

%changelog
* Tue Dec 01 2020 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.

* Fri May 08 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt3
- Build with cairo support (Closes: #38456).

* Mon Jan 13 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- Fixed FTBFS.

* Tue Jul 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Build new version.

* Tue May 15 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Build new version.

* Mon Oct 30 2017 Grigory Ustinov <grenka@altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus.
