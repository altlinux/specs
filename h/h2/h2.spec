# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           h2
Version:        1.3.168
Release:        alt1_3jpp7
Summary:        Java SQL database

Group:          Development/Java
License:        EPL
URL:            http://www.h2database.com
Source0:        http://www.h2database.com/h2-2012-07-13.zip
Source1:        http://repo2.maven.org/maven2/com/h2database/h2/%{version}/h2-%{version}.pom
Patch1:         fix-build.patch
BuildArch: noarch
BuildRequires:  ant
BuildRequires:  lucene >= 2.4
BuildRequires:  lucene-contrib
BuildRequires:  slf4j >= 1.5
BuildRequires:  felix-osgi-core >= 1.2
BuildRequires:  servlet3
Source44: import.info

%description
H2 is a the Java SQL database. The main features of H2 are:
* Very fast, open source, JDBC API
* Embedded and server modes; in-memory databases
* Browser based Console application
* Small footprint: around 1 MB jar file size 

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
pushd src/test/org/h2/test/unit
rm -fr TestServlet.java
popd
pushd src/tools/org/h2/build
%patch1 
popd
find -name '*.orig' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

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

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc src/docsrc/html/license.html

%files javadoc
%{_javadocdir}/%{name}
%doc src/docsrc/html/license.html

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.168-alt1_3jpp7
- new release

* Sun Sep 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.168-alt1_2jpp7
- new version

* Sat Sep 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.147-alt2_5jpp7
- fixed build

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.147-alt1_5jpp7
- new version

