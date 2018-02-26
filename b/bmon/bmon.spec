Name: bmon
Version: 2.1.0
Release: alt1.1

Summary: A portable bandwidth monitor
License: GPL 
Group: Monitoring

Url: http://people.suug.ch/~tgr/bmon/
Source: http://people.suug.ch/~tgr/bmon/files/%name-%version.tar.gz 
Patch1: bmon-2.1.0-gcc4.diff
Patch2: bmon-2.1.0-nostrip.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Feb 12 2007
BuildRequires: libncurses-devel librrd-devel

%description
%name is a portable bandwidth monitor and rate estimator
running on various operating systems.

It supports various input methods for different architectures.
Various output modes exist including an interactive curses
interface, lightweight HTML output but also formatable ASCII
output.  Statistics may be distributed over a network using
multicast or unicast and collected at some point to generate
a summary of statistics for a set of nodes. 

%prep
%setup 
%patch1 -p1
%patch2 -p0

%build
%configure --disable-asound
%make_build

%install
%makeinstall

%files
%_bindir/*
%_mandir/man?/*
%doc TODO BUGS etc/ trem/ xtra/ 

%changelog
* Sat Apr 17 2010 Sergey Y. Afonin <asy@altlinux.ru> 2.1.0-alt1.1
- rebuilt with new librrd

* Sun Feb 11 2007 Michael Shigorin <mike@altlinux.org> 2.1.0-alt1
- adopted an orphan
- fixed build with gcc4.1 (applied Gentoo patches)
- updated buildrequires

* Sun Nov 13 2005 Sasha Martsinuk <scampler@altlinux.ru> 2.1.0-alt1
- Initial build for ALTLinux Sisyphus 


