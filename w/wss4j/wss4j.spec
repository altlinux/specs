Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           wss4j 
Version:        1.6.18
Release:        alt1_5jpp8
Summary:        Apache WS-Security implementation
License:        ASL 2.0
URL:            http://ws.apache.org/wss4j/
Source0:        http://archive.apache.org/dist/ws/wss4j/1_6_18/wss4j-src-%{version}.zip
Patch0:         fix-tests.patch

BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(net.shibboleth:parent:pom:)
BuildRequires:  mvn(org.apache.santuario:xmlsec)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.opensaml:opensaml)
BuildRequires:  mvn(org.slf4j:slf4j-log4j12)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildRequires:  dos2unix
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  plexus-pom
BuildRequires:  plexus-components-pom

BuildArch:      noarch
Source44: import.info

%description
The Apache WSS4J project provides a Java implementation of the
primary security standards for Web Services. 

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0

# This plugin does not impact the build, and it currently raises this error:
# Reporting mojo's can only be called from ReportDocumentRender
%pom_remove_plugin "org.apache.maven.plugins:maven-pmd-plugin"

%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"
%pom_xpath_set "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:source" 1.6
%pom_xpath_set "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:target" 1.6

dos2unix NOTICE

# Fails on java8
rm -r src/test/java/org/apache/ws/security/message/EncryptionCRLTest.java \
 src/test/java/org/apache/ws/security/message/SignatureCRLTest.java \
 src/test/java/org/apache/ws/security/message/EncryptionGCMTest.java

%build
# Some tests now failing with "Algorithm constraints check failed: MD5withRSA"
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc ChangeLog.txt README.txt
%doc LICENSE.txt NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.18-alt1_5jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.18-alt1_3jpp8
- java 8 mass update

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.10-alt2_1jpp7
- fixed build

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

