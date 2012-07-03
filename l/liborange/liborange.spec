%def_disable static
%def_without ole2
%def_with libgsf
%def_enable msi
%def_enable inno
%def_enable vise

Name: liborange
Version: 0.4
Release: alt2

Summary: A library to squeeze out installable Microsoft cabinet files
License: MIT
Group: Archiving/Compression

Url: http://synce.sourceforge.net
Source: %name-%version.tar.gz
Packager: Mobile Development Team <mobile@packages.altlinux.org>

BuildPreReq: libsynce-devel >= 0.9.1
BuildPreReq: libdynamite-devel >= 0.1
BuildPreReq: libunshield-devel >= 0.5
%{?_with_ole2:BuildPreReq: libole2-devel >= 0.2.4}
%{?_with_libgsf:BuildPreReq:libgsf-devel}

BuildRequires: gcc-c++ zlib-devel

%description
See %url for more information.

%package devel
Summary: Headers for library to squeeze out installable Microsoft cabinet files
Group: Development/C
Requires: %name = %version

%description devel
Headers for library to squeeze out
installable Microsoft cabinet files.

%if_enabled static
%package devel-static
Summary: Static library to squeeze out installable Microsoft cabinet files
Group: Development/C
Requires: %name-devel = %version

%description devel-static
Headers for library to squeeze out
installable Microsoft cabinet files.
%endif

%prep
%setup

%build
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' configure
%configure \
	%{subst_enable static} \
	%{subst_with libole2} \
	%{subst_with libgsf} \
	%{subst_enable msi} \
	%{subst_enable inno} \
	%{subst_enable vise}

%make

%install
%makeinstall_std

%files
%doc LICENSE
%_bindir/orange
%_libdir/liborange.so.*
%_man1dir/*

%files devel
%_includedir/liborange.h
%_includedir/liborange_stub.h
%_libdir/liborange.so
%_libdir/pkgconfig/*.pc

%if_enabled static
%files devel-static
%_libdir/liborange.a
%endif

%changelog
* Thu Jan 19 2012 Michael Shigorin <mike@altlinux.org> 0.4-alt2
- drop RPATH
- minor spec cleanup

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Aug 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt1
- 0.4
- remove obsoleted pre/post scripts

* Sat Oct 04 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt1
- 0.3.2
- build with msi, inno, vise support

* Fri Jan 04 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.3-alt3
- fix build

* Sat Dec 08 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.3-alt2
- update to SVN 20071207 version

* Sun Jul 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.3-alt1
- 0.3

* Fri Sep 03 2004 Michael Shigorin <mike@altlinux.ru> 0.2-alt1
- built for ALT Linux (synce-kde dependency)

