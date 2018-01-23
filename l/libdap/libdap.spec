# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libossp-uuid-devel
# END SourceDeps(oneline)
BuildRequires: chrpath
%add_optflags %optflags_shared
%define mips mips
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: libdap
Summary: The C++ DAP2 library from OPeNDAP
Version: 3.18.3
Release: alt3_4

License: LGPLv2+
Group: Development/Other
URL: http://www.opendap.org/
Source0: http://www.opendap.org/pub/source/libdap-%{version}.tar.gz
#Don't run HTTP tests - builders don't have network connections
Patch0: libdap-offline.patch
Patch1: libdap-alt-cppunit-pkgconfig.patch

# For autoreconf
BuildRequires: libtool
BuildRequires: bison >= 3.0
BuildRequires: cppunit-devel
BuildRequires: libcurl-devel
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: graphviz libgraphviz
BuildRequires: libuuid-devel
BuildRequires: libxml2-devel
BuildRequires: libssl-devel
%ifnarch s390 %{mips}
BuildRequires: valgrind
%endif
BuildRequires: /usr/bin/groff

Provides: bundled(gnulib)
Source44: import.info


%description
The libdap++ library contains an implementation of DAP2. This package
contains the library, dap-config, and getdap. The script dap-config
simplifies using the library in other projects. The getdap utility is a
simple command-line tool to read from DAP2 servers. It is built using the
library and demonstrates simple uses of it.


%package devel
Summary: Development and header files from libdap
Group: Development/Other
Requires: %{name} = %{version}-%{release}
Requires: pkg-config
# for the /usr/share/aclocal directory ownership
Requires: automake

%description devel
This package contains all the files needed to develop applications that
will use libdap.


%package doc
Summary: Documentation of the libdap library
Group: Documentation
BuildArch: noarch

%description doc
Documentation of the libdap library.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .offline
%patch1 -p2
iconv -f latin1 -t utf8 < COPYRIGHT_W3C > COPYRIGHT_W3C.utf8
touch -r COPYRIGHT_W3C COPYRIGHT_W3C.utf8
mv COPYRIGHT_W3C.utf8 COPYRIGHT_W3C


%build
# To fix rpath
%autoreconf
%configure --disable-static --disable-dependency-tracking
# --enable-valgrind - missing valgrind exclusions file
%make_build

make docs


%install
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%{_libdir}/libdap
mv $RPM_BUILD_ROOT%{_libdir}/libtest-types.a $RPM_BUILD_ROOT%{_libdir}/libdap/
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mv $RPM_BUILD_ROOT%{_bindir}/dap-config-pkgconfig $RPM_BUILD_ROOT%{_bindir}/dap-config

rm -rf __dist_docs
cp -pr docs __dist_docs
# those .map and .md5 are of dubious use, remove them
rm -f __dist_docs/html/*.map __dist_docs/html/*.md5
# use the ChangeLog timestamp to have the same timestamps for the doc files 
# for all arches
touch -r ChangeLog __dist_docs/html/*
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done


%files
%doc COPYRIGHT_W3C COPYING COPYRIGHT_URI
%doc README NEWS README.dodsrc
%{_bindir}/getdap
%{_bindir}/getdap4
%{_libdir}/libdap.so.23*
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

%files doc
%doc COPYING COPYRIGHT_URI COPYRIGHT_W3C
%doc __dist_docs/html/


%changelog
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

