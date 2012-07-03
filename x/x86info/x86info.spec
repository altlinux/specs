Name: x86info
Version: 1.30
Release: alt1

Summary: Displays extended CPU information
License: GPLv2
Group: System/Kernel and hardware

URL: http://www.codemonkey.org.uk/projects/x86info
Source0: %url/x86info-%version.tgz

ExclusiveArch: %ix86 x86_64

# Automatically added by buildreq on Fri Apr 08 2011
BuildRequires: libpci-devel

%description
Unlike other `cpuinfo' tools which just parse /proc/cpuinfo, x86info probes the
CPU registers to find out a lot more information. It can discover the contents
of model-specific registers, discover CPU silicon revisions, and lots more.

%prep
%setup

%build
subst 's/-O./%optflags/' Makefile
%make_build x86info

%install
install -pDm755 x86info %buildroot%_bindir/x86info
install -pDm644 x86info.1 %buildroot%_man1dir/x86info.1

%files
%_bindir/*
%_man1dir/*

%changelog
* Sat Dec 10 2011 Victor Forsiuk <force@altlinux.org> 1.30-alt1
- 1.30

* Fri Apr 08 2011 Victor Forsiuk <force@altlinux.org> 1.29-alt1
- 1.29

* Tue Mar 15 2011 Victor Forsiuk <force@altlinux.org> 1.28-alt1
- 1.28

* Thu Sep 09 2010 Victor Forsiuk <force@altlinux.org> 1.27-alt1
- 1.27

* Sun Nov 15 2009 Victor Forsyuk <force@altlinux.org> 1.25-alt1
- 1.25

* Tue Jul 07 2009 Victor Forsyuk <force@altlinux.org> 1.24-alt1
- 1.24

* Tue Dec 18 2007 Victor Forsyuk <force@altlinux.org> 1.21-alt1
- 1.21

* Mon Apr 02 2007 Victor Forsyuk <force@altlinux.org> 1.20-alt2
- Add x86_64 to ExclusiveArch.

* Fri Oct 06 2006 Victor Forsyuk <force@altlinux.org> 1.20-alt1
- 1.20

* Fri Aug 11 2006 Victor Forsyuk <force@altlinux.ru> 1.18-alt1
- 1.18

* Tue Nov 15 2005 Victor Forsyuk <force@altlinux.ru> 1.17-alt1
- 1.17

* Wed Oct 19 2005 Victor Forsyuk <force@altlinux.ru> 1.16-alt1
- 1.16

* Thu Jul 14 2005 Victor Forsyuk <force@altlinux.ru> 1.13-alt1
- Initial build.
