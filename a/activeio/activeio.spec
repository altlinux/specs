BuildRequires: apache-parent
Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          activeio
Version:       3.1.4
Release:       alt2_15jpp8
Summary:       Apache ActiveMQ ActiveIO :: Core
License:       ASL 2.0
Url:           http://activemq.apache.org/
# svn export http://svn.apache.org/repos/asf/activemq/activeio/tags/activeio-parent-3.1.4/ activeio-3.1.4
# tar czf activeio-3.1.4-src-svn.tar.gz activeio-3.1.4
Source0:       activeio-3.1.4-src-svn.tar.gz
# build fix for howl-logger 1.0.2
Patch0:        activeio-3.1.4-howl-logger.patch

BuildRequires: maven-local
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.jboss.spec.javax.management.j2ee:jboss-j2eemgmt-api_1.1_spec)
%if 0
BuildRequires: mvn(org.objectweb.howl:howl)
%endif

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


%pom_change_dep -r :geronimo-j2ee-management_1.1_spec org.jboss.spec.javax.management.j2ee:jboss-j2eemgmt-api_1.1_spec:1.0.1.Final

%pom_add_dep junit:junit::test %{name}-core

# TODO remove when howl-logger is available
%pom_remove_dep -r howl:howl-logger

%if 0
%pom_xpath_set "pom:properties/pom:howl-version" 1.0.2
%pom_change_dep -r :howl-logger org.objectweb.howl:howl:'${howl-version}'
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

%pom_remove_plugin :maven-bundle-plugin
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 %{name}-core '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-Name>${project.artifactId}</Bundle-Name>
    <Bundle-SymbolicName>${activeio.osgi.symbolic.name}</Bundle-SymbolicName>
    <Implementation-Title>Apache ActiveIO</Implementation-Title>
    <Implementation-Version>${project.version}</Implementation-Version>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%pom_remove_plugin :maven-jar-plugin %{name}-core
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin: %{name}-core "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    <manifest>
      <addDefaultImplementationEntries>true</addDefaultImplementationEntries>
      <addDefaultSpecificationEntries>true</addDefaultSpecificationEntries>
    </manifest>
  </archive>
</configuration>
<executions>
  <execution>
    <goals>
      <goal>test-jar</goal>
    </goals>
  </execution>
</executions>"

sed -i 's/\r//' NOTICE

%mvn_file :%{name}-core activemq/%{name}-core
%mvn_package :%{name}-core::tests:

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.1.4-alt2_15jpp8
- added BR: apache-parent for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.1.4-alt1_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.1.4-alt1_14jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.1.4-alt1_13jpp8
- bugfix release

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

