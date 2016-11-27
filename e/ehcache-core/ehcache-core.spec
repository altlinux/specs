Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          ehcache-core
Version:       2.6.11
Release:       alt1_2jpp8
Summary:       Easy Hibernate Cache
License:       ASL 2.0
URL:           http://ehcache.org/
# svn export http://svn.terracotta.org/svn/ehcache/tags/ehcache-core-2.6.11
# find ehcache-core-2.6.11 -name '*.jar' -delete
# tools/maven-ant-tasks-2.0.7.jar
# src/test/resources/resourceclassloader/private-classpath.jar
# find ehcache-core-2.6.11 -name '*.class' -delete
# tar cJf ehcache-core-2.6.11.tar.xz ehcache-core-2.6.11
Source0:       %{name}-%{version}.tar.xz
Patch0:        %{name}-2.6.7-java8.patch

BuildRequires: maven-local
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.transaction:jta)
BuildRequires: mvn(net.sf.ehcache:ehcache-parent:pom:)
BuildRequires: mvn(net.sf.ehcache:sizeof-agent)
BuildRequires: mvn(org.codehaus.mojo:rmic-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:xml-maven-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-resources)
BuildRequires: mvn(org.hibernate:hibernate-core:3)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-jdk14)

# test
%if 0
BuildRequires: mvn(com.sun.xsom:xsom)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(javassist:javassist)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.hibernate:hibernate:2.1.8)
BuildRequires: mvn(org.apache.derby:derby)
BuildRequires: mvn(org.beanshell:bsh:1.3.0)
BuildRequires: mvn(org.codehaus.btm:btm)
BuildRequires: mvn(org.hamcrest:hamcrest-core:1.2)
BuildRequires: mvn(org.hamcrest:hamcrest-library:1.2)
BuildRequires: mvn(org.hibernate:hibernate-ehcache:3.3.2.GA)
BuildRequires: mvn(org.mockito:mockito-core)
%endif

Requires:      hibernate3 >= 3.6.10

BuildArch:     noarch
Source44: import.info

%description
Ehcache is a pure Java, in-process cache.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p0
# Use net.sf.ehcache:ehcache-parent:2.5
# Remove its support because it breaks build during javadoc task
%pom_remove_parent
# disable doclint
%pom_remove_plugin :maven-javadoc-plugin
%pom_xpath_inject "pom:project" "<groupId>net.sf.ehcache</groupId>"

%pom_remove_plugin :gmaven-plugin
%pom_remove_plugin :lifecycle-mapping
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-source-plugin

# don't generate source archive
%pom_remove_plugin :maven-assembly-plugin

# Make sure we require version '3' of Hibernate
%pom_xpath_set "pom:dependency[pom:groupId = 'org.hibernate']/pom:version" 3

%pom_change_dep :servlet-api :javax.servlet-api:3.1.0

# Don't use buildnumber-plugin, because jna is required (and currently broken)
%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'buildnumber-git']"

# circular deps
# org.hibernate hibernate-ehcache 3.3.2.GA
# unavailable deps
%pom_remove_dep net.sf.hibernate:hibernate
%pom_xpath_remove "pom:dependency[pom:scope = 'test']"

%pom_xpath_remove "pom:dependency/pom:scope"

# disable embedded ehcache-sizeof-agent.jar copy
%pom_remove_plugin :maven-dependency-plugin

%mvn_file :%{name} %{name}
%mvn_alias :%{name} net.sf.ehcache:ehcache

%build

# tests skipped. cause: missing dependencies
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc src/assemble/EHCACHE-CORE-LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc src/assemble/EHCACHE-CORE-LICENSE.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6.11-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6.7-alt3_9jpp8
- unbootsrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.7-alt1_3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_2jpp7
- new version

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_1jpp6
- new version

