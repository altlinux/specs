Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          wss4j
Version:       2.1.5
Release:       alt1_4jpp8
Summary:       Apache WS-Security implementation
License:       ASL 2.0
URL:           http://ws.apache.org/wss4j/

Source0:       http://archive.apache.org/dist/ws/wss4j/%{version}/%{name}-%{version}-source-release.zip
Patch0:        wss4j-2.1.5-ehcache-core-2.6.patch

BuildRequires: maven-local
BuildRequires: mvn(com.sun.mail:javax.mail)
BuildRequires: mvn(junit:junit)
# ehcache:2.10.1 https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=1364535
BuildRequires: mvn(net.sf.ehcache:ehcache-core)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.apache.directory.server:apacheds-kerberos-codec)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
# neethi:3.0.3
BuildRequires: mvn(org.apache.neethi:neethi)
BuildRequires: mvn(org.apache.santuario:xmlsec) >= 2.0.5
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.jasypt:jasypt)
BuildRequires: mvn(org.opensaml:opensaml-saml-impl) >= 3.1.1
BuildRequires: mvn(org.opensaml:opensaml-xacml-impl)
BuildRequires: mvn(org.opensaml:opensaml-xacml-saml-impl)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.tukaani:xz)
BuildRequires: mvn(wsdl4j:wsdl4j)
BuildRequires: mvn(xalan:xalan)
BuildRequires: mvn(xmlunit:xmlunit)

BuildArch:     noarch
Source44: import.info

%description
The Apache WSS4J project provides a Java implementation of the
primary security standards for Web Services.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1

%pom_disable_module integration

# This plugin does not impact the build, and it currently raises this error:
# Reporting mojo's can only be called from ReportDocumentRender
%pom_remove_plugin "org.apache.maven.plugins:maven-pmd-plugin"
%pom_remove_plugin "org.apache.maven.plugins:maven-checkstyle-plugin"

%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"

%pom_change_dep -r net.sf.ehcache:ehcache net.sf.ehcache:ehcache-core
%pom_change_dep -r :geronimo-javamail_1.4_spec com.sun.mail:javax.mail

# VulnerabliltyVectorsTest.testMaximumAllowedDecompressedBytes:572->AbstractTestBase.doOutboundSecurity:167 ? NoClassDefFound: org.tukaani.xz.FilterOptions
%pom_add_dep org.tukaani:xz:1.5:test ws-security-stax

# OutOfMemoryError: unable to create new native thread (only on koji)
rm ws-security-stax/src/test/java/org/apache/wss4j/stax/test/AttachmentTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/DerivedKeyTokenTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/FaultTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/HeaderOrderingTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/ReplayTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/VulnerabliltyVectorsTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/saml/SamlAuthnTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/saml/SamlConditionsTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/saml/SamlTokenDerivedTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/saml/SAMLTokenHOKTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/saml/SAMLTokenReferenceTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/saml/SAMLTokenSVTest.java \
 ws-security-stax/src/test/java/org/apache/wss4j/stax/test/saml/SAMLTokenTest.java

%build

%mvn_build -- -Dmaven.test.skip.exec=true

%install
%mvn_install

%files -f .mfiles
%doc ChangeLog.txt README.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1.5-alt1_4jpp8
- fixed build with new checkstyle

* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1.5-alt1_2jpp8
- new version

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

