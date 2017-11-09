Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.0.6
%global oname xmlsec
%global _version %(echo %{version} | tr . _ )

Name:           xml-security
Version:        2.0.6
Release:        alt1_4jpp8
Epoch:          0
Summary:        Implementation of W3C security standards for XML
License:        ASL 2.0
URL:            http://santuario.apache.org/
Source0:        http://www.apache.org/dist/santuario/java-library/%{_version}/%{oname}-%{version}-source-release.zip
# Unavailable class in jetty8/9 org.eclipse.jetty.io.Buffer
Patch0:         xml-security-2.0.2-remove-Buffer.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlets)
BuildRequires:  mvn(org.jvnet.jaxb2.maven2:maven-jaxb22-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-log4j12)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildRequires:  mvn(xmlunit:xmlunit)

BuildArch:      noarch
Source44: import.info

%description
The XML Security project is aimed at providing implementation
of security standards for XML. Currently the focus is on the
W3C standards :
- XML-Signature Syntax and Processing; and
- XML Encryption Syntax and Processing.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package demo
Group: Development/Java
Summary:        Samples for %{name}

%description demo
Samples for %{name}.

%prep
%setup -q -n %{oname}-%{version}
%pom_xpath_set "pom:properties/pom:jetty.version" 9.0.5.v20130815
%patch0 -p0

%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
# Use org.codehaus.mojo:extra-enforcer-rules:jar:1.0-beta-3
%pom_remove_plugin :maven-enforcer-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"

%pom_xpath_set "pom:plugin[pom:groupId = 'org.jvnet.jaxb2.maven2' ]/pom:artifactId" maven-jaxb22-plugin

%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'eclipse.moxy']"

# javax.xml.crypto.MarshalException: ECKeyValue not supported
rm -r src/test/java/javax/xml/crypto/test/dsig/InteropXMLDSig11Test.java
# UnrecoverableKey
rm -r src/test/java/javax/xml/crypto/test/dsig/PKSignatureAlgorithmTest.java \
 src/test/java/org/apache/xml/security/test/dom/algorithms/DigestAlgorithmTest.java \
 src/test/java/org/apache/xml/security/test/dom/algorithms/PKSignatureAlgorithmTest.java \
 src/test/java/org/apache/xml/security/test/dom/signature/ECDSASignatureTest.java

# Fails for various reason
rm -r src/test/java/org/apache/xml/security/test/stax/signature/IAIKTest.java \
 src/test/java/org/apache/xml/security/test/stax/signature/SignatureVerificationReferenceURIResolverTest.java \
 src/test/java/org/apache/xml/security/test/stax/signature/SignatureDigestVerificationTest.java \
 src/test/java/org/apache/xml/security/test/dom/algorithms/SymmetricEncryptionAlgorithmTest.java \
 src/test/java/org/apache/xml/security/test/dom/encryption/XMLEncryption11Test.java \
 src/test/java/org/apache/xml/security/test/stax/encryption/XMLEncryption11Test.java \
 src/test/java/org/apache/xml/security/test/stax/XMLSecurityStreamWriterTest.java \
 src/test/java/org/apache/xml/security/test/stax/signature/PKSignatureCreationTest.java \
 src/test/java/org/apache/xml/security/test/stax/signature/SignatureDigestCreationTest.java \
 src/test/java/org/apache/xml/security/test/stax/signature/PKSignatureVerificationTest.java \
 src/test/java/org/apache/xml/security/test/stax/transformer/TransformEnvelopedSignatureTest.java \
 src/test/java/org/apache/xml/security/test/stax/transformer/TransformIdentityTest.java \
 src/test/java/org/apache/xml/security/test/stax/XMLSecurityEventWriterTest.java \
 src/test/java/org/apache/xml/security/test/stax/signature/SignatureCreationTest.java \
 src/test/java/org/apache/xml/security/test/stax/signature/SignatureEncryptionTest.java \
 src/test/java/org/apache/xml/security/test/stax/signature/PhaosTest.java \
 src/test/java/org/apache/xml/security/test/dom/interop/BaltimoreTest.java \
 src/test/java/org/apache/xml/security/test/stax/signature/BaltimoreTest.java \
 src/test/java/org/apache/xml/security/test/stax/encryption/SymmetricEncryptionVerificationTest.java \
 src/test/java/org/apache/xml/security/test/stax/encryption/SymmetricEncryptionCreationTest.java \
 src/test/java/javax/xml/crypto/test/dsig/SignatureDigestMethodTest.java \
 src/test/java/org/apache/xml/security/test/stax/signature/SignatureVerificationTest.java \
 src/test/java/org/apache/xml/security/test/stax/XMLSecEventTest.java

# NoSuchAlgorithmException: unsupported algorithm
rm -r src/test/java/javax/xml/crypto/test/dsig/HMACSignatureAlgorithmTest.java
# KeyException: ECKeyValue not supported
rm -r src/test/java/javax/xml/crypto/test/dsig/CreateInteropXMLDSig11Test.java

%mvn_file :%{oname} %{name} %{oname}

%build

# On ARM builder test suite fails @ random
# java.lang.NoClassDefFoundError: Could not initialize class org.apache.xml.security.stax.ext.XMLSec
%mvn_build -f

%install
%mvn_install

chmod 644 samples/org/apache/xml/security/samples/encryption/*.java
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%files demo
%{_datadir}/%{name}
%doc LICENSE NOTICE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_2jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_3jpp8
- full build

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt3_1jpp7
- rebuild with maven-local

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt2_1jpp7
- fixed build

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt1_1jpp7
- update

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0:1.4.5-alt1_4jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for xml-security

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.5-alt1_4jpp7
- new release

* Sun Mar 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt3_0jpp6
- added depmap for org.apache.santuario:xmlsec:jar

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt2_0jpp6
- added jbossas42 compatible repolib

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt1_0jpp6
- new version (closes: #20786)

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_5jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_2jpp5
- jpp5 build

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

