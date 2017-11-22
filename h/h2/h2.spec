Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           h2
Version:        1.4.196
Release:        alt1_2jpp8
Summary:        Java SQL database

License:        EPL or MPLv1.1
URL:            http://www.h2database.com
Source0:        http://www.h2database.com/h2-2017-06-10.zip
Source1:        http://repo2.maven.org/maven2/com/h2database/h2/%{version}/h2-%{version}.pom

Patch0:         port-to-lucene-6.patch

BuildArch: noarch

BuildRequires:  javapackages-local
BuildRequires:  lucene >= 6.1.0
BuildRequires:  lucene-analysis >= 6.1.0
BuildRequires:  lucene-queryparser >= 6.1.0
BuildRequires:  slf4j
BuildRequires:  felix-osgi-core
BuildRequires:  glassfish-servlet-api
BuildRequires:  jts
Source44: import.info

%description
H2 is a the Java SQL database. The main features of H2 are: Very fast, open
source, JDBC API; Embedded and server modes; In-memory databases; Browser
based Console application; Small footprint: around 1 MB jar file size.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p2

# Because no Fedora package provides org.osgi.service.jdbc interfaces yet
rm src/main/org/h2/util/OsgiDataSourceFactory.java
sed -i -e '/OsgiDataSourceFactory/d' src/main/org/h2/util/DbDriverActivator.java
sed -i -e '/org.osgi.service.jdbc/d' src/main/META-INF/MANIFEST.MF

# Delete pre-built binaries
find -name '*.class' -delete
find -name '*.jar' -delete
find -name '*.exe' -delete
find -name '*.dll' -delete

# Don't attempt to download from Internet
sed -i -e '/downloadTest();/d' -e '/download();/d' \
  src/tools/org/h2/build/Build.java

# Tests that use the network
sed -i -e '/TestNetUtils/d' \
  src/test/org/h2/test/TestAll.java

# Use system libraries instead
mkdir ext
ln -s -T $(build-classpath jts) ext/jts-core-1.14.0.jar
ln -s -T $(build-classpath glassfish-servlet-api) ext/servlet-api-3.1.0.jar
ln -s -T $(build-classpath slf4j/api) ext/slf4j-api-1.6.0.jar
ln -s -T $(build-classpath slf4j/nop) ext/slf4j-nop-1.6.0.jar
ln -s -T $(build-classpath lucene/lucene-core) ext/lucene-core-6.1.0.jar
ln -s -T $(build-classpath lucene/lucene-analyzers-common) ext/lucene-analyzers-common-6.1.0.jar
ln -s -T $(build-classpath lucene/lucene-queryparser) ext/lucene-queryparser-6.1.0.jar
ln -s -T $(build-classpath felix/org.osgi.core) ext/org.osgi.core-4.2.0.jar

echo "classic queryparser" >> src/tools/org/h2/build/doc/dictionary.txt
find . -name '*.orig' -print -delete

%build
export JAVA_HOME=%{_jvmdir}/java
sh build.sh jar docs 
#testFast

%install
%mvn_artifact %SOURCE1 bin/h2-%{version}.jar
%mvn_install -J docs/javadoc

%files -f .mfiles
%doc docs/index.html
%doc docs/html
%doc src/docsrc/html/license.html

%files javadoc -f .mfiles-javadoc
%doc src/docsrc/html/license.html

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.196-alt1_2jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.192-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.176-alt1_6jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.176-alt1_4jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.168-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.168-alt1_3jpp7
- new release

* Sun Sep 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.168-alt1_2jpp7
- new version

* Sat Sep 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.147-alt2_5jpp7
- fixed build

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.147-alt1_5jpp7
- new version

