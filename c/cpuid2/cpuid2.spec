Name: cpuid2
Version: 20120601
Release: alt1

Summary: dumps CPUID information about the CPU(s)
License: GPLv2+
Group: System/Kernel and hardware
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://www.etallen.com/cpuid.html
Source: http://www.etallen.com/cpuid/cpuid-%version.src.tar.gz

%description
cpuid dumps detailed information about the CPU(s) gathered from the CPUID
instruction, and also determines the exact model of CPU(s).

%prep
%setup -n cpuid-%version

%build
%make_build

%install
%make install BUILDROOT=%buildroot

%files
%_bindir/*
%_man1dir/*

%changelog

* Tue Jun 19 2012 Ilya Mashkin <oddity@altlinux.ru> 20120601-alt1
- new version

* Mon Apr 02 2012 Victor Forsiuk <force@altlinux.org> 20120225-alt1
- 20120225
- License is GPLv2+, not BSD.

* Sun Sep 26 2010 Ilya Mashkin <oddity@altlinux.ru> 20100902-alt1
- new version

* Mon Nov 13 2006 Lunar Child <luch@altlinux.ru> 20060917-alt1
- First build for ALT Linux Sisyphus
