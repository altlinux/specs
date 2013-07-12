Name:           curseofwar
Version:        1.1.0
Release:        alt1
Summary:        A Real Time Strategy game for Linux

Group:          Games/Strategy
License:        GPLv3+
URL:            https://github.com/a-nikolaev/curseofwar/
Source:         %name-master.zip

BuildRequires: libncurses-devel unzip

%description
Curse of War is a fast-paced action strategy game for Linux
implemented using C and ncurses.
Unlike most RTS, you are not controlling units, but focus on
high-level strategic planning: Building infrastructure, securing
resources, and moving your armies. The core game mechanics turns
out to be quite close to WWI-WWII type of warfare, however, there
is no explicit reference to any historical period.
Multiplayer mode is now available!

%prep
%setup -n %name-master

%build
%make_build

%install
%makeinstall_std

%files
%doc README VERSION
%_bindir/*

%changelog
* Fri Jul 12 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.1.0-alt1
- initial build
