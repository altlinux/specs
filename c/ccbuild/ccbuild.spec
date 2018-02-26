Name: ccbuild
Version: 1.5.7
Release: alt1

Summary: Dynamic Makefile
License: GPL
Group: Development/Other
Url: http://ccbuild.sourceforge.net/

Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Automatically added by buildreq on Fri Aug 03 2007
BuildRequires: flex gcc-c++ libgcrypt-devel

%description
ccbuild is like a dynamic Makefile. ccbuild finds all programs in the
current directory (containing "int main") and builds them. For this,
it reads the C++ sources and looks at all local and global includes. All
C++ files surrounding local includes are considered objects for the main
program. The global includes lead to extra compiler arguments using a
configuration file. ccbuild splits these arguments for compilation and
linking, keeping the linking arguments back for later use. It should
allow development without any scripting and only simple reusable
configuration. Deployment and distribution should still be done with
other tools. It can create simple Makefiles, A-A-P files, and graph
dependencies using DOT (graphviz) graphs.

%prep
%setup -q
#%patch0 -b .env

%build
%configure
%make_build

%install
%makeinstall_std
%__install -D -m 0644 doc/ccbuild/%name.1 %buildroot%_man1dir/%name.1

%files
%doc README NEWS TODO doc/ccbuild/ccbuild.html/
%_bindir/*
%_man1dir/*

%changelog
* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.7-alt1
- new version 1.5.7 (with rpmrb script)

* Mon Jul 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.6-alt1
- new version 1.5.6 (with rpmrb script)

* Fri Aug 03 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt1
- new version 1.5.5 (with rpmrb script)
- fix build, update buildreq

* Sat Dec 30 2006 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt0.1
- new version 1.5.3 (with rpmrb script)

* Mon Mar 27 2006 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version (1.5.2)
- update Url, Source

* Tue Sep 13 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- initial build for ALT Linux Sysiphus
