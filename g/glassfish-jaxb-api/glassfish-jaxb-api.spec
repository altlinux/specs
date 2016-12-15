Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oname jaxb-api
Name:          glassfish-jaxb-api
Version:       2.2.12
Release:       alt1_5jpp8
Summary:       Java Architecture for XML Binding
License:       CDDL or GPLv2 with exception
URL:           http://jaxb.java.net/
# jaxb api and impl have different version
# svn export https://svn.java.net/svn/jaxb~version2/tags/jaxb-2_2_6/tools/lib/redist/jaxb-api-src.zip

Source0:       http://repo1.maven.org/maven2/javax/xml/bind/%{oname}/%{version}/%{oname}-%{version}-b141001.1542-sources.jar
Source1:       http://repo1.maven.org/maven2/javax/xml/bind/%{oname}/%{version}/%{oname}-%{version}-b141001.1542.pom


BuildRequires:  java-javadoc
BuildRequires:  maven-local
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)

BuildArch:     noarch
Source44: import.info

# The Fedora Packaging Committee granted openjdk a bundling exception to carry JAXP and
# JAX-WS (glassfish doesn't need one, since it is the upstream for these files).
# Reference: https://fedorahosted.org/fpc/ticket/292

%description
Glassfish - JAXB (JSR 222) API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{oname}
Requires:      %{name} = %{version}
BuildArch: noarch

%description javadoc
Glassfish - JAXB (JSR 222) API.

This package contains javadoc for %{name}.

%prep
%setup -T -q -c

# fixing incomplete source directory structure
mkdir -p src/main/java

(
  cd src/main/java
  unzip -qq %{SOURCE0}
  rm -rf META-INF
)

cp -p %{SOURCE1} pom.xml

%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.glassfish.build:gfnexus-maven-plugin


sed -i 's|<location>${basedir}/offline-javadoc</location>|<location>%{_javadocdir}/java</location>|' pom.xml

%build

%mvn_file :%{oname} %{oname}
%mvn_build

%install
%mvn_install

mv %{buildroot}%{_javadocdir}/%{name} \
 %{buildroot}%{_javadocdir}/%{oname}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{oname}

%changelog
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.12-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.12-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.12-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.9-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_1jpp7
- new version

