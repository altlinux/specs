Name: bandwidth
Version: 0.26c
Release: alt1

Summary: Artificial benchmark for measuring memory bandwidth
License: GPL
Group: System/Kernel and hardware

Url: http://home.comcast.net/~fbui/bandwidth.html
Packager: Michael Shigorin <mike@altlinux.org>
Source: http://home.comcast.net/~fbui/%name-%version.tar.bz2

BuildRequires: nasm

ExclusiveArch: %ix86 x86_64 arm

%ifarch %ix86
Provides: bandwidth32 = %version
Obsoletes: bandwidth32 <= 0.15
%define namearch %{name}32
%endif
%ifarch x86_64
%define namearch %{name}64
%endif
%ifarch arm
%define namearch %{name}-arm
%endif

%description
bandwidth is a benchmark to estimate the memory bandwidth of
a system, including main memory, L2 cache, framebuffer memory,
and string library performance.

%prep
%setup

%build
%make_build %namearch

%install
# ...so that %_bindir/%name is real file in both packages
install -pDm755 %namearch %buildroot%_bindir/%namearch
ln -s %namearch %buildroot%_bindir/%name

%files
%doc README.txt
%_bindir/%namearch
%_bindir/%name

%changelog
* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 0.26c-alt1
- 0.26c:
  + fixes an issue with AMD processors

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 0.25a-alt1
- 0.25a (thanks force@)
  + upstream merged arches, added arm support

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 0.16-alt1
- 0.16
- NB: 0.15 brought assembly core and diverged between arches
  (this package is 64-bit only)

* Thu Aug 16 2007 Michael Shigorin <mike@altlinux.org> 0.13-alt1
- built for ALT Linux
- spec based on Dag Wieers' 0.12-1

* Sat Jul 28 2007 Dag Wieers <dag@wieers.com> - 0.12-1 - +/
- Initial package. (using DAR)
