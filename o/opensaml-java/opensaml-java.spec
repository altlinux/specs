# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          opensaml-java
Version:       2.5.3
Release:       alt2_10jpp8
Summary:       Java OpenSAML library
License:       ASL 2.0
Group:         Development/Other
URL:           http://www.opensaml.org/

# svn export https://svn.shibboleth.net/java-opensaml2/tags/2.5.3/ opensaml-java-2.5.3
# tar cafJ opensaml-java-2.5.3.tar.xz opensaml-java-2.5.3
Source0:       opensaml-java-%{version}.tar.xz

# HTTPS Connections Via HTTP Resources Do Not Perform Hostname Verification
Patch0:        rhbz1132022.patch

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: opensaml-java-parent
BuildRequires: opensaml-java-openws >= 1.5.0
BuildRequires: owasp-esapi-java
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-lang
BuildRequires: velocity
BuildRequires: joda-time
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-resolver
BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires: logback
BuildRequires: junit
BuildRequires: springframework
BuildRequires: xmlunit
Source44: import.info

%description
OpenSAML is a set of open source C++ & Java libraries meant to support
developers working with the Security Assertion Markup Language (SAML).
OpenSAML 2, the current version, supports SAML 1.0, 1.1, and 2.0. 

%package javadoc
Summary:       Javadocs for %{name}
Group:         Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n opensaml-java-%{version}

%patch0 -p1

sed -i "s|\${xerces.groupId}|xerces|" pom.xml

%pom_remove_dep "xerces:xml-apis"
%pom_remove_dep "xerces:serializer"
%pom_remove_dep "org.springframework:spring-mock"

iconv -f iso8859-1 -t utf-8 doc/CREDITS.txt > doc/CREDITS.txt.conv 
mv -f doc/CREDITS.txt.conv doc/CREDITS.txt

%build
# No org.springframework:spring-mock available
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc doc
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt2_10jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt2_9jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt2_6jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt2_4jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_4jpp7
- new release

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_2jpp7
- fc update

