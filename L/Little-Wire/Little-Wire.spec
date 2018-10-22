Name: Little-Wire
Version: 1.3
Release: alt1
License: GNU GPL
Url: http://littlewire.github.io
Packager: Pavel Isopenko <pauli@altlinux.org>

Group: System/Kernel and hardware
Summary: Multi-featured USB controlled open source hardware tool
Summary(ru_RU.UTF-8): Многофункциональный USB контроллер с открытым исходным кодом
%description
Multi-featured USB controlled open source hardware tool packed in a minimal form factor designed by ihsan Kehribar http://kehribar.me
%description -l ru_RU.UTF-8
Многофункциональный USB-контроллер минимальных габаритов, разработанный ihsan Kehribar http://kehribar.me

%package examples
Group: System/Kernel and hardware
Summary: Little-Wire utility set
Summary(ru_RU.UTF-8): Набор утилит Little-Wire
Source: %name-%version.tar
Requires: libusb libusb-compat udev-micronucleus
BuildRequires: libusb-devel libusb-compat-devel
%description examples
Little-Wire utility set
%description -l ru_RU.UTF-8 examples
Набор утилит, демонстрирующих возможности применения USB-контроллера Little-Wire

%prep
%setup

%build
%make

%install
install -d -m0755 %buildroot%_bindir
install -m0755 adc %buildroot%_bindir
install -m0755 blink %buildroot%_bindir
install -m0755 blink_ws2812 %buildroot%_bindir
install -m0755 button %buildroot%_bindir
install -m0755 debugConsole %buildroot%_bindir
install -m0755 fade_ws2812 %buildroot%_bindir
install -m0755 hardwarePWM %buildroot%_bindir
install -m0755 i2c_blinkM %buildroot%_bindir
install -m0755 i2c_nunchuck %buildroot%_bindir
install -m0755 lwbuttond %buildroot%_bindir
install -m0755 onewire %buildroot%_bindir
install -m0755 rgb_cycle_ws2812 %buildroot%_bindir
install -m0755 servo %buildroot%_bindir
install -m0755 softPWM %buildroot%_bindir
install -m0755 spi_LTC1448 %buildroot%_bindir

%files examples
%attr(4711, root, root) %_bindir/*

%changelog
* Sun Oct 21 2018 Pavel isopenko <pauli@altlinux.org> 1.3-alt1
- initial build for Sisyphus



