Name: blackmagic
Version: 1.8.0
Release: alt1

Summary: In-application debugging tool for embedded microprocessors
License: GPLv3
Group: Development/Other
Url: https://github.com/blacksphere/blackmagic/wiki

Source0: %name-%version-%release.tar

BuildRequires: pkgconfig(hidapi-libusb) pkgconfig(libftdi1) pkgconfig(libusb-1.0)

%description
The Black Magic Probe is a modern, in-application debugging tool for embedded
microprocessors. It allows you see what is going on 'inside' an application
running on an embedded microprocessor while it executes. It is able to control
and examine the state of the target microprocessor using a JTAG or Serial Wire
Debugging (SWD) port and on-chip debug logic provided by the microprocessor.
The probe connects to a host computer using a standard USB interface. The user
is able to control exactly what happens using the GNU source level debugging
software, GDB.

%prep
%setup

%build
CFLAGS='%optflags' \
make PROBE_HOST=hosted
gcc %optflags -I/usr/include/libusb-1.0 scripts/swolisten.c -o swolisten -lusb-1.0
cp -pv src/platforms/hosted/Readme.md README.hosted.md

%install
install -pm0755 -D src/blackmagic %buildroot%_bindir/blackmagic
install -pm0755    swolisten %buildroot%_bindir/swolisten
install -pm0644 -D driver/99-blackmagic.rules %buildroot%_udevrulesdir/60-blackmagic.rules

%files
%doc COPYING README*.md UsingSWO
%_udevrulesdir/60-blackmagic.rules
%_bindir/blackmagic
%_bindir/swolisten

%changelog
* Thu Jun 02 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.0-alt1
- 1.8.0 released

* Mon Apr 05 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt2
- updated to git.a6a8606
- udev rule packaged

* Wed Feb 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt1
- initial
