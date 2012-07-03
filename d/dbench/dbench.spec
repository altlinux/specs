Name: dbench
Version: 4.0
Release: alt3

Summary: Filesystem and TCP networking benchmark similar to Netbench
License: GPLv3
Group: System/Kernel and hardware

URL: http://samba.org/ftp/tridge/dbench/
Source: %url/%name-%version.tar.gz
Patch1: dbench-4.0-manpage.patch

Requires: %name-data

# Automatically added by buildreq on Mon Sep 28 2009
BuildRequires: libattr-devel libpopt-devel

%description
dbench is a filesystem benchmark that generates load patterns similar to
those of the commercial Netbench benchmark, but without requiring a lab of
Windows load generators to run. It is now considered a de-facto standard for
generating load on the Linux VFS.

tbench is a network benchmark which generates only the TCP and process load
similar to the one created by Netbench.

%package data
Summary: Architecture independent data files for dbench
Group: System/Kernel and hardware
BuildArch: noarch

%description data
Architecture independent data files for dbench.

%prep
%setup
%patch1 -p1

%build
./autogen.sh
%configure
%make_build bindir="%_bindir" mandir="%_man1dir" datadir="%_datadir/%name"

%install
%makeinstall \
	bindir="%buildroot%_bindir" \
	mandir="%buildroot%_man1dir" \
	datadir="%buildroot%_datadir/%name"

%files
%_bindir/*
%doc README

%files data
%_datadir/%name
%_man1dir/*

%changelog
* Tue Nov 09 2010 Victor Forsiuk <force@altlinux.org> 4.0-alt3
- Fix man page (closes: #24498).

* Mon Sep 28 2009 Victor Forsyuk <force@altlinux.org> 4.0-alt2
- Split architecture independent data files to noarch subpackage.

* Mon Mar 03 2008 Victor Forsyuk <force@altlinux.org> 4.0-alt1
- 4.0

* Tue Nov 15 2005 Victor Forsyuk <force@altlinux.ru> 3.04-alt1
- 3.04

* Tue Apr 19 2005 Victor Forsyuk <force@altlinux.ru> 3.03-alt1
- 3.03

* Wed Jul 02 2003 Sergey Vlasov <vsu@altlinux.ru> 2.0-alt1
- First build for ALT Linux.
