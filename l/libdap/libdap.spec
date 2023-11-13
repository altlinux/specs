Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-generic-compat rpm-macros-valgrind
BuildRequires: libossp-uuid-devel
# END SourceDeps(oneline)
BuildRequires: /usr/bin/groff
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
BuildRequires: chrpath
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: libdap
Summary: The C++ DAP2 library from OPeNDAP
Version: 3.20.10
Release: alt1_5

License: LGPL-2.1-or-later
URL: http://www.opendap.org/
Source0: http://www.opendap.org/pub/source/libdap-%{version}.tar.gz
#Don't run HTTP tests - builders don't have network connections
Patch0: libdap-offline.patch
# Fix for i686 build
Patch1: https://github.com/OPENDAP/libdap4/pull/192.patch
# Add missing includes for gcc 13
# https://github.com/OPENDAP/libdap4/pull/215
Patch2: libdap-include.patch

BuildRequires: gcc-c++
# For autoreconf
BuildRequires: libtool
BuildRequires: bison >= 3.0
BuildRequires: cppunit-devel
BuildRequires: curl-devel
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: graphviz libgraphviz
BuildRequires: libtirpc-devel
BuildRequires: libuuid-devel
BuildRequires: libxml2-devel
BuildRequires: libssl-devel
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif

Provides: bundled(gnulib)
Source44: import.info
Patch33: libdap-alt-cppunit-pkgconfig.patch


%description
The libdap++ library contains an implementation of DAP2. This package
contains the library, dap-config, and getdap. The script dap-config
simplifies using the library in other projects. The getdap utility is a
simple command-line tool to read from DAP2 servers. It is built using the
library and demonstrates simple uses of it.


%package devel
Group: Development/Other
Summary: Development and header files from libdap
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
# for the /usr/share/aclocal directory ownership
Requires: automake

%description devel
This package contains all the files needed to develop applications that
will use libdap.


%package doc
Group: Documentation
Summary: Documentation of the libdap library
BuildArch: noarch

%description doc
Documentation of the libdap library.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

iconv -f latin1 -t utf8 < COPYRIGHT_W3C > COPYRIGHT_W3C.utf8
touch -r COPYRIGHT_W3C COPYRIGHT_W3C.utf8
mv COPYRIGHT_W3C.utf8 COPYRIGHT_W3C
%patch33 -p2


%build
# To fix rpath
autoreconf -f -i
%configure --disable-static --disable-dependency-tracking
# --enable-valgrind - missing valgrind exclusions file
%make_build

make docs


%install
%makeinstall_std INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_libdir}/libdap
mv $RPM_BUILD_ROOT%{_libdir}/libtest-types.a $RPM_BUILD_ROOT%{_libdir}/libdap/
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mv $RPM_BUILD_ROOT%{_bindir}/dap-config-pkgconfig $RPM_BUILD_ROOT%{_bindir}/dap-config

rm -rf __dist_docs
cp -pr html __dist_docs
# those .map and .md5 are of dubious use, remove them
rm -f __dist_docs/*.map __dist_docs/*.md5
# use the ChangeLog timestamp to have the same timestamps for the doc files 
# for all arches
touch -r ChangeLog __dist_docs/*
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done


%files
%doc --no-dereference COPYRIGHT_W3C COPYING COPYRIGHT_URI
%doc README.md NEWS README.dodsrc
%{_bindir}/getdap
%{_bindir}/getdap4
%{_libdir}/libdap.so.27*
%{_libdir}/libdapclient.so.6*
%{_libdir}/libdapserver.so.7*
%{_mandir}/man1/getdap.1*
%{_mandir}/man1/getdap4.1*

%files devel
%{_libdir}/libdap.so
%{_libdir}/libdapclient.so
%{_libdir}/libdapserver.so
%{_libdir}/libdap/
%{_libdir}/pkgconfig/libdap*.pc
%{_bindir}/dap-config
%{_includedir}/libdap/
%{_datadir}/aclocal/*
%{_mandir}/man1/dap-config.1*

#%files doc
#%doc --no-dereference COPYING COPYRIGHT_URI COPYRIGHT_W3C
#%doc __dist_docs/


%changelog
* Mon Nov 13 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 3.20.10-alt1_5
- NMU: fixed FTBFS on LoongArch

* Sun Nov 12 2023 Igor Vlasenko <viy@altlinux.org> 3.20.10-alt1_4
- new version

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 3.20.6-alt1_1
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 3.20.5-alt1_1
- update to new release by fcimport

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 3.20.4-alt1_1
- update to new release by fcimport

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 3.20.3-alt1_1
- update to new release by fcimport

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 3.19.1-alt1_3
- new version

* Tue Jan 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.18.3-alt3_4
- Fixed build.

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.18.3-alt2_4
- set doc to noarch

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.18.3-alt1_4
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 3.17.2-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 3.17.0-alt1_1
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 3.15.1-alt1_1
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 3.13.3-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.13.1-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt1_2
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt1_1
- update to new release by fcimport

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 3.11.3-alt2_3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libdap-doc
  * postclean-03-private-rpm-macros for the spec file

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.11.3-alt2_3
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 3.11.3-alt2_2
- applied repocop patches

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.11.3-alt1_2
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.11.3-alt1_1
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt1_5
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt1_4
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt1_2
- update to new release by fcimport

* Sat Dec 24 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.0-alt2_2
- fixed build after mass spec cleanup

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.0-alt1_2
- initial import by fcimport

