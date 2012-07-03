Name: lnav
Version: 0.4.0
Release: alt1

Summary: The log file navigator
License: BSD
Group: File tools

Url: http://tstack.github.com/lnav/
Source: %name-%version.tar.gz
Patch0: lnav-0.4.0-alt-fixes.patch
Patch1: lnav-fix_32bit_use_size_t.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Sep 25 2011
# optimized out: libpcre-devel libstdc++-devel libtinfo-devel
BuildRequires: bzlib-devel gcc-c++ libncurses-devel libpcrecpp-devel libreadline-devel libsqlite3-devel libssl-devel zlib-devel

%description
The log file navigator, lnav, is an enhanced log file viewer that
takes advantage of any semantic information that can be gleaned
from the files being viewed, such as timestamps and log levels.
Using this extra semantic information, lnav can do things like
interleaving messages from different files, generate histograms
of messages over time, and providing hotkeys for navigating
through the file.  It is hoped that these features will allow
the user to quickly and efficiently zero in on problems.

%prep
%setup
%patch0 -p1
%patch1 -p0
touch AUTHORS ChangeLog COPYING

%build
%autoreconf
%configure --disable-static
%make_build CXXFLAGS+="-I%_includedir/pcre"

%install
%makeinstall_std

%files
%_bindir/*
%doc LICENSE README

# TODO:
# - they really should use pkg-config wrt libpcre
# - and check for /dev/ptmx or whatever to have opened ok
#   (putting out meaningful diags otherwise, e.g. in a chroot)

%changelog
* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- 0.4.0
- updated patch
- added a suse patch

* Thu Dec 02 2010 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- built for ALT Linux

