BuildRequires: maven-plugin-plugin
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# set to 0 provides a minimal test suite
%global with_tests 0
Name:          openjpa
Version:       2.2.0
Release:       alt3_2jpp7
Summary:       Java Persistence 2.0 API
Group:         Development/Java
# # For a breakdown of the licensing, see NOTICE file
License:       ASL 2.0 and CDDL
Url:           http://openjpa.apache.org/
Source0:       ftp://ftp.gbnet.net/pub/apache/dist/%{name}/%{version}/apache-%{name}-%{version}-source.zip
# force tomcat 7.x apis
Source1:       %{name}-%{version}-depmap

# remove org.codehaus.mojo ianal-maven-plugin 1.0-alpha-1
Patch0:        %{name}-%{version}-remove-ianal-plugin.patch
# remove unavailable deps
Patch1:        %{name}-%{version}-parent-pom.patch
Patch2:        %{name}-%{version}-remove-checkstyle-plugin.patch
# remove com.ibm.websphere websphere_uow_api 0.0.1
# change org.osgi org.osgi.core 4.2.0 in org.apache.felix 1.4.0
Patch3:        %{name}-%{version}-kernel-pom.patch
# remove unavailable test deps org.jmock jmock jmock-junit3 2.5.1
Patch4:        %{name}-%{version}-jdbc-pom.patch
# change 
#   org.osgi org.osgi.core 4.2.0 in org.apache.felix 1.4.0
#   org.apache.geronimo.specs geronimo-jpa_2.0_spec 1.1 with org.hibernate.javax.persistence hibernate-jpa-2.0-api 1.0.1.Final
Patch5:        %{name}-%{version}-persistence-pom.patch
# fix test failure
Patch6:        %{name}-%{version}-persistence-jdbc-DynamicEnhancementSuite.patch
# replace 
#   org.apache.bval org.apache.bval.bundle with bval-core and bval-jsr303
#   org.apache.geronimo.specs geronimo-jpa_2.0_spec with org.hibernate.javax.persistence hibernate-jpa-2.0-api
Patch7:        %{name}-%{version}-maven-plugin-pom.patch
Patch8:        %{name}-%{version}-slice-pom.patch
Patch9:        %{name}-%{version}-jest-pom.patch
Patch10:       %{name}-%{version}-tools-it-poms.patch
# remove testing profiles for unavailable drivers: db2jcc informix-driver jcc-driver jdbc-driver jdbc-oracle jtds sqljdbc
Patch11:       %{name}-%{version}-remove-test-profiles.patch

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
BuildRequires: felix-osgi-core
BuildRequires: geronimo-jms
BuildRequires: geronimo-jta
BuildRequires: geronimo-validation
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jaxb-api
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: log4j
BuildRequires: objectweb-asm
BuildRequires: postgresql-jdbc
BuildRequires: serp
BuildRequires: slf4j
BuildRequires: tomcat-servlet-3.0-api

# test deps
BuildRequires: apache-commons-jci-rhino
BuildRequires: derby
BuildRequires: hsqldb
BuildRequires: httpunit
#BuildRequires: jtds
BuildRequires: junit
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
BuildRequires: bval
BuildRequires: plexus-utils
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

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p1

sed -i "s|<module>openjpa</module>|<!--module>openjpa</module-->|" pom.xml
sed -i "s|<module>openjpa-all</module>|<!--module>openjpa-all</module-->|" pom.xml
sed -i "s|<module>openjpa-examples</module>|<!--module>openjpa-examples</module-->|" pom.xml
sed -i "s|<module>openjpa-integration</module>|<!--module>openjpa-integration</module-->|" pom.xml
sed -i "s|<module>openjpa-project</module>|<!--module>openjpa-project</module-->|" pom.xml
sed -i "s|<module>openbooks</module>|<!--module>openbooks</module-->|" openjpa-examples/pom.xml

# require non free com.ibm.websphere websphere_uow_api 0.0.1
rm openjpa-kernel/src/main/java/org/apache/openjpa/ee/WASRegistryManagedRuntime.java
rm openjpa-kernel/src/main/java/org/apache/openjpa/ee/AutomaticManagedRuntime.java

# require unavailable jmock
rm -r openjpa-jdbc/src/test/java/org/apache/openjpa/jdbc/sql/*

%build
# test random fails
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
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

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
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

