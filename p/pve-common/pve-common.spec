Name: pve-common
Summary: Proxmox VE base library
Version: 4.0.74
Release: alt3
License: GPLv3
Group: Development/Perl
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(IO/Socket/IP.pm)
BuildRequires: perl(Filesys/Df.pm)
BuildRequires: perl(URI/Escape.pm)
BuildRequires: perl(Digest/SHA.pm)
BuildRequires: perl(String/ShellQuote.pm)
BuildRequires: perl(IO/AtomicFile.pm)
BuildRequires: perl(HTTP/Status.pm)
BuildRequires: perl(Devel/Cycle.pm)
BuildRequires: perl(Net/IP.pm)
BuildRequires: perl(Net/DBus.pm)
BuildRequires: perl(Pod/Parser.pm)
BuildRequires: perl(Clone.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(Linux/Inotify2.pm)
BuildRequires: perl(JSON.pm)

%description
This package contains the base library used by other Proxmox VE components.

%prep
%setup -q -n %name-%version

%install
cd src
%make DESTDIR=%buildroot install

%files
%perl_vendor_privlib/PVE

%changelog
* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt3
- OVS fixes for ovsbond

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt2
- OVS bugfixes

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.74-alt1
- 4.0-74

* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.73-alt1
- 4.0-73

* Mon Sep 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.72-alt2
- Network Device: replace rate limit MB/s to MBit/s

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.72-alt1
- 4.0-72

* Fri Jul 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.71-alt1
- 4.0-71

* Thu Jul 14 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.70-alt3
- OVS bugfixes

* Sat Jul 09 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.70-alt2
- OVS fixes

* Wed Jul 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.70-alt1
- 4.0-70

* Mon Jul 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.68-alt2
- OVS support

* Tue Jun 14 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.68-alt1
- 4.0-68

* Mon Jun 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.67-alt1
- 4.0-67

* Wed Jun 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.65-alt1
- 4.0-65

* Fri May 20 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.63-alt1
- 4.0-63

* Wed May 18 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.63-alt0.2.etcnet_reader_test2
- 2nd test release of etcnet_reader

* Sat May 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.59-alt0.2.etcnet_reader_test1
- 1st test release of etcnet_reader

* Sat May 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.59-alt0.1.etcnet_writer_test3
- stable release of etcnet_writer_test

* Wed May 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.59-alt0.1.etcnet_writer_test2
- 2nd test release of etcnet_writer_test

* Thu Apr 28 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.59-alt0.1.etcnet_writer_test1
- test release of etcnet_writer_test

* Mon Feb 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.46-alt1
- 4.0-46

* Mon Dec 14 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.41-alt1
- initial release

