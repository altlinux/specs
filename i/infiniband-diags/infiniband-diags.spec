Summary: OpenFabrics InfiniBand Diagnostic Tools

Name: infiniband-diags
Version: 1.5.7
Release: alt2

# old names
Provides: openib-diags = %version
Obsoletes: openib-diags

License: GPL/BSD

Group: System/Base

# git://git.openfabrics.org/~sashak/management.git
Source: %name-%version.tar.gz
Packager: Timur Aitov <timonbl4@altlinux.org>

Url: http://openib.org/

BuildPreReq: libibmad-devel >= 1.3.6
BuildPreReq: libopensm-devel >= 3.3.7
Requires: lib%name = %version-%release
Requires: libibmad >= 1.3.6 libopensm >= 3.3.7

%description
This package provides IB diagnostic programs and scripts needed to
diagnose an IB subnet.

%package -n lib%name
Summary: Shared libraries for IB diagnostic programs
Group: System/Libraries

%description -n lib%name
This package contains shared libraries for IB diagnostic programs.

%package -n lib%name-devel
Summary: Development files for IB diagnostic programs
Group: Development/C
Requires: lib%name = %version-%release
Requires: libibcommon-devel >= 1.2.0

%description -n lib%name-devel
This package contains development files for IB diagnostic programs.

%package -n lib%name-devel-static
Summary: Static library for IB diagnostic programs
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static library for IB diagnostic programs.

%prep
%setup

%build
./autogen.sh
%configure  \
    --with-perl-installdir=%perl_vendor_privlib
#sed -i -e '1a\echo=echo' libtool
%make_build
bzip2 --best --keep --force ChangeLog

%install
%makeinstall_std

%files
%doc README ChangeLog.*
%perl_vendor_privlib/*.pm
%_sbindir/*
%_man8dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/infiniband/*
%_man3dir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.7-alt2
- Rebuilt for debuginfo

* Mon Dec 20 2010 Timur Aitov <timonbl4@altlinux.org> 1.5.7-alt1
- New version

* Tue Aug 31 2010 Andriy Stepanov <stanv@altlinux.ru> 1.5.6-alt1
- New version

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt2.1
- Added build requirement on libibcommon-devel

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt2
- Rebuild from upstream git repository

* Tue Jun 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1
- Version 1.5.2

* Thu May 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4_20081207-alt2
- Rebuild with gcc 4.4
- Disable -no-as-needed

* Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4_20081207-alt1
- Version 1.4.4_20081207

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.6-alt1
- OFED 1.3.1

* Fri Feb 22 2008 Stanislav Ievlev <inger@altlinux.org> 1.2.7-alt2
- fix /usr/local in scripts

* Mon Aug 27 2007 Stanislav Ievlev <inger@altlinux.org> 1.2.7-alt1
- Initial build
