%def_disable docs
%define develname libdbi-devel

Name: libdbi
Version: 1.0
Release: alt1.cvs20092729.3

Summary: Database Independent Abstraction Layer for C
License: LGPL
Group: System/Libraries

Url: http://libdbi.sourceforge.net/
Source: %name-%version.tar.gz
Packager: Boris Savelev <boris@altlinux.org>

# Automatically added by buildreq on Mon Feb 09 2009
BuildRequires: gcc-c++

%if_enabled docs
BuildRequires: docbook-style-dsssl openjade w3c-markup-validator-libs
%endif

%description
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

%package -n %develname
Summary: Library and header files for the %name library
Group: Development/C
Requires: %name = %version-%release

%description -n %develname
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This package contains the header files.

%package -n %develname-static
Summary: Statis library for the %name library
Group: Development/C
Requires: %develname = %version-%release

%description -n %develname-static
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This package contains the static library.

%prep
%setup
%if_enabled docs
touch doc/libdbi-versioning.sgml
%endif
%ifarch e2k
sed -i 's,-O20,-O2,g' configure*
%endif

%build
%autoreconf
%configure %{subst_enable docs}
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog INSTALL README
%_libdir/*.so.*

%files -n %develname
%doc README TODO
%if_enabled docs
%doc doc/programmers-guide doc/driver-guide doc/*.pdf
%endif
%_includedir/dbi
%_libdir/*.so
%_pkgconfigdir/dbi.pc

%files -n %develname-static
%_libdir/*.a

%changelog
* Wed Feb 22 2017 Michael Shigorin <mike@altlinux.org> 1.0-alt1.cvs20092729.3
- BOOTSTRAP: introduced docs knob (leave off by default)
- E2K: "-O20" is a bit too much!

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.cvs20092729.2
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.cvs20092729.1
- Rebuilt for soname set-versions

* Wed Apr 29 2009 Boris Savelev <boris@altlinux.org> 1.0-alt1.cvs20092729
- build from CVS
- disable doc build
- add static lib

* Mon Feb 09 2009 Boris Savelev <boris@altlinux.org> 0.8.3-alt1
- initial build for Sisyphus from Mandriva

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-2mdv2009.0
+ Revision: 233726
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Feb 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-1mdv2008.1
+ Revision: 169619
- fix build deps (docbook-dtd41-sgml)
- fix build deps (docbook-style-dsssl)
- fix deps
- 0.8.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-1mdv2008.0
+ Revision: 81033
- 0.8.2

* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdv2007.0
+ Revision: 93762
- Import libdbi

* Wed Aug 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdk
- 0.8.1

* Fri Sep 02 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-1mdk
- 0.8.0

* Wed May 11 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-3mdk
- rpmlint fixes

* Thu Apr 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-2mdk
- rebuilt against new postgresql libs

* Fri Jun 18 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.7.2-1mdk
- 0.7.2

