Name: xbase
Version: 2.1.1
Release: alt1.2

Summary: Xbase dBase database file library

License: LGPL
Group: Development/Other
Url: http://linux.techass.com/projects/xdb/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/xdb/%name-%version.tar.bz2
Patch: %name-2.0.0-gcc4.patch
Patch1: %name-2.1.1-fix-pld.patch

# Automatically added by buildreq on Sat Jun 18 2005
BuildRequires: gcc-c++ libstdc++-devel

%description
Library for accessing dBase .dbf, .ndx, .dbt, and Clipper .ntx files.

%package -n lib%name
Summary: Libraries needed for %name
Group: System/Libraries

%description -n lib%name
Libraries needed for %name

%package -n lib%name-devel
Summary: Xbase development package
Group: Development/Other

Requires: lib%name = %version-%release

%description -n lib%name-devel
Headers and such for compiling programs that use the Xbase library.

%prep
%setup
%patch
%patch1 -p1


%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc NEWS README TODO AUTHORS ChangeLog
%_bindir/*
%exclude %_bindir/%name-config

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc docs html
%_bindir/%name-config
%_includedir/xbase
%_libdir/libxbase.so

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.2
- Rebuilt for debuginfo

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.1
- Rebuilt for soname set-versions

* Wed Mar 10 2010 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- update to 2.1.1 (thanks, PLD)
- cleanup spec

* Thu Nov 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt4
- fix build with gcc 4.3 (thanks, Mandriva)

* Thu May 25 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3
- changes for GCC4: fix constructor declaration (bug #9611)
- replace iostream.h with iostream, assort using std namespace

* Sun Feb 19 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- add correct Source URL
- cleanup spec

* Sat Jun 18 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- first build for ALT Linux Sisyphus

* Sat Jun 5 2004 Spencer Anderson <sdander@oberon.ark.com> 2.0.0-4mdk
- rebuild
- spec cleaning

* Sun Jan 11 2004 Spencer Anderson <sdander@oberon.ark.com> 2.0.0-3mdk
- correct typo in ntx.cpp

* Thu Dec 25 2003 Spencer Anderson <sdander@oberon.ark.com> 2.0.0-2mdk
- fix provides and requires

* Tue Nov 18 2003 Spencer Anderson <sdander@oberon.ark.com> 2.0.0-1mdk
- initial Mandrake release
- don't use configure macro (breaks build right now)
- needed for new rekall
