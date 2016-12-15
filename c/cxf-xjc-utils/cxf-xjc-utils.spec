Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          cxf-xjc-utils
Version:       3.0.5
Release:       alt1_1jpp8
Summary:       Apache CXF XJC-Utils
License:       ASL 2.0
URL:           http://cxf.apache.org/xjc-utils.html
Source0:       https://github.com/apache/cxf-xjc-utils/archive/xjc-utils-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.shared:maven-artifact-resolver)
BuildRequires: mvn(org.apache.ws.jaxme:jaxme2)
BuildRequires: mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-core)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires: mvn(org.javassist:javassist)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(wsdl4j:wsdl4j)
BuildRequires: mvn(xml-resolver:xml-resolver)

BuildArch:     noarch
Source44: import.info

%description
The Apache CXF XJC-Utils provides a bunch of utilities for working
with JAXB to generate better or more usable code.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-xjc-utils-%{version}

%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin
%pom_disable_module bug671

%pom_change_dep -r :jaxb-core org.glassfish.jaxb::2.2.11
%pom_change_dep -r :jaxb-impl org.glassfish.jaxb:jaxb-runtime:2.2.11
%pom_change_dep -r :jaxb-xjc org.glassfish.jaxb::2.2.11
%pom_change_dep -r :jaxme2 org.apache.ws.jaxme:

%pom_remove_plugin -r :maven-checkstyle-plugin

# ClassNotFoundException: org.apache.commons.codec.binary.Base64
%pom_add_dep commons-codec:commons-codec:1.10:test dv-test

# Not available test deps
# org.eclipse.equinox:app:jar:1.3.100-v20130327-1442
%pom_remove_dep org.eclipse.equinox:app javadoc
# com.cedarsoft.commons:io:jar:6.0.1:
%pom_remove_dep com.cedarsoft.commons:io javadoc
rm -r javadoc/src/test/java/*
# org.eclipse.jdt:core:3.3.0-v_771
%pom_remove_dep org.eclipse.jdt:core javadoc

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.5-alt1_1jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.2-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt3_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt3_5jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_3jpp7
- new version

