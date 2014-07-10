Name: flow-tools-ng
Version: 0.68.5
Release: alt1.1

Summary: Tool set for working with NetFlow data version %version
License: BSD
Group: Monitoring

Url: http://code.google.com/p/flow-tools/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

Provides: flow-tools
Conflicts: flow-tools

BuildPreReq: flex zlib-devel %{?_with_mysql: libMySQL-devel} %{?_with_pgsql: postgresql-devel}

# Automatically added by buildreq on Tue Jul 02 2013
# optimized out: OpenSP docbook-dtds docbook-style-dsssl libpq-devel openjade perl-SGMLSpm sgml-common zlib-devel
BuildRequires: checkstyle docbook-utils flex glibc-devel libwrap-devel postgresql-devel w3c-markup-validator-libs

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
# fix broken env path
find -type f | xargs subst "s|#!/bin/env|#/!/usr/bin/env|g"

%build
%autoreconf
%configure --sysconfdir=%_sysconfdir/%name/ \
		--disable-static \
%{?_with_mysql:--with-mysql} \
%{?_with_pgsql:--with-pgsql}

%make_build

%install
%makeinstall_std

install -pm644 configs/filter-acl %buildroot/%_sysconfdir/%name/
install -pm644 configs/flow.acl %buildroot/%_sysconfdir/%name/

rm -f %buildroot%_libdir/*.la

%files
%doc  AUTHORS README SECURITY TODO contrib docs/*.html
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/cfg/
%dir %_sysconfdir/%name/sym/
%config(noreplace) %_sysconfdir/%name/cfg/*
%config(noreplace) %_sysconfdir/%name/sym/*
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
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.68.5-alt1.1
- NMU: corrected java dependencies

* Tue Jul 02 2013 Vitaly Lipatov <lav@altlinux.ru> 0.68.5-alt1
- initial build flow-tools fork for ALT Linux Sisyphus (ALT bug #16128)
