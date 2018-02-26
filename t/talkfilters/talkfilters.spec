Name: talkfilters
Version: 2.3.8
Release: alt2.qa1.1

Summary: GNU Talk filters

License: GPL
Group: Text tools
Url: http://www.hyperrealm.com/main.php?s=talkfilters

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.hyperrealm.com/talkfilters/%name-%version.tar.bz2

# Automatically added by buildreq on Mon Jan 07 2008
BuildRequires: flex gcc-c++

%description
Set of filters to text processing.

%package -n lib%name
Summary: Library of talkfilters
Group: Development/C
#Requires: lib%name = %version-%release

%description -n lib%name
This package contain header files for libtalkfilters.

%package -n lib%name-devel
Summary: Header files for development with talkfilters
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contain header files for libtalkfilters.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_infodir/

%files
%doc README
%_bindir/*
%_man1dir/*
#%_infodir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/*.so

%changelog
* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.8-alt2.qa1.1
- Rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.3.8-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Fri Aug 28 2009 Vitaly Lipatov <lav@altlinux.ru> 2.3.8-alt2
- fix build (remove broken info page)

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.8-alt1
- new version 2.3.8
- change Url, Source URL, update buildreqs
- enable SMP-build

* Tue Feb 15 2005 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt0.1
- first build for ALT Linux Sisyphus
- original spec from PLD Team <feedback@pld-linux.org>
