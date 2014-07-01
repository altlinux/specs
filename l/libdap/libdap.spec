# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison gcc-c++ pkgconfig(libcurl)
# END SourceDeps(oneline)
BuildRequires: chrpath
%add_optflags %optflags_shared
Name: libdap
Summary: The C++ DAP2 library from OPeNDAP
Version: 3.11.7
Release: alt1_3

License: LGPLv2+
Group: Development/C
URL: http://www.opendap.org/
Source0: http://www.opendap.org/pub/source/libdap-%{version}.tar.gz
#Don't run HTTP tests - builders don't have network connections
Patch0:  libdap-3.10.2-offline.patch

BuildRequires: cppunit-devel
BuildRequires: curl-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libuuid-devel
BuildRequires: libxml2-devel
BuildRequires: libssl-devel

Provides: bundled(gnulib)
Source44: import.info

# This package could be relocatable. In that case uncomment the following
# line
#Prefix: %{_prefix}


%description
The libdap++ library contains an implementation of DAP2. This package
contains the library, dap-config, and getdap. The script dap-config
simplifies using the library in other projects. The getdap utility is a
simple command-line tool to read from DAP2 servers. It is built using the
library and demonstrates simple uses of it.


%package devel
Summary: Development and header files from libdap
Group: Development/C
Requires: %{name} = %{version}-%{release}
# for the /usr/share/aclocal directory ownership
Requires: automake

%description devel
This package contains all the files needed to develop applications that
will use libdap.


%package doc
Summary: Documentation of the libdap library
Group: Documentation

%description doc
Documentation of the libdap library.


%prep
%setup -q
%patch0 -p1 -b .offline
iconv -f latin1 -t utf8 < COPYRIGHT_W3C > COPYRIGHT_W3C.utf8
touch -r COPYRIGHT_W3C COPYRIGHT_W3C.utf8
mv COPYRIGHT_W3C.utf8 COPYRIGHT_W3C


%build
%configure --disable-static --disable-dependency-tracking
make %{?_smp_mflags}

make docs


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"
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
%{_bindir}/getdap
%{_libdir}/libdap.so.*
%{_libdir}/libdapclient.so.*
%{_libdir}/libdapserver.so.*
%{_mandir}/man1/getdap.1*
%doc README NEWS COPYING COPYRIGHT_URI README.dodsrc
%doc COPYRIGHT_W3C

%files devel
%{_libdir}/libdap.so
%{_libdir}/libdapclient.so
%{_libdir}/libdapserver.so
%{_libdir}/pkgconfig/libdap*.pc
%{_bindir}/dap-config
%{_includedir}/libdap/
%{_datadir}/aclocal/*
%{_mandir}/man1/dap-config.1*

%files doc
%doc COPYING COPYRIGHT_URI COPYRIGHT_W3C
%doc __dist_docs/html/


%changelog
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

