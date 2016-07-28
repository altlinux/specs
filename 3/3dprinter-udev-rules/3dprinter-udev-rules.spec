Group: Engineering
Name:           3dprinter-udev-rules
Version:        0.1
Release:        alt1_2
Summary:        Rules for udev to give regular users access to operate 3D printers
License:        CC0
URL:            https://github.com/hroncok/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

# For the %%_udevrulesdir macro
BuildRequires: journalctl libsystemd-devel libudev-devel systemd systemd-analyze systemd-coredump systemd-networkd systemd-services systemd-utils

# For the directory
Requires: systemd udev

%global file_name 66-3dprinter.rules
Source44: import.info

%description
Normally, when you connect a RepRap like 3D printer to a Linux machine by an
USB cable, you need to be in dialout or similar group to be able to control
it via OctoPrint, Printrun, Cura or any other control software. Not any more.

Install this package to grant all users read and write access to
/dev/ttyUSB[0-9] and /dev/ttyACM[0-9].

Disclaimer: Such device might not be a 3D printer, it my be an Arduino, it
might be a modem and it might even be a blender. But normally you would
add your user to dialout and get access to all of those and more anyway.
So I guess be careful when some of the users should not get access to
your blenders.

%prep
%setup -q

%build
# nothing

%install
install -D -p -m 644 %{file_name} %{buildroot}%_udevrulesdir/%{file_name}

%files
%doc README.md
%doc LICENSE
%_udevrulesdir/%{file_name}

%changelog
* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_2
- converted for ALT Linux by srpmconvert tools

