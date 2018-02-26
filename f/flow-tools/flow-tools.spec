# Optional builds
# _with_mysql
# _with_pgsql
# --with mysql --with pgsql
Name: flow-tools
Version: 0.68
Release: alt6.1

Summary: Tool set for working with NetFlow data version %version
License: BSD
Group: Monitoring

Url: http://www.splintered.net/sw/flow-tools/
Source: ftp://ftp.eng.oar.net/pub/flow-tools/%name-%version.tar.bz2
Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

Patch1: flow-tools-0.67-shared.patch
Patch2: flow-tools-0.68-alt-config.patch
Patch3: flow-tools-0.68-alt-docs.patch.gz
Patch4: flow-tools-0.68-alt-path.patch
Patch5: flow-tools-0.68-alt-gcc41-compile.patch
Patch6: flow-tools-0.68-alt-x86_64-time.patch

Patch20: flow-tools-0.67-mysql.patch
Patch21: flow-tools-0.68-alt-bug9607.patch

# not used now
Patch102: flow-tools-0.67-config.patch
Patch103: flow-tools-0.67-docs.patch
Patch104: flow-tools-0.67-gcc34.patch
Patch105: flow-tools-0.67-gcc4_amd64.patch
Patch106: flow-tools-0.67-debug.patch


Provides: flow-tools
BuildPreReq: flex zlib-devel %{?_with_mysql: libMySQL-devel} %{?_with_pgsql: postgresql-devel}

# Automatically added by buildreq on Tue Jan 08 2008
BuildRequires: libwrap-devel

Requires: lib%name = %version-%release

%description
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
Summary:        Shared libraries of %{name}
Group:          System/Libraries

%description -n lib%name
Shared libraries of %name.

%package -n lib%name-devel
Summary:        Development headers and libraries for %{name}
Group:          Development/C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development headers and libraries for %name

%package utils
Summary:        %{name} utilities
Group:          Monitoring
Requires:	%name = %version-%release
BuildArch:	noarch

%description utils
This package contains scripts to provide ASCII, HTML, RRD output

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%if_with mysql
%patch20 -p1
%patch21 -p1
%endif

%build
%autoreconf

%configure \
		--disable-static \
    %{?_with_mysql:--with-mysql} \
    %{?_with_pgsql:--with-pgsql}

%make_build

%install
%makeinstall

install -pm644 configs/filter-acl %buildroot/%_sysconfdir/flow-tools/
install -pm644 configs/flow.acl %buildroot/%_sysconfdir/flow-tools/

rm -f %buildroot%_libdir/*.la

%files
%doc  AUTHORS ChangeLog INSTALL README SECURITY TODO contrib docs/*.html
%dir %_sysconfdir/flow-tools/
%dir %_sysconfdir/flow-tools/cfg
%config(noreplace) %_sysconfdir/flow-tools/cfg/*
%_sysconfdir/flow-tools/filter-acl
%_sysconfdir/flow-tools/flow.acl
%dir %_datadir/flow-tools/
%dir %_datadir/flow-tools/sym
%_datadir/flow-tools/sym/*
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
#_libdir/*.a

%files utils
%_bindir/flow-rpt2rrd
%_bindir/flow-log2rrd
%_bindir/flow-rptfmt

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.68-alt6.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.68-alt6
- Rebuilt for debuginfo
- Extracted %_libdir/*.so.* into lib%name
- Renamed %name-devel to lib%name-devel
- Removed static libraries

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.68-alt5
- Rebuilt for soname set-versions

* Tue Aug 31 2010 Michael Shigorin <mike@altlinux.org> 0.68-alt4.2
- moved flow-rptfmt, flow-rpt2rrd, flow-log2rrd to a separate subpackage
  to reduce main package dependencies (thanks wrar@; closes: #23944)
- spec cleanup
- NB: this package needs proper maintainer

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.68-alt4.1
- Rebuilt with python 2.6

* Tue May 27 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.68-alt4
- spec-file fix -- add unpackaged directories

* Fri Feb 08 2008 Grigory Batalov <bga@altlinux.ru> 0.68-alt3.1
- Rebuilt with python-2.5.

* Tue Jan 08 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.68-alt3
- fix for x86_64 by emp-at-zra-dot-ru (patch #6)
- rebuild with latest autotools

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.68-alt2.0
- Automated rebuild.

* Mon Jul 03 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.68-alt2
- fix:
   + ALT bug #9607
   + compile with gcc4.1

* Wed Jan 18 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.68-alt1
- 0.68

* Fri May 06 2005 Konstantin Klimchev <koka@altlinux.ru> 0.67-alt6
- fix:
  bug #6786 (bugzilla.altlinux.ru)
- remove: 
  flow-tools-0.67-gcc34.patch
- add: 
  flow-tools-0.67-gcc4_amd64.patch 
     from ftp.debian.org
  flow-tools-0.67-mysql.patch (only --with mysql) 
     from #6790 (bugzilla.altlinux.ru)

* Mon Jan 17 2005 Konstantin Klimchev <koka@altlinux.ru> 0.67-alt5
- fix flow-tools-0.67-gcc34.patch

* Fri Jun 18 2004 Konstantin Klimchev <koka@altlinux.ru> 0.67-alt4
- fix flow-tools-0.67-config.patch

* Wed Apr 28 2004 Konstantin Klimchev <koka@altlinux.ru> 0.67-alt3
- return: FT_PATH_CGF_ACL = "/etc/flow-tools/filter-acl" (default 
  config for flow-filter)

* Wed Feb 18 2004 Konstantin Klimchev <koka@altlinux.ru> 0.67-alt2
- rebuild for Sisyphus

* Thu Feb 5 2004 Konstantin Klimchev <koka@altlinux.ru> 0.67-alt0.2
- add patch to build shared library

* Wed Dec 24 2003 Konstantin Klimchev <koka@altlinux.ru> 0.67-alt0.1
- initial release for Daedalus

* Thu Dec 11 2003 Konstantin Klimchev <koka@atvc.ru> 0.67-1
- 0.67
- add optional build "--with mysql" and "--with pgsql"
- rewrite spec

* Tue Nov 19 2002 Oleg Prokopyev <riiki@altlinux.ru> 0.59-alt1
- Initial build for Sisyphus.

