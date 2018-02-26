Name: pktstat
Version: 1.8.5
Release: alt1

Summary: Real-time packet viewer
License: Public domain
Group: Monitoring

Url: http://www.adaptive-enterprises.com.au/~d/software/pktstat
Source: %url/pktstat-%version.tar.gz

# Automatically added by buildreq on Fri Mar 16 2012
BuildRequires: libncurses-devel libpcap-devel

%description
Display a real-time list of active connections seen on a network
interface, and how much bandwidth is being used by what. Partially
decodes HTTP and FTP protocols to show what filename is being
transferred. X11 application names are also shown. Entries hang around
on the screen for a few seconds so you can see what just happened.
Also accepts filter expressions a'la tcpdump.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 1.8.5-alt1
- 1.8.5

* Wed Sep 05 2007 Victor Forsyuk <force@altlinux.org> 1.8.4-alt1
- Initial build.
