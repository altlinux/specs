# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# Provide an option to build the Maven plugin.  As far as I can tell, RPM versions
# of Maven plugins are only really useful as BuildRequires for other RPMs and it's
# unlikely that an RPM would need to run Liquibase during its build process.
#def_with maven_plugin
%bcond_with maven_plugin

Name: liquibase
Summary: Database Refactoring Tool
Version: 3.4.1
Release: alt1_1jpp8
License: ASL 2.0
Group: Databases

# Liquibase does not distribute source releases. To generate:
#   git clone https://github.com/liquibase/liquibase.git
#   cd liquibase/
#   git archive --format=tar.gz --prefix=liquibase-3.4.1/ liquibase-parent-3.4.1 > liquibase-3.4.1.tar.gz
Source0: %{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: maven-local
BuildRequires: servlet
BuildRequires: snakeyaml >= 0:1.13
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.jboss.weld.se:weld-se)
BuildRequires: mvn(org.apache.commons:commons-cli)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires: mvn(javax.enterprise:cdi-api)

Requires: maven-local
Requires: servlet
Requires: snakeyaml >= 0:1.13
Requires: mvn(org.springframework:spring-context)
Requires: mvn(org.springframework:spring-beans)
Requires: mvn(org.springframework:spring-core)
Requires: mvn(org.jboss.weld.se:weld-se)
Requires: mvn(org.apache.commons:commons-cli)
Requires: mvn(org.apache.velocity:velocity)
Requires: mvn(org.eclipse.jetty:jetty-servlet)
Requires: mvn(javax.enterprise:cdi-api)

BuildArch: noarch
Url: http://liquibase.org/
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

%if %{with maven_plugin}
%package maven-plugin
Group: Development/Java
Summary: Maven plugin for %{name}
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven:maven-core)
Requires: %{name} = %{version}
Requires: maven

%description maven-plugin
%{summary}.
%endif

%prep
%setup -q

%pom_disable_module liquibase-osgi
%pom_disable_module liquibase-integration-tests
%pom_disable_module liquibase-debian
%pom_disable_module liquibase-rpm

%if %{without maven_plugin}
%pom_disable_module liquibase-maven-plugin
%endif

%pom_remove_dep org.springframework:spring %{name}-core
%pom_add_dep org.springframework:spring-core %{name}-core
%pom_add_dep org.springframework:spring-beans %{name}-core
%pom_add_dep org.springframework:spring-context %{name}-core

# Disable filtering of bundled JS, fonts, etc. which cause
# maven-filtering to fail with IOException (see MSHARED-325 and
# BZ 1077375).
%pom_add_plugin :maven-resources-plugin %{name}-core "
    <configuration>
      <nonFilteredFileExtensions>
        <nonFilteredFileExtension>js</nonFilteredFileExtension>
        <nonFilteredFileExtension>eot</nonFilteredFileExtension>
        <nonFilteredFileExtension>svg</nonFilteredFileExtension>
        <nonFilteredFileExtension>ttf</nonFilteredFileExtension>
        <nonFilteredFileExtension>woff</nonFilteredFileExtension>
        <nonFilteredFileExtension>xsd</nonFilteredFileExtension>
        <nonFilteredFileExtension>vm</nonFilteredFileExtension>
        <nonFilteredFileExtension>sh</nonFilteredFileExtension>
      </nonFilteredFileExtensions>
    </configuration>"

# Symlink liquibase/liquibase-core.jar to liquibase.jar
%mvn_file :%{name}-core %{name}/%{name}-core %{name}

# Remove all test dependencies.  We aren't running tests with this build.
%pom_xpath_remove "//pom:dependency[pom:scope='test']" %{name}-core
%pom_remove_plugin org.codehaus.gmaven:gmaven-plugin %{name}-core

%if %{with maven_plugin}
# Build maven plugin
%mvn_package ":liquibase-maven-plugin" %{name}-maven-plugin
%pom_add_dep org.apache.maven:maven-core %{name}-maven-plugin
%endif

%build
%mvn_build -f

%install
%mvn_install
%jpackage_script liquibase.integration.commandline.Main "" "" %{name} %{name} true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc changelog.txt LICENSE.txt
%dir %{_javadir}/%{name}
%{_bindir}/%{name}
%config(noreplace,missingok) /etc/java/%{name}.conf

%if %{with maven_plugin}
%files maven-plugin -f .mfiles-%{name}-maven-plugin
%endif

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 3.4.1-alt1_1jpp8
- new version

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.7-alt1_4jpp7
- update

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_2jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1_8jpp7
- new version

