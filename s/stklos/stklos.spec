Name: stklos
Version: 0.98
Release: alt3
License: GPL
Group: Development/Scheme
Summary: STklos is a free Scheme System

Packager: Alexey Voinov <voins@altlinux.ru>

Url: http://www.stklos.org
Source: %name-%version.tar

BuildRequires: /proc
# Automatically added by buildreq on Wed Aug 15 2007
BuildRequires: gtk+-devel libgc-devel libgmp-devel libldap-devel libpcre-devel

%description
STklos is a free Scheme System (nearly) conform to R5RS. The aim of this
implementation is to be fast as well as light. The implementation is based
on an ad-hoc Virtual Machine. STklos can also be compiled as a library, so
that one can easily embed it in an application.

%package lib
Summary: Scheme library for STklos
Group: Development/Scheme
Requires: %name = %version-%release
BuildArch: noarch

%description lib
STklos is a free Scheme System (nearly) conform to R5RS. The aim of this
implementation is to be fast as well as light. The implementation is based
on an ad-hoc Virtual Machine. STklos can also be compiled as a library, so
that one can easily embed it in an application.

This package contains STklos scheme library files.

%package docs
Summary: Manual for STklos
Group: Development/Documentation
Requires: %name = %version-%release
BuildArch: noarch

%description docs
STklos is a free Scheme System (nearly) conform to R5RS. The aim of this
implementation is to be fast as well as light. The implementation is based
on an ad-hoc Virtual Machine. STklos can also be compiled as a library, so
that one can easily embed it in an application.

This package contains STklos manual.

%prep
%setup -q

%build
%autoreconf
%configure --enable-ldap --disable-gnome
make

%install
%makeinstall
rm -rf $RPM_BUILD_ROOT/%_datadir/doc/%name-%version

%files
%_bindir/*
%_man1dir/*
%dir %_includedir/%name/
%_includedir/%name/*
%dir %_libdir/%name/
%_libdir/%name/*

%files lib
%dir %_datadir/%name
%_datadir/%name/*

%files docs
%doc AUTHORS ChangeLog PACKAGES-USED PORTING-NOTES README SUPPORTED-SRFIS
%doc TODO NEWS doc/html

%changelog
* Sat Sep 19 2009 Alexey Voinov <voins@altlinux.ru> 0.98-alt3
- fixed ownership of /usr/include,lib}/stklos

* Sat Sep 19 2009 Alexey Voinov <voins@altlinux.ru> 0.98-alt2
- safer stklos-ext-install script (not much really)
- docs and lib noarch subpackages created
- rebuilt with libldap2.4

* Thu Jul 24 2008 Alexey Voinov <voins@altlinux.ru> 0.98-alt1
- new version (0.98)
- cinvoke patch removed

* Mon Dec 17 2007 Alexey Voinov <voins@altlinux.ru> 0.97-alt1
- new version (0.97)

* Wed Aug 15 2007 Alexey Voinov <voins@altlinux.ru> 0.96-alt1
- new version (0.96)
- url updated
- cinvoke patch
- buildreqs updated

* Sun Dec 31 2006 Alexey Voinov <voins@altlinux.ru> 0.82-alt1
- new version (0.82)
- ldap support re-enabled
- x86-64 build fixed

* Thu Dec 07 2006 Alexey Voinov <voins@altlinux.ru> 0.81-alt1
- new version (0.81)
- ldap support disabled because of TEXTREL.

* Sun Oct 08 2006 Alexey Voinov <voins@altlinux.ru> 0.72-alt1
- new version 0.72

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.71-alt1.1
- Rebuilt with libldap-2.3.so.0.

* Fri Nov 04 2005 Alexey Voinov <voins@altlinux.ru> 0.71-alt1
- new version (0.71)

* Wed Jun 01 2005 Alexey Voinov <voins@altlinux.ru> 0.70-alt1
- new version (0.70)

* Wed Apr 06 2005 Alexey Voinov <voins@altlinux.ru> 0.61-alt1
- new version (0.61)
- pcre patch added
- buildreqs updated

* Fri Mar 18 2005 Alexey Voinov <voins@altlinux.ru> 0.60-alt1
- new version (0.60)
- .texinfo patch removed
- docs in info format disappeared
- buildreqs updated

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.58-alt1.1
- Rebuilt with openldap-2.2.18-alt3.

* Tue Aug 03 2004 Alexey Voinov <voins@altlinux.ru> 0.58-alt1
- new version (0.58)

* Sun Jan 18 2004 Ott Alex <ott@altlinux.ru> 0.57-alt1
- New version. various fixes and additions

* Mon Nov 17 2003 Ott Alex <ott@altlinux.ru> 0.56-alt1
- New release

* Sat Jun 28 2003 Alex Ott <ott@altlinux.ru> 0.55-alt1
- First build for ALTLinux


