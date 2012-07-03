Name: dumpet
Version: 2.1
Release: alt1
Summary: A tool to dump and debug bootable CD images
Packager: Mike Pluzhnikov <amike@altlinux.ru>
License: GPLv2+
Group: Development/Tools
Url: https://fedorahosted.org/dumpet/
Source0: https://fedorahosted.org/releases/d/u/dumpet/dumpet-%version.tar
BuildRequires: libpopt-devel libxml2-devel

%description
DumpET is a utility to aid in the debugging of bootable CD-ROM images.

%prep
%setup 

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
* Fri Jun 01 2012 Mikhail Pluzhnikov <amike@altlinux.ru> 2.1-alt1
- First build

