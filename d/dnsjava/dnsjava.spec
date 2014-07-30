Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Test of properly function library need DNS querys. It work perfectly on my machine and pass all tests.
# But internet access is not allowed from mock chroot. So, I need disable it by default. Yo may enable it if you want.
%global do_not_test 1

Name:          dnsjava
Version:       2.1.3
Release:       alt1_4jpp7
Summary:       Java DNS implementation
Group:         System/Libraries
License:       BSD and MIT
URL:           http://www.dnsjava.org/
Source0:       http://www.dnsjava.org/download/%{name}-%{version}.tar.gz
Source1:       %{name}-%{version}.pom
# bz#842582
Patch0:        dnsjava-2.0.6-java1.5.target.patch

BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.5

# For tests
BuildRequires: ant-junit

Requires:      jpackage-utils
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
Summary:       Javadoc for %{name}
Group:         Development/Java
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
rm -rf doc/

%patch0 -p1 -b .java1.5

iconv -f iso8859-1 -t utf8 Changelog > Changelog.tmp
touch -r Changelog Changelog.tmp
mv -f Changelog.tmp Changelog

%build
export CLASSPATH=%(build-classpath jce)
ant -Dj2se.javadoc=%{_javadocdir}/java clean docsclean jar docs

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom and depmap
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}


%if ! 0%{?do_not_test}
%check
export CLASSPATH='%(build-classpath junit):%{name}-%{version}.jar'
ant -Dj2se.javadoc=%{_javadocdir}/java compile_tests
ant -Dj2se.javadoc=%{_javadocdir}/java run_tests
%endif

%files
%doc Changelog README USAGE examples.html *.java
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
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

