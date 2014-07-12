Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
Name:           wss4j 
Version:        1.6.10
Release:        alt1_1jpp7
Summary:        Apache WS-Security implementation

Group:          Development/Java
License:        ASL 2.0
URL:            http://ws.apache.org/wss4j/
Source0:        http://archive.apache.org/dist/ws/wss4j/1_6_10/wss4j-src-%{version}.zip

BuildRequires:  axis
BuildRequires:  xml-security >= 0:1.5
BuildRequires:  xml-commons-apis
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-remote-resources-plugin
BuildRequires: apache-resource-bundles apache-jar-resource-bundle
BuildRequires:  dos2unix
BuildRequires:  opensaml-java
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  junit
BuildRequires:  slf4j
BuildRequires:  apache-commons-logging
BuildRequires:  opensaml-java-parent
BuildRequires:  maven-surefire-provider-junit4

%if 0%{?fedora} > 17
BuildRequires:  plexus-pom
BuildRequires:  plexus-components-pom
%endif

Requires:       jpackage-utils
Requires:       axis
Requires:       xml-security >= 0:1.5
Requires:       xml-commons-apis
Requires:       opensaml-java
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       apache-commons-logging

BuildArch:      noarch
Source44: import.info

%description
The Apache WSS4J project provides a Java implementation of the
primary security standards for Web Services. 

%package javadoc
Summary: Javadoc for %{name}
Group:   Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

sed -i "s|bcprov-jdk15on|bcprov-jdk16|" pom.xml

# This plugin does not impact the build, and it currently raises this error:
# Reporting mojo's can only be called from ReportDocumentRender
%pom_remove_plugin "org.apache.maven.plugins:maven-pmd-plugin"

dos2unix NOTICE

%build
mvn-rpmbuild package javadoc:javadoc

%install
# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -m 0644 target/%{name}-%{version}.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 0644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap

%files
%doc ChangeLog.txt NOTICE LICENSE.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.10-alt1_1jpp7
- update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.12-alt1_3jpp7
- new fc release

* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.12-alt1_2jpp7
- fc version

* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.10-alt1_1jpp6
- new jpp relase

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.8-alt1_7jpp6
- jpp 6 release

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt3_1jpp5
- fixes for java6 support

* Tue Jun 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_1jpp5
- fixed build

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_1jpp5
- jpackage 5.0

* Sat Jan 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

