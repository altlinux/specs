%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libdotconf
Version: 1.3
Release: alt2
Summary: configuration file parser
License: %lgpl2only
Group: System/Libraries
URL: git://github.com/williamh/dotconf.git

BuildRequires: glibc-devel-static rpm-build-licenses

Source: dotconf-%version.tar

%description
dotconf is a configuration file parser.

%package devel
Summary: Development files for dotconf library
Group: Development/C

%description devel
Development files for dotconf library

%prep
%setup -q -n dotconf-%version

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%_libdir/libdotconf*.so.*

%files devel
%_libdir/libdotconf.so
%_includedir/dotconf.h
%_pkgconfigdir/*
%_defaultdocdir/dotconf

%changelog
* Thu Oct 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt2
- Fixed build with LTO

* Fri May 10 2013 Michael Pozhidaev <msp@altlinux.ru> 1.3-alt1
- New version 1.3
- devel-static subpackage is removed
- libpool-devel-static subpackage is removed (no more in original distribution)

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.13-alt2.qa3
- NMU: rebuilt for debuginfo.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt2.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.13-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libdotconf
  * postun_ldconfig for libdotconf
  * postclean-05-filetriggers for spec file

* Sun Sep 14 2008 Michael Pozhidaev <msp@altlinux.ru> 1.0.13-alt2
- Fixed bug in m4 script

* Sun Sep 07 2008 Michael Pozhidaev <msp@altlinux.ru> 1.0.13-alt1
- ALT Linux package

* Fri Apr 05 2002 Mike Javorski <mike_javorski@bigfoot.com>
- Fixed inclusion of .so files

* Mon Dec 24 2001 Benjamin Lee <benjamin.lee@dotwap.com>
- initial release of dotconf rpm package.
