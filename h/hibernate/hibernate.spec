# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate
%define version 4.1.7
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          hibernate
Version:       4.1.7
Release:       alt1_6jpp7
Summary:       Relational persistence and query service
Group:         Development/Java
License:       LGPLv2+ and ASL 2.0
URL:           http://www.hibernate.org/
Source0:       http://sourceforge.net/projects/hibernate/files/hibernate4/%{namedversion}/hibernate-release-%{namedversion}.tgz
# TODO remove these poms when gradle maven plugin work properly
Source1:       http://repo1.maven.org/maven2/org/hibernate/hibernate-c3p0/%{namedversion}/hibernate-c3p0-%{namedversion}.pom
Source2:       http://repo1.maven.org/maven2/org/hibernate/hibernate-core/%{namedversion}/hibernate-core-%{namedversion}.pom
Source3:       http://repo1.maven.org/maven2/org/hibernate/hibernate-ehcache/%{namedversion}/hibernate-ehcache-%{namedversion}.pom
Source4:       http://repo1.maven.org/maven2/org/hibernate/hibernate-entitymanager/%{namedversion}/hibernate-entitymanager-%{namedversion}.pom
Source5:       http://repo1.maven.org/maven2/org/hibernate/hibernate-envers/%{namedversion}/hibernate-envers-%{namedversion}.pom
Source6:       http://repo1.maven.org/maven2/org/hibernate/hibernate-infinispan/%{namedversion}/hibernate-infinispan-%{namedversion}.pom
Source7:       http://repo1.maven.org/maven2/org/hibernate/hibernate-proxool/%{namedversion}/hibernate-proxool-%{namedversion}.pom
Source8:       http://repo1.maven.org/maven2/org/hibernate/hibernate-testing/%{namedversion}/hibernate-testing-%{namedversion}.pom

# hibernate package don't include ASL license file
Source9:       http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:        hibernate-4.1.7.Final-build.patch
Patch1:        hibernate-4.1.6.Final-fix-incorrect-fsf-address.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: antlr-tool
BuildRequires: bean-validation-api
BuildRequires: byteman
BuildRequires: c3p0
BuildRequires: classmate
BuildRequires: dom4j
BuildRequires: ehcache-core
BuildRequires: h2
BuildRequires: hibernate-commons-annotations
BuildRequires: hibernate-jpa-2.0-api
# BuildRequires: hibernate-tools https://bugzilla.redhat.com/show_bug.cgi?id=826701
BuildRequires: hibernate-validator
BuildRequires: infinispan
BuildRequires: jandex
BuildRequires: javassist
BuildRequires: jboss-common-core
BuildRequires: jboss-jacc-1.4-api
# jboss-jts 4.16.4.Final
BuildRequires: jboss-jts
BuildRequires: jboss-logging
BuildRequires: jboss-naming
BuildRequires: jboss-transaction-1.1-api
BuildRequires: junit
BuildRequires: log4j
BuildRequires: mchange-commons
BuildRequires: mockito
BuildRequires: proxool
BuildRequires: rhq-plugin-annotations
BuildRequires: shrinkwrap
BuildRequires: slf4j
BuildRequires: xapool

# build tools and deps
BuildRequires: annox
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: codemodel
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jaxb-api
BuildRequires: gradle
BuildRequires: hibernate-jpamodelgen
BuildRequires: istack-commons
BuildRequires: jaxb2-common-basics
BuildRequires: jboss-logging-tools
# BuildRequires: maven-wagon
BuildRequires: rngom
BuildRequires: txw2
BuildRequires: xsom

Requires:      ant
Requires:      antlr-tool
Requires:      bean-validation-api
Requires:      classmate
Requires:      dom4j
Requires:      hibernate-commons-annotations
Requires:      hibernate-jpa-2.0-api
Requires:      hibernate-validator
Requires:      jandex
Requires:      javassist
Requires:      jboss-jacc-1.4-api
Requires:      jboss-logging
Requires:      jboss-transaction-1.1-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Hibernate is a powerful, ultra-high performance
object/relational persistence and query service
for Java. Hibernate lets you develop persistent
objects following common Java idiom - including
association, inheritance, polymorphism, composition
and the Java collections framework. Extremely
fine-grained, richly typed object models are
possible. The Hibernate Query Language, designed
as a "minimal" object-oriented extension to SQL,
provides an elegant bridge between the object and
relational worlds. Hibernate is now the most
popular ORM solution for Java.

%package c3p0
Group:         Development/Java
Summary:       Hibernate C3P0 ConnectionProvider
Requires:      c3p0
Requires:      jboss-logging
Requires:      %{name} = %{version}-%{release}

%description c3p0
C3P0-based implementation of the Hibernate ConnectionProvder contract.

%package ehcache
Group:         Development/Java
Summary:       Hibernate Ehcache Integration
Requires:      ehcache-core
Requires:      jboss-logging
Requires:      %{name} = %{version}-%{release}

%description ehcache
Integration of Hibernate with Ehcache.

%package entitymanager
Group:         Development/Java
Summary:       Hibernate Entity Manager
Requires:      dom4j
Requires:      hibernate-commons-annotations
Requires:      hibernate-jpa-2.0-api
Requires:      javassist
Requires:      jboss-logging
Requires:      jboss-transaction-1.1-api
Requires:      %{name} = %{version}-%{release}

%description entitymanager
Hibernate Entity Manager.

%package envers
Group:         Development/Java
Summary:       Hibernate Envers
# Requires:      hibernate-tools
Requires:      jboss-logging
Requires:      %{name} = %{version}-%{release}
Requires:      %{name}-entitymanager = %{version}-%{release}

%description envers
Support for entity auditing.

%package infinispan
Group:         Development/Java
Summary:       Hibernate Infinispan Integration
Requires:      infinispan
Requires:      jboss-common-core
Requires:      jboss-logging
Requires:      rhq-plugin-annotations
Requires:      %{name} = %{version}-%{release}
Requires:      %{name}-testing = %{version}-%{release}

%description infinispan
Integration of Hibernate with Infinispan.

%package proxool
Group:         Development/Java
Summary:       Hibernate Proxool ConnectionProvider
Requires:      jboss-logging
Requires:      proxool
Requires:      %{name} = %{version}-%{release}

%description proxool
Proxool-based implementation of the Hibernate ConnectionProvder contract.

%package testing
Group:         Development/Java
Summary:       Hibernate Testing
Requires:      byteman
# jboss-jts 4.16.4.Final
Requires:      jboss-jts
Requires:      junit
Requires:      xapool
Requires:      %{name} = %{version}-%{release}

%description testing
Hibernate JUnit test utilities.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n hibernate-release-%{namedversion}

find .  -name "*.jar" -delete
find .  -name "*.class" -delete
rm -r documentation/*
mv -f project/* .

%patch0 -p1
%patch1 -p0


# FIXME
cp -p %{SOURCE6} .
# infinispan
sed -i "s|<version>5.1.6.FINAL</version>|<version>5.1.2.FINAL</version>|" hibernate-infinispan-%{namedversion}.pom
cp -p %{SOURCE8} .
# jboss-jts
sed -i "s|<version>4.16.4.Final</version>|<version>4.16.2.Final</version>|" hibernate-testing-%{namedversion}.pom

sed -i "s|<artifactId>jbossjta</artifactId>|<artifactId>jbossjts</artifactId>|" hibernate-testing-%{namedversion}.pom
# jbossjta was removed in jboss-jts 4.16.2-10 package
sed -i "s|org.jboss.jbossts:jboss-jts/jbossjta:4.16.4.Final|org.jboss.jbossts:jboss-jts/jbossjts:4.16.4.Final|" libraries.gradle


cp -p %{SOURCE9} .
sed -i 's/\r//' LICENSE-2.0.txt

# fix non ASCII chars
for s in hibernate-core/src/main/java/org/hibernate/annotations/FlushModeType.java\
 hibernate-core/src/main/java/org/hibernate/annotations/SQLUpdate.java\
 hibernate-core/src/main/java/org/hibernate/annotations/NamedQueries.java\
 hibernate-core/src/main/java/org/hibernate/annotations/NaturalId.java\
 hibernate-core/src/main/java/org/hibernate/annotations/ResultCheckStyle.java\
 hibernate-core/src/main/java/org/hibernate/annotations/SQLDeleteAll.java\
 hibernate-core/src/main/java/org/hibernate/annotations/SQLDelete.java\
 hibernate-core/src/main/java/org/hibernate/annotations/Loader.java\
 hibernate-core/src/main/java/org/hibernate/annotations/SQLInsert.java\
 hibernate-envers/src/main/java/org/hibernate/envers/event/BaseEnversEventListener.java\
 hibernate-envers/src/main/java/org/hibernate/envers/event/EnversPreCollectionUpdateEventListenerImpl.java\
 hibernate-envers/src/main/java/org/hibernate/envers/event/EnversPostDeleteEventListenerImpl.java\
 hibernate-envers/src/main/java/org/hibernate/envers/event/BaseEnversCollectionEventListener.java\
 hibernate-envers/src/main/java/org/hibernate/envers/event/EnversPostUpdateEventListenerImpl.java\
 hibernate-envers/src/main/java/org/hibernate/envers/event/EnversPreCollectionRemoveEventListenerImpl.java\
 hibernate-envers/src/main/java/org/hibernate/envers/event/EnversPostInsertEventListenerImpl.java\
 hibernate-envers/src/main/java/org/hibernate/envers/event/EnversPostCollectionRecreateEventListenerImpl.java\
 hibernate-envers/src/main/java/org/hibernate/envers/configuration/metadata/CollectionMetadataGenerator.java\
 hibernate-envers/src/main/java/org/hibernate/envers/entities/EntityConfiguration.java\
 hibernate-envers/src/main/java/org/hibernate/envers/entities/mapper/relation/OneToOneNotOwningMapper.java\
 hibernate-envers/src/main/java/org/hibernate/envers/entities/mapper/relation/ToOneIdMapper.java\
 hibernate-envers/src/main/java/org/hibernate/envers/entities/mapper/relation/lazy/ToOneDelegateSessionImplementor.java\
 hibernate-envers/src/main/java/org/hibernate/envers/query/AuditQueryCreator.java\
 hibernate-envers/src/main/java/org/hibernate/envers/query/impl/AbstractAuditQuery.java\
 hibernate-envers/src/main/java/org/hibernate/envers/query/impl/RevisionsOfEntityQuery.java\
 hibernate-envers/src/main/java/org/hibernate/envers/query/impl/EntitiesAtRevisionQuery.java\
 hibernate-envers/src/main/java/org/hibernate/envers/tools/Tools.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/JndiInfinispanRegionFactory.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/InfinispanRegionFactory.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/TypeOverrides.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/AddressAdapterImpl.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/EvictAllCommand.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/CacheCommandInitializer.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/CacheCommandFactory.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/AddressAdapter.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/FlagAdapter.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/CacheAdapter.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/CacheCommandIds.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/CacheAdapterImpl.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/CacheHelper.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/util/CacheCommandExtensions.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/entity/EntityRegionImpl.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/entity/ReadOnlyAccess.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/entity/TransactionalAccess.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/impl/BaseRegion.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/impl/BaseTransactionalDataRegion.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/impl/BaseGeneralDataRegion.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/collection/CollectionRegionImpl.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/collection/CollectionRegionImpl.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/collection/TransactionalAccess.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/timestamp/TimestampsRegionImpl.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/timestamp/TimestampTypeOverrides.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/access/PutFromLoadValidator.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/access/TransactionalAccessDelegate.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/query/QueryResultsRegionImpl.java\
 hibernate-infinispan/src/main/java/org/hibernate/cache/infinispan/tm/HibernateTransactionManagerLookup.java\
 hibernate-proxool/src/main/java/org/hibernate/service/jdbc/connections/internal/ProxoolConnectionProvider.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

# disable hibernate-tools support
rm -r hibernate-envers/src/main/java/org/hibernate/tool/ant/*.java \
  hibernate-envers/src/main/java/org/hibernate/envers/ant/*.java
sed -i "s|provided( |//provided(|" hibernate-envers/hibernate-envers.gradle

# require gradle maven plugin
# Caused by: org.gradle.api.InvalidUserDataException: You can't change a configuration which is not in unresolved state!
sed -i "s|provided( libraries.validation )|compile( libraries.validation )|" hibernate-c3p0/hibernate-c3p0.gradle
sed -i "s|provided( libraries.jandex )|compile( libraries.jandex )|" hibernate-core/hibernate-core.gradle
sed -i "s|provided( libraries.classmate )|compile( libraries.classmate )|" hibernate-core/hibernate-core.gradle
sed -i "s|provided( libraries.ant )|compile( libraries.ant )|" hibernate-core/hibernate-core.gradle
sed -i "s|provided( libraries.jacc )|compile( libraries.jacc )|" hibernate-core/hibernate-core.gradle
sed -i "s|provided( libraries.validation )|compile( libraries.validation )|" hibernate-core/hibernate-core.gradle
sed -i "s|all|//all|" hibernate-infinispan/hibernate-infinispan.gradle

# TODO test fails also for unavailable test deps, 
# should be updated the test deps list in each sub module
# e.g. Test testHHH6635(org.hibernate.test.c3p0.C3P0ConnectionProviderTest) FAILED: java.lang.NoClassDefFoundError: Could not initialize class com.arjuna.ats.internal.jts.OTSImpleManager
rm -r hibernate-c3p0/src/test/java/org \
 hibernate-core/src/test/java/org \
 hibernate-ehcache/src/test/java/org \
 hibernate-entitymanager/src/test/java/org \
 hibernate-envers/src/test/java/org \
 hibernate-infinispan/src/test/java/org \
 hibernate-proxool/src/test/java/org

sed -i "s|jboss-logging:3.1.0.GA|jboss-logging/jboss-logging:3.1.0.GA|" libraries.gradle
sed -i "s|mchange-commons|mchange-commons-java|" hibernate-c3p0/hibernate-c3p0.gradle
# require maven2/empty.jar for empty commons-logging:commons-logging:99.0-does-not-exist
sed -i "s|jcl_api:|//jcl_api:|" libraries.gradle
sed -i "s|jcl:|//jcl:|" libraries.gradle
sed -i "s|testRuntime( libraries.jcl_api )|//testRuntime( libraries.jcl_api )|" build.gradle
sed -i "s|testRuntime( libraries.jcl )|//testRuntime( libraries.jcl )|" build.gradle
 
%build

unset JAVA_HOME
export JAVA_HOME=%{_jvmdir}/java
export GRADLE_USER_HOME=$PWD SKIP_UNIT_TEST=true
mkdir -p gradlehome
# build buildSrc.jar
gradle --debug jar javadoc -g $PWD/gradlehome -b $PWD/buildSrc/build.gradle
# use buildReleaseBundles for aggregate javadoc
gradle --debug build buildReleaseBundles -g $PWD/gradlehome -b $PWD/build.gradle

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
for module in c3p0 core ehcache entitymanager envers infinispan proxool testing; do
    install -m 644 hibernate-${module}/target/libs/hibernate-${module}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/hibernate-${module}.jar
done

mkdir -p %{buildroot}%{_mavenpomdir}
# TODO use the poms files generated by gradle maven plugin
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP.%{name}-hibernate-c3p0.pom
%add_maven_depmap JPP.%{name}-hibernate-c3p0.pom %{name}/hibernate-c3p0.jar -f c3p0

install -pm 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP.%{name}-hibernate-core.pom
%add_maven_depmap JPP.%{name}-hibernate-core.pom %{name}/hibernate-core.jar

install -pm 644 %{SOURCE3} %{buildroot}%{_mavenpomdir}/JPP.%{name}-hibernate-ehcache.pom
%add_maven_depmap JPP.%{name}-hibernate-ehcache.pom %{name}/hibernate-ehcache.jar -f ehcache

install -pm 644 %{SOURCE4} %{buildroot}%{_mavenpomdir}/JPP.%{name}-hibernate-entitymanager.pom
%add_maven_depmap JPP.%{name}-hibernate-entitymanager.pom %{name}/hibernate-entitymanager.jar -f entitymanager

install -pm 644 %{SOURCE5} %{buildroot}%{_mavenpomdir}/JPP.%{name}-hibernate-envers.pom
%add_maven_depmap JPP.%{name}-hibernate-envers.pom %{name}/hibernate-envers.jar -f envers

install -pm 644 hibernate-infinispan-%{namedversion}.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-hibernate-infinispan.pom
%add_maven_depmap JPP.%{name}-hibernate-infinispan.pom %{name}/hibernate-infinispan.jar -f infinispan

install -pm 644 %{SOURCE7} %{buildroot}%{_mavenpomdir}/JPP.%{name}-hibernate-proxool.pom
%add_maven_depmap JPP.%{name}-hibernate-proxool.pom %{name}/hibernate-proxool.jar -f proxool

install -pm 644 hibernate-testing-%{namedversion}.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-hibernate-testing.pom
%add_maven_depmap JPP.%{name}-hibernate-testing.pom %{name}/hibernate-testing.jar -f testing

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp release/target/documentation/javadocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/hibernate-core.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-core.pom
%{_mavendepmapfragdir}/%{name}
%doc changelog.txt lgpl.txt LICENSE-2.0.txt README.md

%files javadoc
%{_javadocdir}/%{name}
%doc lgpl.txt LICENSE-2.0.txt

%files c3p0
%{_javadir}/%{name}/hibernate-c3p0.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-c3p0.pom
%{_mavendepmapfragdir}/%{name}-c3p0
%doc lgpl.txt

%files ehcache
%{_javadir}/%{name}/hibernate-ehcache.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-ehcache.pom
%{_mavendepmapfragdir}/%{name}-ehcache
%doc lgpl.txt LICENSE-2.0.txt

%files entitymanager
%{_javadir}/%{name}/hibernate-entitymanager.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-entitymanager.pom
%{_mavendepmapfragdir}/%{name}-entitymanager
%doc lgpl.txt

%files envers
%{_javadir}/%{name}/hibernate-envers.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-envers.pom
%{_mavendepmapfragdir}/%{name}-envers
%doc lgpl.txt LICENSE-2.0.txt

%files infinispan
%{_javadir}/%{name}/hibernate-infinispan.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-infinispan.pom
%{_mavendepmapfragdir}/%{name}-infinispan
%doc lgpl.txt LICENSE-2.0.txt

%files proxool
%{_javadir}/%{name}/hibernate-proxool.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-proxool.pom
%{_mavendepmapfragdir}/%{name}-proxool
%doc lgpl.txt LICENSE-2.0.txt

%files testing
%{_javadir}/%{name}/hibernate-testing.jar
%{_mavenpomdir}/JPP.%{name}-hibernate-testing.pom
%{_mavendepmapfragdir}/%{name}-testing
%doc lgpl.txt LICENSE-2.0.txt

%changelog
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.7-alt1_6jpp7
- new version

