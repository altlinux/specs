%define mibsdir %_datadir/mibs
%define pibsdir %_datadir/pibs

%def_disable static
%def_disable mibs_internal

Name: libsmi
Version: 0.4.8
Release: alt2

Summary: A library to access SMI MIB information
License: BSD
Group: System/Libraries
URL: http://www.ibr.cs.tu-bs.de/projects/libsmi/index.html

Packager: Alexey Shabalin <shaba@altlinux.ru>

Source0: ftp://ftp.ibr.cs.tu-bs.de/pub/local/libsmi/%name-%version.tar
Source1: smi.conf
Patch1: %name-backports.patch
Patch2: %name-man.patch
Patch3: %name-smistrip.patch
Patch4: %name-fix-parallel-build.patch

Requires: snmp-mibs
BuildRequires: flex gcc-c++ wget
%if_enabled static
BuildRequires: glibc-devel-static
%endif

%package devel
Summary: Development environment for libsmi library
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: Static libsmi library
Group: Development/C
Requires: %name-devel = %version-%release

%package mibs
Summary: MIB files for LibSMI
Group: Networking/Other
BuildArch: noarch
Provides: snmp-mibs

%package -n smi-tools
Summary: LibSMI tools
Group: Networking/Other
Requires: %name = %version-%release
Requires: wget

%description
Libsmi is a C library to access MIB module information through
a well defined API that hides the nasty details of locating
and parsing SMIv1/v2 MIB modules. 

This package contains tools to check, dump, and convert MIB 
definitions and a steadily maintained and revised archive 
of all IETF and IANA maintained standard MIB modules. 

%description devel
Libsmi is a C library to access MIB module information through
a well defined API that hides the nasty details of locating
and parsing SMIv1/v2 MIB modules. 

This package contains development files needed to develop %name-based
applications.

%description devel-static
Libsmi is a C library to access MIB module information through
a well defined API that hides the nasty details of locating
and parsing SMIv1/v2 MIB modules. 

This package contains the static %name library needed to develop 
statically linked %name-based applications.

%description mibs
MIBs for %name. May be used with other packages (net-snmp, for example)

%description -n smi-tools
This package contains the LibSMI tools.


%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-shared \
	--with-mibdir=%mibsdir \
	--with-pibdir=%pibsdir \
	--with-smipath=%mibsdir/site:%mibsdir/ietf:%mibsdir/iana \
	--sysconfdir=%_sysconfdir \
	--enable-smi \
	--enable-sming
%make_build

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot%_sysconfdir
install -p -m 644 %SOURCE1 %buildroot%_sysconfdir/smi.conf

#%%check
#%%make_build check

%files
%doc ChangeLog ANNOUNCE README COPYING THANKS smi.conf-example
%config(noreplace) %_sysconfdir/smi.conf
%_libdir/*.so.*

%files devel
%doc TODO doc/draft-irtf-nmrg-sming-02.txt
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*.m4
%_includedir/*
%_man3dir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%if_enabled mibs_internal
%files mibs
%mibsdir
%pibsdir
%else
%exclude %mibsdir
%exclude %pibsdir
%endif

%files -n smi-tools
%_bindir/*
%_man1dir/*

%changelog
* Mon Oct 25 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.8-alt2
- some backports
- security fix: CVE-2010-2891 (ALT #24394)

* Thu Feb 25 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.8-alt1
- 0.4.8
- move tools to smi-tools subpackage
- move mibs to libsmi-mibs subpackage, but not build by default; use external snmp-mibs package
- disable build static by default
- add debian smistrip.patch
- change Packager

* Fri Nov 29 2002 Oleg Prokopyev <riiki@altlinux.ru> 0.4.1-alt1
- new version

* Fri Nov 22 2002 Oleg Prokopyev <riiki@altlinux.ru> 0.4.0-alt1
- Initial build for Sisyphus.
