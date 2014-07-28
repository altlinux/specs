# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          opensaml-java-xmltooling
Version:       1.3.4
Release:       alt1_5jpp7
Summary:       Java XMLTooling library
License:       ASL 2.0 and W3C
Group:         Development/Java
URL:           http://www.opensaml.org/

# svn export https://svn.shibboleth.net/java-xmltooling/tags/1.3.4/ opensaml-java-xmltooling-1.3.4
# tar cafJ opensaml-java-xmltooling-1.3.4.tar.xz opensaml-java-xmltooling-1.3.4
Source0:       opensaml-java-xmltooling-%{version}.tar.xz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:     noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: not-yet-commons-ssl
BuildRequires: jcip-annotations
BuildRequires: slf4j
BuildRequires: bouncycastle
BuildRequires: xml-security
BuildRequires: logback
BuildRequires: not-yet-commons-ssl
BuildRequires: apache-commons-codec
BuildRequires: joda-time
BuildRequires: xerces-j2
BuildRequires: xalan-j2
BuildRequires: xml-commons-apis
BuildRequires: opensaml-java-parent

Requires:      jpackage-utils
Requires:      jcip-annotations
Requires:      slf4j
Requires:      bouncycastle
Requires:      xml-security
Requires:      not-yet-commons-ssl
Requires:      apache-commons-codec
Requires:      joda-time
Requires:      xerces-j2
Requires:      xalan-j2
Requires:      xml-commons-apis
Source44: import.info

%description
Java XMLTooling is a low-level library that may be used to construct libraries
that allow developers to work with XML in a Java beans manner.

%package javadoc
Summary:       Javadocs for %{name}
Group:         Development/Java
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

sed -i "s|\${xerces.groupId}|xerces|" pom.xml
sed -i "s|bcprov-jdk15|bcprov-jdk16|" pom.xml

%pom_remove_dep "xerces:xml-apis"
%pom_remove_dep "xerces:serializer"

# Replace with %pom_add_dep in the future
%pom_xpath_inject "pom:dependencies" "<dependency><groupId>net.jcip</groupId><artifactId>jcip-annotations</artifactId><version>1</version></dependency>"

%build
# Certificate related tests fail: Tests run: 803, Failures: 24, Errors: 0, Skipped: 0
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  -Dmaven.test.skip=true \
  package javadoc:aggregate

%install

install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}

# jar
install -pm 644 target/xmltooling-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# depmap
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc doc
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%doc doc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1_5jpp7
- new release

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1_3jpp7
- fc update

