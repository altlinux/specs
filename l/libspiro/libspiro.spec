Name: libspiro
Version: 20071029
Release: alt2.qa1

Summary: Raph Levien's spiro splines library

License: GPL
Group: System/Libraries
Url: http://libspiro.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-src-%version.tar.bz2


# Automatically added by buildreq on Tue Oct 30 2007
BuildRequires: gcc-c++

%description
This is a shared library designed to give FontForge (and others) access to
Raph Levien's spiro splines. 

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name library.

%prep
%setup -n %name

%build
%configure --disable-static
%make_build

%install
mkdir -p %buildroot%_includedir/
%makeinstall

%files
%doc README README-RaphLevien
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/*

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 20071029-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 20071029-alt2
- cleanup spec

* Tue Oct 30 2007 Vitaly Lipatov <lav@altlinux.ru> 20071029-alt1
- initial build for ALT Linux Sisyphus
