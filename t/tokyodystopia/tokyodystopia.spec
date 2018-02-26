%def_disable debug
%def_disable devel
%def_disable profile
%def_enable shared
%def_enable static
%def_enable zlib
%def_disable check
#----------------------------------------------------------------------

%define Name Tokyo Dystopia
Name: tokyodystopia
%define lname lib%name
Summary: A full-text search system for Tokyo Cabinet
Version: 0.9.13
Release: alt2
License: %lgpl2plus
Group: Databases
URL: http://tokyocabinet.sourceforge.net/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libtokyocabinet-devel bzlib-devel
%{?_enable_zlib:BuildRequires: zlib-devel}

%description
%Name is a full-text search system for Tokyo Cabinet.


%package utils
Summary: Command line tools for managing %Name
Group: Databases
Requires: %lname = %version-%release

%description utils
%Name is a full-text search system for Tokyo Cabinet.
This package contains command line tools for managing %Name.


%if_enabled shared
%package -n %lname
Summary: %Name library
Group: System/Libraries

%description -n %lname
%Name is a full-text search system for Tokyo Cabinet.
This package contains %Name sharerd library.
%endif


%package -n %lname-devel
Summary: Headers for developing programs that will use %lname
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
%Name is a full-text search system for Tokyo Cabinet.
This package contains the libraries and header files needed for
developing with %lname.


%if_enabled static
%package -n %lname-devel-static
Summary: Static version of %Name database library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%Name is a full-text search system for Tokyo Cabinet.
This package contains static libraries for building statically linked
programs which use %Name.
%endif


%package doc
Summary: Documentation for %Name
Group: Documentation
BuildArch: noarch

%description doc
%Name is a full-text search system for Tokyo Cabinet.
This package contains documentation for developers.


%prep
%setup
%patch -p1


%build
%define _optlevel 3
%autoreconf
%configure \
    %{subst_enable debug} \
    %{subst_enable devel} \
    %{subst_enable profile} \
    %{subst_enable shared} \
    %{subst_enable zlib}
%make_build
%{?_enable_check:%make_build check}


%install
%make_install DESTDIR=%buildroot install
rm -f %buildroot%_datadir/%name/COPYING
install -d -m 0755 %buildroot%_docdir
mv %buildroot{%_datadir/%name,%_docdir/%name-%version}


%files utils
%_bindir/*
%_libexecdir/*.cgi
%_man1dir/*


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_includedir/*
%{?_enable_shared:%_libdir/*.so}
%_pkgconfigdir/*
%_man3dir/*


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%files doc
%_docdir/%name-%version


%changelog
* Wed Nov 11 2009 Led <led@altlinux.ru> 0.9.13-alt2
- rebuild with libtokyocabinet.so.9

* Sat Jul 11 2009 Led <led@altlinux.ru> 0.9.13-alt1
- 0.9.13:
  + performance was improved

* Tue Jun 16 2009 Led <led@altlinux.ru> 0.9.12-alt1
- 0.9.12:
  + new functions: sysprint
- fixed URL

* Sun Apr 26 2009 Led <led@altlinux.ru> 0.9.11-alt1
- 0.9.11

* Wed Mar 11 2009 Led <led@altlinux.ru> 0.9.9-alt2
- rebuild with libtokyocabinet.so.8

* Wed Jan 07 2009 Led <led@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Mon Dec 15 2008 Led <led@altlinux.ru> 0.9.8-alt3
- rebuild with libtokyocabinet.so.7

* Mon Dec 15 2008 Led <led@altlinux.ru> 0.9.8-alt2
- cleaned up spec

* Thu Oct 30 2008 Led <led@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Tue Sep 09 2008 Led <led@altlinux.ru> 0.9.5-alt3
- rebuild with libtokyocabinet.so.5

* Wed Aug 13 2008 Led <led@altlinux.ru> 0.9.5-alt2
- fixed spec

* Wed Jul 30 2008 Led <led@altlinux.ru> 0.9.5-alt1
- initial build
