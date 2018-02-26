Name:    libomniORB
License: LGPL
URL:     http://omniorb.sourceforge.net/

Version: 4.2.0
Release: alt3.1

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: omniORB-%version.tar.gz
Source1: omniORB.cfg
Source2: omninames
Source3: omninames.sysconfig

Patch0: libomniORB-non-strict.patch
Patch1: libomniORB-all-cosifaces.patch

# Automatically added by buildreq on Wed Aug 26 2009
BuildRequires: gcc-c++ libssl-devel python-devel python-modules-compiler

Summary: ORB from AT&T (core libraries)
Group:   Networking/Remote access
%description
omniORB is an Object Request Broker (ORB) that implements the 2.3
specification of the Common Object Request Broker Architecture
(CORBA) [OMG99]. It has passed the Open Group CORBA compliant
testsuite and is one of the three ORBs to have been granted the CORBA
brand in June 1999.

This package contains core libraries need for all omniORB applications.

%package idl
Summary: IDL definitions shipped with omniORB
Group:   Networking/Remote access
BuildArch: noarch
%description idl
This package contains standard IDL definitions shipped with omniORB.
You need this package if you write IDL specification which uses
standard IDL definitions.

%package docs
Summary: Documentations for omniORB
Group:   Networking/Remote access
BuildArch: noarch
%description docs
This package contains documentation for omniORB.

%package COS
Summary: ORB from AT&T (COS service stub and skel libraries)
Group:   Networking/Remote access
Requires: %name = %version-%release
%description COS
This package contains libraries, compiled from auto generated
stub and skel code for COS services.

%package utils
Summary: ORB from AT&T (utilities)
Group:   Networking/Remote access
Requires: %name = %version-%release
%description utils
This package contains utilities for omniORB.

%package names
Summary: NameService implementation for omniORB
Group:   Networking/Remote access
Requires: %name = %version-%release
Requires: %name-COS = %version-%release
%description names
This package contains standard compliant NameService implementation
for omniORB.

%setup_python_subpackage omniidl
%package -n %{packagename}
Summary: Python module for omniidl
Group:   Development/C++
%setup_std_python_package_deps
%description -n %{packagename}
This package includes python files for the omniORB package.

%package devel
Summary: development part of omniORB (core definitions and tools)
Group:   Development/C++
Requires: %name = %version-%release
Requires: %packagename = %version-%release
%description devel
This devel package includes the libraries and header files
for the omniORB package.

%package devel-COS
Summary: development part of omniORB (COS headers)
Group:   Development/C++
Requires: %name-devel = %version-%release
%description devel-COS
This devel package includes the libraries and header files
for the omniORB package (COS module). You need this package if
you write applications that uses standard services and want
share COS code.

%package devel-static
Summary: development part of omniORB (core static libraries)
Group:   Development/C++
Requires: %name-devel = %version-%release
%description devel-static
This devel package includes static libraries
for the omniORB package.

%package devel-static-COS
Summary: development part of omniORB (COS static libraries)
Group:   Development/C++
Requires: %name-devel = %version-%release
%description devel-static-COS
This devel package includes static libraries
for the omniORB package (COS module).

%prep
%setup
%patch0 -p 1
%patch1 -p 1

%build
%configure \
	--disable-thread-tracing \
	--with-openssl=%_prefix \
	--with-omniORB-config=%_sysconfdir/omniORB.cfg \
	--with-omniNames-logdir=%_logdir/omniORB

%make

%install
# hasher workaround
unset target ||:
# end

%makeinstall_std

install -d -m 755 %buildroot%_logdir/omniORB
install -d -m 755 %buildroot%_man1dir
install -d -m 755 %buildroot%_initdir

cp -a man/man1/* %buildroot%_man1dir
install -p -m 644 %SOURCE1 %buildroot%_sysconfdir
install -p -D -m 755 %SOURCE2 %buildroot%_initdir/omninames
install -p -D -m 644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/omninames

%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/* %buildroot%python_sitelibdir/
%endif

%files
%config(noreplace) %_sysconfdir/omniORB.cfg
%_libdir/libomni*.so.*

%files idl
%_datadir/idl/omniORB

%files docs
%doc doc/*.pdf

%files COS
%_libdir/libCOS*.so.*

%files utils
%_bindir/catior
%_bindir/convertior
%_bindir/genior
%_bindir/omniMapper
%_man1dir/catior*
%_man1dir/convertior*
%_man1dir/genior*

%files names
%config(noreplace) %_sysconfdir/sysconfig/omninames
%_initdir/omninames
%_bindir/omniNames
%_bindir/nameclt
%_man1dir/nameclt*
%attr(755,daemon,daemon) %dir %_logdir/omniORB

%files -n %packagename
%python_sitelibdir/*

%files devel
%_bindir/omniidl*
%_bindir/omnicpp
%_bindir/omkdepend
%_includedir/omniORB4
%_includedir/omniconfig.h
%_includedir/omnithread
%_includedir/omnithread.h
%_libdir/libomni*.so
%_libdir/pkgconfig/omniORB*
%_libdir/pkgconfig/omniDynamic*
%_libdir/pkgconfig/omnithread*
%_libdir/pkgconfig/omniConnectionMgmt*
%_man1dir/omniidl*
%_man1dir/omnicpp*

%files devel-COS
%_includedir/COS
%_libdir/libCOS*.so
%_libdir/pkgconfig/omniCOS*

%files devel-static
%_libdir/libomni*.a

%files devel-static-COS
%_libdir/libCOS*.a

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.0-alt3.1
- Rebuild with Python-2.7

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt3
- Rebuilt for debuginfo
- Set idl subpackage as noarch

* Thu Oct 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt2
- Packed missing python files
- Fixed linking of libraries

* Tue Oct 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1
- Version 4.2.0 from svn

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.4-alt2.1
- Rebuilt with python 2.6

* Wed Aug 26 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.4-alt2
- remove obsolete python = %%__python_version dependency

* Wed Aug 26 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.4-alt1
- 4.1.4

* Sat Oct 25 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.3-alt1
- 4.1.3

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 4.1.2-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Mon Feb 18 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.2-alt1
- 4.1.2

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 4.1.1-alt1.1
- Rebuilt with python-2.5.

* Fri Oct 19 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.1-alt1
- 4.1.1

* Mon Dec 04 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt12
- 4.1.0 Released

* Wed Nov 22 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt11rc2
- 4.1.0-rc2

* Tue Jun 27 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt10beta2
- Enable configure naming server address and port (/etc/sysconfig/omniNames)
- Resolve some compile warnings

* Fri May 19 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt9beta2
- 4.1.0-beta2

* Mon Mar 20 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt8beta1
- Temporarely set unresolved=relaxed

* Thu Feb 23 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt7beta1
- success build under hasher

* Tue Feb 14 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt6beta1
- Spec cleanup

* Wed Feb 08 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt5beta1
- 4.1.0-beta1

* Tue Jan 17 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt4cvs20060116
- CVS snapshot date added to packages release number

* Mon Jan 16 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt4cvs
- New CVS snapshot 2006.01.16

* Sun Jan 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt3cvs
- Build all COSS interfaces into COSS library
- Split code into more packages

* Mon Jan 02 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt2cvs
- Fix CosTime.idl TIO interface definition

* Wed Dec 21 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.1.0-alt1cvs
- 4.1.0 from CVS

* Thu Nov 24 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 4.0.6-alt1
- 4.0.6
- Build with openSSL

* Sat Mar 12 2005 Andrey Orlov <cray@altlinux.ru> 4.0.5-alt2
- setup_python_subpackage macro has been used

* Mon Feb 28 2005 Andrey Orlov <cray@altlinux.ru> 4.0.5-alt1
- 4.0.5, check python 2.4 compatibility

* Fri Oct 08 2004 Stanislav Ievlev <inger@altlinux.org> 4.0.4-alt1
- 4.0.4, remove unused sources.

* Sat Jun 26 2004 Andrey Orlov <cray@altlinux.ru> 4.0.3-alt5
- Omninames startup file added

* Fri May 28 2004 Andrey Orlov <cray@altlinux.ru> 4.0.3-alt4
- Fix lost dependences between devel & python-module-omniidl

* Wed May 26 2004 Andrey Orlov <cray@altlinux.ru> 4.0.3-alt3
- Fix for python policy compatibility

* Thu Dec 04 2003 Andrey Orlov <cray@altlinux.ru> 4.0.3-alt2
- New version from Source Forge
- Now, python23 used

* Tue Sep 30 2003 Stanislav Ievlev <inger@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Tue May 20 2003 Stanislav Ievlev <inger@altlinux.ru> 4.0.1-alt1
- 4.0.1
- remove omninames startup script (still in doc dir)
- omniORBPy in separate package now

* Fri Feb 28 2003 Stanislav Ievlev <inger@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Wed Sep 04 2002 Stanislav Ievlev <inger@altlinux.ru> 3.0.5-alt1
- 3.0.5
- build with gcc3

* Tue Feb 12 2002 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt11
- fix dirs ownerships.

* Tue Jan 29 2002 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt10
- added latest bugfix patches to omniORBpy and omniNotify
- rebuild with new python

* Fri Oct 19 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt9
- omniNotify 1.1
- latest bugfixes for omniORB and omniORBpy

* Mon Sep 10 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt8
- Applied latest bugfixes.

* Mon Jul 30 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt7
- Added omniROBpy package.
- move python files to right place.

* Thu Jul 26 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt6
- Added omniNotify service
- New package with demo stuff.

* Tue Jul 24 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt5
- Added omniEvents service.

* Fri Jul 06 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt4
- Small fixes. Buildreq and Requires on python.

* Tue Jul 03 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt3
- Changed default config and log locations.

* Mon Jul 02 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt2
- Splited bin files into main package and devel. Added config file.

* Fri Jun 29 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.4-alt1
- 3.0.4

* Wed Jun 27 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.3-alt3
- Rebuilt with python-2.1

* Wed May 16 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.3-alt2
- Rename ols to o_ls to avoid conflicts with speach_*

* Wed Apr 25 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.3-alt1
- Initial release for ALT Linux

