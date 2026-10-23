%define _unpackaged_files_terminate_build 1

Name: gtkterm
Version: 1.4
Release: alt1

Summary: A simple GTK+ serial port terminal
Group: Terminals
License: GPL-3.0-or-later
URL: https://github.com/wvdakker/gtkterm

Source: %name-%version.tar

Patch0: gtkterm-1.4-alt-glibc-termios.patch

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gettext-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(vte-2.91)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libpcre2-8)

%description
It is a "clone" of the famous Hyperterminal. But it is much more simple,
that is to say, that it can only communicate with a serial link and that
it does not support all the modem protocols. 

Features :

  * Serial port terminal window
  * Serial port setup (speed, parity, bits, stopbits, flow control)
  * Using the termios API
  * Possible to send a file (only RAW data, no protocol)
  * Possible to save data (RAW also)
  * End of line delay while sending a file
  * Special character wait before next line while sending a file
  * Possible to toggle control lines manually (DTR, CTS) and send breaks
  * Also reads the state of control lines (RTS, CD, DSR, RI)
  * Hexadecimal view
  * Possible to send raw hexadecimal chars
  * Possible to define macros (keyboard shortcuts)

%prep
%setup 
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/%name.1*

%changelog
* Fri Oct 23 2026 Dina Tagantseva <dinchik@altlinux.org> 1.4-alt1
- New version.

* Thu Sep 27 2012 Andriy Stepanov <stanv@altlinux.ru> 0.99.7-alt0.1
- Update to new version. git commit 20c313b1

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.99.5-alt1.qa2
- NMU: converted menu to desktop file

* Wed Dec 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.5-alt1.1
- Fixed build

* Mon Apr 19 2010 Andriy Stepanov <stanv@altlinux.ru> 0.99.5-alt1
- Package for ALT Linux
