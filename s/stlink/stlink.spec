Summary: STM32 microcontrolles programmer and debuger, using STLINKv1/v2
Name: stlink
Version: 2014.03.05
Release: alt2
License: Other
Group: Development/Other
URL: https://github.com/texane/stlink.git
Source0: %name.tar.bz2
Patch0: prem-fix.patch

# Automatically added by buildreq on Wed Mar 05 2014
# optimized out: at-spi2-atk fontconfig glib2-devel gnu-config libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libusb-compat libwayland-client libwayland-cursor libwayland-server pkg-config
BuildRequires: libgtk+3-devel libusb-compat-devel libusb-devel ruby ruby-stdlibs

%description
First, you have to know there are several boards supported by the software.
Those boards use a chip to translate from USB to JTAG commands. The chip is
called stlink and there are 2 versions:
. STLINKv1, present on STM32VL discovery kits,
. STLINKv2, present on STM32L discovery and later kits.

2 different transport layers are used:
. STLINKv1 uses SCSI passthru commands over USB,
. STLINKv2 uses raw USB commands.

%prep
%setup -q -n %name
%patch0 -p1

%build
./autogen.sh
%configure --with-gtk
%make_build

%install
%makeinstall

%files
%doc ACKNOWLEDGMENTS AUTHORS COPYING ChangeLog INSTALL LICENSE NEWS README TODO doc/tutorial/tutorial.pdf
%doc stlink_v1.modprobe.conf 49-stlinkv1.rules 49-stlinkv2-1.rules 49-stlinkv2.rules
%dir %_datadir/%name
%_bindir/*
%_datadir/%name/*

%changelog
* Wed Mar 05 2014 Grigory Milev <week@altlinux.ru> 2014.03.05-alt2
- Change 0700 -> 0644 for file saved from flash

* Wed Mar 05 2014 Grigory Milev <week@altlinux.ru> 2014.03.05-alt1
- Initial build.
