Name: dumpet
Version: 2.1
Release: alt2
Summary: A tool to dump and debug bootable CD images
License: GPLv2+
Group: Development/Tools
Url: https://fedorahosted.org/dumpet/
Source0: https://fedorahosted.org/releases/d/u/dumpet/dumpet-%version.tar
BuildRequires: libpopt-devel libxml2-devel

Patch: fix-build-with-new-libxml2-2.14.patch

%description
DumpET is a utility to aid in the debugging of bootable CD-ROM images.

%prep
%setup
%patch -p1

%build
%make_build

%install
mkdir -p %buildroot/%_bindir
%makeinstall_std

%files
%doc README TODO COPYING
%_man1dir/dumpet.1*
%_bindir/dumpet

%changelog
* Fri Jan 16 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.1-alt2
- FTBFS: fix build with new libxml2 2.14

* Fri Jun 01 2012 Mikhail Pluzhnikov <amike@altlinux.ru> 2.1-alt1
- First build

