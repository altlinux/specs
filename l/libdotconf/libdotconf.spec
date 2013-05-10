
Name: libdotconf
Version: 1.3
Release: alt1
Summary: configuration file parser
License: %lgpl2only
Packager: Michael Pozhidaev <msp@altlinux.ru>
Group: System/Libraries
URL: git://github.com/williamh/dotconf.git

BuildRequires: glibc-devel-static rpm-build-licenses

Source: dotconf-%version.tar.gz

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
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR='%buildroot' install

%files
#%defattr(-,root,root)
%doc AUTHORS COPYING README 
%_libdir/libdotconf*.so.*

%files devel
%_libdir/libdotconf.so
%_includedir/dotconf.h
%_pkgconfigdir/*
/usr/share/doc/dotconf

%changelog
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
