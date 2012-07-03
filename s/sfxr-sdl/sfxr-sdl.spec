Name:		sfxr-sdl
Version:	1.1
Release:	alt1
Group:		Sound
Summary:	GUI-based sound effect generator
License:	MIT
Source:		%name-%version.tar.gz
Patch:		sfxr-sdl-1.1-asneeded.patch
URL:		http://drpetter.se/project_sfxr.html

BuildRequires:	desktop-file-utils

# Automatically added by buildreq on Thu May 12 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel pkg-config
BuildRequires: gcc-c++ libSDL-devel libgtk+2-devel

%description
Its original purpose was to provide a simple means of getting basic
sound effects into a game for those people who were working hard to get
their entries done within the 48 hours and didn't have time to spend
looking for suitable ways of doing this.
The idea was that they could just hit a few buttons in this application
and get some largely randomized effects that were custom in the sense
that the user could accept/reject each proposed sound.

%prep
%setup
%patch -p3

%build
%make

%install
%makeinstall DESTDIR=%buildroot

%files
%doc readme.txt ChangeLog
%_bindir/*
%_datadir/sfxr
%_desktopdir/*
%_liconsdir/*

%changelog
* Thu May 12 2011 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initial build from scratch

