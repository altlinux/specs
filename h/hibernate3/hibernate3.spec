Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: docbook-dtds
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate3
%define version 3.6.10
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global majorversion 3
%global oname hibernate-orm

Name:    hibernate3
Version: 3.6.10
Release: alt3_20jpp8
Summary: Relational persistence and query service
License: LGPLv2+
URL:     http://www.hibernate.org/
# git clone git://github.com/hibernate/hibernate-orm
# cd hibernate-orm/ && git archive --format=tar --prefix=hibernate-orm-3.6.10.Final/ 3.6.10.Final | xz > hibernate-3.6.10.Final.tar.xz
Source0: hibernate-orm-3.6.10.Final.tar.xz
Source1: hibernate3-depmap
Patch0:  hibernate-orm-fix-cglib-gid.patch
Patch1:  hibernate-orm-fix-jacc-gid-aid.patch
Patch2:  hibernate-orm-fix-ant-gid.patch
Patch3:  hibernate-orm-infinispan-5-support.patch
Patch4:  hibernate-orm-cglib-3.1.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local >= 0.7.2
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-injection-plugin
BuildRequires: antlr-maven-plugin
BuildRequires: geronimo-validation
BuildRequires: geronimo-jta
BuildRequires: hibernate-validator
BuildRequires: cglib
BuildRequires: jboss-jacc-1.4-api
BuildRequires: c3p0
BuildRequires: proxool
BuildRequires: hibernate-commons-annotations
BuildRequires: jboss-servlet-3.0-api
BuildRequires: ehcache-core
# jbosscache was retired
# BuildRequires: jbosscache-core
# BuildRequires: jbosscache-common-parent
# H3 dont support infinispan > 5.3.0
# BuildRequires: infinispan
BuildRequires: rhq-plugin-annotations
BuildRequires: h2
BuildRequires: mvn(hsqldb:hsqldb:1)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: glassfish-jaxb
BuildRequires: shrinkwrap
BuildRequires: jboss-transaction-1.1-api

Obsoletes: %{name}-infinispan < %{version}-%{release}
Obsoletes: %{name}-jbosscache < %{version}-%{release}
Source44: import.info

%description
Hibernate is a powerful, ultra-high performance
object/relational persistence and query service
for Java.

%package javadoc
Group: Development/Java
Summary: API docs for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package entitymanager
Group: Development/Java
Summary: Hibernate Entity Manager

%description entitymanager
%{summary}.

%package envers
Group: Development/Java
Summary: Hibernate support for entity auditing

%description envers
%{summary}.

%package c3p0
Group: Development/Java
Summary: C3P0-based implementation of Hibernate ConnectionProvider

%description c3p0
%{summary}.

%package proxool
Group: Development/Java
Summary: Proxool-based implementation of Hibernate ConnectionProvder

%description proxool
%{summary}.

%package ehcache
Group: Development/Java
Summary: Integration of Hibernate with Ehcache

%description ehcache
%{summary}.

%package testing
Group: Development/Java
Summary: Hibernate JUnit test utilities

%description testing
%{summary}.

%prep
%setup -q -n %{oname}-%{namedversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%%patch3 -p1
%patch4 -p1

%pom_remove_plugin org.jboss.maven.plugins:maven-jdocbook-plugin hibernate-parent
%pom_remove_plugin org.jboss.maven.plugins:maven-jdocbook-style-plugin hibernate-parent
%pom_remove_plugin :gmaven-plugin hibernate-parent
%pom_disable_module hibernate-testsuite
%pom_disable_module hibernate-oscache
%pom_disable_module hibernate-swarmcache
%pom_disable_module hibernate-jdbc3-testing
%pom_disable_module hibernate-jdbc4-testing

%pom_disable_module hibernate-infinispan
%pom_disable_module hibernate-jbosscache

# Remove test deps infinispan jbosscache
for m in envers entitymanager ehcache; do
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope = 'test']" hibernate-${m}/pom.xml
done

# We don't need it
%pom_xpath_remove pom:build/pom:extensions hibernate-parent/pom.xml

# disable hibernate-tools support
%pom_remove_dep org.hibernate:hibernate-tools hibernate-envers
%pom_remove_dep ant:ant hibernate-envers
rm -r hibernate-envers/src/main/java/org/hibernate/tool/ant/*.java \
  hibernate-envers/src/main/java/org/hibernate/envers/ant/*.java

# Make hibernate-testing back a test dependency...
#sed -i "s|<!-- <scope>test</scope> TODO fix this -->|<scope>test</scope>|" hibernate-infinispan/pom.xml

# Fix the c3p0 gid
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId = 'c3p0' ]/pom:groupId" com.mchange  hibernate-c3p0

# Fix the hibernate-commons-annotations gid
for f in hibernate-core hibernate-envers;do
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId = 'hibernate-commons-annotations' ]/pom:groupId" org.hibernate.common  ${f}
done

for f in hibernate-core hibernate-entitymanager hibernate-parent;do
sed -i "s|<groupId>javax.validation|<groupId>org.apache.geronimo.specs|" ${f}/pom.xml
sed -i "s|<artifactId>validation-api|<artifactId>geronimo-validation_1.0_spec|" ${f}/pom.xml
done

sed -i "s|<groupId>javax.transaction|<groupId>org.jboss.spec.javax.transaction|" hibernate-core/pom.xml
sed -i "s|<artifactId>jta|<artifactId>jboss-transaction-api_1.1_spec|" hibernate-core/pom.xml
sed -i "s|<version>1.1</version>|<version>1.0.1.Final</version>|" hibernate-core/pom.xml

%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId = 'hibernate-commons-annotations' ]/pom:groupId" org.hibernate.common  hibernate-parent

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," lgpl.txt

%mvn_compat_version : %{majorversion} %{namedversion}
%mvn_package ":hibernate-parent" %{name}
%mvn_package ":hibernate-core" %{name}
%mvn_package ":hibernate" __noinstall

%build

# Currently 4 tests fail with this error:
# "Unable to get the default Bean Validation factory"
export jdk16_home=/usr
export LANG=en_US.UTF-8
%mvn_build -s -f -- -DdisableDistribution=true

%install
%mvn_install

%files -f .mfiles-%{name}
%doc changelog.txt
%doc lgpl.txt

%files javadoc -f .mfiles-javadoc
%doc lgpl.txt

%files entitymanager -f .mfiles-hibernate-entitymanager
%doc lgpl.txt

%files envers -f .mfiles-hibernate-envers
%doc lgpl.txt

%files c3p0 -f .mfiles-hibernate-c3p0
%doc lgpl.txt

%files ehcache -f .mfiles-hibernate-ehcache
%doc lgpl.txt

%files proxool -f .mfiles-hibernate-proxool
%doc lgpl.txt

%files testing -f .mfiles-hibernate-testing
%doc lgpl.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.6.10-alt3_20jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.6.10-alt3_19jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.6.10-alt3_17jpp8
- java 8 mass update

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

