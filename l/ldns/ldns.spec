Name: ldns
Version: 1.6.13
Release: alt1
License: BSD
Url: http://www.nlnetlabs.nl/%name/
Source: %name-%version.tar
Group: System/Libraries
Summary: Lowlevel DNS(SEC) library with API
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

%define with_python 1

BuildRequires: gcc-c++ libssl-devel doxygen perl libpcap-devel
%if %with_python
BuildRequires:  python-devel, swig
%endif

%description
ldns is a library with the aim to simplify DNS programing in C. All
lowlevel DNS/DNSSEC operations are supported. We also define a higher
level API which allows a programmer to (for instance) create or sign
packets.

%package -n drill
Summary: Drill  is a tool to designed to get all sorts of information out of the DNS
Group: Networking/DNS

%description -n drill
Drill  is a tool to designed to get all sorts of information out of the DNS. 
It is specificly designed to be used with DNSSEC

The name drill is a pun on dig. With drill you should be able get  even
more information than with dig.

%package -n lib%name
Summary: Lowlevel DNS(SEC) library with API
Group: System/Libraries
Provides: %name = %version-%release

%description -n lib%name
libldns is a library with the aim to simplify DNS programing in C. All
lowlevel DNS/DNSSEC operations are supported. We also define a higher
level API which allows a programmer to (for instance) create or sign
packets.

%package -n lib%name-devel-static
Summary: Lowlevel DNS(SEC) static library with API
Group: System/Libraries

%description -n lib%name-devel-static
libldns is a static library with the aim to simplify DNS programing in C. 
All lowlevel DNS/DNSSEC operations are supported. We also define a higher
level API which allows a programmer to (for instance) create or sign
packets.

%package -n lib%name-devel
Summary: Development package that includes the ldns header files
Group: Development/C
Requires: lib%name = %version-%release libssl-devel

%description -n lib%name-devel
The devel package contains the ldns library and the include files

%package -n lib%name-examples
Summary: Examples for library
Group: Development/C

%description -n lib%name-examples
Examples for library

%if %with_python
%package -n python-module-%name
Summary: Python extensions for ldns
Group: Development/Python

%description -n python-module-%name
Python extensions for ldns
%endif

%prep
%setup

%build
%autoreconf
%configure --disable-rpath --with-drill --with-examples \
%if %with_python
	--with-pyldns
%endif

%make_build
%make  doc

%install
%make DESTDIR=%buildroot install
%make DESTDIR=%buildroot install-doc


# don't package building script in doc
rm doc/doxyparse.pl
#remove doc stubs
rm -rf doc/.svn
#remove double set of man pages
rm -rf doc/man
# remove .la files
rm -rf %buildroot%python_sitelibdir/*.la

install -pD -m644 packaging/libldns.pc %buildroot%_pkgconfigdir/libldns.pc
install -pD -m644 libdns.vim %buildroot%_sysconfdir/vim/libldns

%check
#make test

%files -n drill
%_bindir/drill
%_mandir/man1/drill*

%files -n lib%name
%_libdir/libldns*.so.*
%doc README LICENSE

%files -n lib%name-devel-static
%_libdir/libldns.a

%files -n lib%name-devel
%_bindir/ldns-config
%_man1dir/ldns-config*
%_includedir/ldns
%_pkgconfigdir/*
%_libdir/libldns*so
%doc doc Changelog README
%_man3dir/*
%_sysconfdir/vim/*

%files -n lib%name-examples
%_bindir/ldns-*
%_bindir/ldnsd
%_man1dir/ldns-*
%_man1dir/ldnsd*

%exclude %_bindir/ldns-config
%exclude %_man1dir/ldns-config*


%if %with_python
%files -n python-module-%name
%python_sitelibdir/*
%endif

%changelog
* Mon May 21 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.13-alt1
- 1.6.13

* Fri Feb 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.12-alt1
- 1.6.12

* Thu Sep 29 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.11-alt1
- 1.6.11
- enable sha2
- add python module
- add ldns-config and libldns.pc
- add /etc/vim/libldns
- gzip mans

* Sun Jul 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.10-alt1
- 1.6.10

* Thu Mar 31 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.9-alt1
- 1.6.9
- disable tests

* Thu Feb 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.8-alt1
- 1.6.8

* Sat Nov 13 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.7-alt1
- 1.6.7

* Tue Oct 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.6-alt2
- Rebuild with new libcrypt

* Fri Aug 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.6-alt1
- 1.6.6

* Tue Jun 22 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.5-alt1
- 1.6.5

* Wed Feb 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.4-alt1
- 1.6.4

* Mon Dec 14 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.3-alt1
- 1.6.3

* Tue Nov 17 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.2-alt1
- 1.6.2

* Sat Aug 15 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.1-alt2
- Rename lib%name-static to lib%name-devel-static
- Move links to libs to devel package

* Sat Aug 15 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.1-alt1
- 1.6.1

* Mon May 11 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.5.1-alt2
- Update spec for fix build with new toolchain

* Thu Mar 26 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.0_pre_20080715-alt1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Thu Aug 07 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.3.0_pre_20080715-alt1
- New version

* Sun May 25 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.3.0_pre_20080229-alt1
- New version

* Sun May 25 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.2.2-alt1
- Build for ALT
