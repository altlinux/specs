Group: Databases
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name: liquibase
Summary: Database Refactoring Tool
Version: 3.5.1
Release: alt1_1jpp8
License: ASL 2.0
URL: http://www.liquibase.org

Source0: https://github.com/liquibase/liquibase/archive/%{name}-parent-%{version}.tar.gz

BuildRequires: felix-framework
BuildRequires: felix-osgi-core
BuildRequires: java-devel >= 1.6.0
BuildRequires: maven-local
BuildRequires: maven-local
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.servlet:servlet-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.derby:derby)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.hsqldb:hsqldb)
BuildRequires: mvn(org.hsqldb:hsqldb)
BuildRequires: mvn(org.jboss.weld.se:weld-se)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.yaml:snakeyaml)

BuildArch:     noarch

Requires: mvn(org.yaml:snakeyaml) >= 0:1.13
Source44: import.info

%description
LiquiBase is an open source (Apache 2.0 License), database-independent library
for tracking, managing and applying database changes. It is built on a simple
premise: All database changes are stored in a human readable but tracked in
source control.


%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch
%description javadoc
This package contains %{summary}.


%package cdi
Group: Databases
Summary: Liquibase CDI
%description cdi
Liquibase CDI extension.


%package parent
Group: Databases
Summary: Liquibase Parent Configuration POM
%description parent
This package contains the %{summary}.


%package maven-plugin
Group: Development/Java
Summary: Maven plugin for %{name}
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven:maven-core)
Requires: %{name} = %{version}
Requires: maven

%description maven-plugin
%{summary}.

%prep
%setup -q -n %{name}-%{name}-parent-%{version}

find -name "*.bat" -print -delete
find -name "*.class" -print -delete
find -name "*.jar" -print -delete
# Do not bundle javascript libraries and fonts
find -name "*.js" -print -delete
rm -r %{name}-core/src/main/resources/liquibase/sdk/watch/{css,fonts}
rm -r %{name}-core/src/main/resources/assembly
rm -r %{name}-core/src/main/resources/dist

%pom_disable_module %{name}-integration-tests
%pom_disable_module %{name}-debian
%pom_disable_module %{name}-rpm

# Use Maven 3 APIs only
%pom_change_dep -r :maven-project :maven-compat
# Add missing test dep
%pom_add_dep junit:junit:4.12:test %{name}-maven-plugin

# Unavailable plugin
%pom_remove_plugin -r :gmaven-plugin
# Unwanted tasks
%pom_remove_plugin -r :maven-assembly-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

%pom_change_dep -r org.springframework:spring :spring-core
%pom_add_dep org.springframework:spring-beans %{name}-core
%pom_add_dep org.springframework:spring-context %{name}-core
%pom_add_dep org.apache.felix:org.apache.felix.framework %{name}-core

# Remove all test dependencies.  We aren't running tests with this build.
%pom_xpath_remove "pom:dependency[pom:scope = 'test' ]" %{name}-core
rm -r %{name}-core/src/test/*
# Disable test jar
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-jar-plugin' ]/pom:executions" %{name}-core

# Drop pre-existent manifest file and prevent OutOfMemoryError
rm %{name}-core/src/main/resources/META-INF/MANIFEST.MF

%pom_xpath_remove "pom:finalName" %{name}-core
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 %{name}-core '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Liquibase-Package>liquibase.change,liquibase.changelog,liquibase.database,liquibase.parser,liquibase.precondition,liquibase.datatype,liquibase.serializer,liquibase.sqlgenerator,liquibase.executor,liquibase.snapshot,liquibase.logging,liquibase.diff,liquibase.structure,liquibase.structurecompare,liquibase.lockservice,liquibase.sdk.database,liquibase.ext</Liquibase-Package>
    <Main-Class>liquibase.integration.commandline.Main</Main-Class>
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
%pom_xpath_set pom:manifestFile '${project.build.outputDirectory}/META-INF/MANIFEST.MF' %{name}-core

# Symlink liquibase/liquibase-core.jar to liquibase.jar
%mvn_file :%{name}-core %{name}/%{name}-core %{name}


%build
%mvn_build -s -f


%install
%mvn_install
%jpackage_script liquibase.integration.commandline.Main "" "" %{name}/%{name}-core %{name} true
%__mkdir_p %{buildroot}%{_mandir}/man1
install -pm 0644 %{name}-rpm/src/main/resources/%{name}.1 %{buildroot}%{_mandir}/man1/

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf


%files -f .mfiles-%{name}-core
%doc changelog.txt %{name}-core/DEV_NOTES.txt
%doc LICENSE.txt
%doc %{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%files parent -f .mfiles-%{name}-parent
%doc LICENSE.txt

%files cdi -f .mfiles-%{name}-cdi
%doc LICENSE.txt

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1_1jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 3.4.1-alt1_1jpp8
- new version

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.7-alt1_4jpp7
- update

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_2jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1_8jpp7
- new version

