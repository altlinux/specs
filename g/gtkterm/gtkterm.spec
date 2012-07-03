Name: gtkterm
Version: 0.99.5
Release: alt1.qa2

Summary: A simple GTK+ serial port terminal
Group: Terminals
License: %gpl2only
URL: http://www.jls-info.com/julien/linux

Packager: Andriy Stepanov <stanv@altlinux.ru>

Source: %name-%version.tar
Source1: %name.desktop

BuildRequires: rpm-build-licenses
BuildRequires: libvte-devel

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
%setup -q

%build
%add_optflags -I%_includedir/vte-0.0
%configure
%make_build

%install
%makeinstall

# Desktop file
install -d -pm 755 %buildroot%_desktopdir
install -D -pm 644 %{S:1} %buildroot%_desktopdir

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_man1dir/%name.*

%changelog
* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.99.5-alt1.qa2
- NMU: converted menu to desktop file

* Wed Dec 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.5-alt1.1
- Fixed build

* Mon Apr 19 2010 Andriy Stepanov <stanv@altlinux.ru> 0.99.5-alt1
- Package for ALT Linux

