Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          activeio
Version:       3.1.4
Release:       alt1_11jpp8
Summary:       Apache ActiveMQ ActiveIO :: Core
License:       ASL 2.0
Url:           http://activemq.apache.org/
# svn export http://svn.apache.org/repos/asf/activemq/activeio/tags/activeio-parent-3.1.4/ activeio-3.1.4
# tar czf activeio-3.1.4-src-svn.tar.gz activeio-3.1.4
Source0:       activeio-3.1.4-src-svn.tar.gz
# build fix for howl-logger 1.0.2
Patch0:        activeio-3.1.4-howl-logger.patch

BuildRequires: apache-commons-logging
%if 0
BuildRequires: howl-logger
%endif
BuildRequires: jboss-j2eemgmt-1.1-api
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle

BuildArch:     noarch
Source44: import.info

%description
A high performance IO abstraction framework.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%pom_remove_plugin :ianal-maven-plugin
%pom_remove_plugin :rat-maven-plugin
%pom_remove_plugin :taglist-maven-plugin
%pom_remove_plugin :maven-assembly-plugin

%pom_remove_dep org.apache.geronimo.specs:geronimo-j2ee-management_1.1_spec
%pom_xpath_inject "pom:project/pom:dependencyManagement/pom:dependencies" "
<dependency>
  <groupId>org.jboss.spec.javax.management.j2ee</groupId>
  <artifactId>jboss-j2eemgmt-api_1.1_spec</artifactId>
  <version>1.0.1.Final</version>
</dependency>"

%pom_remove_dep org.apache.geronimo.specs:geronimo-j2ee-management_1.1_spec %{name}-core
%pom_add_dep org.jboss.spec.javax.management.j2ee:jboss-j2eemgmt-api_1.1_spec %{name}-core

%pom_add_dep junit:junit::test %{name}-core

# TODO remove when howl-logger is available
%pom_remove_dep howl:howl-logger
%pom_remove_dep howl:howl-logger %{name}-core/pom.xml
%if 0
sed -i "s|<howl-version>0.1.8|<howl-version>1.0.2|" pom.xml
%pom_xpath_inject "pom:project/pom:dependencyManagement/pom:dependencies" '
<dependency>
  <groupId>org.objectweb.howl</groupId>
  <artifactId>howl</artifactId>
  <version>${howl-version}</version>
</dependency>'
%pom_xpath_inject "pom:project/pom:dependencies" "
<dependency>
  <groupId>org.objectweb.howl</groupId>
  <artifactId>howl</artifactId>
  <optional>true</optional>
</dependency>" %{name}-core/pom.xml
%patch0 -p0
%else
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin  %{name}-core "
<executions>
  <execution>
    <id>default-compile</id>
    <phase>compile</phase>
    <configuration>
      <excludes>
	<exclude>**/HowlJournal.*</exclude>
      </excludes>
    </configuration>
    <goals>
      <goal>compile</goal>
    </goals>
  </execution>
  <execution>
    <id>default-testCompile</id>
    <phase>test-compile</phase>
    <configuration>
      <testExcludes>
	<exclude>**/JournalPerfTool.*</exclude>
      </testExcludes>
    </configuration> 
    <goals>
      <goal>testCompile</goal>
    </goals>
  </execution>
</executions>"
%endif

sed -i 's/\r//' NOTICE

%mvn_file :%{name}-core activemq/%{name}-core

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

install -m 644 %{name}-core/target/%{name}-core-%{version}-tests.jar \
   %{buildroot}%{_javadir}/activemq/%{name}-core-tests.jar
   
%files -f .mfiles
%{_javadir}/activemq/%{name}-core-tests.jar
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.1.4-alt1_11jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.4-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.4-alt1_5jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.4-alt1_3jpp7
- new version

* Wed Jun 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_3jpp5
- test src/test/org/activeio/ChannelFactoryTest.java was too long idle

* Sun Feb 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_3jpp5
- fixed build with maven 2.0.7

* Tue Dec 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

