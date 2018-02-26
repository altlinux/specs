%def_disable static

Name: libnfsidmap
Version: 0.25
Release: alt1

Summary: Name to user id mapping library
License: BSD
Group: System/Libraries
Url: http://www.citi.umich.edu/projects/nfsv4/linux/

Source: %name-%version-%release.tar

BuildRequires: libldap-devel

Conflicts: nfs-clients < 1:1.2.4

%package ldap
Summary: Name to user id mapping library via LDAP
Group: System/Libraries
Requires: %name = %version-%release

%package devel
Summary: Name to user id mapping library and headers
Group: Development/C
Requires: %name = %version-%release

%if_enabled static
%package devel-static
Summary: Name to user id mapping static library
Group: Development/C
Requires: %name-devel = %version-%release
%endif

%description
%name is a library holding mulitiple methods of mapping names to id's
and visa versa, mainly for NFSv4.

%description ldap
%name is a package, containing LDAP method of mapping names to id's
and visa versa, mainly for NFSv4.

%description devel
%name is a library holding mulitiple methods of mapping names to id's
and visa versa, mainly for NFSv4.
This package holds development part of %name library

%if_enabled static
%description devel-static
%name is a library holding mulitiple methods of mapping names to id's
and visa versa, mainly for NFSv4.
This package contains static %name library
%endif

%prep
%setup

%build
[ ! -f autogen.sh ] || sh autogen.sh
%configure %{subst_enable static} --libdir=/%_lib --with-pluginpath=/%_lib/libnfsidmap
%make_build

%install
%makeinstall libdir=%buildroot/%_lib pkgconfigdir=%buildroot%_pkgconfigdir
install -m0644 -pD idmapd.conf %buildroot%_sysconfdir/idmapd.conf
find %buildroot/%_lib -maxdepth 1 -name \*.so|while read; do
	ln -snf ../../%_lib/`readlink $REPLY` %buildroot%_libdir/${REPLY##*/}
	rm -f -- $REPLY
done
find %buildroot -type f -name \*.la -delete
sed -i 's,/%_lib,%_libdir,' %buildroot%_pkgconfigdir/%name.pc
 
%files
%doc COPYING README
%config(noreplace) %_sysconfdir/idmapd.conf

/%_lib/%name.so.*

/%_lib/%name
%exclude /%_lib/%name/umich_ldap.*

%_man5dir/idmapd.conf.*

%files ldap
/%_lib/%name/umich_ldap.*

%files devel
%_libdir/%name.so
%_includedir/nfsidmap.h
%_pkgconfigdir/*
%_man3dir/*

%if_enabled static
%files devel-static
%_libdir/%name.a
%endif

%changelog
* Tue Dec 06 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.25-alt1
- 0.25 released

* Thu May 12 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.24-alt2
- conflicts: added due to idmapd.conf relocation from nfs-clients

* Mon Feb 28 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.24-alt1
- 0.24 released

* Sat Nov 06 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.23-alt1
- 0.23 released

* Sat Sep 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22-alt1
- 0.22 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21-alt2
- obsolete by filetriggers macros removed

* Sat Aug 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21-alt1
- 0.21 released

* Sat Oct 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20-alt1
- 0.20 released

* Sun Dec  3 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18-alt1
- 0.18 released

* Tue Aug 15 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17-alt1
- 0.17 released

* Mon Jul 17 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16-alt1
- 0.16 released

* Fri Oct 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11-alt1
- 0.11 released
- #7878 fixed

* Sat May  7 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt2
- made umich_ldap mappings build conditional and disabled by default

* Sat Feb 19 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt1
- Initial build.

