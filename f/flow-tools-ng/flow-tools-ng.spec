%def_without mysql
%def_with pgsql

Name: flow-tools-ng
Version: 0.68.6
Release: alt1

Summary: Tool set for working with NetFlow data version %version
License: BSD
Group: Monitoring
Url: https://github.com/5u623l20/flow-tools

Source: %name-%version.tar
Patch1: flow-tools-ng-0.68.5-gcc-10-extern.patch
Patch2: aclyacc-0.68.5-alt-build.patch

Provides: flow-tools
Conflicts: flow-tools

BuildRequires: docbook-utils flex zlib-devel docbook-to-man %{?_with_mysql: libmysqlclient-devel} %{?_with_pgsql: libpq-devel}

Requires: lib%name = %version-%release

%description
This fork was created because original flow-tools upstream disappeared.

Flow-tools is library and a collection of programs used to
collect, send, process, and generate reports from NetFlow data.
The tools can be used together on a single server or distributed
to multiple servers for large deployments. The flow-toools library
provides an API for development of custom applications for NetFlow
export versions 1,5,6 and the 14 currently defined version 8
subversions.

Optional : mysql pgsql
Enabled  :%{?_with_mysql: mysql} %{?_with_pgsql: pgsql}

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

Conflicts: libflow-tools

%description -n lib%name
Shared libraries of %name.

%package -n lib%name-devel
Summary: Development headers and libraries for %name
Group: Development/C

Requires: lib%name = %version-%release
Conflicts: libflow-tools-devel

%description -n lib%name-devel
Development headers and libraries for %name

%package utils
Summary: %name utilities
Group: Monitoring
Requires: %name = %version-%release
BuildArch: noarch
Conflicts: flow-tools-utils

%description utils
This package contains scripts to provide ASCII, HTML, RRD output

%prep
%setup
%patch1 -p1
%patch2 -p0
# fix broken env path
find -type f | xargs subst "s|#!/usr/bin/env python|#/!/usr/bin/python|g"
find -type f | xargs subst "s|#!/usr/bin/env perl|#/!/usr/bin/perl|g"

%build
%autoreconf
%configure --sysconfdir=%_sysconfdir/%name/ \
		--disable-static \
		%{?_with_mysql:--with-mysql} \
		%{?_with_pgsql:--with-postgresql=yes}

%make_build CFLAGS="$CFLAGS -std=gnu11"

%install
%makeinstall_std

install -pm644 configs/filter-acl %buildroot/%_sysconfdir/%name/
install -pm644 configs/flow.acl %buildroot/%_sysconfdir/%name/

rm -f %buildroot%_libdir/*.la

%files
%doc  AUTHORS README SECURITY TODO contrib
%dir %_sysconfdir/%name/
%_sysconfdir/%name/flow-tools
%config(noreplace) %_sysconfdir/%name/filter-acl
%config(noreplace) %_sysconfdir/%name/flow.acl
%_datadir/flow-tools/
%_bindir/*
%exclude %_bindir/flow-rpt2rrd
%exclude %_bindir/flow-log2rrd
%exclude %_bindir/flow-rptfmt
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files utils
%_bindir/flow-rpt2rrd
%_bindir/flow-log2rrd
%_bindir/flow-rptfmt

%changelog
* Wed Oct 07 2026 Alexei Takaseev <taf@altlinux.org> 0.68.6-alt1
- 0.68.6

* Tue Dec 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.68.5-alt6
- NMU:FTBFS: Fix error of yyerror() (thnx FreeBSD fix)

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0.68.5-alt5
- NMU: drop obsolete checkstyle BR:

* Fri Mar 26 2021 Slava Aseev <ptrnine@altlinux.org> 0.68.5-alt4
- fix build with gcc-10

* Thu Mar 21 2019 Anton Farygin <rider@altlinux.ru> 0.68.5-alt3
- rebuild without w3c-markup-validator-libs

* Tue Sep 18 2018 Vitaly Lipatov <lav@altlinux.ru> 0.68.5-alt2
- rebuild without libwrap-devel

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.68.5-alt1.1
- NMU: corrected java dependencies

* Tue Jul 02 2013 Vitaly Lipatov <lav@altlinux.ru> 0.68.5-alt1
- initial build flow-tools fork for ALT Linux Sisyphus (ALT bug #16128)
