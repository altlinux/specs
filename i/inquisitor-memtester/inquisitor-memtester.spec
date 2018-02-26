%define origname memtester

Name: inquisitor-%origname
Version: 4.0.8
Release: alt1

Summary: Userspace utility for testing the memory subsystem for faults
License: GPLv2 only
Group: System/Kernel and hardware

Url: http://pyropus.ca/software/memtester/
Source: %url/old-versions/memtester-%version.tar.gz
Patch: memtester-4.0.8-inquisitor.patch

Conflicts: %origname

%description
Memtester is a userspace utility for testing the memory subsystem
for faults.

This build has been patched for use with Inquisitor burn-in system.

%prep
%setup -n %origname-%version
%patch -p1

%build
%make_build

%install
install -pDm755 memtester %buildroot%_bindir/memtester
install -pDm644 memtester.8 %buildroot%_man8dir/memtester.8

%files
%doc BUGS CHANGELOG README README.tests
%_bindir/*
%_man8dir/*

# TODO:
# - propose the patch upstream

%changelog
* Thu Oct 15 2009 Michael Shigorin <mike@altlinux.org> 4.0.8-alt1
- built for Sisyphus (renamed with adding a conflict on origname)

* Sun Jul 20 2008 Mikhail Yakshin <greycat@altlinux.org> 4.0.8-inq1
- Build for Inquisitor

* Fri Nov 23 2007 Victor Forsyuk <force@altlinux.org> 4.0.8-alt1
- 4.0.8
- More precise License tag: this software is GPL v2 only.

* Wed May 16 2007 Victor Forsyuk <force@altlinux.org> 4.0.7-alt1
- Initial build.
