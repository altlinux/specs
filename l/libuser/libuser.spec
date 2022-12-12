Name: libuser
Version: 0.63
Release: alt3

Summary: A user and group account administration library
License: LGPLv2+
Group: System/Base

Url: https://pagure.io/libuser
# repacked https://releases.pagure.org/libuser/libuser-%version.tar.xz
Source0: %name-%version.tar
Source1: import.info
Patch0: %name-0.63-PR49_add_yescrypt.patch
Patch1: %name-0.63-downstream_test_xcrypt.patch
Patch2: %name-0.63-fix_ldap_test.patch 

# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: libcrypt-devel
# END SourceDeps(oneline)
BuildRequires: OpenSP
BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: linuxdoc-tools
BuildRequires: libpam0-devel
BuildRequires: libpopt-devel
BuildRequires: libsasl2-devel
BuildRequires: libselinux-devel
BuildRequires: libldap-devel
BuildRequires: python3-devel
# To make sure the configure script can find it
BuildRequires: nscd
BuildRequires: gcc
# For %%check
#BuildRequires: fakeroot
BuildRequires: openldap-clients
BuildRequires: openldap-servers
BuildRequires: openssl
BuildRequires: bison
BuildRequires: libtool
BuildRequires: gettext-tools libasprintf-devel
BuildRequires: gtk-doc gtk-doc-mkpdf
BuildRequires: libaudit-devel

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

%description
The libuser library implements a standardized interface for manipulating
and administering user and group accounts.  The library uses pluggable
back-ends to interface to its data sources.

Sample applications modeled after those included with the shadow password
suite are included.

%package devel
Summary: Files needed for developing applications which use libuser
Group: Development/C
Requires: %name = %version-%release
Requires: libgio

%description devel
The libuser-devel package contains header files, static libraries, and other
files useful for developing applications with libuser.

%package -n python3-module-libuser
Summary: Python 3 bindings for the libuser library
Group: System/Base
Requires: %name = %version-%release

%description -n python3-module-libuser
The python3-libuser package contains the Python bindings for
the libuser library, which provides a Python 3 API for manipulating and
administering user and group accounts.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p2

%build
./autogen.sh
%configure --with-selinux --with-ldap --with-audit \
           --enable-gtk-doc --with-html-dir=%_datadir/gtk-doc/html \
           PYTHON=python3
make

%install
%makeinstall_std

%find_lang %name

%check
%make_build check || { cat test-suite.log; false; }

%files -f %name.lang
%doc --no-dereference COPYING
%doc AUTHORS NEWS README TODO docs/*.txt
%config(noreplace) %_sysconfdir/libuser.conf

%attr(0755,root,root) %_bindir/*
%_libdir/*.so.*
%dir %_libdir/%name
%_libdir/%name/*.so
%attr(0755,root,root) %_sbindir/*
%_mandir/man1/*
%_mandir/man5/*

%exclude %_libdir/%name/*.la

%files -n python3-module-libuser
%doc python/modules.txt
%python3_sitelibdir/*.so
%exclude %python3_sitelibdir/*.la

%files devel
%_includedir/libuser
%_libdir/*.so
%_pkgconfigdir/*
%_datadir/gtk-doc/html/*

%changelog
* Mon Dec 12 2022 Nikolay Burykin <bne@altlinux.org> 0.63-alt3
- fix ldap test

* Mon Jan 24 2022 Nikolay Burykin <bne@altlinux.org> 0.63-alt2
- update Release to avoid conflicts with Autoimports

* Wed Jan 12 2022 Nikolay Burykin <bne@altlinux.org> 0.63-alt1
- Build from Autoimports to Sisyphus

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.63-alt1_7
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.63-alt1_6
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.63-alt1_1
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.62-alt2_30
- update to new release by fcimport

* Fri Dec 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1_30
- update to new release by fcimport

* Wed Feb 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1_2
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1_1
- update to new release by fcimport

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.57.7-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.57.6-alt1_2
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.57.6-alt1_1
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.57.4-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.57.3-alt2_2
- spec cleanup thanks to ldv@

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.57.3-alt1_2.1
- Rebuild with Python-2.7

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.57.3-alt1_2
- update to new release by fcimport

* Thu Oct 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.57.3-alt1_1
- update to new release by fcimport

* Mon Aug 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.57.2-alt1_1
- initial release by fcimport

