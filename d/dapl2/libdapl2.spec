%def_enable shared
%def_enable static

Name: dapl2
%define lname lib%name
%define oldlname libdapl
Version: 2.0.30
Release: alt2
Summary: A Library for userspace access to RDMA devices using OS Agnostic DAT APIs
Group: System/Libraries
License: %gpl2only, %bsdstyle, CPL
Url: http://www.openfabrics.org/
# git://git.openfabrics.org/~ardavis/dapl.git
Source: %name-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: librdmacm-devel

%description
Along with the OpenFabrics kernel drivers, libdat and libdapl provides
a userspace RDMA API that supports DAT 2.0 specification and IB
transport extensions for atomic operations and rdma write with
immediate data.


%package -n %lname
Summary: A Library for userspace access to RDMA devices using OS Agnostic DAT APIs
Group: System/Libraries

%description -n %lname
Along with the OpenFabrics kernel drivers, libdat and libdapl provides
a userspace RDMA API that supports DAT 2.0 specification and IB
transport extensions for atomic operations and rdma write with
immediate data.


%package -n %lname-devel
Summary: Development files for the libdat and libdapl libraries
Group: Development/C
Requires: %lname = %version-%release
Conflicts: %oldlname-devel

%description -n %lname-devel
Header files for libdat and libdapl library.


%package -n %lname-devel-static
Summary: Static development files for libdat and libdapl library
Group: Development/C
Requires: %lname-devel = %version-%release
Conflicts: %oldlname-devel-static

%description -n %lname-devel-static
Static libraries for libdat and libdapl library.


%package utils
Summary: Test suites for uDAPL library
Group: Development/Other
Requires: %lname = %version-%release
Conflicts: %oldlname-utils

%description utils
Useful test suites to validate uDAPL library API's.


%prep
%setup


%build
%autoreconf
%configure \
    --with-pic \
    %{subst_enable shared} \
    %{subst_enable static} \
    --with-gnu-ld \
    --enable-ext-type=ib
%make_build


%install
%make_install DESTDIR=%buildroot install{-datlibLTLIBRARIES,}

mv %buildroot%_sysconfdir/dat.conf \
	%buildroot%_sysconfdir/dat2.conf

%files -n %lname
%doc AUTHORS README ChangeLog
%_libdir/*.so.*
%config(noreplace) %_sysconfdir/dat2.conf


%files -n %lname-devel
%_libdir/*.so
%_includedir/dat2


#files -n %lname-devel-static
#_libdir/*.a


%files utils
%_bindir/*
%_man1dir/*
%_man5dir/*


%changelog
* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.30-alt2
- Rebuilt for debuginfo
- Disabled static package

* Tue Dec 07 2010 Andriy Stepanov <stanv@altlinux.ru> 2.0.30-alt1
- New version (OFED 1.5.2_v2)

* Mon Aug 16 2010 Andriy Stepanov <stanv@altlinux.ru> 2.0.27-alt2
- New version (OFED 1.5.1)

* Mon Jul 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.20-alt2
- Added default %_sysconfdir/dat2.conf (thnx led@)

* Wed Jul 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.20-alt1.1
- Build from upstream git repository

* Wed Jul 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.20-alt1
- Version 2.0.20

* Wed Jun 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.19-alt2.1
- Build for Sisyphus

* Tue Jun 23 2009 Led <led@altlinux.ru> 2.0.19-alt2
- fixed linking
- cleaned up spec

* Sun Jun 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.19-alt1.1
- Build for Sisyphus

* Wed May 20 2009 Led <led@altlinux.ru> 2.0.19-alt1
- 2.0.19

* Thu Apr 23 2009 Led <led@altlinux.ru> 2.0.16-alt1
- initial build for ALT

* Mon Mar 16 2009 Arlin Davis <ardavis@ichips.intel.com> - 2.0.16
- DAT/DAPL Version 2.0.16 Release 1, OFED 1.4.1 

* Fri Nov 07 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.15
- DAT/DAPL Version 2.0.15 Release 1, OFED 1.4 GA

	Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.15-alt1
- Version 2.0.15
- New names of libraries -> new names of packages
- Add static devel package

* Sat Nov 01 2008 Stanislav Ievlev <inger@altlinux.org> 1.2.7-alt2
- fix build with gcc 4.3

* Mon Oct 13 2008 Stanislav Ievlev <inger@altlinux.org> 1.2.7-alt1
- OFED-1.3.1

* Fri Oct 03 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.14
- DAT/DAPL Version 2.0.14 Release 1, OFED 1.4 rc3

* Mon Sep 01 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.13
- DAT/DAPL Version 2.0.13 Release 1, OFED 1.4 rc1

* Thu Aug 21 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.12
- DAT/DAPL Version 2.0.12 Release 1, OFED 1.4 beta

* Sun Jul 20 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.11
- DAT/DAPL Version 2.0.11 Release 1, IB UD extensions in SCM provider 

* Tue Jun 23 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.10
- DAT/DAPL Version 2.0.10 Release 1, socket CM provider 

* Tue May 20 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.9
- DAT/DAPL Version 2.0.9 Release 1, OFED 1.3.1 GA  

* Thu May 1 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.8
- DAT/DAPL Version 2.0.8 Release 1, OFED 1.3.1  

* Thu Feb 14 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.7
- DAT/DAPL Version 2.0.7 Release 1, OFED 1.3 GA 

* Mon Feb 04 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.6
- DAT/DAPL Version 2.0.6 Release 1, OFED 1.3 RC4

* Tue Jan 29 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.5
- DAT/DAPL Version 2.0.5 Release 1, OFED 1.3 RC3

* Thu Jan 17 2008 Arlin Davis <ardavis@ichips.intel.com> - 2.0.4
- DAT/DAPL Version 2.0.4 Release 1, OFED 1.3 RC2

* Tue Nov 20 2007 Arlin Davis <ardavis@ichips.intel.com> - 2.0.3
- DAT/DAPL Version 2.0.3 Release 1

* Tue Oct 30 2007 Arlin Davis <ardavis@ichips.intel.com> - 2.0.2
- DAT/DAPL Version 2.0.2 Release 1

* Tue Sep 18 2007 Arlin Davis <ardavis@ichips.intel.com> - 2.0.1-1
- OFED 1.3-alpha, co-exist with DAT 1.2 library package.  

* Fri Aug 24 2007 Stanislav Ievlev <inger@altlinux.org> 1.2.1-alt1
- Initial build

* Wed Mar 7 2007 Arlin Davis <ardavis@ichips.intel.com> - 2.0.0.pre
- Initial release of DAT 2.0 APIs, includes IB extensions 
