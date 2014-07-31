# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          simple
Version:       4.1.21
Release:       alt2_5jpp7
Summary:       Asynchronous HTTP server for Java
Group:         Development/Java
License:       ASL 2.0 and LGPLv2+
URL:           http://www.simpleframework.org/
Source0:       http://sourceforge.net/projects/simpleweb/files/simpleweb/%{version}/%{name}-%{version}.tar.gz
Source1:       http://repo1.maven.org/maven2/org/simpleframework/%{name}/%{version}/%{name}-%{version}.pom
# simple package don't include the license file
Source2:       http://www.apache.org/licenses/LICENSE-2.0.txt
# add system junit
Patch0:        %{name}-%{version}-test-build.patch
# include FileIndexer.properties in jar file
Patch1:        %{name}-%{version}-include-resources.patch
# fix test build for java7+
Patch2:        %{name}-%{version}-jdk7.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: ant-junit
# test deps
BuildRequires: junit

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Simple is a high performance asynchronous HTTP server for Java.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# cleanup
rm -r javadoc/* test/report/*
find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -p0
%patch1 -p0
%patch2 -p0
cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE2} .
sed -i 's/\r//' LICENSE-2.0.txt

# some tests @ random fails
sed -i 's|haltonfailure="yes"|haltonfailure="false"|' test/build.xml

%build

%ant -Djar.path=target -Djavadoc.path=target/site/apidocs all

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.21-alt2_5jpp7
- new release

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.21-alt2_3jpp7
- added ant-junit BR:

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.21-alt1_3jpp7
- new version

