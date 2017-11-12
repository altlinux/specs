# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ java-devel-default perl(File/Spec/Functions.pm) perl(IO/File.pm) rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           tomcat-native
Version:        1.2.12
Release:        alt1_3jpp8
Summary:        Tomcat native library

Group:          System/Libraries
License:        ASL 2.0
URL:            http://tomcat.apache.org/tomcat-8.0-doc/apr.html
Source0:        http://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/%{name}-%{version}-src.tar.gz

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  libapr1-devel >= 1.4.3
BuildRequires:  libssl-devel >= 1.0.2
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
cd native
%configure \
    --with-apr=%{_bindir}/apr-1-config \
    --with-java-home=%{java_home}
%make_build


%install
make -C native install DESTDIR=$RPM_BUILD_ROOT
# Perhaps a devel package sometime?  Not for now; no headers are installed.
rm -f $RPM_BUILD_ROOT%{_libdir}/libtcnative*.*a
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig


%files
%{!?_licensedir:%global license %%doc}
%doc LICENSE NOTICE
%doc CHANGELOG.txt TODO.txt
# Note: unversioned *.so needed here due to how Tomcat loads the lib :(
%{_libdir}/libtcnative*.so*


%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt1_1jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.8-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.33-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.29-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.27-alt1_2jpp7
- new release

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.27-alt1_1jpp7
- fc update

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.24-alt1_2jpp7
- update to new release by jppimport

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

