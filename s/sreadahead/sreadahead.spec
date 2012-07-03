Name: sreadahead
Version: 1.0
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Super Read Ahead
License: GPLv2+
Group: System/Configuration/Boot and Init

Url: http://code.google.com/p/sreadahead/
Source: http://sreadahead.googlecode.com/files/sreadahead-%version.tar.gz
Patch0: sreadahead-1.0-asneeded.patch

%description
sreadahead speeds up booting by pre-reading disk blocks used during previous boots.

%prep
%setup
%patch0 -p1

%build
%define _optlevel s
%make_build CFLAGS="%optflags"

%install
install -d %buildroot/var/lib/sreadahead/debugfs
install -d %buildroot/sbin
install -p -m755 sreadahead %buildroot/sbin/

%files
/sbin/*
/var/lib/sreadahead

%changelog
* Fri Aug 20 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- 1.0

* Tue Oct 07 2008 Victor Forsyuk <force@altlinux.org> 0.02-alt1
- Initial build.
