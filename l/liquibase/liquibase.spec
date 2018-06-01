Group: Databases
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: liquibase
Summary: Database Refactoring Tool
Version: 3.6.1
Release: alt1_1jpp8
License: ASL 2.0
URL: http://www.liquibase.org

Source0: https://github.com/liquibase/liquibase/archive/%{name}-parent-%{version}.tar.gz

BuildRequires: java-devel >= 1.6.0
BuildRequires: javapackages-tools
BuildRequires: maven-local
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.servlet:servlet-api)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.felix:org.apache.felix.framework)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.yaml:snakeyaml)

BuildArch:     noarch

Requires: javapackages-tools
Requires: mvn(ch.qos.logback:logback-classic)
Requires: mvn(commons-cli:commons-cli)
Requires: mvn(org.apache.felix:org.apache.felix.framework)
Requires: mvn(org.slf4j:slf4j-api)
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
Requires: %{name} = %{version}-%{release}
Requires: mvn(javax.enterprise:cdi-api)
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
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)
Requires: %{name} = %{version}-%{release}
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
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
rm -r %{name}-core/src/main/resources/liquibase/sdk
rm -r %{name}-core/src/main/resources/assembly
rm -r %{name}-core/src/main/resources/dist

%pom_disable_module %{name}-integration-tests
%pom_disable_module %{name}-debian
%pom_disable_module %{name}-rpm

# Use Maven 3 APIs only
%pom_change_dep -r :maven-project :maven-compat

# Unavailable plugin
%pom_remove_plugin -r :gmaven-plugin
# Unwanted tasks or tasks that break the build
%pom_remove_plugin -r :maven-assembly-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-deploy-plugin

%pom_remove_dep -r org.osgi:org.osgi.core
%pom_add_dep org.apache.felix:org.apache.felix.framework %{name}-core

# Disable test jar
%pom_xpath_remove "pom:finalName" %{name}-core

# Symlink liquibase/liquibase-core.jar to liquibase.jar
%mvn_file :%{name}-core %{name}/%{name}-core %{name}


%build
# No tests (-f) and singleton packaging (-s) (i.e. one artifact per package)
%mvn_build -s -f


%install
%mvn_install
%jpackage_script liquibase.integration.commandline.Main "" "" %{name}/%{name}-core:logback/logback-core:logback/logback-classic:slf4j/slf4j-api %{name} true
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 %{name}-rpm/src/main/resources/%{name}.1 %{buildroot}%{_mandir}/man1/

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf


%files -f .mfiles-%{name}-core
%doc changelog.txt %{name}-core/DEV_NOTES.txt
%doc --no-dereference LICENSE.txt
%doc %{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%files parent -f .mfiles-%{name}-parent
%doc --no-dereference LICENSE.txt

%files cdi -f .mfiles-%{name}-cdi
%doc --no-dereference LICENSE.txt

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%changelog
* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.6.1-alt1_1jpp8
- java update

* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 3.5.3-alt1_4jpp8
- java update

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.5.3-alt1_1jpp8
- new version

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

