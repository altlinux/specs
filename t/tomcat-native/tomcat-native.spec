# BEGIN SourceDeps(oneline):
BuildRequires: perl(IO/File.pm)
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           tomcat-native
Version:        1.1.23
Release:        alt1_1jpp7
Summary:        Tomcat native library

Group:          System/Libraries
License:        ASL 2.0
URL:            http://tomcat.apache.org/tomcat-7.0-doc/apr.html
Source0:        http://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/%{name}-%{version}-src.tar.gz

BuildRequires:  jpackage-utils
BuildRequires:  libapr1-devel >= 1.2.1
BuildRequires:  libssl-devel
# Upstream compatibility:
Provides:       tcnative = %{version}-%{release}
Source44: import.info

%description
Tomcat can use the Apache Portable Runtime to provide superior
scalability, performance, and better integration with native server
technologies.  The Apache Portable Runtime is a highly portable library
that is at the heart of Apache HTTP Server 2.x.  APR has many uses,
including access to advanced IO functionality (such as sendfile, epoll
and OpenSSL), OS level functionality (random number generation, system
status, etc), and native process handling (shared memory, NT pipes and
Unix sockets).  This package contains the Tomcat native library which
provides support for using APR in Tomcat.


%prep
%setup -q -n %{name}-%{version}-src
f=CHANGELOG.txt ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f


%build
cd jni/native
%configure \
    --with-apr=%{_bindir}/apr-1-config \
    --with-java-home=%{java_home} \
    --with-java-platform=2
make %{?_smp_mflags}


%install
make -C jni/native install DESTDIR=$RPM_BUILD_ROOT
# Perhaps a devel package sometime?  Not for now; no headers are installed.
rm -f $RPM_BUILD_ROOT%{_libdir}/libtcnative*.*a
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig


%files
%doc CHANGELOG.txt LICENSE NOTICE
# Note: unversioned *.so needed here due to how Tomcat loads the lib :(
%{_libdir}/libtcnative*.so*


%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.23-alt1_1jpp7
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.22-alt1_1jpp6
- update to new release by jppimport

* Mon Oct 04 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.20-alt1_1jpp6
- new version

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.1.16-alt2_1jpp5
- repocop fixes applied

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.1.16-alt1_1jpp5
- new version

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 1.1.13-alt1_1jpp1.7.2
- NMU (by repocop): the following fixes applied:
 * postun_ldconfig for tomcat-native
 * post_ldconfig for tomcat-native

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.13-alt1_1jpp1.7.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sat Mar 08 2008 Igor Vlasenko <viy@altlinux.ru> 1.1.13-alt1_1jpp1.7
- new version; merged from fc9-devel

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt1_1jpp1.7
- converted from JPackage by jppimport script

