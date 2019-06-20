Name: sreadahead
Version: 1.0
Release: alt2

Summary: Super Read Ahead
License: GPLv2+
Group: System/Configuration/Boot and Init

Url: http://code.google.com/p/sreadahead/
Source: http://sreadahead.googlecode.com/files/sreadahead-%version.tar.gz
Patch0: sreadahead-1.0-asneeded.patch
Patch1: sreadahead-1.0-alt-ioprio-arches.patch
Packager: Michael Shigorin <mike@altlinux.org>

%description
sreadahead speeds up booting by pre-reading disk blocks
used during previous boots.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%make_build CFLAGS="%optflags"

%install
install -d %buildroot%_localstatedir/%name/debugfs
install -pDm755 %name %buildroot/sbin/%name

%files
/sbin/*
%_localstatedir/%name

%changelog
* Thu Jun 20 2019 Michael Shigorin <mike@altlinux.org> 1.0-alt2
- added patch to support non-x86 arches

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Aug 20 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- 1.0

* Tue Oct 07 2008 Victor Forsyuk <force@altlinux.org> 0.02-alt1
- Initial build.
