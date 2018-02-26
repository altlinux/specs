Name: iksemel
Version: 1.4
Release: alt3

Summary: iksemel Jabber Library
Group: Development/C
License: LGPL

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar.gz

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
Requires: lib%name = %version

%description -n lib%name-devel
%summary

%description
%summary

%prep
%setup

%build
#autoreconf -fisv
%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make ||:
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
