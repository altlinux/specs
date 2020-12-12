Name: cm6206ctl
Version: 0
Release: alt1

Summary: Control your CM6206 based USB sound card
License: GPLv2+
Group: System/Configuration/Hardware

URL: git://github.com/vestom/cm6206ctl.git
Vcs: git://github.com/vestom/cm6206ctl.git
Source0: %name-%version.tar

BuildRequires: libhidapi-devel

%description
Command line utility to control a CM6206 based USB sound card. Enables readout of all registers and enables control of special settings (e.g. internal mixer settings, SPDIF parameters etc.).


%prep
%setup

%build
gcc cm6206ctl.c -lhidapi-libusb -o cm6206ctl

%install
install -m 755 -D %name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Sat Dec 12 2020 Igor Vlasenko <viy@altlinux.ru> 0-alt1
- Sisyphus build

