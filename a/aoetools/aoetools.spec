Name: aoetools
Version: 37
Release: alt1

Summary: ATA over Ethernet Tools
License: GPLv2
Group: System/Kernel and hardware
Url: https://github.com/OpenAoE/aoetools

Source: %name-%version-%release.tar

%description
The aoetools are programs that assist in using ATA over Ethernet on
systems with version 2.6 Linux kernels.

%prep
%setup

%build
%make

%install
%makeinstall_std
install -pm0644 -D 60-aoe.rules %buildroot/lib/udev/rules.d/60-aoe.rules

%files
%doc COPYING HACKING NEWS README devnodes.txt
/lib/udev/rules.d/60-aoe.rules
%_sbindir/*
%_man8dir/*

%changelog
* Mon Sep 20 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 37-alt1
- 37 released

* Thu Jun 02 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 31-alt1
- 31 released

* Sat Oct 25 2008 Alexander Volkov <vaa@altlinux.org> 27-alt1
- New build for ALT, added udev rule (#17525)

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 23-1
- New upstream release

