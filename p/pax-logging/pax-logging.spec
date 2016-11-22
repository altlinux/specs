Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          pax-logging
Version:       1.6.9
Release:       alt1_13jpp8
Summary:       OSGi Logging framework implementation
License:       ASL 2.0 and BSD and MIT
URL:           http://team.ops4j.org/wiki//display/paxlogging/Pax+Logging
Source0:       https://github.com/ops4j/org.ops4j.pax.logging/archive/logging-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(avalon-framework:avalon-framework-api)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)

# Those files are modifications of code included in:
# pax-logging-api/src/main/java/org/osgi/service/log/*
Provides:      bundled(felix-osgi-compendium) = 1.3
# pax-logging-api/src/main/java/org/apache/log4j/*
Provides:      bundled(log4j12) = 1.2.15
# pax-logging-api/src/main/java/org/apache/commons/logging/Log.java
# pax-logging-api/src/main/java/org/apache/commons/logging/LogConfigurationException.java
# pax-logging-api/src/main/java/org/apache/commons/logging/LogFactory.java
# pax-logging-api/src/main/java/org/apache/commons/logging/impl/NoOpLog.java
Provides:      bundled(jcl-over-slf4j) = 1.6.1
# pax-logging-api/src/main/java/org/apache/log4j/xml/DOMConfigurator.java
# pax-logging-api/src/main/java/org/apache/log4j/spi/Configurator.java
# pax-logging-api/src/main/java/org/apache/log4j/PropertyConfigurator.java
# pax-logging-api/src/main/java/org/apache/log4j/Category.java
# pax-logging-api/src/main/java/org/apache/log4j/Level.java
# pax-logging-api/src/main/java/org/apache/log4j/Logger.java
# pax-logging-api/src/main/java/org/apache/log4j/MDC.java
# pax-logging-api/src/main/java/org/apache/log4j/NDC.java
Provides:      bundled(log4j-over-slf4j) = 1.6.1
# pax-logging-api/src/main/java/org/slf4j/*
Provides:      bundled(slf4j-api) = 1.6.1

BuildArch:     noarch
Source44: import.info

%description
The OSGi Logging framework implementation. Supports SLF4J,
LOG4J,Jakarta Commons Logging etc.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n org.ops4j.pax.logging-logging-%{version}
%pom_remove_parent
%pom_disable_module pax-logging-it
%pom_disable_module pax-logging-samples
# test deps*
%pom_remove_dep -r junit:junit
%pom_remove_dep -r org.easymock:easymock
# unavailable
%pom_remove_dep -r jmock:jmock
%pom_remove_dep -r org.ops4j.pax.exam:pax-exam
%pom_remove_dep -r org.ops4j.pax.exam:pax-exam-container-default
%pom_remove_dep -r org.ops4j.pax.exam:pax-exam-junit
%pom_remove_dep -r org.ops4j.pax.runner:pax-runner-no-jcl
# sample deps
%pom_remove_dep -r org.mortbay.jetty:jetty

%pom_remove_plugin -r org.ops4j:maven-pax-plugin
%pom_remove_plugin -r :maven-shade-plugin

sed -i "s|<source>1.4</source>|<source>1.5</source>|" pom.xml
sed -i "s|<target>1.4</target>|<target>1.5</target>|" pom.xml

# prevent log4j re-bundle 
%pom_xpath_remove "pom:_include"
%pom_xpath_inject "pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:configuration" "<excludeDependencies>true</excludeDependencies>"

%pom_change_dep :log4j ::1.2.17
%pom_change_dep :log4j ::1.2.17 pax-logging-service

%pom_remove_plugin -r :maven-dependency-plugin pax-logging-api pax-logging-service
%pom_remove_plugin -r :maven-source-plugin pax-logging-api pax-logging-service

%mvn_file :%{name}-api %{name}-api
%mvn_file :%{name}-service %{name}-service

%build

# test skip unavailable test deps*
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

cp -rp pax-logging-api/NOTICE.txt .

%install
%mvn_install

%files -f .mfiles
%doc CONTRIBUTORS.txt RELEASE-NOTES.html
%doc LICENSE.txt NOTICE.txt 

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_5jpp7
- new release

* Sat Mar 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_3jpp7
- fc update

