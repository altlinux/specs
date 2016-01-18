Name: iksemel
Version: 1.4
Release: alt5

Summary: iksemel Jabber Library
Group: Development/C
License: LGPL
Url: http://code.google.com/p/iksemel/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Patch0: iksemel-1.3-gnutls-2.8.patch

# Automatically added by buildreq on Tue May 23 2006
BuildRequires: gcc-c++ libgnutls-devel

%package -n lib%name
Group: %group
Summary: %summary

%description -n lib%name
%summary

%package -n lib%name-devel
Group: %group
Summary: %summary
Requires: lib%name = %version-%release

%description -n lib%name-devel
%summary

%description
%summary

%prep
%setup
%patch0 -p0

%build
%autoreconf
%configure --with-gnutls
%make

%install
%makeinstall
rm -f %buildroot/%_infodir/*
rmdir %buildroot%_infodir

%files -n lib%name
%_libdir/lib%name.so.3.1.1
%_libdir/lib%name.so.3

%files -n lib%name-devel
%_bindir/ikslint
%_bindir/iksperf
%_bindir/iksroster
%_libdir/lib%name.so
%_includedir/%name.h
%_pkgconfigdir/%name.pc
# %_infodir/%name.bz2

%exclude %_libdir/libiksemel.a

%changelog
* Mon Jan 18 2016 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt5
- Rebuild with new gnutls
- https://github.com/meduketto/iksemel/issues/45

* Tue Dec 31 2013 Terechkov Evgenii <evg@altlinux.org> 1.4-alt4.1
- Patch from gentoo to really build with gnutls

* Sat Jan 26 2013 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt4
- add Url tag
- fix non-strict dependency

* Sun Jan 15 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt3
- fix rpath bug (thanks to ldv@)

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt2
- fix build

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt1
- 1.4

* Sat Apr 02 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt7
- rebuild

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt6
- exclude libiksemel.a

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt5
- auto rebuild

* Mon Jul 06 2009 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt4
- remove info file
- fix building with new gnutls

* Thu Feb 12 2009 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt3
- rebuild with new gnutls

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt2
- cleanup spec

* Sat Mar 15 2008 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt1
- update to 1.3

* Thu Mar 13 2008 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt2
- fix #13513

* Tue May 23 2006 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt1
- first build for Sisyphus
