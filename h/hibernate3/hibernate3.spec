Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: docbook-dtds
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate3
%define version 3.6.10
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global majorversion 3
%global oname hibernate-orm

Name: hibernate3
Version: 3.6.10
Release: alt3_7jpp7
Summary: Relational persistence and query service

Group: Development/Java
License: LGPLv2+

URL: http://www.hibernate.org/

# git clone git://github.com/hibernate/hibernate-orm
# cd hibernate-orm/ && git archive --format=tar --prefix=hibernate-orm-3.6.10.Final/ 3.6.10.Final | xz > hibernate-3.6.10.Final.tar.xz
Source0: hibernate-orm-3.6.10.Final.tar.xz
Source1: hibernate3-depmap

Patch0:  hibernate-orm-fix-cglib-gid.patch
Patch1:  hibernate-orm-fix-jacc-gid-aid.patch
Patch2:  hibernate-orm-fix-ant-gid.patch
Patch3:  hibernate-orm-infinispan-5-support.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: javapackages-tools >= 0.7.2
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: geronimo-validation
BuildRequires: maven-injection-plugin
BuildRequires: antlr-maven-plugin
BuildRequires: hibernate-validator
BuildRequires: cglib
BuildRequires: jboss-jacc-1.4-api
BuildRequires: c3p0
BuildRequires: proxool
BuildRequires: hibernate-commons-annotations
BuildRequires: jboss-servlet-3.0-api
BuildRequires: ehcache-core
BuildRequires: jbosscache-core
BuildRequires: jbosscache-common-parent
BuildRequires: infinispan
BuildRequires: rhq-plugin-annotations

Requires: jpackage-utils
Requires: javapackages-tools >= 0.7.2
Requires: apache-commons-collections
Requires: dom4j
Requires: geronimo-validation
Requires: hibernate-commons-annotations
Requires: hibernate-jpa-2.0-api
Requires: jboss-servlet-3.0-api
Source44: import.info

%description
Hibernate is a powerful, ultra-high performance
object/relational persistence and query service
for Java.

%package javadoc
Summary: API docs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package entitymanager
Group: Development/Java
Summary: Hibernate Entity Manager
Requires: cglib
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires: hibernate-jpa-2.0-api
Requires: hibernate-validator
Requires: javassist

%description entitymanager
%{summary}.

%package envers
Group: Development/Java
Summary: Hibernate support for entity auditing
Requires: hibernate-commons-annotations
Requires: hibernate-jpa-2.0-api
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires: %{name}-entitymanager = %{?epoch:%epoch:}%{version}-%{release}

%description envers
%{summary}.

%package c3p0
Group: Development/Java
Summary: C3P0-based implementation of Hibernate ConnectionProvider
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires: c3p0

%description c3p0
%{summary}.

%package proxool
Group: Development/Java
Summary: Proxool-based implementation of Hibernate ConnectionProvder
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description proxool
%{summary}.

%package ehcache
Group: Development/Java
Summary: Integration of Hibernate with Ehcache
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires: ehcache-core

%description ehcache
%{summary}.

%package jbosscache
Group: Development/Java
Summary: Integration of hibernate with jbosscache
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires: jbosscache-core

%description jbosscache
%{summary}.

%package infinispan
Group: Development/Java
Summary: Integration of Hibernate with Infinispan
Requires: infinispan

%description infinispan
%{summary}.

%package testing
Group: Development/Java
Summary: Hibernate JUnit test utilities
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires: junit

%description testing
%{summary}.

%prep
%setup -q -n %{oname}-%{namedversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%pom_remove_plugin org.jboss.maven.plugins:maven-jdocbook-plugin hibernate-parent
%pom_remove_plugin org.jboss.maven.plugins:maven-jdocbook-style-plugin hibernate-parent
%pom_disable_module hibernate-testsuite
%pom_disable_module hibernate-oscache
%pom_disable_module hibernate-swarmcache
%pom_disable_module hibernate-jdbc3-testing
%pom_disable_module hibernate-jdbc4-testing

# disable hibernate-tools support
%pom_remove_dep org.hibernate:hibernate-tools hibernate-envers
%pom_remove_dep ant:ant hibernate-envers
rm -r hibernate-envers/src/main/java/org/hibernate/tool/ant/*.java \
  hibernate-envers/src/main/java/org/hibernate/envers/ant/*.java

# Make hibernate-testing back a test dependency...
sed -i "s|<!-- <scope>test</scope> TODO fix this -->|<scope>test</scope>|" hibernate-infinispan/pom.xml

%build

# Currently 4 tests fail with this error:
# "Unable to get the default Bean Validation factory"
export jdk16_home=/usr
export LANG=en_US.UTF-8
mvn-rpmbuild \
  -Dmaven.local.depmap.file=%{SOURCE1} \
  -DdisableDistribution=true \
  -Dmaven.test.skip=true \
  install \
  javadoc:aggregate


%install

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}

install -pm 644 hibernate-parent/pom.xml  %{buildroot}%{_mavenpomdir}/JPP-%{name}-parent.pom

%add_maven_depmap JPP-%{name}-parent.pom -v "%{majorversion},%{namedversion}"

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}/%{name}

install -m 644 hibernate-core/target/hibernate-core-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/hibernate-core.jar
install -pm 644 hibernate-core/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-hibernate-core.pom

%add_maven_depmap JPP.%{name}-hibernate-core.pom %{name}/hibernate-core.jar -v "%{majorversion},%{namedversion}"

for module in c3p0 ehcache infinispan jbosscache proxool \
              entitymanager envers testing; do
    install -m 644 hibernate-${module}/target/hibernate-${module}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/hibernate-${module}.jar
    install -pm 644 hibernate-${module}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-hibernate-${module}.pom
%add_maven_depmap JPP.%{name}-hibernate-${module}.pom %{name}/hibernate-${module}.jar -f ${module} -v "%{majorversion},%{namedversion}"
done

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc changelog.txt lgpl.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/hibernate-core-%{version}.jar
%{_javadir}/%{name}/hibernate-core-%{majorversion}.jar
%{_javadir}/%{name}/hibernate-core-%{namedversion}.jar
%{_mavenpomdir}/JPP-%{name}-parent-%{version}.pom
%{_mavenpomdir}/JPP-%{name}-parent-%{majorversion}.pom
%{_mavenpomdir}/JPP-%{name}-parent-%{namedversion}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-core-%{version}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-core-%{majorversion}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-core-%{namedversion}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc lgpl.txt
%{_javadocdir}/%{name}

%files entitymanager
%{_javadir}/%{name}/hibernate-entitymanager-%{version}.jar
%{_javadir}/%{name}/hibernate-entitymanager-%{majorversion}.jar
%{_javadir}/%{name}/hibernate-entitymanager-%{namedversion}.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-entitymanager-%{version}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-entitymanager-%{majorversion}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-entitymanager-%{namedversion}.pom
%{_mavendepmapfragdir}/%{name}-entitymanager

%files envers
%{_javadir}/%{name}/hibernate-envers-%{version}.jar
%{_javadir}/%{name}/hibernate-envers-%{majorversion}.jar
%{_javadir}/%{name}/hibernate-envers-%{namedversion}.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-envers-%{version}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-envers-%{majorversion}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-envers-%{namedversion}.pom
%{_mavendepmapfragdir}/%{name}-envers

%files c3p0
%{_javadir}/%{name}/hibernate-c3p0-%{version}.jar
%{_javadir}/%{name}/hibernate-c3p0-%{majorversion}.jar
%{_javadir}/%{name}/hibernate-c3p0-%{namedversion}.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-c3p0-%{version}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-c3p0-%{majorversion}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-c3p0-%{namedversion}.pom
%{_mavendepmapfragdir}/%{name}-c3p0

%files ehcache
%{_javadir}/%{name}/hibernate-ehcache-%{version}.jar
%{_javadir}/%{name}/hibernate-ehcache-%{majorversion}.jar
%{_javadir}/%{name}/hibernate-ehcache-%{namedversion}.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-ehcache-%{version}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-ehcache-%{majorversion}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-ehcache-%{namedversion}.pom
%{_mavendepmapfragdir}/%{name}-ehcache

%files infinispan
%{_javadir}/%{name}/hibernate-infinispan-%{version}.jar
%{_javadir}/%{name}/hibernate-infinispan-%{majorversion}.jar
%{_javadir}/%{name}/hibernate-infinispan-%{namedversion}.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-infinispan-%{version}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-infinispan-%{majorversion}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-infinispan-%{namedversion}.pom
%{_mavendepmapfragdir}/%{name}-infinispan

%files proxool
%{_javadir}/%{name}/hibernate-proxool-%{version}.jar
%{_javadir}/%{name}/hibernate-proxool-%{majorversion}.jar
%{_javadir}/%{name}/hibernate-proxool-%{namedversion}.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-proxool-%{version}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-proxool-%{majorversion}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-proxool-%{namedversion}.pom
%{_mavendepmapfragdir}/%{name}-proxool

%files jbosscache
%{_javadir}/%{name}/hibernate-jbosscache-%{version}.jar
%{_javadir}/%{name}/hibernate-jbosscache-%{majorversion}.jar
%{_javadir}/%{name}/hibernate-jbosscache-%{namedversion}.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-jbosscache-%{version}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-jbosscache-%{majorversion}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-jbosscache-%{namedversion}.pom
%{_mavendepmapfragdir}/%{name}-jbosscache

%files testing
%{_javadir}/%{name}/hibernate-testing-%{version}.jar
%{_javadir}/%{name}/hibernate-testing-%{majorversion}.jar
%{_javadir}/%{name}/hibernate-testing-%{namedversion}.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-testing-%{version}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-testing-%{majorversion}.pom
%{_mavenpomdir}/JPP.%{name}-hibernate-testing-%{namedversion}.pom
%{_mavendepmapfragdir}/%{name}-testing

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.6.10-alt3_7jpp7
- rebuild with maven-local

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.6.10-alt2_7jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.6.10-alt2_6jpp7
- fixed deps

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.6.10-alt1_6jpp7
- new fc release

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.6.10-alt1_5jpp7
- new version

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt5_1jpp6
- use antlr-maven-plugin

* Sun Jun 10 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt4_1jpp6
- build with maven-enforcer-api

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt3_1jpp6
- fixed build with new testng and xbean

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt2_1jpp6
- build w/java6

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt1_1jpp6
- new jpp release

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt1_0.7jpp6
- new version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt3_1.SP1_CP01.9jpp5
- fixed build; use cglib21

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt2_1.SP1_CP01.9jpp5
- selected java5 compiler explicitly

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_1.SP1_CP01.9jpp5
- new jpp release

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_1.SP1_CP01.1jpp5
- new version

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt2_0.cr2.1jpp5
- fixed build

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_0.cr2.1jpp5
- fixed build with java 5

* Tue Jan 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_0.cr2.1jpp1.7
- nobootstrap build

