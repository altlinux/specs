Name:    sixpair
Version: 1.8
Release: alt2

Summary: Associate PS3 Sixaxis controller to system bluetoothd via USB
License: GPL-2.0
Group:   Other
URL:     http://www.pabr.org/sixlinux/

# Source-url: https://www.pabr.org/sixlinux/sixpair.c
Source: sixpair.c
# Source1-url: https://www.pabr.org/sixlinux/sixhidtest.c
Source1: sixhidtest.c
# Source2-url: https://www.pabr.org/sixlinux/xsixhidtest.c
Source2: xsixhidtest.c

BuildRequires: libusb-compat-devel libX11-devel

ExclusiveArch: x86_64 i586

%description
With this tool you can pair a PS3 Controller with a bluetooth Host.
sixpair can change the MAC address of the Controller via USB to the new
destination MAC.

%prep

%build
gcc %optflags -o sixpair %SOURCE0 -lusb
gcc %optflags -o sixhidtest %SOURCE1
gcc %optflags -o xsixhidtest %SOURCE2 -lX11 -lm

%install
install -Dm755 sixpair %buildroot%_bindir/sixpair
install -m755 sixhidtest %buildroot%_bindir/sixhidtest
install -m755 xsixhidtest %buildroot%_bindir/xsixhidtest

%files
%_bindir/sixhidtest
%_bindir/sixpair
%_bindir/xsixhidtest

%changelog
* Mon May 18 2026 Sergey Palcheh <minergenon@altlinux.org> 1.8-alt2
- add %optflags

* Tue Mar 04 2025 Sergey Palcheh <minergenon@altlinux.org> 1.8-alt1
- Initial build for Sisyphus

