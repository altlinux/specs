Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# Test of properly function library need DNS querys. It work perfectly on my machine and pass all tests.
# But internet access is not allowed from mock chroot. So, I need disable it by default. Yo may enable it if you want.
%define do_not_test 1

Name:		dnsjava
Version:		2.0.6
Release:		alt2_9jpp7
Summary:		Java DNS implementation
License:		BSD and MIT
URL:			http://www.dnsjava.org/
Source0:		http://www.dnsjava.org/download/%{name}-%{version}.tar.gz
Group:		System/Libraries
#Epoch:		0
#Vendor:		JPackage Project
#Distribution:	JPackage

BuildRequires:	ant jpackage-utils >= 0:1.5

Requires:		jpackage-utils
BuildArch:	noarch

# For tests
BuildRequires:	ant-junit
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

%package		javadoc
Summary:		Javadoc for %{name}
Group:		Development/Java
BuildArch: noarch

%description	javadoc
Javadoc for %{name}.

%prep
%setup -q
rm -rf doc/

iconv -f iso8859-1 -t utf8 Changelog > Changelog.tmp
touch -r Changelog Changelog.tmp
mv -f Changelog.tmp Changelog

%build
export CLASSPATH=%(build-classpath jce)
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dj2se.javadoc=%{_javadocdir}/java clean docsclean jar docs

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p %{name}-%{version}.jar %{buildroot}%{_javadir}
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}-%{version}

%if ! 0%{?do_not_test}
%check
export CLASSPATH='%(build-classpath junit):%{name}-%{version}.jar'
ant -Dj2se.javadoc=%{_javadocdir}/java compile_tests
ant -Dj2se.javadoc=%{_javadocdir}/java run_tests
%endif

%files
%doc Changelog README USAGE examples.html *.java
%{_javadir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}


%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt2_9jpp7
- update to new release by jppimport

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt2_8jpp6
- update to new release by jppimport

* Sun May 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt2_1jpp5
- explicitly selected java5 as default

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_1jpp5
- new jpp release

