Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# set to 0 provides a minimal test suite
%global with_tests 0

Name:          openjpa
Version:       2.4.0
Release:       alt1_3jpp8
Summary:       Java Persistence 2.0 API
# For a breakdown of the licensing, see NOTICE file
License:       ASL 2.0 and CDDL
Url:           http://openjpa.apache.org/
Source0:       http://www.apache.org/dist/openjpa/%{version}/%{name}-parent-%{version}-source-release.zip
# fix test failure
Patch0:        %{name}-2.2.0-persistence-jdbc-DynamicEnhancementSuite.patch
# Thanks to Robert Rati
Patch1:        %{name}-2.3.0-remove-WASRegistryManagedRuntime.patch
# No idea why this is needed, but compiler complains loudly without it:
# [ERROR] .../AnnotationPersistenceXMLMetaDataParser.java:[164,64] cannot find symbol
# [ERROR] symbol:   method booleanValue()
# [ERROR] location: class java.lang.Object
Patch2:        openjpa-2.4.0-java8.patch

BuildRequires: maven-local
BuildRequires: mvn(ant-contrib:ant-contrib)
BuildRequires: mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-dbcp:commons-dbcp)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(commons-pool:commons-pool)
BuildRequires: mvn(hsqldb:hsqldb:1)
BuildRequires: mvn(httpunit:httpunit)
BuildRequires: mvn(jakarta-regexp:jakarta-regexp)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(mysql:mysql-connector-java)
BuildRequires: mvn(net.sourceforge.serp:serp)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-jsch)
BuildRequires: mvn(org.apache.bval:bval-core)
BuildRequires: mvn(org.apache.bval:bval-jsr303)
BuildRequires: mvn(org.apache.commons:commons-jci-rhino)
BuildRequires: mvn(org.apache.derby:derby)
BuildRequires: mvn(org.apache.derby:derbyclient)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-validation_1.0_spec)
BuildRequires: mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.apache.xbean:xbean-finder)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
BuildRequires: mvn(org.jmock:jmock)
BuildRequires: mvn(org.jmock:jmock-junit3)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(postgresql:postgresql)
BuildRequires: mvn(simple-jndi:simple-jndi)

# Test deps
%if 0
# https://gil.fedorapeople.org/mariadb-java-client-1.1.8-1.fc20.src.rpm
BuildRequires: mvn(mariadb:mariadb-connector-java)
%endif

BuildArch:     noarch
Source44: import.info

%description
OpenJPA is Apache's implementation of Sun's Java Persistence 2.0 API
(JSR-317 JPA 2.0) specification for the transparent persistence of
Java objects.

It is an object-relational mapping (ORM) solution for the Java language,
which simplifies storing objects in databases.

%package tools
Group: Development/Java
Summary:       OpenJPA tools - Maven Plugin

%description tools
OpenJPA tasks for enhancing, SQL creation and
schema mapping creation using Apache maven.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-parent-%{version}
find . -name "*.class" -delete
find . -name "*.jar" -delete
# openjpa-kernel/internal-repository/com/ibm/websphere/websphere_uow_api/0.0.1/websphere_uow_api-0.0.1.jar
%patch0 -p0
%patch1 -p0
%patch2 -p1

# Remove deprecated stuff which don't build with Java8
rm -r %{name}-lib/src/main/java/org/apache/openjpa/lib/util/concurrent/NullSafeConcurrentHashMap.java \
 %{name}-lib/src/main/java/org/apache/openjpa/lib/util/concurrent/SizedConcurrentHashMap.java

%pom_disable_module %{name}
%pom_disable_module %{name}-all
%pom_disable_module %{name}-examples
%pom_disable_module %{name}-integration
%pom_disable_module %{name}-project
%pom_disable_module openbooks %{name}-examples

%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :ianal-maven-plugin
%pom_remove_plugin :taglist-maven-plugin
%pom_remove_plugin :apache-rat-plugin

%pom_remove_dep net.sourceforge.findbugs:annotations

%pom_xpath_remove "pom:profile[pom:id='ydoc-profile']"
# Remove testing profiles for unavailable drivers: 
# db2jcc informix-driver jcc-driver jdbc-driver jdbc-oracle jtds sqljdbc
%pom_xpath_remove "pom:profile[pom:id='test-sybase-jconnect']" %{name}-persistence-jdbc
%pom_xpath_remove "pom:profile[pom:id='test-soliddb']" %{name}-persistence-jdbc
for p in persistence-jdbc persistence-locking; do
%pom_xpath_remove "pom:profile[pom:id='test-custom']" %{name}-${p}
%pom_xpath_remove "pom:profile[pom:id='test-custom2']" %{name}-${p}
%pom_xpath_remove "pom:profile[pom:id='test-db2-jcc']" %{name}-${p}
%pom_xpath_remove "pom:profile[pom:id='test-derbyjcc']" %{name}-${p}
%pom_xpath_remove "pom:profile[pom:id='test-ids-jcc']" %{name}-${p}
%pom_xpath_remove "pom:profile[pom:id='test-ids-informix']" %{name}-${p}
%pom_xpath_remove "pom:profile[pom:id='test-ingres']" %{name}-${p}
%pom_xpath_remove "pom:profile[pom:id='test-mssql']" %{name}-${p}
%pom_xpath_remove "pom:profile[pom:id='test-oracle']" %{name}-${p}
%pom_xpath_remove "pom:profile[pom:id='test-sqlserver']" %{name}-${p}
%pom_xpath_remove "pom:profile[pom:id='test-sybase']" %{name}-${p}
done

%pom_remove_dep org.apache.geronimo.specs:geronimo-jpa_2.0_spec
%pom_xpath_inject "pom:project/pom:dependencyManagement/pom:dependencies" "
  <dependency>
    <groupId>org.hibernate.javax.persistence</groupId>
    <artifactId>hibernate-jpa-2.0-api</artifactId>
    <version>1.0.1.Final</version>
  </dependency>"

%pom_remove_dep com.ibm.websphere:websphere_uow_api %{name}-kernel
# Require non free com.ibm.websphere websphere_uow_api 0.0.1
rm %{name}-kernel/src/main/java/org/apache/openjpa/ee/WASRegistryManagedRuntime.java
# Remove bundled asm
%pom_xpath_set "pom:dependency[pom:groupId = 'org.apache.xbean']/pom:artifactId" xbean-finder %{name}-kernel
sed -i "s|org.apache.xbean.asm5|org.objectweb.asm|" \
 %{name}-kernel/src/main/java/org/apache/openjpa/enhance/AsmAdaptor.java
%pom_add_dep org.ow2.asm:asm:5.0.3 %{name}-kernel

# Use proper hsqldb version
%pom_xpath_inject "pom:dependency[pom:artifactId='hsqldb']" "<version>1</version>" %{name}-jdbc
%pom_xpath_set "pom:properties/pom:hsqldb.version" 1

# Use proper log4j version
%pom_xpath_set "pom:dependency[pom:groupId='log4j']/pom:version" 1.2.17 
%pom_xpath_set "pom:dependency[pom:groupId='log4j']/pom:version" 1.2.17 %{name}-tools/%{name}-maven-plugin
%pom_xpath_inject "pom:dependency[pom:groupId='log4j']" "<version>1.2.17</version>" %{name}-lib

# Fix jpa apis deps
for p in %{name}-jest \
  %{name}-persistence \
  %{name}-slice \
  %{name}-tools/%{name}-fetch-statistics \
  %{name}-tools/%{name}-maven-plugin \
  %{name}-tools/%{name}-maven-plugin/src/it/default_settings \
  %{name}-tools/%{name}-maven-plugin/src/it/dependingArtifact \
  %{name}-tools/%{name}-maven-plugin/src/it/nonDefaultPersistenceXml \
  %{name}-tools/%{name}-maven-plugin/src/it/testDependencies \
  ; do
%pom_remove_dep org.apache.geronimo.specs:geronimo-jpa_2.0_spec ${p}
%pom_add_dep org.hibernate.javax.persistence:hibernate-jpa-2.0-api:1.0.1.Final ${p}
done

# Break build in f>=19
%pom_remove_plugin :maven-invoker-plugin %{name}-tools/%{name}-maven-plugin

# Fix bval deps
%pom_xpath_set "pom:dependency[pom:groupId='org.apache.bval']/pom:artifactId" bval-core
%pom_xpath_set "pom:dependency[pom:groupId='org.apache.bval']/pom:artifactId" bval-core %{name}-tools/%{name}-maven-plugin
%pom_add_dep org.apache.bval:bval-jsr303:0.5 %{name}-tools/%{name}-maven-plugin

# Force servlet 3.1 apis
%pom_xpath_set "pom:dependency[pom:groupId='javax.servlet']/pom:artifactId" javax.servlet-api %{name}-jest
%pom_xpath_set "pom:dependency[pom:groupId='javax.servlet']/pom:version" 3.1.0 %{name}-jest

%mvn_package ":%{name}-tools" tools
%mvn_package ":%{name}-maven-plugin" tools
%mvn_package ":%{name}-fetch-statistics" tools
%mvn_package ":%{name}-fetch-statistics-was" tools

%build

# test random fails
%mvn_build -- \
%if %{with_tests}
  -Ptest-derby \
%else
  -Dtest=false \
%endif
  -DfailIfNoTests=false \
  -Dmaven.test.failure.ignore=true \
  process-resources

%install
%mvn_install

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant %{name}/%{name}-jdbc %{name}/%{name}-kernel %{name}/%{name}-lib" > %{name}-ant
install -p -m 644 %{name}-ant %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%doc README.txt
%doc LICENSE NOTICE

%files tools -f .mfiles-tools
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_3jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_1jpp8
- java 8 mass update

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

