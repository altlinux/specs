Name: latencytop
Version: 0.5
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: A tool to visualize system latencies
License: GPLv2 only
Group: System/Kernel and hardware

URL: http://www.latencytop.org/
Source: http://www.latencytop.org/download/latencytop-%version.tar.gz
# Patches from Debian's latencytop 0.4
Patch0: latencytop-0.5-manpage.patch
Patch1: latencytop-misc.patch

# Automatically added by buildreq on Wed Mar 03 2010
BuildRequires: libgtk+2-devel libncursesw-devel

%description
LatencyTOP is a Linux tool for software developers (both kernel and userspace),
aimed at identifying where in the system latency is happening, and what kind of
operation/action is causing the latency to happen so that the code can be
changed to avoid the worst latency hiccups.

%prep
%setup
%patch0 -p1
#%patch1 -p1

%build
%make_build CFLAGS="%optflags"

%install
install -d %buildroot%_sbindir
%makeinstall_std
install -pD -m644 latencytop.8 %buildroot%_man8dir/latencytop.8

%files
%_sbindir/*
%_datadir/latencytop
%_man8dir/*

%changelog
* Wed Mar 03 2010 Victor Forsiuk <force@altlinux.org> 0.5-alt1
- 0.5

* Tue Oct 14 2008 Victor Forsyuk <force@altlinux.org> 0.4-alt1
- Initial build.
