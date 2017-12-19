Name:     curseofwar
Version:  1.2.0.0.11.git47f7989
Release:  alt1

Summary:  A Real Time Strategy game for Linux
License:  GPLv3
Group:    Games/Strategy
Url:      https://github.com/a-nikolaev/curseofwar

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar
Patch0:   %name-1.2.0.0.11.git47f7989-use_libncursesw.patch
Patch1:   %name-1.2.0.0.11.git47f7989-fix_SDL_path.patch

BuildRequires: libncursesw-devel libSDL-devel
Requires: %name-ncurses %name-SDL

%define common_description \
This is a fast-paced action strategy game for Linux implemented using ncurses\
user interface.\
Unlike most RTS, you are not controlling units, but focus on high-level\
strategic planning: Building infrastructure, securing resources,\
and moving your armies.\
The core game mechanics turns out to be quite close to WWI-WWII type of\
warfare, however, there is no explicit reference to any historical period.

%description
%common_description

%package common
Summary:   Common files of %name
Group:     Games/Strategy
BuildArch: noarch

%description common
%common_description

%summary.

%package ncurses
Summary:  Ncurses version of %name
Group:    Games/Strategy
Requires: %name-common

%description ncurses
%common_description

%summary.

%package SDL
Summary:  SDL version of %name
Group:    Games/Strategy
Requires: %name-common

%description SDL
%common_description

%summary.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%make_build CFLAGS="$CFLAGS -Werror"
%make_build SDL=yes CFLAGS="$CFLAGS -Werror"

%install
%makeinstall_std
%makeinstall_std SDL=yes

%files common
%exclude %_defaultdocdir/%name/changelog.gz
%_man6dir/*
%_datadir/%name
%doc CHANGELOG LICENSE README

%files ncurses
%_bindir/%name

%files SDL
%_bindir/%name-sdl

%files

%changelog
* Tue Dec 19 2017 Grigory Ustinov <grenka@altlinux.org> 1.2.0.0.11.git47f7989-alt1
- Build new version.
- Fix SDL path.
- Change ncurses to ncursesw.
- Add Werror flag.
- Significant change of spec.

* Fri Jul 12 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.1.0-alt1
- initial build
