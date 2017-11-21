Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           sonar
Version:        3.2
Release:        alt2_10jpp8
Summary:        An open platform to manage code quality
License:        LGPLv3+
URL:            http://www.sonarqube.org
BuildArch:      noarch

Source0:        https://github.com/SonarSource/sonarqube/archive/%{version}.tar.gz

# dbunit with (unavailable) oracle support
Patch0:         0001-Remove-oracle-DB-support.patch
Patch1:         0002-Port-to-guava-18.patch
Patch2:         0003-Never-thrown-exception.patch
Patch3:         0004-Port-maven-plugin-to-current-maven-dependency-tree.patch

BuildRequires:  maven-local
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(ch.qos.logback:logback-core)
BuildRequires:  mvn(com.fasterxml.staxmate:staxmate)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.googlecode.json-simple:json-simple)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-configuration:commons-configuration)
BuildRequires:  mvn(commons-dbcp:commons-dbcp)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(com.puppycrawl.tools:checkstyle:7)
BuildRequires:  mvn(com.thoughtworks.xstream:xstream)
BuildRequires:  mvn(javax.persistence:persistence-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(net.jcip:jcip-annotations)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-email)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:native2ascii-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.sonar:sonar-packaging-maven-plugin)
BuildRequires:  mvn(org.codehaus.sonar:sonar-update-center-common)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-lgpl)
BuildRequires:  mvn(org.hibernate.common:hibernate-commons-annotations)
BuildRequires:  mvn(org.hibernate:hibernate-core:3)
BuildRequires:  mvn(org.hibernate:hibernate-ehcache:3)
BuildRequires:  mvn(org.hibernate:hibernate-entitymanager:3)
BuildRequires:  mvn(org.jacoco:org.jacoco.agent)
BuildRequires:  mvn(org.jacoco:org.jacoco.core)
BuildRequires:  mvn(org.jfree:jfreechart)
BuildRequires:  mvn(org.mybatis:mybatis)
BuildRequires:  mvn(org.picocontainer:picocontainer)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:log4j-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xpp3:xpp3)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
Source44: import.info


%description
Open source platform for continuous inspection of code quality.


%package batch
Group: Development/Java
Summary: Batch module for sonar

%description batch
Batch module for sonar.


%package batch-bootstrapper
Group: Development/Java
Summary: Provides API to bootstrap Sonar Batch

%description batch-bootstrapper
Provides API to bootstrap Sonar Batch.


%package batch-maven-compat
Group: Development/Java
Summary: Compatibility layer, which provides MavenProject for non-Maven environments

%description batch-maven-compat
Compatibility layer, which provides MavenProject for non-Maven environments.


%package channel
Group: Development/Java
Summary: Code Channel

%description channel
Code Channel.


%package check-api
Group: Development/Java
Summary: Check API

%description check-api
Check API.


%package colorizer
Group: Development/Java
Summary: Code syntax highlighter

%description colorizer
Code syntax highlighter.


%package core
Group: Development/Java
Summary: Core components shared to batch and server

%description core
Core components shared to batch and server.


%package deprecated
Group: Development/Java
Summary: Deprecated module for sonar

%description deprecated
Deprecated module for sonar.


%package duplications
Group: Development/Java
Summary: Detect duplicated code

%description duplications
Detect duplicated code.


%package graph
Group: Development/Java
Summary: Graph module for sonar

%description graph
Graph module for sonar.


%package java-api
Group: Development/Java
Summary: Java-api module for sonar

%description java-api
Java-api module for sonar.


%package markdown
Group: Development/Java
Summary: Markdown module for sonar

%description markdown
Markdown module for sonar.


%package maven-plugin
Group: Development/Java
Summary: Maven-plugin module for sonar

%description maven-plugin
Maven-plugin module for sonar.


%package plugin-api
Group: Development/Java
Summary: Plugin-api module for sonar

%description plugin-api
Plugin-api module for sonar.


%package squid
Group: Development/Java
Summary: Squid module for sonar

%description squid
Squid module for sonar.


%package ws-client
Group: Development/Java
Summary: Java library to request Sonar web services

%description ws-client
Java library to request Sonar web services.


%package dbcleaner-plugin
Group: Development/Java
Summary: Optimizes database performances by removing old and useless data

%description dbcleaner-plugin
Optimizes database performances by removing old and useless data.


%package checkstyle-plugin
Group: Development/Java
Summary: Sonar checkstyle plugin

%description checkstyle-plugin
Checkstyle is a code analyser to help programmers write Java code that adheres
to a coding standard.


%package cobertura-plugin
Group: Development/Java
Summary: Cobertura-plugin module for sonar

%description cobertura-plugin
Cobertura-plugin module for sonar.


%package surefire-plugin
Group: Development/Java
Summary: Surefire-plugin module for sonar

%description surefire-plugin
Surefire-plugin module for sonar.


%package cpd-plugin
Group: Development/Java
Summary: Find duplicated source code within project

%description cpd-plugin
Find duplicated source code within project.


%package l10n-en-plugin
Group: Development/Java
Summary: L10n-en-plugin module for sonar

%description l10n-en-plugin
L10n-en-plugin module for sonar.


%package email-notifications-plugin
Group: Development/Java
Summary: Email Notifications

%description email-notifications-plugin
Email Notifications.


%package jacoco-plugin
Group: Development/Java
Summary: JaCoCo plugin for Sonar

%description jacoco-plugin
JaCoCo is an alternative to Clover and Cobertura to measure coverage by unit
tests.


%prep
%setup -q -n sonarqube-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

find . -name "*.bat" -delete
find . -name "*.class" -delete
find . -name "*.jar" -delete

# Bundled libraries in parts that are not built. Removed them just to be sure
rm -r plugins/sonar-squid-java-plugin/test-resources/ sonar-duplications/src/test/files \
      sonar-server/src/main/webapp/WEB-INF/

# guava stopped reexporting @Nullable
%pom_add_dep com.google.code.findbugs:jsr305

# wagon-webdav, unnecessary
%pom_xpath_remove pom:build/pom:extensions

%pom_change_dep -r :jruby-complete :jruby
%pom_change_dep -r jfree org.jfree
%pom_change_dep -r :staxmate com.fasterxml.staxmate:
%pom_change_dep org.hibernate:hibernate-commons-annotations org.hibernate.common: sonar-core
%pom_change_dep geronimo-spec:geronimo-spec-jta org.apache.geronimo.specs:geronimo-jta_1.1_spec sonar-core
%pom_add_dep javax.persistence:persistence-api sonar-plugin-api
%pom_add_dep org.apache.maven:maven-artifact sonar-plugin-api
%pom_add_dep org.apache.maven:maven-core sonar-plugin-api

# to prevent duplicity remove hibernate-anotations
%pom_remove_dep :hibernate-annotations ./pom.xml
%pom_remove_dep :hibernate-annotations ./sonar-core/pom.xml
%pom_change_dep -r :hibernate-annotations org.hibernate:hibernate-core

# requires maven 2.x
%pom_disable_module sonar-maven-plugin

%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-dependency-plugin
# for uploading artifacts, useless
%pom_remove_plugin -r :sonar-dev-maven-plugin

%pom_disable_module sonar-server

# missing com.google.gwt:gwt-user, com.google.gwt:gwt-incubator
%pom_disable_module sonar-gwt-api
%pom_disable_module plugins/sonar-core-gwt
%pom_disable_module plugins/sonar-core-plugin
%pom_disable_module plugins/sonar-design-plugin
# old version of pmd
%pom_disable_module plugins/sonar-pmd-plugin

# missing provider within findbugs
%pom_disable_module plugins/sonar-findbugs-plugin

# TODO incorrect ow:asm
%pom_disable_module plugins/sonar-squid-java-plugin

# circular dependency on sonar-rules
%pom_disable_module plugins/sonar-java-plugin

# missing fest-assert
%pom_disable_module sonar-testing-harness

# requires all the things I just disabled
%pom_disable_module sonar-application

# compat versions
%pom_change_dep -r :hibernate-core ::3
%pom_change_dep -r :hibernate-ehcache ::3
%pom_change_dep -r :hibernate-entitymanager ::3

%pom_change_dep -r :checkstyle ::7


%mvn_package :%{name}
%mvn_package :%{name}-core

%build
# missing fest-assert, javadoc doesn't like sonar-batch-bootstrapper
%mvn_build -fjs

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc COPYING copyright.txt

%files batch -f .mfiles-%{name}-batch
%files batch-bootstrapper -f .mfiles-%{name}-batch-bootstrapper
%files batch-maven-compat -f .mfiles-%{name}-batch-maven-compat
%files channel -f .mfiles-%{name}-channel
%files check-api -f .mfiles-%{name}-check-api
%files colorizer -f .mfiles-%{name}-colorizer
%files deprecated -f .mfiles-%{name}-deprecated
%files duplications -f .mfiles-%{name}-duplications
%files graph -f .mfiles-%{name}-graph
%files java-api -f .mfiles-%{name}-java-api
%files markdown -f .mfiles-%{name}-markdown
%files maven-plugin -f .mfiles-%{name}-maven3-plugin
%files plugin-api -f .mfiles-%{name}-plugin-api
%files squid -f .mfiles-%{name}-squid
%files ws-client -f .mfiles-%{name}-ws-client
%files dbcleaner-plugin -f .mfiles-%{name}-dbcleaner-plugin
%files checkstyle-plugin -f .mfiles-%{name}-checkstyle-plugin
%files cobertura-plugin -f .mfiles-%{name}-cobertura-plugin
%files surefire-plugin -f .mfiles-%{name}-surefire-plugin
%files cpd-plugin -f .mfiles-%{name}-cpd-plugin
%files l10n-en-plugin -f .mfiles-%{name}-l10n-en-plugin
%files email-notifications-plugin -f .mfiles-%{name}-email-notifications-plugin
%files jacoco-plugin -f .mfiles-%{name}-jacoco-plugin

%changelog
* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 3.2-alt2_10jpp8
- fixed build with new checkstyle

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_10jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_8jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_7jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_5jpp8
- unbootstrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

