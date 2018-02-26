%def_disable static

Name: librpcsecgss
Version: 0.19
Release: alt1

Summary: RPCSEC_GSS implementation
License: BSD
Group: System/Libraries
Url: http://www.citi.umich.edu/projects/nfsv4/linux/

Source: %name-%version-%release.tar

BuildRequires: libgssglue-devel

%package devel
Summary: RPCSEC_GSS library and headers
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: RPCSEC_GSS static library
Group: Development/C
Requires: %name-devel = %version-%release

%description
%name library allows secure rpc communication using the rpcsec_gss protocol

%description devel
%name library allows secure rpc communication using the rpcsec_gss protocol
This package holds development part of %name library

%description devel-static
%name library allows secure rpc communication using the rpcsec_gss protocol
This package contains static %name library

%prep
%setup

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

%files
%doc AUTHORS COPYING README
/%_lib/%name.so.*

%files devel
%_libdir/%name.so
%_pkgconfigdir/*
%_includedir/rpcsecgss

%if_enabled static
%files devel-static
%_libdir/%name.a
%endif

%changelog
* Sat Nov 06 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19-alt1
- 0.19 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18-alt1
- 0.18 released

* Sat Oct 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17-alt1
- 0.17 released

* Wed Sep  5 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14-alt2
- CVE-2007-3999 fixed

* Sun Dec  3 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14-alt1
- 0.14 released

* Mon Jul 17 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13-alt1
- 0.13 released

* Sun Mar 19 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8-alt1
- 0.8 released

* Mon Jan 16 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6-alt2
- fixed build for x86_64

* Sat Oct 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6-alt1
- 0.6 released

