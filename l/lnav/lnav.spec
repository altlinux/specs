Name: lnav
Version: 0.8.1
Release: alt1

Summary: The log file navigator
License: BSD
Group: File tools

Url: http://lnav.org
Source0: %name-%version.tar.gz
Source1: %name.watch
Patch0: lnav-0.4.0-alt-fixes.patch
Patch1: lnav-fix_32bit_use_size_t.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Jun 23 2014
# optimized out: libcloog-isl4 libpcre-devel libstdc++-devel libtinfo-devel python-base
BuildRequires: bzlib-devel gcc-c++ libncurses-devel libpcrecpp-devel libreadline-devel libsqlite3-devel sqlite3 zlib-devel

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
sed -i 's,var/log/syslog,&/messages,g' src/lnav.cc
touch AUTHORS ChangeLog COPYING

%build
%autoreconf
%configure --disable-static
%make_build CXXFLAGS+="-I%_includedir/pcre"

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%doc LICENSE README

# TODO:
# - they really should use pkg-config wrt libpcre
# - and check for /dev/ptmx or whatever to have opened ok
#   (putting out meaningful diags otherwise, e.g. in a chroot)

%changelog
* Thu Aug 11 2016 Michael Shigorin <mike@altlinux.org> 0.8.1-alt1
- new version (watch file uupdate)

* Mon Nov 16 2015 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- new version (watch file uupdate)
- tweaked default logfile location

* Thu May 28 2015 Michael Shigorin <mike@altlinux.org> 0.7.3-alt2
- rebuilt against current libpcre*

* Sun Apr 12 2015 Michael Shigorin <mike@altlinux.org> 0.7.3-alt1
- new version (watch file uupdate)

* Wed Mar 04 2015 Michael Shigorin <mike@altlinux.org> 0.7.2-alt1
- new version (watch file uupdate)

* Mon Nov 10 2014 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- new version (watch file uupdate)

* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- new version (watch file uupdate)
- dropped patches
- buildreq

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- 0.4.0
- updated patch
- added a suse patch

* Thu Dec 02 2010 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- built for ALT Linux

