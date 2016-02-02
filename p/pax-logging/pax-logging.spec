Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          pax-logging
Version:       1.6.9
Release:       alt1_10jpp8
Summary:       OSGi Logging framework implementation
License:       ASL 2.0 and BSD and MIT
URL:           http://team.ops4j.org/wiki//display/paxlogging/Pax+Logging
Source0:       https://github.com/ops4j/org.ops4j.pax.logging/archive/logging-%{version}.tar.gz


BuildRequires: mvn(avalon-framework:avalon-framework-api)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

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
%pom_remove_dep junit:junit
%pom_remove_dep org.easymock:easymock
# unavailable
%pom_remove_dep jmock:jmock
%pom_remove_dep org.ops4j.pax.exam:pax-exam
%pom_remove_dep org.ops4j.pax.exam:pax-exam-container-default
%pom_remove_dep org.ops4j.pax.exam:pax-exam-junit
%pom_remove_dep org.ops4j.pax.runner:pax-runner-no-jcl
# sample deps
%pom_remove_dep org.mortbay.jetty:jetty

%pom_remove_plugin org.ops4j:maven-pax-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-shade-plugin

sed -i "s|<source>1.4</source>|<source>1.5</source>|" pom.xml
sed -i "s|<target>1.4</target>|<target>1.5</target>|" pom.xml
# prevent log4j re-bundle 
sed -i "s|<_include>-osgi.bnd</_include>|<!--_include>-osgi.bnd</_include-->|" pom.xml

sed -i "s|<version>1.2.16</version>|<version>1.2.17</version>|" pom.xml
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId='log4j']" "<version>1.2.17</version>" pax-logging-service

%pom_remove_dep jmock:jmock pax-logging-api
%pom_remove_dep junit:junit pax-logging-api
%pom_remove_plugin org.ops4j:maven-pax-plugin pax-logging-api
%pom_remove_plugin org.apache.maven.plugins:maven-dependency-plugin pax-logging-api

%pom_remove_dep jmock:jmock pax-logging-service
%pom_remove_plugin org.ops4j:maven-pax-plugin pax-logging-service
%pom_remove_plugin org.apache.maven.plugins:maven-shade-plugin pax-logging-service
%pom_remove_plugin org.apache.maven.plugins:maven-dependency-plugin pax-logging-service

%mvn_file :%{name}-api %{name}-api
%mvn_file :%{name}-service %{name}-service

%build

# test skip unavailable test deps*
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

cp -rp pax-logging-api/NOTICE.txt .

%install
%mvn_install

%files -f .mfiles
%doc CONTRIBUTORS.txt LICENSE.txt NOTICE.txt RELEASE-NOTES.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_5jpp7
- new release

* Sat Mar 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_3jpp7
- fc update

