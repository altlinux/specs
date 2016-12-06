Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jaxb2-common-basics
Version:       0.9.5
Release:       alt1_2jpp8
Summary:       JAXB2 Basics
License:       BSD
Url:           https://github.com/highsource/jaxb2-basics
Source0:       https://github.com/highsource/jaxb2-basics/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.javaparser:javaparser)
BuildRequires: mvn(com.vividsolutions:jts)
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-launcher)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires: mvn(org.jvnet.jaxb2.maven2:maven-jaxb22-plugin)
BuildRequires: mvn(org.jvnet.jaxb2.maven2:maven-jaxb2-plugin-testing)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.springframework:spring-context-support)
BuildRequires: mvn(xmlunit:xmlunit)

BuildArch:     noarch
Source44: import.info

%description
JAXB2 Basics is a part of JAXB2 Commons project which
implements plugins and tools for JAXB 2.x reference
implementation.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jaxb2-basics-%{version}
# Cleanup
find -name "*.bat" -print -delete
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-deploy-plugin plugins
%pom_remove_plugin :maven-shade-plugin plugins
%pom_disable_module dist
%pom_disable_module samples
%pom_disable_module tests

%pom_change_dep :ant-optional org.apache.ant:ant
%pom_change_dep -r org.springframework:spring org.springframework:spring-context-support
# rm -rf tools/src/main/java/org/jvnet/jaxb2_commons/plugin/spring
%pom_change_dep :maven-jaxb2-plugin :maven-jaxb22-plugin

%pom_xpath_set "pom:dependency[pom:artifactId = 'tools' ]/pom:groupId" com.sun
%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools' ]/pom:scope"
%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools' ]/pom:systemPath"

%pom_xpath_set "pom:plugin[pom:groupId = 'org.jvnet.jaxb2.maven2' ]/pom:artifactId" maven-jaxb22-plugin

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md TODO.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.5-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt2_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt1_4jpp7
- new version

