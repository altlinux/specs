Name:    libofx
Version: 0.9.4
Release: alt2.1

Summary: The OFX parser library
Group:   System/Libraries
License: GPLv2

Packager: Andrey Cherepanov <cas@altlinux.ru> 
URL:      http://libofx.sourceforge.net
Source:   http://download.sourceforge.net/libofx/%name-%version.tar.gz

BuildRequires: libOpenSP-devel gcc-c++ libcurl-devel

%description
This is the LibOFX library.  It is a API designed to allow applications
to very easily support OFX command responses, usually provided by
financial institutions. See http://www.ofx.net/ for details
and specification.

%package devel
Summary: The OFX parser development library
Group: Development/C++
Requires: %name = %version-%release
Provides: %name-docs = %version-%release
Obsoletes: %name-docs

%description devel
This is the LibOFX library.  It is a API designed to allow applications
to very easily support OFX command responses, usually provided
by financial institutions.  See http://www.ofx.net/ for details
and specification. LibOFX is based on the excellent OpenSP library
written by James Clark, and now part of the OpenJADE
http://openjade.sourceforge.net/ project.  OpenSP by itself is not
widely distributed.  OpenJADE 1.3.1 includes a version on OpenSP that
will link, however, it has some major problems with LibOFX and isn't
recommended. Since LibOFX uses the generic interface to OpenSP, it
should be compatible with all recent versions of OpenSP (It has been
developed with OpenSP-1.5pre5). LibOFX is written in C++, but provides
a C style interface usable transparently from both C and C++ using
a single include file.

Headers, documentation and other files for development with libofx.

%prep
%setup -q

%build
%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.a

%files
%_bindir/*
%_libdir/*.so.*
%_datadir/%name
%_man1dir/ofxdump.1.gz

%files devel
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README totest.txt
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/%name.pc
%dir %_docdir/%name 
%_docdir/%name/* 

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt2.1
- Removed bad RPATH

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt2
- Move libofx-docs to libofx-devel

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1
- New version 0.9.4

* Wed Nov 10 2010 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt3
- rebuld

* Tue Nov 25 2008 Andrey Cherepanov <cas@altlinux.ru> 0.9.0-alt2
- fixed build for gcc4.3 

* Thu Sep 25 2008 Lebedev Sergey <barabashka@altlinux.org> 0.9.0-alt1
- new version 0.9.0

* Wed Feb 14 2007 Igor Muratov <migor@altlinux.org> 0.8.3-alt1
- new version

* Tue Jun 20 2006 Igor Muratov <migor@altlinux.org> 0.8.0-alt4
- Rebuild with new OpenSP

* Mon Apr 03 2006 Igor Muratov <migor@altlinux.org> 0.8.0-alt3
- Build with gcc4

* Tue Jan 10 2006 Igor Muratov <migor@altlinux.org> 0.8.0-alt2
- patch for makefiles

* Mon Aug 22 2005 Igor Muratov <migor@altlinux.org> 0.8.0-alt1
- new version

* Mon Jan 17 2005 Igor Muratov <migor@altlinux.org> 0.7.0-alt3
- Spec cleanup

* Mon Jan 10 2005 Igor Muratov <migor@altlinux.org> 0.7.0-alt2
- Split packet

* Sun Jan  2 2005 Igor Muratov <migor@altlinux.org> 0.7.0-alt1
- Initial build for ALT

* Sat Nov 23 2002 Chris Lyttle <chris@wilddev.net>
- Created spec file
