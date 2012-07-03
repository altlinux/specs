Name: inquisitor-bnbt
Version: 20060727
Release: alt1.beta85

Summary: A C++ BitTorrent Tracker
License: LGPL 2.1+
Group: System/Servers

Url: http://sourceforge.net/projects/bnbt/
Source: 20060727-bnbt85-src.tar.gz
Patch0: bnbt85-20060727-gcc44.patch
Patch1: bnbt85-20060727-inquisitor.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Nov 02 2009
BuildRequires: gcc-c++ libMySQL-devel zlib-devel

BuildRequires: gcc-c++

%description
This package contains a version of BNBT BitTorrent tracker
patched specifically for Inquisitor.

%prep
%setup -n 20060727-bnbt85-src
%patch0 -p1
%patch1 -p1

%build
%make_build

%install
install -pDm755 bnbt %buildroot%_bindir/bnbt

%files
%_bindir/bnbt

%changelog
* Mon Nov 02 2009 Michael Shigorin <mike@altlinux.org> 20060727-alt1.beta85
- built for ALT Linux
- fixed build with gcc-4.4
