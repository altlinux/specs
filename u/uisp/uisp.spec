Name:           uisp
Version:        20050207
Release:        alt1
Summary:        Universal In-System Programmer for Atmel AVR and 8051


Group:          System/Kernel and hardware
License:        GPL
URL:            http://www.nongnu.org/uisp
Source0:        http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz
Packager:       Evgeny Sinelnikov <sin@altlinux.ru>

# Automatically added by buildreq on Wed Mar 12 2008
BuildRequires: gcc-c++

%description
Uisp is utility for downloading/uploading programs to AVR devices. Can also be
used for some Atmel 8051 type devices. In addition, uisp can erase the device,
write lock bits, verify and set the active segment.

For use with the following hardware to program the devices:
  pavr      http://avr.jpk.co.nz/pavr/pavr.html
  stk500    Atmel STK500
  dapa      Direct AVR Parallel Access
  stk200    Parallel Starter Kit STK200, STK300
  abb       Altera ByteBlasterMV Parallel Port Download Cable
  avrisp    Atmel AVR ISP (?)
  bsd       http://www.bsdhome.com/avrprog/ (parallel)
  fbprg     http://ln.com.ua/~real/avreal/adapters.html (parallel)
  dt006     http://www.dontronics.com/dt006.html (parallel)
  dasa      serial (RESET=RTS SCK=DTR MOSI=TXD MISO=CTS)
  dasa2     serial (RESET=!TXD SCK=RTS MOSI=DTR MISO=CTS)


%prep
%setup -q

%build
%configure
make

%install
make install DESTDIR=%buildroot


%files
%doc AUTHORS CHANGES CHANGES.old COPYING ChangeLog* TODO
%_bindir/%name
%_man1dir/%name.1.gz


%changelog
* Wed Mar 12 2008 Evgeny Sinelnikov <sin@altlinux.ru> 20050207-alt1
- Initial ALT Linux release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20050207-2
- Autorebuild for GCC 4.3

* Mon Mar 12 2007 Trond Danielsen <trond.danielsen@fedoraproject.org> - 20050207-1
- Initial version.
- Summary and description taken from spec file included in uisp.
