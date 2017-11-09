Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          xapool
Version:       1.5.0
Release:       alt4_11jpp8
Summary:       Open source XA JDBC Pool
License:       LGPLv2+
URL:           http://xapool.ow2.org/
# wget http://download.forge.objectweb.org/xapool/xapool-1.5.0-src.tgz
# tar -xf xapool-1.5.0-src.tgz
# find xapool-1.5.0-src -name "*.jar" -delete
# find xapool-1.5.0-src -name "*.class" -delete
# find xapool-1.5.0-src -name "*.java~" -delete
# rm -rf $(find xapool-1.5.0-src -name "CVS")
# tar czf xapool-1.5.0-src-clean.tar.gz xapool-1.5.0-src
Source0:       %{name}-%{version}-src-clean.tar.gz
Source1:       http://repo1.maven.org/maven2/com/experlog/%{name}/%{version}/%{name}-%{version}.pom
# disable p6spy howl-logger oracle classes12 support
Patch0:        %{name}-%{version}-build.patch
Patch1:        %{name}-%{version}-jdk7.patch

BuildRequires: ant
BuildRequires: apache-commons-logging
BuildRequires: geronimo-jta
BuildRequires: java-devel
BuildRequires: javapackages-local

BuildArch:     noarch
Source44: import.info

%description
XAPool is a software component which allows to:

 - Store objects with a Generic Pool
 - Export a DataSource (javax.sql.DataSource)
 - Export a XADataSource (javax.sql.XADataSource)

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
find . -name "*.jar" -delete
find . -name "*.class" -delete
find . -name "*.java~" -delete

rm -rf $(find . -name "CVS")

%patch0 -p0
%patch1 -p1
sed -i "s|Class-Path: idb.jar classes12.jar jta-spec1_0_1.jar log4j.jar commons-logging.jar p6psy.jar||" archive/xapool.mf

ln -sf $(build-classpath commons-logging) externals/
ln -sf $(build-classpath geronimo-jta) externals/

rm -r src/org/enhydra/jdbc/instantdb \
  src/org/enhydra/jdbc/oracle

%mvn_file com.experlog:%{name} %{name}

%build

ant dist

%install
%mvn_artifact %{SOURCE1} output/dist/lib/%{name}.jar
%mvn_install -J output/dist/jdoc

%files -f .mfiles
%doc README.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt4_11jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt4_10jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt4_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt4_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt4_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt4_3jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt4_2jpp7
- fc update

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt3_3jpp6
- jpp 6 release

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt3_2jpp5
- new jpp release

* Thu Feb 26 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt3_1jpp5
- fixed build

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt2_1jpp5
- fixed build with java 5

* Thu Nov 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

