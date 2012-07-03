%def_disable static

Name: libgssglue
Version: 0.4
Release: alt1

Summary: GSSAPI frontend library
License: Distributable
Group: System/Libraries
Url: http://www.citi.umich.edu/projects/nfsv4/linux/

Provides: libgssapi
Obsoletes: libgssapi

Source0: %name-%version-%release.tar

%package devel
Summary: GSSAPI frontend library and headers
Group: Development/C
Requires: %name = %version-%release
Provides: libgssapi-devel
Obsoletes: libgssapi-devel

%if_enabled static
%package devel-static
Summary: GSSAPI frontend static library
Group: Development/C
Requires: %name-devel = %version-%release
Provides: libgssapi-devel-static
Obsoletes: libgssapi-devel-static
%endif

%description
This library exports a gssapi interface, but doesn't implement any gssapi
mechanisms itself; instead it calls gssapi routines in other libraries,
depending on the mechanism.

%description devel
This library exports a gssapi interface, but doesn't implement any gssapi
mechanisms itself; instead it calls gssapi routines in other libraries,
depending on the mechanism.

This package holds development part of %name library

%if_enabled static
%description devel-static
This library exports a gssapi interface, but doesn't implement any gssapi
mechanisms itself; instead it calls gssapi routines in other libraries,
depending on the mechanism.

This package contains static %name library
%endif

%prep
%setup -q
sed -i 's@^/usr/lib@/%_lib@; s@krb5\.so[ 	]@krb5.so.2 @' doc/gssapi_mech.conf

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/
find %buildroot%_libdir -name \*.so|while read; do
	ln -snf ../../%_lib/`readlink $REPLY` %buildroot%_libdir/${REPLY##*/}
done
install -pD -m644 doc/gssapi_mech.conf %buildroot%_sysconfdir/gssapi_mech.conf

%files
%doc AUTHORS COPYING README
%config(noreplace) %_sysconfdir/gssapi_mech.conf
/%_lib/%name.so.*

%files devel
%_libdir/%name.so
%_pkgconfigdir/*
%_includedir/gssglue

%if_enabled static
%files devel-static
%_libdir/%name.a
%endif

%changelog
* Sat Jun 23 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt1
- 0.4 released

* Thu Jun 30 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- 0.3 released

* Sat Nov 06 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt3
- rebuilt with set-versioned rpm

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt2
- obsolete by filetriggers macros removed

* Tue Oct 16 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- new release after rename from libgssapi

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.10-alt1.0
- Automated rebuild.

* Mon Jul 17 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt1
- 0.10 released

* Sun Mar 19 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt1
- 0.7 released

* Mon Jan 16 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt2
- fixed build on x86_64

* Fri Oct 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt1
- 0.5 released

* Sun Aug 21 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt1
- Initial build.
