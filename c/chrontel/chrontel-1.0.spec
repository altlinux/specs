Name:           chrontel
Version:        1.0
Release:        alt11203.1.4.3
Summary:        Control Tool for Chrontel CH7036 HDMI chip
License:        Public Domain

BuildRequires: libqt4-devel gcc-c++

Source:		chrontel-1.0.tar.bz2
Source1:	tiitoo-hdmi-daemon.init
Source2:	modprobe
Group: System/Configuration/Hardware
Requires: firmware-chrontel-7036

%description
Control Tool from Google Chromium Project for Chrontel CH7036 HDMI chip

%package -n firmware-chrontel-7036
BuildArch: noarch
Group: System/Kernel and hardware
Summary: Firmware for Chrontel CH7036 HDMI chip

%description -n firmware-chrontel-7036
Firmware for Chrontel CH7036 HDMI chip

%prep
%setup -q
%_libdir/qt4/bin/qmake tiitoo-hdmi-daemon.pro

%build
unset LD_AS_NEEDED
make %{?_smp_mflags}

%install

install -d -m 755 %buildroot/usr/sbin
install -d -m 755 %buildroot/lib/firmware/chrontel
install -m 755 tiitoo-hdmi-daemon %buildroot/usr/sbin
install -m 644 resources/fw7036.bin %buildroot/lib/firmware/chrontel
mkdir -p %buildroot/%_initdir
install -m 755 %SOURCE1 %buildroot/%_initdir/tiitoo-hdmi-daemon
mkdir -p %buildroot/etc/modprobe.d
install -m 644 %SOURCE2 %buildroot/etc/modprobe.d/tiitoo-hdmi-daemon.conf

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/sbin/tiitoo-hdmi-daemon
%_initdir/tiitoo-hdmi-daemon
/etc/modprobe.d/tiitoo-hdmi-daemon.conf

%files -n firmware-chrontel-7036
/lib/firmware/chrontel/fw7036.bin

%changelog
* Sun Mar 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt11203.1.4.3
- initscript fixed
- modprobe conf file installation fixed

* Tue Feb 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt11203.1.4.2
- first build based on weetab src.rpm


