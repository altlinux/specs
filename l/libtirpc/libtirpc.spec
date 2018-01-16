Name: libtirpc
Version: 1.0.2
Release: alt2

Summary: transport-independent RPC library
License: BSD
Group: System/Libraries

Source0: %name-%version-%release.tar

BuildRequires: libkrb5-devel

%package devel
Summary: TI-RPC library and headers
Group: Development/C
Requires: %name = %version-%release

%description
This package contains SunLib's implementation of transport-independent
RPC (TI-RPC) documentation.  This library forms a piece of the base of
Open Network Computing (ONC), and is derived directly from the Solaris 2.3 source.

%description devel
This package contains SunLib's implementation of transport-independent
RPC (TI-RPC) documentation.  This library forms a piece of the base of Open Network
Computing (ONC), and is derived directly from the Solaris 2.3 source.

This package holds development part of %name library

%prep
%setup

%build
[ ! -f autogen.sh ] || sh autogen.sh
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/
find %buildroot%_libdir -name \*.so|while read; do
	ln -snf ../../%_lib/`readlink $REPLY` %buildroot%_libdir/${REPLY##*/}
done

%files
%doc AUTHORS COPYING INSTALL README
%config(noreplace) %_sysconfdir/netconfig
/%_lib/%name.so.*
%_man5dir/netconfig.5.*

%files devel
%_libdir/%name.so
%_pkgconfigdir/*
%_includedir/tirpc
%_man3dir/*

%changelog
* Tue Jan 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt2
- Fixed build.

* Thu Jul 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt1
- 1.0.2 released

* Wed Apr 27 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.1-alt1
- 1.0.1 released

* Thu May 07 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released

* Mon Apr 27 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.6-alt0.3
- 0.2.6 rc3

* Mon Dec 29 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.6-alt0.2
- 0.2.6 rc2

* Thu Mar 20 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.4-alt1
- 0.2.4 released

* Tue Apr 16 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.3-alt1
- 0.2.3 released

* Fri Apr 22 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.2-alt0.4
- 0.2.2 rc4

* Wed Nov  3 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.2-alt0.3
- 0.2.2 rc3

* Fri Mar 26 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt1
- 0.2.1 released

* Thu May 28 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.11-alt1
- Initial build.
