BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jtds
Version:       1.3.1
Release:       alt2_7jpp8
Summary:       SQL Server and Sybase JDBC driver
License:       MIT and LGPLv2+
URL:           http://jtds.sourceforge.net/
# sh jtds-create-tarball.sh < VERSION >
Source0:       %{name}-%{version}-clean.tar.xz
Source1:       %{name}-create-tarball.sh
# fix libraries path
# disable test unavailable deps
# fix javac/javadoc source/target/encoding parameters
# remove classpath from manifest
Patch0:        %{name}-1.3.1-build.patch

BuildRequires: java-devel
BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: jcifs
BuildRequires: jdbc-stdext
# test deps
#BuildRequires: ant-junit
#BuildRequires: junit

Requires:      jcifs

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
TDS is an open source 100% pure Java (type 4) JDBC 3.0 driver 
for Microsoft SQL Server (6.5, 7, 2000,2005, and 2008) and
Sybase (10, 11, 12, 15). jTDS is based on FreeTDS and is currently the
fastest production-ready JDBC  driver for SQL Server and Sybase.
jTDS is 100% JDBC 3.0 compatible, supporting forward-only and
scrollable/updateable ResultSets, concurrent (completely 
independent) Statements and implementing all the DatabaseMetaData and 
ResultSetMetaData methods. 

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

for d in CHANGELOG LICENSE README* ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

%patch0 -p0

# fix non ASCII chars
for s in src/main/net/sourceforge/jtds/jdbc/JtdsDatabaseMetaData.java \
  src/test/net/sourceforge/jtds/jdbc/CSUnitTest.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%build

%ant dist

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/doc/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc CHANGELOG README*
%doc LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_7jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_7jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_6jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_5jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt1_2jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt1_1jpp7
- new version

