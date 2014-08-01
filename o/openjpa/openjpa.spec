Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# set to 0 provides a minimal test suite
%global with_tests 0

Name:          openjpa
Version:       2.2.1
Release:       alt1_4jpp7
Summary:       Java Persistence 2.0 API
Group:         Development/Java
# # For a breakdown of the licensing, see NOTICE file
License:       ASL 2.0 and CDDL
Url:           http://openjpa.apache.org/
Source0:       ftp://ftp.gbnet.net/pub/apache/dist/%{name}/%{version}/apache-%{name}-%{version}-source.zip
# force tomcat 7.x apis
Source1:       %{name}-2.2.0-depmap
# fix test failure
Patch0:        %{name}-2.2.0-persistence-jdbc-DynamicEnhancementSuite.patch
# remove testing profiles for unavailable drivers: db2jcc informix-driver jcc-driver jdbc-driver jdbc-oracle jtds sqljdbc
Patch1:        %{name}-2.2.0-remove-test-profiles.patch

BuildRequires: jpackage-utils

BuildRequires: apache-rat-plugin
BuildRequires: buildnumber-maven-plugin
BuildRequires: javacc-maven-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

# maven-antrun-plugin deps
BuildRequires: ant-contrib
BuildRequires: ant-jsch

BuildRequires: ant
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-dbcp
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-pool
BuildRequires: bval
BuildRequires: felix-osgi-core
BuildRequires: geronimo-jms
BuildRequires: geronimo-jta
BuildRequires: geronimo-validation
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jaxb-api
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: hsqldb
BuildRequires: log4j
BuildRequires: maven-local
BuildRequires: objectweb-asm
BuildRequires: plexus-utils
BuildRequires: postgresql-jdbc
BuildRequires: serp
BuildRequires: slf4j
BuildRequires: tomcat-servlet-3.0-api

# test deps
BuildRequires: apache-commons-jci-rhino
BuildRequires: derby
BuildRequires: httpunit
BuildRequires: jmock
#BuildRequires: jtds
BuildRequires: junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: mysql-connector-java
BuildRequires: regexp
BuildRequires: simple-jndi

Requires:      ant
Requires:      apache-commons-collections
Requires:      apache-commons-dbcp
Requires:      apache-commons-lang
Requires:      apache-commons-logging
Requires:      apache-commons-pool
Requires:      felix-osgi-core
Requires:      geronimo-jms
Requires:      geronimo-jta
Requires:      geronimo-validation
Requires:      glassfish-jaxb
Requires:      glassfish-jaxb-api
Requires:      hibernate-jpa-2.0-api
Requires:      hsqldb
Requires:      log4j
Requires:      objectweb-asm
Requires:      postgresql-jdbc
Requires:      serp
Requires:      slf4j
# servlet-api 2.4
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
OpenJPA is Apache's implementation of Sun's Java Persistence 2.0 API
(JSR-317 JPA 2.0) specification for the transparent persistence of
Java objects.

It is an object-relational mapping (ORM) solution for the Java language,
which simplifies storing objects in databases.

%package tools
Group:         Development/Java
Summary:       OpenJPA tools - Maven Plugin
Requires:      maven
Requires:      bval
Requires:      geronimo-validation
Requires:      hibernate-jpa-2.0-api
Requires:      log4j
Requires:      plexus-utils
Requires:      jpackage-utils
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description tools
OpenJPA tasks for enhancing, SQL creation and
schema mapping creation using Apache maven.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n apache-openjpa-%{version}-source
find . -name "*.class" -delete
find . -name "*.jar" -delete

%pom_remove_plugin com.agilejava.docbkx:docbkx-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:ianal-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin

%pom_remove_dep net.sourceforge.findbugs:annotations

%pom_remove_dep org.apache.geronimo.specs:geronimo-jpa_2.0_spec
%pom_xpath_inject "pom:project/pom:dependencyManagement/pom:dependencies" "
  <dependency>
    <groupId>org.hibernate.javax.persistence</groupId>
    <artifactId>hibernate-jpa-2.0-api</artifactId>
    <version>1.0.1.Final</version>
  </dependency>"
%pom_remove_dep org.apache.bval:org.apache.bval.bundle
%pom_xpath_inject "pom:project/pom:dependencyManagement/pom:dependencies" "
  <dependency>
    <groupId>org.apache.bval</groupId>
    <artifactId>bval-core</artifactId>
    <version>0.5</version>
  </dependency>
  <dependency>
    <groupId>org.apache.bval</groupId>
    <artifactId>bval-jsr303</artifactId>
    <version>0.5</version>
  </dependency>"

%pom_remove_dep com.ibm.websphere:websphere_uow_api openjpa-kernel
# require non free com.ibm.websphere websphere_uow_api 0.0.1
rm openjpa-kernel/src/main/java/org/apache/openjpa/ee/WASRegistryManagedRuntime.java
rm openjpa-kernel/src/main/java/org/apache/openjpa/ee/AutomaticManagedRuntime.java

for p in kernel persistence; do
%pom_remove_dep org.osgi:org.osgi.core openjpa-${p}
%pom_xpath_inject "pom:project/pom:dependencies" "
  <dependency>
    <groupId>org.apache.felix</groupId>
    <artifactId>org.osgi.core</artifactId>
    <version>1.4.0</version>
    <scope>provided</scope>
  </dependency>" openjpa-${p}
done

for p in openjpa-jest \
  openjpa-persistence \
  openjpa-tools/openjpa-maven-plugin \
  openjpa-tools/openjpa-maven-plugin/src/it/default_settings \
  openjpa-tools/openjpa-maven-plugin/src/it/dependingArtifact \
  openjpa-tools/openjpa-maven-plugin/src/it/nonDefaultPersistenceXml \
  openjpa-tools/openjpa-maven-plugin/src/it/testDependencies \
  ; do
%pom_remove_dep org.apache.geronimo.specs:geronimo-jpa_2.0_spec ${p}
%pom_xpath_inject "pom:project/pom:dependencies" "
  <dependency>
    <groupId>org.hibernate.javax.persistence</groupId>
    <artifactId>hibernate-jpa-2.0-api</artifactId>
    <version>1.0.1.Final</version>
  </dependency>" ${p}
done

%pom_remove_dep org.apache.geronimo.specs:geronimo-jpa_2.0_spec openjpa-slice
%pom_xpath_inject "pom:project/pom:dependencies" "
  <dependency>
    <groupId>org.hibernate.javax.persistence</groupId>
    <artifactId>hibernate-jpa-2.0-api</artifactId>
    <version>1.0.1.Final</version>
    <scope>test</scope>
  </dependency>" openjpa-slice

%pom_remove_dep org.apache.bval:org.apache.bval.bundle openjpa-tools/openjpa-maven-plugin
%pom_xpath_inject "pom:project/pom:dependencies" "
  <dependency>
    <groupId>org.apache.bval</groupId>
    <artifactId>bval-core</artifactId>
    <version>0.5</version>
  </dependency>
  <dependency>
    <groupId>org.apache.bval</groupId>
    <artifactId>bval-jsr303</artifactId>
    <version>0.5</version>
  </dependency>" openjpa-tools/openjpa-maven-plugin

%patch0 -p0
%patch1 -p1
# in f17 buildnumber dont work
#om_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin


%pom_disable_module openjpa
%pom_disable_module openjpa-all
%pom_disable_module openjpa-examples
%pom_disable_module openjpa-integration
%pom_disable_module openjpa-project
%pom_disable_module openbooks openjpa-examples

# break build in f19
%pom_remove_plugin :maven-invoker-plugin openjpa-tools/openjpa-maven-plugin

%build
# test random fails

mvn-rpmbuild -e \
%if %{with_tests}
  -Ptest-derby \
%else
  -Dtest=false \
%endif
  -DfailIfNoTests=false \
  -Dmaven.test.failure.ignore=true \
  -Dmaven.local.depmap.file="%{SOURCE1}" \
  install javadoc:aggregate process-resources

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

mkdir -p %{buildroot}%{_javadir}/%{name}
for m in jdbc \
  jest \
  kernel \
  lib \
  persistence \
  persistence-jdbc \
  persistence-locking \
  slice \
  xmlstore;do
    install -m 644 %{name}-${m}/target/%{name}-${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
    install -pm 644 %{name}-${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
    %add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

install -pm 644 %{name}-tools/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-tools.pom
%add_maven_depmap -f tools JPP.%{name}-tools.pom
install -pm 644 %{name}-tools/%{name}-maven-plugin/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-maven-plugin.pom
install -m 644 %{name}-tools/%{name}-maven-plugin/target/%{name}-maven-plugin-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}/maven-plugin.jar
%add_maven_depmap -f tools JPP.%{name}-maven-plugin.pom %{name}/maven-plugin.jar -a "org.codehaus.mojo:openjpa-maven-plugin"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant %{name}/jdbc %{name}/kernel %{name}/lib" > %{name}-ant
install -p -m 644 %{name}-ant %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jdbc.jar
%{_javadir}/%{name}/jest.jar
%{_javadir}/%{name}/kernel.jar
%{_javadir}/%{name}/lib.jar
%{_javadir}/%{name}/persistence.jar
%{_javadir}/%{name}/persistence-jdbc.jar
%{_javadir}/%{name}/persistence-locking.jar
%{_javadir}/%{name}/slice.jar
%{_javadir}/%{name}/xmlstore.jar
%{_mavenpomdir}/JPP.%{name}-jdbc.pom
%{_mavenpomdir}/JPP.%{name}-jest.pom
%{_mavenpomdir}/JPP.%{name}-kernel.pom
%{_mavenpomdir}/JPP.%{name}-lib.pom
%{_mavenpomdir}/JPP.%{name}-parent.pom
%{_mavenpomdir}/JPP.%{name}-persistence.pom
%{_mavenpomdir}/JPP.%{name}-persistence-jdbc.pom
%{_mavenpomdir}/JPP.%{name}-persistence-locking.pom
%{_mavenpomdir}/JPP.%{name}-slice.pom
%{_mavenpomdir}/JPP.%{name}-xmlstore.pom
%{_mavendepmapfragdir}/%{name}
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%doc CHANGES.txt LICENSE NOTICE README.txt RELEASE-NOTES.html

%files tools
%{_javadir}/%{name}/maven-plugin.jar
%{_mavenpomdir}/JPP.%{name}-tools.pom
%{_mavenpomdir}/JPP.%{name}-maven-plugin.pom
%{_mavendepmapfragdir}/%{name}-tools
%doc LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt1_4jpp7
- new version

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_3jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt1_2jpp7
- fc version

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt6_1jpp5
- fixed build

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt5_1jpp5
- fixed build with new javacc5

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt4_1jpp5
- selected java5 compiler explicitly

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_1jpp5
- fixed docdir ownership

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_1jpp5
- first build

