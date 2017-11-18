Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          opensaml-java-xmltooling
Version:       1.3.4
Release:       alt5_12jpp8
Summary:       Java XMLTooling library
License:       ASL 2.0 and W3C

URL:           http://www.opensaml.org/

# svn export https://svn.shibboleth.net/java-xmltooling/tags/1.3.4/ opensaml-java-xmltooling-1.3.4
# tar cafJ opensaml-java-xmltooling-1.3.4.tar.xz opensaml-java-xmltooling-1.3.4
Source0:       opensaml-java-xmltooling-%{version}.tar.xz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:        0001-Support-for-new-bouncycastle.patch
Patch1:        opensaml-java-xmltooling-1.3.4-bouncycastle1.52.patch

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(ca.juliusdavies:not-yet-commons-ssl)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(net.jcip:jcip-annotations)
BuildRequires: mvn(net.shibboleth:parent:pom:)
BuildRequires: mvn(org.apache.santuario:xmlsec)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(xalan:xalan)
BuildRequires: mvn(xerces:xercesImpl)
BuildRequires: mvn(xml-resolver:xml-resolver)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:jul-to-slf4j)
BuildRequires: mvn(org.slf4j:log4j-over-slf4j)
Source44: import.info

%description
Java XMLTooling is a low-level library that may be used to construct libraries
that allow developers to work with XML in a Java beans manner.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

sed -i "s|\${xerces.groupId}|xerces|" pom.xml
%pom_change_dep :bcprov-jdk15 :bcprov-jdk15on:1.52

%pom_remove_dep "xerces:xml-apis"
%pom_remove_dep "xerces:serializer"
%pom_add_dep net.jcip:jcip-annotations:1

sed -i -e 's,${xalan.groupId},xalan,' pom.xml

%build
# Certificate related tests fail: Tests run: 803, Failures: 24, Errors: 0, Skipped: 0
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc doc/CREDITS.txt doc/README doc/RELEASE-NOTES.txt
%doc doc/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc doc/LICENSE.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt5_12jpp8
- fixed build

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt4_12jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt4_11jpp8
- java8 mass update

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt2_7jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt2_5jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1_5jpp7
- new release

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1_3jpp7
- fc update

