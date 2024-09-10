Name:     nudoku
Version:  5.0.0
Release:  alt1

Summary:  ncurses based sudoku game

License:  GPLv3
Group:    Games/Puzzles
URL:      http://jubalh.github.io/nudoku
VCS:      https://github.com/jubalh/nudoku

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires: libncursesw-devel
BuildRequires: libcairo-devel

%description
Can't code? Can't hack? Can't do anything cool on the command line? This game
will give you an excuse to spend some time in the terminal nevertheless.

Be a cool kid, be in the terminal. Play nudoku!

As a bonus you will even learn the basic vi movement commands.

nudoku can also generate PDF files, containing sudokus.

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
%doc AUTHORS LICENSE README.md
%_bindir/%name
%_man6dir/%name.6.*

%changelog
* Tue Sep 10 2024 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Fri May 10 2024 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Automatically updated to 4.0.1.

* Tue Apr 30 2024 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.

* Mon Dec 25 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

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
