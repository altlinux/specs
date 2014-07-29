Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          activeio
Version:       3.1.4
Release:       alt1_5jpp7
Summary:       Apache ActiveMQ ActiveIO :: Core
Group:         Development/Java
License:       ASL 2.0
Url:           http://activemq.apache.org/
# svn export http://svn.apache.org/repos/asf/activemq/activeio/tags/activeio-parent-3.1.4/ activeio-3.1.4
# tar czf activeio-3.1.4-src-svn.tar.gz activeio-3.1.4
Source0:       activeio-3.1.4-src-svn.tar.gz
# build fix for howl-logger 1.0.2
Patch0:        activeio-3.1.4-howl-logger.patch

BuildRequires: jpackage-utils

BuildRequires: apache-commons-logging
%if 0
BuildRequires: howl-logger
%endif
BuildRequires: jboss-j2eemgmt-1.1-api

BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      apache-commons-logging
%if 0
Requires:      howl-logger
%endif
Requires:      jboss-j2eemgmt-1.1-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
A high performance IO abstraction framework.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%pom_remove_plugin org.codehaus.mojo:ianal-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-assembly-plugin

%pom_remove_dep org.apache.geronimo.specs:geronimo-j2ee-management_1.1_spec
%pom_xpath_inject "pom:project/pom:dependencyManagement/pom:dependencies" "
    <dependency>
      <groupId>org.jboss.spec.javax.management.j2ee</groupId>
      <artifactId>jboss-j2eemgmt-api_1.1_spec</artifactId>
      <version>1.0.1.Final</version>
    </dependency>"

%pom_remove_plugin org.codehaus.mojo:rat-maven-plugin
%pom_xpath_inject "pom:project/pom:build/pom:pluginManagement/pom:plugins" "
        <plugin>
          <groupId>org.apache.rat</groupId>
          <artifactId>apache-rat-plugin</artifactId>
          <version>0.8-SNAPSHOT</version>
          <configuration>
            <excludeSubProjects>false</excludeSubProjects>
          </configuration>
        </plugin>"

%pom_remove_dep org.apache.geronimo.specs:geronimo-j2ee-management_1.1_spec %{name}-core/pom.xml
%pom_xpath_inject "pom:project/pom:dependencies" "
    <dependency>
      <groupId>org.jboss.spec.javax.management.j2ee</groupId>
      <artifactId>jboss-j2eemgmt-api_1.1_spec</artifactId>
      <version>1.0.1.Final</version>
    </dependency>"  %{name}-core/pom.xml

%pom_xpath_inject "pom:project/pom:dependencies" "
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.10</version>
      <scope>test</scope>
    </dependency>" %{name}-core/pom.xml

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
%pom_xpath_inject "pom:project/pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
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
        </executions>
      </plugin>" %{name}-core/pom.xml
%endif

sed -i 's/\r//' NOTICE

%build

mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}/activemq
install -m 644 %{name}-core/target/%{name}-core-%{version}.jar \
   %{buildroot}%{_javadir}/activemq/%{name}-core.jar
install -m 644 %{name}-core/target/%{name}-core-%{version}-tests.jar \
   %{buildroot}%{_javadir}/activemq/%{name}-core-tests.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.activemq-%{name}-parent.pom
%add_maven_depmap JPP.activemq-%{name}-parent.pom
install -pm 644 %{name}-core/pom.xml %{buildroot}%{_mavenpomdir}/JPP.activemq-%{name}-core.pom
%add_maven_depmap JPP.activemq-%{name}-core.pom activemq/%{name}-core.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/activemq/%{name}-core*.jar
%{_mavenpomdir}/JPP.activemq-%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
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

