Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jboss-reflect
Version:        2.0.2
Release:        alt4_10jpp8
Summary:        JBoss Reflection

Group:          Development/Other

License:        LGPLv2+
URL:            http://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/jboss-reflect/tags/2.0.2.GA/ jboss-reflect-2.0.2
# tar cJf jboss-reflect-2.0.2.tar.xz jboss-reflect-2.0.2
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  javassist
BuildRequires:  jboss-common-core
BuildRequires:  jboss-logging
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
Source44: import.info

%description
JBoss Reflection

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# can't compile the test dir because of missing deps
rm -rf src/test

find -type f -name *.jar -delete
find -type f -name *.class -delete

%pom_remove_dep org.jboss.test:jboss-test
%pom_remove_dep jboss.profiler.jvmti:jboss-profiler-jvmti

%pom_remove_dep org.jboss.logging:jboss-logging-spi
%pom_add_dep org.jboss.logging:jboss-logging

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt4_10jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt4_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt4_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt4_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt4_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt3_2jpp7
- new version

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt2_4jpp6
- fixed build

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt1_4jpp6
- jpp 6 release

