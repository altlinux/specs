Epoch: 0
Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Test of properly function library need DNS querys. It work perfectly on my machine and pass all tests.
# But internet access is not allowed from mock chroot. So, I need disable it by default. Yo may enable it if you want.
%global do_not_test 1

Name:          dnsjava
Version:       2.1.3
Release:       alt1_11jpp8
Summary:       Java DNS implementation
License:       BSD and MIT
URL:           http://www.dnsjava.org/
Source0:       http://www.dnsjava.org/download/%{name}-%{version}.tar.gz
Source1:       %{name}-%{version}.pom
# bz#842582
Patch0:        dnsjava-2.0.6-java1.5.target.patch

BuildRequires: ant
BuildRequires: aqute-bnd
# see https://fedorahosted.org/released/javapackages/doc/#_add_maven_depmap_macro_2
BuildRequires: javapackages-local
# For tests
BuildRequires: ant-junit
BuildArch:     noarch
Source44: import.info

%description
dnsjava is an implementation of DNS in Java. It supports all of the common
record types and the DNSSEC types. It can be used for queries, zone transfers,
and dynamic updates. It includes a cache which can be used by clients, and a
minimal implementation of a server. It supports TSIG authenticated messages,
partial DNSSEC verification, and EDNS0.

dnsjava provides functionality above and beyond that of the InetAddress class.
Since it is written in pure Java, dnsjava is fully threadable, and in many
cases is faster than using InetAddress.

dnsjava provides both high and low level access to DNS. The high level
functions perform queries for records of a given name, type, and class, and
return an array of records. There is also a clone of InetAddress, which is
even simpler. A cache is used to reduce the number of DNS queries sent. The
low level functions allow direct manipulation of dns messages and records, as
well as allowing additional resolver properties to be set.

A 'dig' clone and a dynamic update program are included, as well as a
primary-only server.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
rm -rf doc/
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

%patch0 -p0 -b .java1.5

iconv -f iso8859-1 -t utf8 Changelog > Changelog.tmp
touch -r Changelog Changelog.tmp
mv -f Changelog.tmp Changelog
# install in _javadir
%mvn_file %{name}:%{name} %{name}

%build

export CLASSPATH=%(build-classpath jce aqute-bnd)
ant -Dj2se.javadoc=%{_javadocdir}/java clean docsclean bundle docs

%mvn_artifact %{SOURCE1} org.xbill.dns_%{version}.jar

%install
%mvn_install -J doc

%if ! 0%{?do_not_test}
%check
export CLASSPATH='%(build-classpath junit):%{name}-%{version}.jar'
ant -Dj2se.javadoc=%{_javadocdir}/java compile_tests
ant -Dj2se.javadoc=%{_javadocdir}/java run_tests
%endif

%files -f .mfiles
%doc LICENSE
%doc Changelog README USAGE examples.html *.java

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_11jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_4jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_3jpp7
- new fc release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt2_9jpp7
- update to new release by jppimport

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt2_8jpp6
- update to new release by jppimport

* Sun May 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt2_1jpp5
- explicitly selected java5 as default

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_1jpp5
- new jpp release

