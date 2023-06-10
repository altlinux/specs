Name: evtest
Version: 1.35
Release: alt1

Summary: Input device event monitor and query tool
License: GPLv2+
Group: Other

Url: http://cgit.freedesktop.org/%name/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: https://gitlab.freedesktop.org/libevdev/%name/-/archive/%name-%version/%name-%name-%version.tar

BuildRequires: asciidoc
BuildRequires: time
BuildRequires: xmlto

%description
The first invocation type displayed above ("capture mode") causes evtest to
display information about the specified input device, including all the events
supported by the device. It then monitors the device and displays all the
events layer events generated.

In the second invocation type ("query mode"), evtest performs a one-shot query
of the state of a specific key *value* of an event *type*.

*type* is one of: *EV_KEY*, *EV_SW*, *EV_SND*, *EV_LED* (or the numerical value)

*value* can be either a decimal representation (e.g. 44), hex
(e.g. 0x2c), or the constant name (e.g. KEY_Z) of the key/switch/sound/LED
being queried.

If the state bit is set (key pressed, switch on, ...), evtest exits with
code 10. If the state bit is unset (key depressed, switch off, ...), evtest
exits with code 0. No other output is generated.

evtest needs to be able to read from the device; in most cases this means it
must be run as root.

evtest is commonly used to debug issues with input devices in X.Org. The
output of evtest shows the information presented by the kernel; based on
this information it can be determined whether a bug may be a kernel or an
X.Org issue.

%prep
%setup -n %name-%name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc COPYING INSTALL README.md
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sat Jun 10 2023 Nazarov Denis <nenderus@altlinux.org> 1.35-alt1
- New version 1.35.

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.34-alt2
- Requires fixed.

* Sat Nov 09 2019 Nazarov Denis <nenderus@altlinux.org> 1.34-alt1
- Version 1.34

* Mon Nov 09 2015 Nazarov Denis <nenderus@altlinux.org> 1.33-alt0.M70P.1
- Build for branch p7

* Sun Nov 08 2015 Nazarov Denis <nenderus@altlinux.org> 1.33-alt0.M70T.1
- Build for branch t7

* Sat Nov 07 2015 Nazarov Denis <nenderus@altlinux.org> 1.33-alt1
- Version 1.33

* Thu Sep 18 2014 Nazarov Denis <nenderus@altlinux.org> 1.32-alt1
- Version 1.32

* Sun May 25 2014 Nazarov Denis <nenderus@altlinux.org> 1.31-alt1.M70P.1
- Build for branch p7

* Sat May 24 2014 Nazarov Denis <nenderus@altlinux.org> 1.31-alt1.M70T.1
- Build for branch t7

* Thu May 22 2014 Nazarov Denis <nenderus@altlinux.org> 1.31-alt2
- Fix release for safe upgrade from autoimports repository

* Wed May 21 2014 Nazarov Denis <nenderus@altlinux.org> 1.31-alt1
- Initial build for ALT Linux
