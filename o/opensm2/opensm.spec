%def_enable shared
%def_enable static

%define Name OpenSM
%define oname opensm
Name: opensm2
%define lname lib%name
Summary: InfiniBand subnet manager and administration
Version: 3.3.7
Release: alt2
License: %gpl2only
Group: Networking/Other
URL: http://openib.org
# git://git.openfabrics.org/~sashak/management.git
Source0: %name-%version.tar.gz
Source1: %oname.init
Requires: libibumad >= 1.1.7
Requires: %lname = %version-%release
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
Provides: %oname = %version-%release
Obsoletes: %oname < %version-%release
Conflicts: %oname < %version-%release
Conflicts: %oname > %version-%release

BuildRequires(pre): rpm-build-licenses
BuildRequires: flex libibumad-devel >= 1.2.0

%description
%Name provides an implementation of an InfiniBand Subnet Manager and
Administration. Such a software entity is required to run for in order
to initialize the InfiniBand hardware (at least one per each InfiniBand
subnet).


%package -n %lname
Summary: Libraries from the %name package
Group: System/Libraries
Provides: lib%oname = %version-%release
Obsoletes: lib%oname < %version-%release
Conflicts: lib%oname < %version-%release
Conflicts: lib%oname > %version-%release

%description -n %lname
Shared libraries that are part of the %name package but are also used
by other applications. If you don't need %name itself installed, these
libraries can be installed to satisfy dependencies of other
applications.


%package -n lib%oname-devel
Summary: Development files for %Name
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release
Requires: libibumad-devel
Provides: %name-devel = %version-%release
Obsoletes: %name-devel
Obsoletes: lib%oname-devel < %version-%release
Conflicts: lib%oname-devel < %version-%release
Conflicts: lib%oname-devel > %version-%release

%description -n lib%oname-devel
Development files for %Name.


%if_enabled static
%package -n lib%oname-devel-static
Summary: Static %Name libraries
Group: Development/C
Requires: lib%oname-devel = %version-%release libibumad-devel-static

%description -n lib%oname-devel-static
Static %Name libraries.
%endif


%prep
%setup


%build
./autogen.sh
%add_optflags %optflags_shared
%configure %{subst_enable shared} %{subst_enable static}
%make_build

rm -f $(find ./ -name 'libosmvendor.la*')
%make_build ADD_OPENSM="-L$PWD/opensm -lopensm -L$PWD/opensm/.libs"
rm -f $(find ./ -name 'libopensm.la*')
%make_build ADD_VENDOR="-L$PWD/libvendor -losmvendor -L$PWD/libvendor/.libs"

%install
%make_install DESTDIR=%buildroot install
install -D -m 0755 %SOURCE1 %buildroot/%_initdir/%oname
install -d -m 0755 %buildroot%_sysconfdir/sysconfig
cat > %buildroot/%_sysconfdir/sysconfig/%oname <<__CONF__
OSM_ARGS=
OSM_HOSTS=
__CONF__


%post 
%post_service %oname

%preun
%preun_service %oname


%files
%doc AUTHORS COPYING README
%config(noreplace) %_sysconfdir/sysconfig/%oname
%_initdir/*
%_sbindir/*
%_man8dir/*


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n lib%oname-devel
%_includedir/infiniband/*
%{?_enable_shared:%_libdir/*.so}


%if_enabled static
%files -n lib%oname-devel-static
%_libdir/*.a
%endif


%changelog
* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.7-alt2
- Rebuilt for debuginfo

* Tue Dec 07 2010 Andriy Stepanov <stanv@altlinux.ru> 3.3.7-alt1
- New version

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.6-alt2
- Rebuilt for soname set-versions
- Fixed underlinking of libraries

* Thu Sep 02 2010 Andriy Stepanov <stanv@altlinux.ru> 3.3.6-alt1
- New version

* Wed Sep 01 2010 Andriy Stepanov <stanv@altlinux.ru> 3.3.5-alt2
- Rebuild with new libibumad

* Wed Aug 18 2010 Andriy Stepanov <stanv@altlinux.ru> 3.3.5-alt1
- 3.3.5 (OFED 1.5.1)

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt3
- Rebuild from upstream git repository
- Fixed libraries linking

* Mon Jun 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt2
- Rename opensm -> opensm2

* Tue May 26 2009 Led <led@altlinux.ru> 3.3.2-alt1
- 3.3.2

* Tue May 26 2009 Led <led@altlinux.ru> 3.2.6-alt1
- 3.2.6

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.5_20081207-alt3
- Rebuild with automake 1.11

* Wed May 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.5_20081207-alt2
- Rebuild with gcc4.4

* Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.5_20081207-alt1
- Version 3.2.5_20081207

* Wed Oct 29 2008 Led <led@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 3.1.11-alt1
- OFED-1.3.1

* Fri Feb 22 2008 Stanislav Ievlev <inger@altlinux.org> 3.0.3-alt3
- add init.d script

* Mon Aug 27 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.3-alt2
- turn on devel part

* Tue Aug 21 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.3-alt1
- Initial build
