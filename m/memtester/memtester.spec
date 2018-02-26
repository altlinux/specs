Name: memtester
Version: 4.2.2
Release: alt1

Summary: Userspace utility for testing the memory subsystem for faults
License: GPLv2 only
Group: System/Kernel and hardware

Url: http://pyropus.ca/software/memtester
Source: %url/old-versions/memtester-%version.tar.gz

%description
Memtester is a userspace utility for testing the memory subsystem for faults.

%prep
%setup

# to apply optflags:
subst 's/-O2/%optflags/' conf-cc
# and be able to verify them in build log:
subst 's#/bin/sh#/bin/sh -x#' warn-auto.sh

%build
%make_build

%install
install -pD -m755 memtester %buildroot%_bindir/memtester
install -pD -m644 memtester.8 %buildroot%_man8dir/memtester.8

%files
%doc BUGS README README.tests
%_bindir/*
%_man8dir/*

%changelog
* Sun Jul 31 2011 Victor Forsiuk <force@altlinux.org> 4.2.2-alt1
- 4.2.2

* Thu Oct 07 2010 Victor Forsiuk <force@altlinux.org> 4.2.1-alt1
- 4.2.1

* Wed Aug 04 2010 Victor Forsiuk <force@altlinux.org> 4.2.0-alt1
- 4.2.0

* Mon Mar 01 2010 Victor Forsiuk <force@altlinux.org> 4.1.3-alt1
- 4.1.3

* Thu Sep 03 2009 Victor Forsyuk <force@altlinux.org> 4.1.2-alt1
- 4.1.2

* Sun Jul 26 2009 Victor Forsyuk <force@altlinux.org> 4.1.1-alt1
- 4.1.1

* Fri Nov 23 2007 Victor Forsyuk <force@altlinux.org> 4.0.8-alt1
- 4.0.8
- More precise License tag: this software is GPL v2 only.

* Wed May 16 2007 Victor Forsyuk <force@altlinux.org> 4.0.7-alt1
- Initial build.
