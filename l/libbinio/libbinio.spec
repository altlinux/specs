# stalled, check 14.01.2009
Name: libbinio
Version: 1.4
Release: alt3.qa1

Summary: Binary I/O stream class library

License: LGPL
Group: System/Libraries
Url: http://libbinio.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/libbinio/%name-%version.tar.bz2
Patch0: %name-infopage.patch
Patch1: %name.patch

# Automatically added by buildreq on Sun Jan 14 2007
BuildRequires: gcc-c++

%description
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++. The library is hardware
independent in the form that it transparently converts between the
different forms of machine-internal binary data representation. It
further employs no special I/O protocol and can be used on arbitrary
binary data sources.

%package devel
Summary: Header files for libbinio library
Group: Development/C++
Requires: %name = %version-%release

%description devel
Header files for libbinio library.

%package static
Summary: Static libbinio library
Group: Development/Other
Requires: %name-devel = %version-%release

%description static
Static libbinio library.

%prep
%setup -q
%patch0 -p1
%patch1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_infodir/%name.info.*

#%files static
#%_libdir/lib*.a

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Fri Aug 28 2009 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt3
- fix build

* Mon Jan 15 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt2
- fix library packing

* Sun Jan 14 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- initial build for ALT Linux Sisyphus

