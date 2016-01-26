
Name: rofi
Version: 0.15.7
Release: alt3
Summary: A window switcher, run dialog and dmenu replacement
License: MIT
Group: Graphical desktop/Other
Url: https://davedavenport.github.io/rofi/
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: https://github.com/DaveDavenport/%name/releases/download/%version/%name-%version.tar.gz
#It tries to use x-terminal-emulator which is only available on debian systems, I replace it with xdg-terminal.
Patch: 0001-Replace-x-terminal-emulator-with-xdg-terminal.patch

# Automatically added by buildreq on Mon Sep 21 2015
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libXft-devel libXrender-devel libfreetype-devel pkg-config python3-base xorg-kbproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: python3-module-zope ruby ruby-stdlibs
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXinerama-devel
BuildRequires: make
BuildRequires: libpango-devel
Requires: xdg-utils

%description
A popup window switcher roughly based on superswitcher, requiring only xlib and pango.
This version started off as a clone of simpleswitcher, the version from Sean Pringle.
All credit for this great tool should go to him. Rofi developed extra features,
like a run-dialog, ssh-launcher and can act as a drop-in dmenu replacement, making it a very versatile tool.

%prep
%setup
%patch0 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc Changelog README.md COPYING
%_bindir/rofi
%_man1dir/%name.*

%changelog
* Tue Jan 26 2016 Konstantin Artyushkin <akv@altlinux.org> 0.15.7-alt3
- replace man file extension

* Mon Sep 21 2015 Konstantin Artyushkin <akv@altlinux.org> 0.15.7-alt2
- initial build for ALT Linux Sisyphus

