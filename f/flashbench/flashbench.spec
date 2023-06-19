Name: flashbench
Version: 72
Release: alt2
Summary: Bench-marking and analysis utility for flash devices
License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/bradfa/flashbench.git
Source: %name-%version.tar

%description
Unfortunately flash manufacturers do not provide random speed, number of
open blocks and erase block size info, to help in deciding the optimum
partitioning strategy for a particular device.
Flashbench is a nice little command line application that can help in
finding this information for you, by checking the speeds achieved over
a range of settings. 
NOTE: This tool will cause loss of data on the device being tested and
should be used with caution. See:- /usr/share/doc/%{name}/README

%prep
%setup

%build
%make_build

%install
install -d -m 0755 %buildroot%_bindir
install -D -m 0755 erase %buildroot%_bindir
install -D -m 0755 %name %buildroot%_bindir

%files
%doc README
%_bindir/*

%changelog
* Mon Jun 19 2023 Anton Midyukov <antohami@altlinux.org> 72-alt2
- initial build
