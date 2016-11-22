Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           h2
Version:        1.3.176
Release:        alt1_6jpp8
Summary:        Java SQL database

License:        EPL or MPLv1.1
URL:            http://www.h2database.com
Source0:        http://www.h2database.com/h2-2014-04-05.zip
Source1:        http://repo2.maven.org/maven2/com/h2database/h2/%{version}/h2-%{version}.pom
Patch0:         fix-build.patch
Patch1:         rm-osgi-jdbc-service.patch
Patch2:         fix-broken-tests.patch
BuildArch: noarch
BuildRequires:  ant
BuildRequires:  lucene3
BuildRequires:  slf4j >= 1.5
BuildRequires:  felix-osgi-core >= 1.2
BuildRequires:  glassfish-servlet-api
BuildRequires:  jts
Source44: import.info

%description
H2 is a the Java SQL database. The main features of H2 are:
* Very fast, open source, JDBC API
* Embedded and server modes; in-memory databases
* Browser based Console application
* Small footprint: around 1 MB jar file size 

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
pushd src/test/org/h2/test/unit
rm TestServlet.java
popd
%patch0
%patch2

# Because no Fedora package provides org.osgi.service.jdbc interfaces yet
%patch1
rm src/main/org/h2/util/OsgiDataSourceFactory.java
rm -fr src/test/org/h2/test/server/TestWeb.java
sed -i -e "s|import org.h2.test.server.TestWeb;||g" src/test/org/h2/test/TestAll.java
sed -i -e "s|new TestWeb().runTest(this);||g" src/test/org/h2/test/TestAll.java
sed -i '/org.osgi.service.jdbc/d' src/main/META-INF/MANIFEST.MF

# Delete pre-built binaries
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

sed -i -e 's|authenticated|authenticate authenticated|' src/tools/org/h2/build/doc/dictionary.txt

%build
export JAVA_HOME=%{java_home}
chmod u+x build.sh
./build.sh jar docs

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p bin/h2-%{version}.jar   \
$RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp docs/javadoc  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp -rp %SOURCE1 $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc src/docsrc/html/license.html

%files javadoc
%{_javadocdir}/%{name}
%doc src/docsrc/html/license.html

%changelog
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

