Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%define libbuild 2
%define svnrev 505

%def_with utils
%def_enable shared
%def_enable static
#----------------------------------------------------------------------

%define Name NUT
Name: libnut
Version: 0.0
%define rel 1
%ifdef svnrev
Release: alt0.%svnrev.%rel.1
Source: %name-svn-r%svnrev.tar.bz2
%else
Release: alt%rel.1
Source: %name-%version.tar.bz2
%endif
Patch0: %name-svn-r505-makefile.patch
Patch1: %name-svn-r505-soname.patch
Summary: %Name open container format
URL: http://www.nut.hu
# svn checkout svn://svn.mplayerhq.hu/nut/trunk/libnut
License: MIT/X
Group: System/Libraries


%description
%Name is a container format under construction by MPlayer and FFmpeg
developers. Its main goals are to be simple to implement and parse,
easy to seek to precise position without unnecessary reads, even on
partial files, error resistant, and with the lowest possible overhead.

This package includes the shared library needed to run %name-based
software.


%if_with utils
%package utils
Group: Video
Summary: %Name utils
Provides: nut-utils = %version-%release
Obsoletes: nut-utils

%description utils
%Name is a container format under construction by MPlayer and FFmpeg
developers. Its main goals are to be simple to implement and parse,
easy to seek to precise position without unnecessary reads, even on
partial files, error resistant, and with the lowest possible overhead.

This package includes %name encoder utils.
%endif


%package devel
Summary: Development files of %Name library
Group: Development/C
Requires: %name%{?_disable_shared:-devel-static} = %version-%release

%description devel
%Name is a container format under construction by MPlayer and FFmpeg
developers. Its main goals are to be simple to implement and parse,
easy to seek to precise position without unnecessary reads, even on
partial files, error resistant, and with the lowest possible overhead.

This package includes the header files needed to develop %name-based
software.


%if_enabled static
%package devel-static
Summary: Static %Name library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
%Name is a container format under construction by MPlayer and FFmpeg
developers. Its main goals are to be simple to implement and parse,
easy to seek to precise position without unnecessary reads, even on
partial files, error resistant, and with the lowest possible overhead.

This package includes the static library needed to develop
%name-based software.
%endif


%prep
%setup -q%{?svnrev: -n %name-svn-r%svnrev}
%patch0 -p1
%patch1 -p1


%build
%define _optlevel s
%add_optflags %optflags_shared
%make_build -C %name CFLAGS="%optflags" PREFIX=%prefix libdir=%_libdir %{?_enable_shared:%name.so} %{?_enable_static:%name.a}
%{?_with_utils:%make_build -C nututils CFLAGS="%optflags" PREFIX=%prefix libdir=%_libdir}


%install
%make_install DESTDIR=%buildroot PREFIX=%prefix libdir=%_libdir install
%if_with utils
install -d -m 0755 %buildroot%_bindir
install -m 0755 nututils/{nut{index,merge},avireader} %buildroot%_bindir/
%endif


%if_enabled shared
%files
%_libdir/*.so.*
%endif


%if_with utils
%files utils
%doc README
%_bindir/*
%endif


%files devel
%doc docs/*.txt
%_includedir/*
%{?_enable_shared:%_libdir/*.so}


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.0-alt0.505.1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libnut
  * postun_ldconfig for libnut

* Fri Aug 17 2007 Led <led@altlinux.ru> 0.0-alt0.505.1
- new SVN revision (505)
- fixed License
- updated %name-svn-r505-soname.patch
- added %name-svn-r505-makefile.patch
- added nutparse to %name-utils

* Mon Mar 12 2007 Led <led@altlinux.ru> 0.0-alt0.282.2
- added %name-svn-r282-soname.patch
- enabled build shared lib

* Mon Mar 12 2007 Led <led@altlinux.ru> 0.0-alt0.282.1
- new SVN revision (282)

* Wed Jan 31 2007 Led <led@altlinux.ru> 0.0-alt0.279.1
- new SVN revision (279)

* Mon Jan 29 2007 Led <led@altlinux.ru> 0.0-alt0.276.1
- new SVN revision (276)

* Mon Dec 25 2006 Led <led@altlinux.ru> 0.0-alt0.274.1
- new SVN revision (274)

* Mon Nov 27 2006 Led <led@altlinux.ru> 0.0-alt0.266.1
- new SVN revision (266)

* Thu Nov 21 2006 Led <led@altlinux.ru> 0.0-alt0.258.1
- new SVN revision (258)
- fixed %%install (for x86_64)

* Mon Nov 20 2006 Led <led@altlinux.ru> 0.0-alt0.255.1
- new SVN revision (255)
- renamed package nut-utils to %name-utils

* Fri Nov 17 2006 Led <led@altlinux.ru> 0.0-alt0.223.1
- new SVN revision (223)
- fixed %%install

* Mon Nov 13 2006 Led <led@altlinux.ru> 0.0-alt0.200.1
- new SVN revision (200)

* Fri Nov 10 2006 Led <led@altlinux.ru> 0.0-alt0.198.1
- new SVN revision (198)

* Thu Oct 19 2006 Led <led@altlinux.ru> 0.0-alt0.158.1
- initial build
